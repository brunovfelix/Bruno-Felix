package concessionaria;

/**
 * Classe modelo para a Venda.
 * Guarda os dados da venda e os objetos relacionados.
 */
public class Venda {
    private String data;
    private double valor;

    // Associacao: A Venda guarda um objeto Cliente, Funcionario e Veiculo
    private Cliente cliente;
    private Funcionario funcionario;
    private Veiculo veiculo;

    // Construtor padrao
    public Venda() {
    }

    // Construtor que recebe os dados
    public Venda(String data, double valor, Cliente cliente, Funcionario funcionario, Veiculo veiculo) {
        this.data = data;
        this.valor = valor;
        this.cliente = cliente;
        this.funcionario = funcionario;
        this.veiculo = veiculo;
    }

    // Imprime os dados da Venda.
    public void imprimeDados() {
        System.out.println("\n--- Dados da Venda ---");
        System.out.println("Data: " + this.getData());
        System.out.printf("Valor: R$ %.2f\n", this.getValor());

        // Pega o nome de dentro dos objetos (cliente.getNome(), etc)
        System.out.println("Cliente: " + (this.getCliente() != null ? this.getCliente().getNome() : "N/A"));
        System.out.println("Funcionário: " + (this.getFuncionario() != null ? this.getFuncionario().getNome() : "N/A"));
        System.out.println("Veículo: " + (this.getVeiculo() != null ? this.getVeiculo().getNome() : "N/A"));

        System.out.println("\n... Detalhes do Cliente da Venda ...");
        if (this.getCliente() != null) {
            this.getCliente().imprimeDados();
        }

        System.out.println("\n... Detalhes do Veículo da Venda ...");
        if (this.getVeiculo() != null) {
            this.getVeiculo().imprimeDados();
        }
    }

    // --- Getters e Setters ---

    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }

    public double getValor() {
        return valor;
    }

    public void setValor(double valor) {
        this.valor = valor;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public Funcionario getFuncionario() {
        return funcionario;
    }

    public void setFuncionario(Funcionario funcionario) {
        this.funcionario = funcionario;
    }

    public Veiculo getVeiculo() {
        return veiculo;
    }

    public void setVeiculo(Veiculo veiculo) {
        this.veiculo = veiculo;
    }
}