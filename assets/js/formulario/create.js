function _getvalue(id){
    let value = document.getElementById(id).value
    return value
}

function alterar_visibilidade(id, div_space){
    let valor = _getvalue(id)
    let space = document.getElementById(div_space).style.display

    if(valor === 'Sim' || valor === 'Outro'){
        if(space == 'none'){
            document.getElementById(div_space).style.display = 'block';
        } else {
            document.getElementById(div_space).style.display = 'none';
        }
    } else if(valor === 'Não'){
        if(space == 'block'){
            document.getElementById(div_space).style.display = 'none';
        } else {
            document.getElementById(div_space).style.display = 'block';
        }
    }
}

//Função da meta de rentabilidade 
function rentabilidade_options(id) {
    let valor = _getvalue(id)
    if(valor === 'Outro'){
        input.removeAttribute('list')
        input.setAttribute('placeholder', 'Digite o indexador')
        input.value = ''
    }
}

//Restaura meta de rentabilidade
function restaurar() {
    let input = document.getElementById("datalist");
    input.setAttribute('list', 'options')
    input.setAttribute('placeholder', 'Selecione')
}

//Despesa custeada por
function func_despesa_custeada(id){
    let valor = _getvalue(id)
    if(valor === 'COM RECURSOS DO RPPS ATRAVÉS DE ALÍQUOTA'){
        document.getElementById('despesa_space').style.display = 'block'
    } else if(valor === 'DIRETAMENTE PELO TESOURO'){
        document.getElementById('despesa_space').style.display = 'none'
    }
}

function func_despesa_custeada_segregado(id){
    let valor = _getvalue(id)
    if(valor === 'COM RECURSOS DO RPPS ATRAVÉS DE ALÍQUOTA'){
        if(space == 'none'){
            document.getElementById(div_space).style.display = 'block';
        } else {
            document.getElementById(div_space).style.display = 'none';
        }
    } else if(valor === 'DIRETAMENTE PELO TESOURO'){
        if(space == 'block'){
            document.getElementById(div_space).style.display = 'none';
        } else {
            document.getElementById(div_space).style.display = 'block';
        }
    }
}

function Mudarestado() {
    var display = document.getElementById('segregado').style.display;
    if(display == "none")
        document.getElementById('segregado').style.display = 'block';
    else
        document.getElementById('segregado').style.display = 'none';
}
