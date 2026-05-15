import{astros} from './data.js'

const canvas = document.querySelector('canvas')
const contexto = canvas.getContext('2d')
const container = document.querySelector('.conteudo')


function obterImagem(caminho){
    const img = new Image()
    img.src = caminho
    return img

}


function ajustarCanvas(){
    canvas.width = container.clientWidth
    canvas.height = container.clientHeight

    astros[0].x = canvas.width / 2
    astros[0].y = canvas.height / 2

}

function desenhar(astro){
    if(astro.raioOrbita){
        const sol = astros[0]
        contexto.strokeStyle = 'gray'
        contexto.beginPath()
        contexto.setLineDash([5,5])
        contexto.arc(sol.x, sol.y, astro.raioOrbita, 0, Math.PI * 2)
        contexto.stroke()
        contexto.closePath()
    }

    let raioAtual = astro.raio
    if (astro === hoveredAstro){
        raioAtual *= 1.2
    }


    const imagemAstro = obterImagem(astro.caminho)
    const posX = astro.x - raioAtual  
    const posY = astro.y - raioAtual  
    const largura = raioAtual * 2
    const altura = raioAtual * 2
    
    contexto.drawImage(imagemAstro, posX, posY , largura, altura)


}

function animar(){
    contexto.clearRect(0 , 0, canvas.width, canvas.height)    

    const sol = astros[0]
    astros.forEach(astro => {
        if (astro.raioOrbita){
            astro.anguloAtual += astro.velocidadeOrbita
            astro.x = sol.x + astro.raioOrbita * Math.cos(astro.anguloAtual)
            astro.y = sol.y + astro.raioOrbita * Math.sin(astro.anguloAtual)
        }
        desenhar(astro)
    })

    requestAnimationFrame(animar)
}

function verificaMouseSobreAstro(mouseX, mouseY, astro) {
    const distancia = Math.sqrt((mouseX - astro.x) ** 2 + (mouseY - astro.y) ** 2 )
    return distancia <= astro.raio
}

let hoveredAstro = null 

canvas.addEventListener('mousemove', (event) =>{
    const rect = canvas.getBoundingClientRect()
    const mouseX = event.clientX - rect.left
    const mouseY = event.clientY - rect.top

    let novoHoveredAstro = null

    for (let i= 1; i < astros.length; i++) {
        if (verificaMouseSobreAstro(mouseX, mouseY, astros[i])){
            novoHoveredAstro = astros[i]
            break
        }
    }

    hoveredAstro = novoHoveredAstro

})

ajustarCanvas()
animar()