package concessionaria;

import java.util.ArrayList;
import java.util.Scanner;

// Classe Principal do Sistema.
// Contem o main e todos os menus.
public class AppConcessionaria {

    // Listas para guardar os dados em memoria (como o professor pediu)
    private static ArrayList<Cliente> listaClientes = new ArrayList<>();
    private static ArrayList<Funcionario> listaFuncionarios = new ArrayList<>();
    private static ArrayList<Veiculo> listaVeiculos = new ArrayList<>();
    private static ArrayList<Venda> listaVendas = new ArrayList<>();

    // Scanner para ler o que o usuario digita
    private static Scanner scanner = new Scanner(System.in);

    // Metodo Principal (main)
    public static void main(String[] args) {
        int opcao = -1;
        System.out.println("--- BEM-VINDO AO SISTEMA DE GERENCIAMENTO DE CONCESSIONÁRIA ---");

        // Loop principal do menu (so sai quando digita 0)
        while (opcao != 0) {
            System.out.println("\n--- MENU PRINCIPAL ---");
            System.out.println("1. Gerenciar Clientes");
            System.out.println("2. Gerenciar Funcionários");
            System.out.println("3. Gerenciar Veículos");
            System.out.println("4. Gerenciar Vendas");
            System.out.println("5. Relatórios");
            System.out.println("0. Sair do Sistema");
            System.out.print("Escolha uma opção: ");

            // Leitura da opcao do menu
            opcao = Integer.parseInt(scanner.nextLine());

            // Menu principal com if-else (o professor nao passou switch)
            if (opcao == 1) {
                menuClientes();
            } else if (opcao == 2) {
                menuFuncionarios();
            } else if (opcao == 3) {
                menuVeiculos();
            } else if (opcao == 4) {
                menuVendas();
            } else if (opcao == 5) {
                menuRelatorios();
            } else if (opcao == 0) {
                System.out.println("\nSaindo do sistema. Obrigado!");
            } else {
                System.out.println("\nOpção inválida! Tente novamente.");
            }
        }
        scanner.close(); // Fecha o scanner ao sair
    }

    // --- MENUS ---

    // Menu de Clientes
    private static void menuClientes() {
        int opcao = -1;
        while (opcao != 0) {
            System.out.println("\n--- Gerenciar Clientes ---");
            System.out.println("1. Cadastrar Cliente");
            System.out.println("2. Consultar Cliente (por CPF)");
            System.out.println("3. Alterar Cliente (por CPF)");
            System.out.println("4. Remover Cliente (por CPF)");
            System.out.println("0. Voltar ao Menu Principal");
            System.out.print("Escolha uma opção: ");

            opcao = Integer.parseInt(scanner.nextLine());

            if (opcao == 1) {
                cadastrarCliente();
            } else if (opcao == 2) {
                consultarCliente();
            } else if (opcao == 3) {
                alterarCliente();
            } else if (opcao == 4) {
                removerCliente();
            } else if (opcao != 0) {
                System.out.println("\nOpção inválida!");
            }
        }
    }

    // Menu de Funcionarios
    private static void menuFuncionarios() {
        int opcao = -1;
        while (opcao != 0) {
            System.out.println("\n--- Gerenciar Funcionários ---");
            System.out.println("1. Cadastrar Funcionário");
            System.out.println("2. Consultar Funcionário (por Matrícula)");
            System.out.println("3. Alterar Funcionário (por Matrícula)");
            System.out.println("4. Remover Funcionário (por Matrícula)");
            System.out.println("0. Voltar ao Menu Principal");
            System.out.print("Escolha uma opção: ");

            opcao = Integer.parseInt(scanner.nextLine());

            if (opcao == 1) {
                cadastrarFuncionario();
            } else if (opcao == 2) {
                consultarFuncionario();
            } else if (opcao == 3) {
                alterarFuncionario();
            } else if (opcao == 4) {
                removerFuncionario();
            } else if (opcao != 0) {
                System.out.println("\nOpção inválida!");
            }
        }
    }

    // Menu de Veiculos
    private static void menuVeiculos() {
        int opcao = -1;
        while (opcao != 0) {
            System.out.println("\n--- Gerenciar Veículos ---");
            System.out.println("1. Cadastrar Veículo");
            System.out.println("2. Consultar Veículo (por Nome/Modelo)");
            System.out.println("3. Alterar Veículo (por Nome/Modelo)");
            System.out.println("4. Remover Veículo (por Nome/Modelo)");
            System.out.println("0. Voltar ao Menu Principal");
            System.out.print("Escolha uma opção: ");

            opcao = Integer.parseInt(scanner.nextLine());

            if (opcao == 1) {
                cadastrarVeiculo();
            } else if (opcao == 2) {
                consultarVeiculo();
            } else if (opcao == 3) {
                alterarVeiculo();
            } else if (opcao == 4) {
                removerVeiculo();
            } else if (opcao != 0) {
                System.out.println("\nOpção inválida!");
            }
        }
    }

