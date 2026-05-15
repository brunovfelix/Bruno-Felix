// CORRECAO: retornar String por valor (transferindo o ownership)
fn cria_string() -> String {
    let s = String::from("ola");
    s // transfere o ownership para o chamador — sem dangling reference
}

fn main() {
    let r = cria_string(); // r e agora o dono da String
    println!("{}", r);
}

// Compilar:
//   rustc ex11_corrigido.rs
//
// Saida:
//   ola
