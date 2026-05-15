fn tamanho(s: &String) -> usize {
    s.len() // apenas le, nao toma posse
}

fn main() {
    let s = String::from("Linguagens de Programacao");
    let tam = tamanho(&s); // empresta s (borrow)

    // s continua valido aqui — nao foi movido
    println!("'{}' tem {} bytes", s, tam);
}

// Compilar:
//   rustc ex9.rs
//
// Saida:
//   'Linguagens de Programacao' tem 25 bytes
