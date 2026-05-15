const input = document.getElementById('input-tarefa')
const btnAdd = document.getElementById('adicionar')
const listaTarefas = document.getElementById('lista-tarefas')

btnAdd.addEventListener('click', () => {
    const texto = input.value
    console.log(texto);
    const itemLista = document.createElement('li');
    const span = document.createElement('span');
    span.textContent = texto;

    const remover = document.createElement('button');
    remover.textContent = 'Remover';
    remover.className = 'remover';
    remover.addEventListener('click', () => {
        listaTarefas.removeChild(itemLista);
    })

    itemLista.appendChild(remover)
    itemLista.appendChild(span);
    listaTarefas.appendChild(itemLista);

    input.value = ''
})