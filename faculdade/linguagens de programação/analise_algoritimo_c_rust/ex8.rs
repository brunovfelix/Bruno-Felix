fn main() {
    let s1 = String::from("hello");
    let s2 = s1; // s1 e "movido" para s2 — ownership transferido

    println!("s2 = {}", s2);
    println!("s1 = {}", s1); // ERRO DE COMPILACAO!
    // error[E0382]: borrow of moved value: `s1`
}

// Compilar (vai falhar intencionalmente):
//   rustc ex8.rs
