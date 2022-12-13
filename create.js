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
    } else if(valor === 'Não' || valor === ''){
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

function nav_bar_navigation(id, space){
    let element = document.getElementById(id)
    if(check_active(id) === true){
        element.classList.remove('active')
        if(document.getElementById(space).style.display === 'block'){
            document.getElementById(space).style.display = 'none'
        }
    } else if(check_active(id) === false){
        element.classList.add('active')
        if(document.getElementById(space).style.display === 'none'){
            document.getElementById(space).style.display = 'block'
        }
    }
}

function check_active(id){
    let element = document.getElementById(id).classList.contains('active')
    return element
}

let already_on = false
let who_on_id = ''
let who_on_space = ''
function change_state(space, id) { // Grupo 0
    if(id === who_on_id){
        already_on = false
        who_on_id = ''
        who_on_space = ''
    }
    var display = document.getElementById(space).style.display;
    if(display == "none"){
        document.getElementById(space).style.display = 'block';
        document.getElementById(id).classList.add('active')
        if(already_on === true){
            document.getElementById(who_on_space).style.display = 'none';
            document.getElementById(who_on_id).classList.remove('active')
            already_on = false
        }
        already_on = true
        who_on_id = id
        who_on_space = space
    } else {
        document.getElementById(space).style.display = 'none';
        document.getElementById(id).classList.remove('active')
    }
}

function segregacao(id){
    let segregado = document.getElementById(id).value
    if(segregado === 'sim'){
        document.getElementById('financeiro_id').style.display = 'block'
        document.getElementById('fundamentacao_legal_space').style.display = 'block'
    } else {
        document.getElementById('financeiro_id').style.display = 'none'
        document.getElementById('fundamentacao_legal_space').style.display = 'none'
    }
}

function tesouro(id){
    let tesouro = document.getElementById(id).value
    if(tesouro === 'sim'){
        document.getElementById('mantido_tesouro_id').style.display = 'block'
        document.getElementById('treasure_space').style.display = 'block'
    } else {
        document.getElementById('mantido_tesouro_id').style.display = 'none'
        document.getElementById('treasure_space').style.display = 'none'
    }
}

function prev_complementar(id){
    let prev = document.getElementById(id).value
    if(prev === 'sim'){
        document.getElementById('prev_space').style.display = 'block'
    } else {
        document.getElementById('prev_space').style.display = 'none'
    }
}

let groups = {
    'group_1': {
        'already_on':false,
        'who_on_id':'',
        'who_on_space':''
    },
    'group_2':{
        'already_on':false,
        'who_on_id':'',
        'who_on_space':''
    }
}

function change_state_groups(space, id, group) { // Grupo 1
    if(id === groups[group]['already_on']){
        groups[group]['already_on'] = false 
        groups[group]['who_on_id'] = '' 
        groups[group]['who_on_space'] = '' 
    }
    var display = document.getElementById(space).style.display;
    if(display == "none"){
        document.getElementById(space).style.display = 'block';
        document.getElementById(id).classList.add('active')
        if(groups[group]['already_on'] === true){ 
            document.getElementById(groups[group]['who_on_space']).style.display = 'none'; 
            document.getElementById(groups[group]['who_on_id']).classList.remove('active') 
            groups[group]['already_on'] = false 
        }
        groups[group]['already_on'] = true 
        groups[group]['who_on_id'] = id 
        groups[group]['who_on_space'] = space 
    } else {
        document.getElementById(space).style.display = 'none';
        document.getElementById(id).classList.remove('active')
    }
    }

let actives = {
    'who_on_id':'',
    'who_on_space':'',
    'already_on':false
}
function dropdown_change_state(id, space){
    if(id === actives['who_on_id']){
        actives['already_on'] = false
        actives['who_on_id'] = ''
        actives['who_on_space'] = ''
    }
    
    var display = document.getElementById(space).style.display;
    if(display == "none"){
        document.getElementById(space).style.display = 'block';
        if(actives['already_on'] === true){
            document.getElementById(actives['who_on_space']).style.display = 'none';
            actives['already_on'] = false
        }
        actives['already_on'] = true
        actives['who_on_id'] = id
        actives['who_on_space'] = space
    } else {
        document.getElementById(space).style.display = 'none';
    }
}

