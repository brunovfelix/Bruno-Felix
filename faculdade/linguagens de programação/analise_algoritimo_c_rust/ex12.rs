fn main() {
    let vetor = vec![1, 2, 3, 4, 5];

    // Acesso valido
    println!("vetor[2] = {}", vetor[2]);

    // Acesso fora dos limites — panic em execucao (nao silencioso como em C!)
    println!("vetor[10] = {}", vetor[10]);
}

// Compilar:
//   rustc ex12.rs
//
// Saida:
//   vetor[2] = 3
//   thread 'main' panicked at 'index out of bounds: the len is 5 but the index is 10'
//
// Em C isso corromperia memoria silenciosamente.
// Em Rust, o programa para imediatamente com mensagem clara.
