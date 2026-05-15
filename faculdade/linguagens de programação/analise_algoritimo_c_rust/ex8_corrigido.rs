fn main() {
    let s1 = String::from("hello");
    let s2 = s1.clone(); // CORRECAO: copia profunda (deep copy)

    println!("s2 = {}", s2);
    println!("s1 = {}", s1); // s1 ainda e valido
}

// Compilar:
//   rustc ex8_corrigido.rs
//
// Saida:
//   s2 = hello
//   s1 = hello
