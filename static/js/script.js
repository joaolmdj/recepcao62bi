const INPUT_BUSCA = document.getElementById('input');
const TABELA_BEBIDAS = document.getElementById('tbody');
const TR_ACOES = document.getElementById('acoes');
var button = document.querySelector('#switchbutton');
let linhas = TABELA_BEBIDAS.getElementsByTagName('tr');


INPUT_BUSCA.addEventListener('keyup', () => {
    let expressao = INPUT_BUSCA.value.toLowerCase();
    console.log(expressao)


    if (expressao.length === 1) {
        return;
    }
    for (let posicao in linhas) {
        if (true === isNaN(posicao)) {
            continue;
        }

        let conteudoDaLinha = linhas[posicao].innerHTML.toLowerCase();

        if (true === conteudoDaLinha.includes(expressao)) {
            linhas[posicao].style.display = '';
        } else {
            linhas[posicao].style.display = 'none';
        }
    }
});

$('.message').hide().fadeIn('slow').delay(1000).fadeOut('slow');  
