import struct
import os
import sys

# --- Constantes Globais ---
TAM_MAX_BUCKET = 5
NOME_ARQ_DIRETORIO = 'diretorio.dat'
NOME_ARQ_BUCKETS = 'buckets.dat'
VAZIO = -1

class Bucket:
    """Representa um bucket de dados, seguindo a estrutura dos slides."""
    @staticmethod
    def get_formato():
        return f'2i{TAM_MAX_BUCKET}i'

    @staticmethod
    def get_tamanho_bytes():
        return struct.calcsize(Bucket.get_formato())

    def __init__(self, prof=0, cont=0):
        self.prof = prof
        self.cont = cont
        self.chaves = [VAZIO] * TAM_MAX_BUCKET

    def __str__(self):
        chaves_validas = sorted([k for k in self.chaves if k != VAZIO])
        return f"Profundidade={self.prof}, Chaves={chaves_validas}"

    def inserir_chave(self, chave):
        if not self.esta_cheio():
            for i in range(TAM_MAX_BUCKET):
                if self.chaves[i] == VAZIO:
                    self.chaves[i] = chave
                    self.cont += 1
                    return True
        return False

    def remover_chave(self, chave):
        try:
            idx = self.chaves.index(chave)
            self.chaves[idx] = VAZIO
            self.cont -= 1
            return True
        except ValueError:
            return False

    def esta_cheio(self):
        return self.cont == TAM_MAX_BUCKET

    def pack(self):
        return struct.pack(self.get_formato(), self.prof, self.cont, *self.chaves)

    @classmethod
    def unpack(cls, dados_bytes):
        dados_desempacotados = struct.unpack(cls.get_formato(), dados_bytes)
        bucket = cls(prof=dados_desempacotados[0], cont=dados_desempacotados[1])
        bucket.chaves = list(dados_desempacotados[2:])
        return bucket

class Diretorio:
    """Representa o diretório do hashing, seguindo os slides."""
    def __init__(self, prof_dir=0):
        self.prof_dir = prof_dir
        tamanho = 2**prof_dir
        self.refs = [0] * tamanho

    def __str__(self):
        total_buckets = len(set(self.refs))
        saida = "----- Diretório -----\n"
        for i, ref in enumerate(self.refs):
            saida += f"dir[{i}] = bucket({ref})\n"
        saida += f"\nProfundidade = {self.prof_dir}\n"
        saida += f"Tamanho atual = {len(self.refs)}\n"
        saida += f"Total de buckets = {total_buckets}\n"
        return saida

    def salvar(self, nome_arquivo):
        with open(nome_arquivo, 'wb') as f:
            f.write(struct.pack('i', self.prof_dir))
            for ref in self.refs:
                f.write(struct.pack('i', ref))

    def carregar(self, nome_arquivo):
        with open(nome_arquivo, 'rb') as f:
            self.prof_dir = struct.unpack('i', f.read(4))[0]
            tamanho = 2**self.prof_dir
            self.refs = [struct.unpack('i', f.read(4))[0] for _ in range(tamanho)]

