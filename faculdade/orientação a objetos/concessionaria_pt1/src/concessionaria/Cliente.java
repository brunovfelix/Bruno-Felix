package concessionaria;

/**
 * Classe modelo para o Cliente.
 * Herda da classe Pessoa.
 */
public class Cliente extends Pessoa {
        // Nao tem atributos a mais, todos estao em Pessoa.

    // --- Construtores ---

    public Cliente() {
    }

    public Cliente(String nome, String telefone, String email, String rg, String cpf) {
        this.setNome(nome);
        this.setTelefone(telefone);
        this.setEmail(email);
        this.setRg(rg);
        this.setCpf(cpf);
    }

    // --- Metodos ---

    public void imprimeDados() {
        System.out.println("\n--- Dados do Cliente ---");
        // Usamos os getters da classe Pessoa (pois os atributos sao private)
        System.out.println("Nome: " + this.getNome());
        System.out.println("Telefone: " + this.getTelefone());
        System.out.println("Email: " + this.getEmail());
        System.out.println("RG: " + this.getRg());
        System.out.println("CPF: " + this.getCpf());
    }
}
