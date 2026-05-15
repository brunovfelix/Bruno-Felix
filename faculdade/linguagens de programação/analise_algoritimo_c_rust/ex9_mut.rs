// Demonstracao da diferenca entre & (imutavel) e &mut (mutavel)

// Referencia imutavel — so leitura
fn tamanho(s: &String) -> usize {
    // s.push_str(" teste"); // ERRO: nao pode modificar via &
    s.len()
}

// Referencia mutavel — permite escrita
fn adiciona_sufixo(s: &mut String) {
    s.push_str(" [modificada]"); // OK com &mut
}

fn main() {
    let mut s = String::from("Linguagens de Programacao");

    let tam = tamanho(&s);
    println!("Tamanho original: {}", tam);

    adiciona_sufixo(&mut s); // passa referencia mutavel
    println!("Apos modificacao: {}", s);
}

// Compilar:
//   rustc ex9_mut.rs