class ExtensibleHashing:
    """Classe principal que implementa o algoritmo de Hashing Extensível."""
    def __init__(self):
        self.diretorio = Diretorio()
        self.arq_buckets = None
        self.inicializar_hashing()

    def inicializar_hashing(self):
        self.arq_buckets = open(NOME_ARQ_BUCKETS, 'a+b')
        if os.path.exists(NOME_ARQ_DIRETORIO) and os.path.getsize(NOME_ARQ_DIRETORIO) > 0:
            self.diretorio.carregar(NOME_ARQ_DIRETORIO)
        else:
            bucket_inicial = Bucket(prof=0)
            self.escrever_bucket(0, bucket_inicial)
            self.diretorio = Diretorio(prof_dir=0)
            self.diretorio.refs[0] = 0

    def fechar(self):
        if self.arq_buckets:
            self.arq_buckets.close()
        self.diretorio.salvar(NOME_ARQ_DIRETORIO)

    def escrever_bucket(self, rrn, bucket):
        self.arq_buckets.seek(rrn * Bucket.get_tamanho_bytes())
        self.arq_buckets.write(bucket.pack())

    def ler_bucket(self, rrn):
        self.arq_buckets.seek(rrn * Bucket.get_tamanho_bytes())
        dados_bytes = self.arq_buckets.read(Bucket.get_tamanho_bytes())
        return Bucket.unpack(dados_bytes) if dados_bytes else None

    def get_proximo_rrn_livre(self):
        self.arq_buckets.seek(0, os.SEEK_END)
        return self.arq_buckets.tell() // Bucket.get_tamanho_bytes()

    def gerar_endereco(self, chave, profundidade):
        # Implementação correta seguindo os slides: inverte os bits
        h = chave
        h_invertido = 0
        for i in range(32):
            if (h & (1 << i)):
                h_invertido |= 1 << (31 - i)
        
        if profundidade == 0:
            return 0
        
        # Pega os 'profundidade' bits mais significativos do valor invertido
        return h_invertido >> (32 - profundidade)

    def op_buscar(self, chave):
        endereco = self.gerar_endereco(chave, self.diretorio.prof_dir)
        rrn_bucket = self.diretorio.refs[endereco]
        bucket = self.ler_bucket(rrn_bucket)
        encontrado = False
        if bucket and chave in bucket.chaves:
            encontrado = True
        
        print(f"> Busca pela chave {chave}: Chave {'encontrada' if encontrado else 'não encontrada'}" + (f" no bucket {rrn_bucket}." if encontrado else ""))
        return rrn_bucket, bucket

    def op_inserir(self, chave):
        print(f"INSERÇÃO CHAVE {chave}:")
        
        endereco = self.gerar_endereco(chave, self.diretorio.prof_dir)
        rrn_bucket = self.diretorio.refs[endereco]
        bucket = self.ler_bucket(rrn_bucket)

        if chave in bucket.chaves:
            print(f"> Inserção da chave {chave}: Falha – Chave duplicada.")
            return

        if not bucket.esta_cheio():
            bucket.inserir_chave(chave)
            self.escrever_bucket(rrn_bucket, bucket)
            print(f"> Inserção da chave {chave}: Sucesso.")
        else:
            self.dividir_bucket(rrn_bucket, bucket)
            # Tenta a inserção novamente após a divisão
            self.op_inserir(chave)

    def op_remover(self, chave):
        print(f"REMOÇÃO CHAVE {chave}:")
        
        endereco = self.gerar_endereco(chave, self.diretorio.prof_dir)
        rrn_bucket = self.diretorio.refs[endereco]
        bucket = self.ler_bucket(rrn_bucket)
        
        if bucket and bucket.remover_chave(chave):
            self.escrever_bucket(rrn_bucket, bucket)
            print(f"> Remoção da chave {chave}: Sucesso.")
        else:
            print(f"> Remoção da chave {chave}: Falha – Chave não encontrada.")

    def dobrar_diretorio(self):
        print("-> Ação: Dobrando o tamanho do diretório.")
        self.diretorio.prof_dir += 1
        self.diretorio.refs.extend(self.diretorio.refs)
        
    def dividir_bucket(self, rrn_bucket_cheio, bucket_cheio):
        print(f"-> Ação: Bucket {rrn_bucket_cheio} cheio. Dividindo.")
        
        prof_antiga = bucket_cheio.prof
        prof_nova = prof_antiga + 1

        # Primeiro, verifica se precisa dobrar
        if prof_nova > self.diretorio.prof_dir:
            self.dobrar_diretorio()

        # Cria novo bucket e atualiza profundidades
        bucket_cheio.prof = prof_nova
        novo_bucket = Bucket(prof=prof_nova)
        rrn_novo_bucket = self.get_proximo_rrn_livre()
        self.escrever_bucket(rrn_novo_bucket, novo_bucket)

        # Lógica de atualização dos ponteiros do diretório
        # Encontra o primeiro endereço que apontava para o bucket antigo
        endereco_base = -1
        for i, rrn in enumerate(self.diretorio.refs):
            if rrn == rrn_bucket_cheio:
                endereco_base = i
                break

        # O padrão de bits que define o bucket antigo (com a profundidade antiga)
        padrao_bits_antigo = self.gerar_endereco(endereco_base, prof_antiga)

        for i in range(len(self.diretorio.refs)):
            # Pega o padrão de bits do endereço atual com a nova profundidade
            padrao_atual = self.gerar_endereco(i, prof_nova)
            # Pega o padrão de bits do endereço atual com a profundidade antiga
            padrao_antigo = self.gerar_endereco(i, prof_antiga)
            
            # Se o endereço 'i' pertencia ao grupo do bucket antigo
            if padrao_antigo == padrao_bits_antigo:
                # E o novo bit (que agora importa) for 1, aponta pro novo bucket
                if (padrao_atual >> prof_antiga) & 1 == 1:
                    self.diretorio.refs[i] = rrn_novo_bucket

        # Pega a lista de chaves do bucket cheio para redistribuir
        chaves_para_redistribuir = [k for k in bucket_cheio.chaves if k != VAZIO]
        
        # Limpa o bucket antigo
        bucket_cheio.cont = 0
        bucket_cheio.chaves = [VAZIO] * TAM_MAX_BUCKET
        self.escrever_bucket(rrn_bucket_cheio, bucket_cheio)

        # Reinsere as chaves na estrutura agora modificada
        print("   - Redistribuindo chaves...")
        for k in chaves_para_redistribuir:
            self.op_inserir(k)

