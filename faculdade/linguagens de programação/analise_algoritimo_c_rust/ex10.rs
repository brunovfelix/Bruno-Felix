fn main() {
    let mut s = String::from("hello");

    let r1 = &mut s;
    let r2 = &mut s; // ERRO DE COMPILACAO!
    // error[E0499]: cannot borrow `s` as mutable more than once at a time

    println!("{}, {}", r1, r2);
}

// Compilar (vai falhar intencionalmente):
//   rustc ex10.rs
