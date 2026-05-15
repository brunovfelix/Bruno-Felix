fn cria_string() -> &String {
    let s = String::from("ola");
    &s // ERRO DE COMPILACAO: retorna referencia a variavel local!
    // error[E0106]: missing lifetime specifier
    // s sera destruida ao fim desta funcao
}

fn main() {
    let r = cria_string();
    println!("{}", r);
}

// Compilar (vai falhar intencionalmente):
//   rustc ex11.rs
//
// Em C isso geraria apenas um WARNING e causaria crash em execucao.
// Em Rust, e um ERRO DE COMPILACAO — o programa nem compila!