# --- Funções para a Interface de Linha de Comando ---

def executar_operacoes_arquivo(hashing, nome_arquivo):
    print(f"Executando operações do arquivo: {nome_arquivo}")
    try:
        with open(nome_arquivo, 'r') as f:
            for linha in f:
                partes = linha.strip().split()
                if not partes: continue
                op, chave_str = partes[0].lower(), partes[1]
                chave = int(chave_str)
                if op == 'i': hashing.op_inserir(chave)
                elif op == 'r': hashing.op_remover(chave)
                elif op == 'b': hashing.op_buscar(chave)
    except FileNotFoundError:
        print(f"Erro: Arquivo de operações '{nome_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo: {e}")

def imprimir_diretorio(hashing):
    print(hashing.diretorio)

def imprimir_buckets(hashing):
    print("----- Buckets -----")
    rrns_unicos = set(hashing.diretorio.refs)
    max_rrn_usado = hashing.get_proximo_rrn_livre()
    for rrn in range(max_rrn_usado):
        bucket = hashing.ler_bucket(rrn)
        if bucket:
            if rrn in rrns_unicos:
                 print(f"Bucket {rrn}: {bucket}")
            else:
                 print(f"Bucket {rrn} -- Removido")

if __name__ == '__main__':
    args = sys.argv[1:]
    arquivo_exec = None
    print_dir = False
    print_bks = False

    i = 0
    while i < len(args):
        if args[i] == '-e':
            if i + 1 < len(args):
                arquivo_exec = args[i+1]
                i += 2
            else:
                print("Erro: Faltando nome do arquivo para o argumento -e")
                sys.exit(1)
        elif args[i] == '-pd':
            print_dir = True
            i += 1
        elif args[i] == '-pb':
            print_bks = True
            i += 1
        else:
            i += 1
    
    if not any([arquivo_exec, print_dir, print_bks]):
        print("Uso: python hashing_extensivel.py [-e <arquivo>] [-pd] [-pb]")
        sys.exit(1)

    if arquivo_exec:
        if os.path.exists(NOME_ARQ_DIRETORIO): os.remove(NOME_ARQ_DIRETORIO)
        if os.path.exists(NOME_ARQ_BUCKETS): os.remove(NOME_ARQ_BUCKETS)

    hashing = ExtensibleHashing()
    
    if arquivo_exec:
        executar_operacoes_arquivo(hashing, arquivo_exec)
    if print_dir:
        imprimir_diretorio(hashing)
    if print_bks:
        imprimir_buckets(hashing)

    hashing.fechar()