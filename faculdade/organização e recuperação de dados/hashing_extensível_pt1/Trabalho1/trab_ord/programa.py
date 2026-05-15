import sys
import os
import struct

class ExtendibleHashing:
    # Inicializa a estrutura de Hashing Extensível
    def __init__(self, bucket_size=5, dir_filename="diretorio.dat", buckets_filename="buckets.dat"):
        self.bucket_size = bucket_size
        self.dir_filename = dir_filename
        self.buckets_filename = buckets_filename
        self.global_depth = 0
        self.directory = []
        self.buckets_file = None
        self.bucket_record_size = 4 + 4 + (self.bucket_size * 4)

        if os.path.exists(self.dir_filename) and os.path.exists(self.buckets_filename):
            self._load_structure()
        else:
            self._init_structure()

    # Cria uma nova estrutura de hashing do zero
    def _init_structure(self):
        self.global_depth = 0
        self.directory = [0]
        if os.path.exists(self.buckets_filename):
            os.remove(self.buckets_filename)
        self.buckets_file = open(self.buckets_filename, 'w+b')
        self._write_bucket(0, self._create_bucket(local_depth=0))
        self._save_directory()

    # Carrega uma estrutura de hashing existente a partir dos arquivos
    def _load_structure(self):
        with open(self.dir_filename, 'rb') as f:
            self.global_depth = struct.unpack('i', f.read(4))[0]
            dir_size = 1 << self.global_depth
            self.directory = list(struct.unpack(f'{dir_size}i', f.read(dir_size * 4)))
        self.buckets_file = open(self.buckets_filename, 'r+b')

    # Salva o estado atual do diretório no arquivo diretorio.dat
    def _save_directory(self):
        with open(self.dir_filename, 'w+b') as f:
            f.write(struct.pack('i', self.global_depth))
            f.write(struct.pack(f'{len(self.directory)}i', *self.directory))

    # Função hash: extrai os 'depth' bits menos significativos da chave
    def _hash(self, key, depth=None):
        if depth is None:
            depth = self.global_depth
        return key & ((1 << depth) - 1)

    # Lê um bucket do arquivo, com opção de retornar a lista de chaves crua (com -1)
    def _read_bucket(self, rrn, return_raw_keys=False):
        if rrn is None: return None
        self.buckets_file.seek(rrn * self.bucket_record_size)
        data = self.buckets_file.read(self.bucket_record_size)
        if not data: return None
        
        local_depth, key_count = struct.unpack('ii', data[:8])
        keys_from_file = list(struct.unpack(f'{self.bucket_size}i', data[8:]))
        
        if return_raw_keys:
            return {'local_depth': local_depth, 'key_count': key_count, 'raw_keys': keys_from_file}
        else:
            return {'local_depth': local_depth, 'keys': keys_from_file[:key_count]}

    # Escreve um bucket no arquivo de buckets no seu RRN correspondente
    def _write_bucket(self, rrn, bucket):
        keys_to_write = bucket['keys'] + [-1] * (self.bucket_size - len(bucket['keys']))
        data = struct.pack(f'ii{self.bucket_size}i', bucket['local_depth'], len(bucket['keys']), *keys_to_write)
        self.buckets_file.seek(rrn * self.bucket_record_size)
        self.buckets_file.write(data)

    # Cria um novo dicionário representando um bucket vazio
    def _create_bucket(self, local_depth):
        return {'local_depth': local_depth, 'keys': []}

    # Obtém o RRN para um novo bucket (no final do arquivo)
    def _get_new_rrn(self):
        self.buckets_file.seek(0, os.SEEK_END)
        return self.buckets_file.tell() // self.bucket_record_size

    # Insere uma nova chave na estrutura
    def insert(self, key_to_insert):
        dir_index = self._hash(key_to_insert)
        rrn = self.directory[dir_index]
        bucket = self._read_bucket(rrn)

        if key_to_insert in bucket['keys']:
            print(f"> Inserção da chave {key_to_insert}: Falha. Chave duplicada.")
            return

        if len(bucket['keys']) < self.bucket_size:
            bucket['keys'].append(key_to_insert)
            self._write_bucket(rrn, bucket)
            print(f"> Inserção da chave {key_to_insert}: Sucesso.")
            return

        local_depth = bucket['local_depth']
        if local_depth == self.global_depth:
            self.directory.extend(self.directory)
            self.global_depth += 1

        new_local_depth = local_depth + 1
        new_rrn = self._get_new_rrn()
        new_bucket = self._create_bucket(local_depth=new_local_depth)
        bucket['local_depth'] = new_local_depth
        
        discriminating_bit = 1 << local_depth
        for i in range(len(self.directory)):
            if self.directory[i] == rrn and (i & discriminating_bit):
                self.directory[i] = new_rrn
        
        keys_to_redistribute = bucket['keys']
        bucket['keys'], new_bucket['keys'] = [], []
        for k in keys_to_redistribute:
            if self._hash(k) & discriminating_bit:
                new_bucket['keys'].append(k)
            else:
                bucket['keys'].append(k)

        self._write_bucket(rrn, bucket)
        self._write_bucket(new_rrn, new_bucket)
        self.insert(key_to_insert)

    # Busca por uma chave na estrutura
    def search(self, key):
        rrn = self.directory[self._hash(key)]
        bucket = self._read_bucket(rrn)
        if bucket and key in bucket['keys']:
            print(f"> Busca pela chave {key}: Chave encontrada no bucket {rrn}.")
        else:
            print(f"> Busca pela chave {key}: Chave não encontrada.")

    # Remove uma chave e inicia o processo de concatenação/redução
    def remove(self, key):
        dir_index = self._hash(key)
        rrn = self.directory[dir_index]
        bucket = self._read_bucket(rrn)

        if not bucket or key not in bucket['keys']:
            print(f"> Remoção da chave {key}: Falha. Chave não encontrada.")
            return

        bucket['keys'].remove(key)
        self._write_bucket(rrn, bucket)
        print(f"> Remoção da chave {key}: Sucesso.")
        
        # Tenta concatenar o bucket que sofreu a remoção
        self._try_to_merge(rrn)
        # Após a cascata de fusões, tenta reduzir o diretório
        self._try_to_shrink_directory()

    # Tenta concatenar um bucket com seu amigo
    def _try_to_merge(self, rrn):
        bucket = self._read_bucket(rrn)
        if not bucket or bucket['local_depth'] == 0:
            return False

        # Encontra o "amigo" do bucket
        try:
            my_dir_index = self.directory.index(rrn)
        except ValueError:
            return False

        buddy_dir_index = my_dir_index ^ (1 << (bucket['local_depth'] - 1))
        buddy_rrn = self.directory[buddy_dir_index]

        if buddy_rrn == rrn: return False

        buddy_bucket = self._read_bucket(buddy_rrn)
        if not buddy_bucket or buddy_bucket['local_depth'] != bucket['local_depth']:
            return False

        # Se a fusão é possível, executa
        if len(bucket['keys']) + len(buddy_bucket['keys']) <= self.bucket_size:
            # REGRA: O bucket de menor RRN absorve o de maior RRN
            absorbing_rrn, absorbed_rrn = (rrn, buddy_rrn) if rrn < buddy_rrn else (buddy_rrn, rrn)
            
            absorbing_bucket = self._read_bucket(absorbing_rrn)
            absorbed_bucket = self._read_bucket(absorbed_rrn)

            absorbing_bucket['keys'].extend(absorbed_bucket['keys'])
            absorbing_bucket['local_depth'] -= 1
            self._write_bucket(absorbing_rrn, absorbing_bucket)
            
            # Atualiza o diretório
            for i in range(len(self.directory)):
                if self.directory[i] == absorbed_rrn:
                    self.directory[i] = absorbing_rrn
            
            # Tenta uma nova fusão com o bucket que sobreviveu
            self._try_to_merge(absorbing_rrn)
            return True
        return False

    # Tenta reduzir o diretório pela metade
    def _try_to_shrink_directory(self):
        if self.global_depth == 0:
            return False

        can_shrink = True
        for i in range(0, len(self.directory), 2):
            if self.directory[i] != self.directory[i+1]:
                can_shrink = False
                break
        
        if can_shrink:
            self.directory = [self.directory[i] for i in range(0, len(self.directory), 2)]
            self.global_depth -= 1
            # Após reduzir, tenta reduzir novamente
            self._try_to_shrink_directory()
            return True
        return False

    def print_buckets(self):
        print("----- Buckets -----")
        self.buckets_file.seek(0, os.SEEK_END)
        file_size = self.buckets_file.tell()
        total_buckets_in_file = file_size // self.bucket_record_size
        active_rrns = set(self.directory)

        for rrn in range(total_buckets_in_file):
            bucket = self._read_bucket(rrn, return_raw_keys=True)
            if not bucket:
                continue

            if rrn in active_rrns:
                print(f"Bucket {rrn} (Prof = {bucket['local_depth']}):")
                print(f"ContaChaves = {bucket['key_count']}")
                print(f"Chaves = {bucket['raw_keys']}")
            else:
                print(f"Bucket {rrn} --> Removido")

            if rrn < total_buckets_in_file - 1:
                print()

    # Imprime o estado atual do diretório
    def print_directory(self):
        print("Diretório")
        for i, rrn in enumerate(self.directory):
            print(f"dir[{i}] = bucket[{rrn}]")
        print(f"Profundidade = {self.global_depth}")
        print(f"Tamanho atual = {len(self.directory)}")
        print(f"Total de buckets = {len(set(self.directory))}")

    # Fecha os arquivos e salva o estado final do diretório
    def close(self):
        self._save_directory()
        if self.buckets_file:
            self.buckets_file.close()

