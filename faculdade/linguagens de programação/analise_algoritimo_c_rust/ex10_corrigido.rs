fn main() {
    let mut s = String::from("hello");

    // CORRECAO: usar escopos para separar os emprestimos mutaveis
    {
        let r1 = &mut s;
        println!("r1 = {}", r1);
    } // r1 sai de escopo aqui — emprestimo liberado

    let r2 = &mut s; // agora e permitido, r1 nao existe mais
    println!("r2 = {}", r2);
}

// Compilar:
//   rustc ex10_corrigido.rs
//
// Saida:
//   r1 = hello
//   r2 = hello
