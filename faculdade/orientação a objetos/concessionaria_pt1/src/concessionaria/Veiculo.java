package concessionaria;

/**
 * Classe modelo para o Veiculo.
 */
public class Veiculo {
    private String nome;
    private String cor;
    private int numeroMarchas;
    private int numeroPortas;
    private String marca;
    private int ano;

    // Construtor padrao
    public Veiculo() {
    }

    // Construtor que recebe os dados
    public Veiculo(String nome, String cor, int numeroMarchas, int numeroPortas, String marca, int ano) {
        this.nome = nome;
        this.cor = cor;
        this.numeroMarchas = numeroMarchas;
        this.numeroPortas = numeroPortas;
        this.marca = marca;
        this.ano = ano;
    }

    // Imprime os dados do veiculo
    public void imprimeDados() {
        System.out.println("\n--- Dados do Veículo ---");
        System.out.println("Nome: " + this.getNome());
        System.out.println("Marca: " + this.getMarca());
        System.out.println("Cor: " + this.getCor());
        System.out.println("Ano: " + this.getAno());
        System.out.println("Portas: " + this.getNumeroPortas());
        System.out.println("Marchas: " + this.getNumeroMarchas());
    }

    // --- Getters e Setters ---

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    public int getNumeroMarchas() {
        return numeroMarchas;
    }

    public void setNumeroMarchas(int numeroMarchas) {
        this.numeroMarchas = numeroMarchas;
    }

    public int getNumeroPortas() {
        return numeroPortas;
    }

    public void setNumeroPortas(int numeroPortas) {
        this.numeroPortas = numeroPortas;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }
}