    // Menu de Vendas
    private static void menuVendas() {
        int opcao = -1;
        while (opcao != 0) {
            System.out.println("\n--- Gerenciar Vendas ---");
            System.out.println("1. Registrar Venda");
            System.out.println("2. Consultar Venda (por Data)");
            System.out.println("0. Voltar ao Menu Principal");
            System.out.print("Escolha uma opção: ");

            opcao = Integer.parseInt(scanner.nextLine());

            if (opcao == 1) {
                registrarVenda();
            } else if (opcao == 2) {
                consultarVenda();
            } else if (opcao != 0) {
                System.out.println("\nOpção inválida!");
            }
        }
    }

    // Menu de Relatorios (mostra tudo)
    private static void menuRelatorios() {
        System.out.println("\n--- RELATÓRIOS DO SISTEMA ---");

        System.out.println("\n--- Relatório de Clientes ---");
        if (listaClientes.isEmpty()) {
            System.out.println("Nenhum cliente cadastrado.");
        } else {
            // Loop para mostrar todos os clientes
            for (Pessoa p : listaClientes) {
                p.imprimeDados(); // Chama o imprimeDados() do Cliente
            }
        }

        System.out.println("\n--- Relatório de Funcionários ---");
        if (listaFuncionarios.isEmpty()) {
            System.out.println("Nenhum funcionário cadastrado.");
        } else {
            // Loop para mostrar todos os funcionarios
            for (Pessoa p : listaFuncionarios) {
                p.imprimeDados(); // Chama o imprimeDados() do Funcionario
            }
        }

        System.out.println("\n--- Relatório de Veículos ---");
        if (listaVeiculos.isEmpty()) {
            System.out.println("Nenhum veículo cadastrado.");
        } else {
            for (Veiculo v : listaVeiculos) {
                v.imprimeDados();
            }
        }

        System.out.println("\n--- Relatório de Vendas ---");
        if (listaVendas.isEmpty()) {
            System.out.println("Nenhuma venda registrada.");
        } else {
            for (Venda v : listaVendas) {
                v.imprimeDados();
            }
        }
    }

    // --- CLIENTES ---

    private static void cadastrarCliente() {
        System.out.println("\n--- Cadastro de Cliente ---");
        System.out.print("Nome: ");
        String nome = scanner.nextLine();
        System.out.print("Telefone: ");
        String telefone = scanner.nextLine();
        System.out.print("Email: ");
        String email = scanner.nextLine();
        System.out.print("RG: ");
        String rg = scanner.nextLine();
        System.out.print("CPF: ");
        String cpf = scanner.nextLine();

        // Verifica se o CPF ja existe antes de cadastrar
        if (buscarClientePorCpf(cpf) != null) {
            System.out.println("Erro: CPF já cadastrado!");
            return;
        }

        Cliente novoCliente = new Cliente(nome, telefone, email, rg, cpf);
        listaClientes.add(novoCliente);
        System.out.println("Cliente cadastrado com sucesso!");
    }

    private static void consultarCliente() {
        System.out.print("\nDigite o CPF do cliente para consulta: ");
        String cpf = scanner.nextLine();
        Cliente cliente = buscarClientePorCpf(cpf);

        if (cliente != null) {
            cliente.imprimeDados();
        } else {
            System.out.println("Cliente não encontrado.");
        }
    }

    private static void alterarCliente() {
        System.out.print("\nDigite o CPF do cliente para alterar: ");
        String cpf = scanner.nextLine();
        Cliente cliente = buscarClientePorCpf(cpf);

        if (cliente != null) {
            System.out.println("Alterando dados de: " + cliente.getNome());
            System.out.print("Novo Nome (Atual: " + cliente.getNome() + "): ");
            cliente.setNome(scanner.nextLine());
            System.out.print("Novo Telefone (Atual: " + cliente.getTelefone() + "): ");
            cliente.setTelefone(scanner.nextLine());
            System.out.print("Novo Email (Atual: " + cliente.getEmail() + "): ");
            cliente.setEmail(scanner.nextLine());
            System.out.println("Dados do cliente alterados com sucesso!");
        } else {
            System.out.println("Cliente não encontrado.");
        }
    }

    private static void removerCliente() {
        System.out.print("\nDigite o CPF do cliente para remover: ");
        String cpf = scanner.nextLine();
        Cliente cliente = buscarClientePorCpf(cpf);

        if (cliente != null) {
            listaClientes.remove(cliente);
            System.out.println("Cliente " + cliente.getNome() + " removido com sucesso.");
        } else {
            System.out.println("Cliente não encontrado.");
        }
    }