def main():
    BUCKET_SIZE = 5

    if len(sys.argv) < 2:
        print("Uso: python programa.py [-e <arquivo_ops> | -pd | -pb]")
        return

    flag = sys.argv[1]

    if flag == '-e':
        if len(sys.argv) > 2:
            ops_file = sys.argv[2]
            hashing = ExtendibleHashing(bucket_size=BUCKET_SIZE)
            with open(ops_file, 'r', encoding='utf-8-sig') as f:
                for line in f:
                    parts = line.strip().split()
                    if not parts: continue
                    op = parts[0].lower()
                    key = int(parts[1])
                    if op == 'i':
                        hashing.insert(key)
                    elif op == 'b':
                        hashing.search(key)
                    elif op == 'r':
                        hashing.remove(key)
            hashing.close()
        else:
            print("Erro: Arquivo de operações não especificado para a flag -e.")

    elif flag == '-pd':
        hashing = ExtendibleHashing(bucket_size=BUCKET_SIZE)
        hashing.print_directory()
        hashing.close()

    elif flag == '-pb':
        hashing = ExtendibleHashing(bucket_size=BUCKET_SIZE)
        hashing.print_buckets()
        hashing.close()

    else:
        print(f"Flag desconhecida: {flag}")

if __name__ == "__main__":
    main()