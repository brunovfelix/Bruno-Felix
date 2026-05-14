import gleam/list
import sgleam/check

pub fn conta_iguais(lst: List(Int)) -> Int {
  case lst {
    [] -> 0
    [primeiro, ..resto] -> conta_aux(resto, primeiro, 1)
  }
}

// Função auxiliar que conta quantos elementos na lista são iguais ao alvo
// e acumula o resultado em acc.
fn conta_aux(lst: List(Int), alvo: Int, acc: Int) -> Int {
  case lst {
    [] -> acc
    [x, ..xs] ->
      case x == alvo {
        True -> conta_aux(xs, alvo, acc + 1)
        False -> acc
      }
  }
}

pub fn conta_iguais_examples() {
  check.eq(conta_iguais([]), 0)
  check.eq(conta_iguais([5]), 1)
  check.eq(conta_iguais([7, 7, 7, 8]), 3)
  check.eq(conta_iguais([9, 2, 2, 2]), 1)
}

//==============================================================================================

pub fn mescla_ordenada(a: List(Int), b: List(Int)) -> List(Int) {
  case a, b {
    [], _ -> b
    _, [] -> a
    [x, ..xs], [y, ..ys] ->
      case x <= y {
        True -> [x, ..mescla_ordenada(xs, b)]
        False -> [y, ..mescla_ordenada(a, ys)]
      }
  }
}

pub fn mescla_ordenada_examples() {
  check.eq(mescla_ordenada([], []), [])
  check.eq(mescla_ordenada([1, 3], []), [1, 3])
  check.eq(mescla_ordenada([], [2, 4]), [2, 4])
  check.eq(mescla_ordenada([1, 4], [2, 3]), [1, 2, 3, 4])
  check.eq(mescla_ordenada([1, 2, 6], [3, 4, 5]), [1, 2, 3, 4, 5, 6])
}

//================================================================================================

pub fn filtra_lista(lst: List(Int)) -> List(Int) {
  list.filter(lst, fn(x: Int) -> Bool { 
  x >= 0 && x % 5 != 0 })
}

pub fn filtra_lista_examples() {
  check.eq(filtra_lista([1, 5, -3, 10, 7]), [1, 7])
  check.eq(filtra_lista([0, -5, -1, -20]), [])
  check.eq(filtra_lista([6, 8, 15, 25, 30]), [6, 8])
  check.eq(filtra_lista([]), [])
}