    // Metodo para buscar um cliente na lista pelo CPF
    private static Cliente buscarClientePorCpf(String cpf) {
        for (Cliente c : listaClientes) {
            if (c.getCpf().equals(cpf)) {
                return c;
            }
        }
        return null; // Nao achou
    }

    // --- FUNCIONARIOS ---

    private static void cadastrarFuncionario() {
        System.out.println("\n--- Cadastro de Funcionário ---");
        // Pede dados de Pessoa
        System.out.print("Nome: ");
        String nome = scanner.nextLine();
        System.out.print("Telefone: ");
        String telefone = scanner.nextLine();
        System.out.print("Email: ");
        String email = scanner.nextLine();
        System.out.print("RG: ");
        String rg = scanner.nextLine();
        System.out.print("CPF: ");
        String cpf = scanner.nextLine();
        // Pede dados especificos de Funcionario
        System.out.print("Número de Matrícula: ");
        String matricula = scanner.nextLine();
        System.out.print("Qualificação: ");
        String qualificacao = scanner.nextLine();
        System.out.print("Descrição da Função: ");
        String funcao = scanner.nextLine();
        System.out.print("Carga Horária Semanal: ");
        int carga = Integer.parseInt(scanner.nextLine());

        if (buscarFuncionarioPorMatricula(matricula) != null) {
            System.out.println("Erro: Matrícula já cadastrada!");
            return;
        }

        Funcionario novoFunc = new Funcionario(nome, telefone, email, rg, cpf, matricula, qualificacao, funcao, carga);
        listaFuncionarios.add(novoFunc);
        System.out.println("Funcionário cadastrado com sucesso!");
    }

    private static void consultarFuncionario() {
        System.out.print("\nDigite a Matrícula do funcionário para consulta: ");
        String matricula = scanner.nextLine();
        Funcionario func = buscarFuncionarioPorMatricula(matricula);

        if (func != null) {
            func.imprimeDados();
        } else {
            System.out.println("Funcionário não encontrado.");
        }
    }

    private static void alterarFuncionario() {
        System.out.print("\nDigite a Matrícula do funcionário para alterar: ");
        String matricula = scanner.nextLine();
        Funcionario func = buscarFuncionarioPorMatricula(matricula);

        if (func != null) {
            System.out.println("Alterando dados de: " + func.getNome());
            // Altera dados de Pessoa
            System.out.print("Novo Nome (Atual: " + func.getNome() + "): ");
            func.setNome(scanner.nextLine());
            System.out.print("Novo Telefone (Atual: " + func.getTelefone() + "): ");
            func.setTelefone(scanner.nextLine());
            // Altera dados de Funcionario
            System.out.print("Nova Qualificação (Atual: " + func.getQualificacao() + "): ");
            func.setQualificacao(scanner.nextLine());
            System.out.print("Nova Função (Atual: " + func.getDescricaoFuncao() + "): ");
            func.setDescricaoFuncao(scanner.nextLine());
            System.out.print("Nova Carga Horária (Atual: " + func.getCargaHorariaSemanal() + "): ");
            func.setCargaHorariaSemanal(Integer.parseInt(scanner.nextLine()));

            System.out.println("Dados do funcionário alterados com sucesso!");
        } else {
            System.out.println("Funcionário não encontrado.");
        }
    }

    private static void removerFuncionario() {
        System.out.print("\nDigite a Matrícula do funcionário para remover: ");
        String matricula = scanner.nextLine();
        Funcionario func = buscarFuncionarioPorMatricula(matricula);

        if (func != null) {
            listaFuncionarios.remove(func);
            System.out.println("Funcionário " + func.getNome() + " removido com sucesso.");
        } else {
            System.out.println("Funcionário não encontrado.");
        }
    }

    // Metodo para buscar um funcionario na lista pela Matricula
    private static Funcionario buscarFuncionarioPorMatricula(String matricula) {
        for (Funcionario f : listaFuncionarios) {
            if (f.getNumeroMatricula().equals(matricula)) {
                return f;
            }
        }
        return null; // Nao achou
    }

    // --- VEICULOS ---

    private static void cadastrarVeiculo() {
        System.out.println("\n--- Cadastro de Veículo ---");
        System.out.print("Nome/Modelo (Ex: Gol, Onix): ");
        String nome = scanner.nextLine();
        System.out.print("Marca (Ex: Volkswagen): ");
        String marca = scanner.nextLine();
        System.out.print("Cor: ");
        String cor = scanner.nextLine();
        System.out.print("Ano: ");
        int ano = Integer.parseInt(scanner.nextLine());
        System.out.print("Número de Portas: ");
        int portas = Integer.parseInt(scanner.nextLine());
        System.out.print("Número de Marchas: ");
        int marchas = Integer.parseInt(scanner.nextLine());

        Veiculo novoVeiculo = new Veiculo(nome, cor, marchas, portas, marca, ano);
        listaVeiculos.add(novoVeiculo);
        System.out.println("Veículo cadastrado com sucesso!");
    }

