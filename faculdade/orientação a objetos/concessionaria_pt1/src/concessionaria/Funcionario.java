package concessionaria;

/**
 * Classe modelo para o Funcionario.*/
public class Funcionario extends Pessoa {

    private String numeroMatricula;
    private String qualificacao;
    private String descricaoFuncao;
    private int cargaHorariaSemanal;

    // --- Construtores ---

    public Funcionario() {
    }

    public Funcionario(
            // Dados de Pessoa:
            String nome, String telefone, String email, String rg, String cpf,
            // Dados de Funcionario:
            String numeroMatricula, String qualificacao, String descricaoFuncao, int cargaHorariaSemanal)
    {

        this.setNome(nome);
        this.setTelefone(telefone);
        this.setEmail(email);
        this.setRg(rg);
        this.setCpf(cpf);


        this.numeroMatricula = numeroMatricula;
        this.qualificacao = qualificacao;
        this.descricaoFuncao = descricaoFuncao;
        this.cargaHorariaSemanal = cargaHorariaSemanal;
    }

    // --- Metodos ---

    /**
     * Polimorfismo.
     */
    public void imprimeDados() {
        System.out.println("\n--- Dados do Funcionário ---");


        System.out.println("Nome: " + this.getNome());
        System.out.println("Telefone: " + this.getTelefone());
        System.out.println("Email: " + this.getEmail());
        System.out.println("RG: " + this.getRg());
        System.out.println("CPF: " + this.getCpf());


        System.out.println("Matrícula: " + this.getNumeroMatricula());
        System.out.println("Qualificação: " + this.getQualificacao());
        System.out.println("Função: " + this.getDescricaoFuncao());
        System.out.println("Carga Horária: " + this.getCargaHorariaSemanal() + "h/semana");
    }

    // --- Getters e Setters Específicos ---
    // (So dos atributos declarados NESTA classe)

    public String getNumeroMatricula() {
        return numeroMatricula;
    }

    public void setNumeroMatricula(String numeroMatricula) {
        this.numeroMatricula = numeroMatricula;
    }



    public String getQualificacao() {
        return qualificacao;
    }

    public void setQualificacao(String qualificacao) {
        this.qualificacao = qualificacao;
    }

    public String getDescricaoFuncao() {
        return descricaoFuncao;
    }

    public void setDescricaoFuncao(String descricaoFuncao) {
        this.descricaoFuncao = descricaoFuncao;
    }

    public int getCargaHorariaSemanal() {
        return cargaHorariaSemanal;
    }

    public void setCargaHorariaSemanal(int cargaHorariaSemanal) {
        this.cargaHorariaSemanal = cargaHorariaSemanal;
    }
}