    // Metodo para buscar um veiculo na lista pelo Nome
    private static Veiculo buscarVeiculoPeloNome(String nome) {
        for (Veiculo v : listaVeiculos) {
            // equalsIgnoreCase ignora maiusculas/minusculas
            if (v.getNome().equalsIgnoreCase(nome)) {
                return v;
            }
        }
        return null; // Nao achou
    }

    private static void consultarVeiculo() {
        System.out.print("\nDigite o Nome/Modelo do veículo para consulta: ");
        String nome = scanner.nextLine();
        Veiculo v = buscarVeiculoPeloNome(nome);

        if (v != null) {
            v.imprimeDados();
        } else {
            System.out.println("Veículo não encontrado.");
        }
    }

    private static void alterarVeiculo() {
        System.out.print("\nDigite o Nome/Modelo do veículo para alterar: ");
        String nome = scanner.nextLine();
        Veiculo v = buscarVeiculoPeloNome(nome);

        if (v != null) {
            System.out.println("Alterando dados de: " + v.getNome());
            System.out.print("Nova Cor (Atual: " + v.getCor() + "): ");
            v.setCor(scanner.nextLine());
            System.out.print("Novo Ano (Atual: " + v.getAno() + "): ");
            v.setAno(Integer.parseInt(scanner.nextLine()));
            System.out.println("Dados do veículo alterados com sucesso!");
        } else {
            System.out.println("Veículo não encontrado.");
        }
    }

    private static void removerVeiculo() {
        System.out.print("\nDigite o Nome/Modelo do veículo para remover: ");
        String nome = scanner.nextLine();
        Veiculo v = buscarVeiculoPeloNome(nome);

        if (v != null) {
            listaVeiculos.remove(v);
            System.out.println("Veículo " + v.getNome() + " removido com sucesso.");
        } else {
            System.out.println("Veículo não encontrado.");
        }
    }

    // --- VENDAS ---

    private static void registrarVenda() {
        System.out.println("\n--- Registro de Venda ---");

        // 1. Achar o Cliente
        System.out.print("Digite o CPF do Cliente: ");
        Cliente cliente = buscarClientePorCpf(scanner.nextLine());
        if (cliente == null) {
            System.out.println("Erro: Cliente não encontrado. Cancele e cadastre o cliente primeiro.");
            return;
        }
        System.out.println("Cliente selecionado: " + cliente.getNome());

        // 2. Achar o Funcionario
        System.out.print("Digite a Matrícula do Funcionário (Vendedor): ");
        Funcionario func = buscarFuncionarioPorMatricula(scanner.nextLine());
        if (func == null) {
            System.out.println("Erro: Funcionário não encontrado.");
            return;
        }
        System.out.println("Vendedor selecionado: " + func.getNome());

        // 3. Achar o Veiculo
        System.out.print("Digite o Nome/Modelo do Veículo a ser vendido: ");
        Veiculo veic = buscarVeiculoPeloNome(scanner.nextLine());
        if (veic == null) {
            System.out.println("Erro: Veículo não encontrado no estoque.");
            return;
        }
        System.out.println("Veículo selecionado: " + veic.getNome() + " " + veic.getMarca());

        // 4. Pedir dados da Venda
        System.out.print("Data da Venda (dd/mm/aaaa): ");
        String data = scanner.nextLine();
        System.out.print("Valor da Venda (R$): ");
        double valor = Double.parseDouble(scanner.nextLine());

        // 5. Criar a Venda e salvar
        Venda novaVenda = new Venda(data, valor, cliente, func, veic);
        listaVendas.add(novaVenda);

        // 6. Tira o veiculo da lista de veiculos (foi vendido)
        listaVeiculos.remove(veic);

        System.out.println("\n--- VENDA REGISTRADA COM SUCESSO ---");
        novaVenda.imprimeDados();
    }

    private static void consultarVenda() {
        System.out.print("\nDigite a Data (dd/mm/aaaa) das vendas para consulta: ");
        String data = scanner.nextLine();
        boolean encontrou = false;

        for (Venda v : listaVendas) {
            if (v.getData().equals(data)) {
                v.imprimeDados();
                encontrou = true;
            }
        }

        if (!encontrou) {
            System.out.println("Nenhuma venda encontrada para esta data.");
        }
    }
}