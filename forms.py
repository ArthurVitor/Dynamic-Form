from logging import PlaceHolder
from django.forms import ModelForm
from django import forms
from .models import *
from datetime import date
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Ente_Formulario(forms.ModelForm):
    #Teto remuneratório begin
    executivo = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Executivo'}), required=True)
    legislativo = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Legislativo'}), required=True)
    judiciario = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Judiciario'}), required=True)


    #Dados de cadastro do ente federativo Begin ('Adicionar foreign key')
    tipo_ente_federativo = forms.CharField(max_length=14, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ente federativo'}), required=True)
    nome_ente = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do ente federativo'}), required=True)

    #Dados de cadastro da unidade gestora
    nome_dirigente = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do dirigente'}), required=True) #Puxar da unidade gestora
    telefone = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserir o Telefone'}), required=False) #Puxar de unidade gestora
    e_mail = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserir o e-mail', 'type': 'email'}), required=True) #Puxar de unidade gestora

    #Informações de meta de rentabilidade
    meta_de_taxa_de_juros = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Taxa de juros'}), required=True)
    indexador_de_inflação = forms.ChoiceField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Indexador da inflação'}), required=False)

    #INFORMAÇÕES DE OUTROS BENEFÍCIOS
    tesouro_responsavel_por_pagar_algum_beneficio = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tesouro paga algum beneficio?'}), required=True)
    numero_da_lei_transfere_o_pagamento = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numero da lei'}), required=False)
    dispositivo_lei_transfere_pagamento = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dispositivo da lei que transfere o pagamento'}), required=False)
    data_publicacao_lei_transfere_pagamento = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data publicação lei'}), required=False)

    #PARAMETROS DE SEGREGAÇÃO DE MASSA
    atuario_responsavel_pela_criacao = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Atuario responsavel'}), required=True)
    miba = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Insira o MIBA'}), required=True)
    tipo_documento = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo do documento'}), required=True)
    numero_documento = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Numero do documento'}), required=True)
    data_documento = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data publicação lei'}), required=True)
    nome_plano = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do plano'}), required=True)
    criterio_segregacao = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Criterio de segregação de massa'}), required=True)

    #Leis vigente no ente
    numero_lei_criacao_rpps = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nº da lei de criação do RPPS'}), required=True)
    data_publicacao_lei_rpps = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data publicação lei'}), required=True)
    numero_lei_reestrutura_rpps = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nº da lei que reestrutura o RPPS'}), required=True)
    data_publicacao_reestruturou_rpps = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data publicação lei'}), required=True)
    numero_lei_define_aliquotas = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nº da lei que define as alíquotas de contribuição de custo normal praticadas'}), required=True)
    publicacao_lei_define_aliquotas = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data publicação lei'}), required=True)
    numero_lei_define_aliquotas_contribuicao = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nº da lei que define as alíquotas de contribuição de aliquotas suplementares OU aportes suplementares praticadas'}), required=True)
    data_lei_define_aliquotas_contribuicao = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data publicação lei'}), required=True)
    
    #Atualização base cadastral
    #Ativos
    ativos_base_cadastral = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ativos na base cadastral', 'value':'', 'id':'ativos_base', 'oninput':'alterar_visibilidade("ativos_base", "ativos_space")', 'list':'sim_nao'}), required=True)
    data_ultimo_recenseamento_ativos = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data ultimo recenseamento'}), required=False)
    percentual_cobertura_ativos = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Percentual de cobertura'}), required=False)

    #Aposentados
    aposentados_base_cadastral = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aposentados na base cadastral', 'id':'aposentados_base', 'oninput':'alterar_visibilidade("aposentados_base", "aposentados_space")', 'list':'sim_nao'}), required=True)
    data_ultimo_recenseamento_aposentados = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data ultimo recenseamento'}), required=False)
    percentual_cobertura_aposentados = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Percentual de cobertura'}), required=False)

    #Ativos garantidores dos compromissos do plano de benefícios do fundo previdenciário
    #Renda fixa
    renda_fixa_valor = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor renda fixa'}), required=True)
    renda_fixa_apuracao = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data apuração'}), required=True)

    #Renda variável
    renda_variavel_valor = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor renda variável'}), required=True)
    renda_variavel_apuracao = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data apuração'}), required=True)

    #Segmento Imobiliário (Bens Imóveis)
    imobiliario_valor_imoveis = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Segmento Imobiliário (Bens Imóveis)'}), required=True)
    imobiliario_apuracao_imoveis = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data apuração'}), required=True)

    #Segmento Imobiliário (Fundos Imobiliários)
    fundos_valor_imoveis = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Segmento Imobiliário (Fundos Imobiliários)'}), required=True)
    fundos_apuracao_imoveis = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data apuração'}), required=True)

    #Aplicações em enquadramento
    enquadramento_valor = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Aplicações em Enquadramento'}), required=True)
    enquadramento_apuracao = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data apuração'}), required=True)

    #Titulos e Valores não sujeitos ao enquadramento
    titulos_valores_nao_enquadramento_valor = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Titulos e Valores não sujeitos ao enquadramento'}), required=True)
    titulos_valores_nao_enquadramento_apuracao = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data apuração'}), required=True)

    #Demais bens, direitos e ativos
    bens_direitos_ativos_valor = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Demais bens, direitos e ativos'}), required=True)
    bens_direitos_ativos_apuracao = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data apuração'}), required=True)

    aliquota_ativos = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aliquota ativos'}), required=True)
    base_calculo_ativos = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Base de Cálculo ativos'}), required=True)

    aliquota_aposentados = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aliquota aposentados'}), required=True)
    base_calculo_aposentados = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Base de Cálculo aposentados'}), required=True)

    aliquota_pensionistas = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aliquota pensionistas'}), required=True)
    base_calculo_pensionistas = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Base De Cálculo Pensionistas'}), required=True)

    aliquota_patronal_servidores_ativos = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aliquota patronal sobre servidores ativos'}), required=True)
    base_calculo_aliquota_patronal = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Base De Cálculo Patronal'}), required=True)

    ente_contribui = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ente contribui?', 'id':'contribuicao_ente', 'oninput':'alterar_visibilidade("contribuicao_ente", "ente_space")', 'list':'sim_nao'}), required=True)
    base_calculo_patronal_sobre_aposentados_pensionistas = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Base de calculo patronal sobre aposentados e pensionistas', 'id':'base_calculos_id', 'oninput':'base_de_calculo("base_calculos_id")'}), required=False)
    #descreva_base_calculo = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descreva base calculo'}), required=False)

    #Administração do fundo previdenciário
    despesa_custeada = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'A DESPESA ADMINSTRATIVA É CUSTEADA...', 'id':'despesa_custeada_por', 'oninput':'func_despesa_custeada("despesa_custeada_por")', 'list':'administradoras'}), required=True)
    numero_norma_define_custeio_despesas_administrativas = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Artigo da norma que define o CUSTEIO das despesas administrativas'}), required=False)
    artigo_norma_define_custeio_despesas_administrativas = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alíquota utilizada para o cálculo do LIMITE de gastos com a despesa administrativa	'}), required=False)
    aliquota_utilizada_calculo_limite_gastos = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alíquota utilizada para o cálculo do LIMITE de gastos com a despesa administrativa'}), required=False)
    aliquota_custeio_despesas_administrativas = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alíquota utilizada para o CUSTEIO das despesas administrativas (custeio administrativo)	'}), required=False)
    aliquota_incluida_na_aliquota_patronal = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'A aliquota para o CUSTEIO das despesas administrativas está incluida na aliquota patronal informada no quadro anterior ?	'}), required=False)

    #CALCULO DO LIMITE DE GASTOS COM AS DESPESAS ADMINISTRATITVAS			
    valor_remuneracao_servidores_ativos = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor da remuneração dos servidores ativos em 2022'}), required=True)
    valor_proventos_aposentados = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor dos proventos dos aposentados em 2022'}), required=True)
    valor_proventos_pensionistas = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor dos proventos dos Pensionistas em 2022'}), required=True)

    #LEVANTAMENTO DAS DESPESAS ADMINISTRATIVAS DOS ÚLTIMOS TRÊS ANOS
    base_calculo_taxa_administracao_2022 = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Base de calculo da taxa de adminstração (para o LIMITE de gastos ) 2022'}), required=True)
    base_calculo_taxa_administracao_2021 = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Base de calculo da taxa de adminstração (para o LIMITE de gastos ) 2021'}), required=True)
    base_calculo_taxa_administracao_2020 = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Base de calculo da taxa de adminstração (para o LIMITE de gastos ) 2020'}), required=True)
    taxa_administracao_2022 = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '% da taxa de administração 2022'}), required=True)
    taxa_administracao_2021 = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '% da taxa de administração 2021'}), required=True)
    taxa_administracao_2020 = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '% da taxa de administração 2020'}), required=True)
    gastos_despesas_administrativas_2022 = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gastos com as despesas administrativas 2022'}), required=True)
    gastos_despesas_administrativas_2021 = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gastos com as despesas administrativas 2021'}), required=True)
    gastos_despesas_administrativas_2020 = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gastos com as despesas administrativas 2020'}), required=True)
    base_contribuicao_servidores_ativos_2022 = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Base de contribuição dos servidores ativos 2022'}), required=True)
    base_contribuicao_servidores_ativos_2021 = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Base de contribuição dos servidores ativos 2021'}), required=True)
    base_contribuicao_servidores_ativos_2020 = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Base de contribuição dos servidores ativos 2020'}), required=True)

    #COMPENSAÇÃO PREVIDENCIÁRIA	
    convenio_assinado_compensacao_previdenciaria = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Há convênio ASSINADO de COMPENSAÇÃO PREVIDENCIÁRIA, de servidores vinculados ao RPPS?', 'id':'convenio_assinado', 'list':'sim_nao', 'oninput':'alterar_visibilidade("convenio_assinado", "compensacao_previdenciaria_space")'}), required=True)
    informado_base_cadastral_aposentados_e_ou_pensionistas = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Foi informado na base cadastral dos aposentados e/ou pensionistas, o valor que este Ente Publico esta recebendo de compensação previdenciária?', 'list':'sim_nao', 'oninput':'func_base_cadastral("id_informado_base_cadastral_aposentados_e_ou_pensionistas")'}), required=False)
    informar_fluxo_mensal_valores_areceber = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Se NÃO, informar o fluxo mensal médio, sobre os valores a receber'}), required=False)
    informar_fluxo_mensal_a_pagar = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informar o fluxo mensal médio, sobre os valores a pagar'}), required=False)
    estoque_compensacao_previdenciaria_receber = forms.FloatField(widget=forms.TextInput(attrs={'class  ': 'form-control', 'placeholder': 'Há ESTOQUE DE COMPENSAÇÃO PREVIDENCIÁRIA para receber?', 'list':'sim_nao'}), required=False)

    #EQUACIONAMENTO DO DÉFICIT ATUARIAL	
    ente_possui_plano_equacionamento_deficit_atuarial = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'O ENTE PÚBLICO POSSUI PLANO PARA EQUACIONAMENTO DO DÉFICIT ATUARIAL (CUSTO SUPLEMENTAR)?'}), required=True)
    mes_ano_inicio_plano_equacionamento = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'QUAL É O MÊS E ANO QUE DEU INÍCIO AO PLANO DE EQUACIONAMENTO'}), required=False)
    numero_norma_define_plano_amortizacao = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NÚMERO DA NORMA QUE DEFINE O PLANO DE AMORTIZAÇÃO'}), required=False)
    data_publicacao_lei = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'DATA DA PUBLICAÇÃO DA LEI'}), required=False)

    #Constituição fundo administrativo
    constituicao_fundo_administrativo = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Há a constituição de FUNDO ADMINISTRATIVO ? (também conhecida como RESERVA ADMINISTRATIVA)', 'list':'sim_nao', 'id':'consituicao_fundo', 'oninput':'alterar_visibilidade("consituicao_fundo", "valores_rpps_space")'}), required=True)
    
    #Dados patrimoniais do RPPS
    renda_fixa_valor_rpps = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Renda Fixa'}), required=False)
    renda_fixa_valor_rpps_apuracao = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data de apuração Renda Fixa'}), required=False)
    renda_variavel_rpps = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Renda variável'}), required=False)
    renda_variavel_rpps_apuracao = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data de apuração Renda variável'}), required=False)
    segmento_imobiliario_rpps_valor = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Segmento Imobiliário'}), required=False)
    segmento_imobiliario_rpps_apuracao = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data de apuração Segmento Imobiliário'}), required=False)
    segmento_fundo_imobiliario_rpps_valor = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Fundos Imobiliários'}), required=False)
    segmento_fundo_imobiliario_rpps_apuracao = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data de apuração Fundos Imobiliários'}), required=False)
    aplicacoes_enquadramento_valor = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Aplicações em Enquadramento'}), required=False)
    aplicacoes_enquadramento_apuracao = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data de apuração Aplicações em Enquadramento'}), required=False)
    titulos_valores_nao_sujeitos_enquadramento_valor = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Titulos e Valores não Sujeitos ao Enquadramento'}), required=False)
    titulos_valores_nao_sujeitos_enquadramento_apuracao = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data de apuração Titulos e Valores não Sujeitos ao Enquadramento'}), required=False)
    demais_bens_valor = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Demais Bens'}), required=False)
    demais_bens_apuracao = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data de apuração Demais Bens'}), required=False)

    #Acordo parcelamento de dividas
    existem_acordos_de_parcelamento_dividas = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'EXISTE(M) ACORDO(S) DE PARCELAMENTO DE DÍVIDAS DO ENTE COM O RPPS ENVIADOS PARA A SPREV ?', 'id':'acordos_parcelamentos', 'oninput':'alterar_visibilidade("acordos_parcelamentos", "acordos_space")', 'list':'sim_nao'}), required=True)
    acordo = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ACORDO Nº (conforme DIPR)'}), required=False)
    data_aprovacao = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Lei / data de aprovação   '}), required=False)
    juros = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Juros ( % a.m.) '}), required=False)
    tipo_juros = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo de juros'}), required=False)
    numero_da_prestacao = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nº da prestação em 31/12/22'}), required=False)
    indice_atualizacao = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Índice de atualização'}), required=False)
    ano_acordo = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ano do acordo'}), required=False)
    valor_divida = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Valor da dívida (em R$)'}), required=False)
    valor_prestacao = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Valor prestação em 31/12/22'}), required=False)
    prazo_total_meses = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Prazo total em meses'}), required=False)
    saldo_devedor = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Saldo devedor em 31/12/22'}), required=False)
    acordo_adimplente = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Acordo adimplente?'}), required=False)

    ###################################################################
    ######################### Segregado ###############################
    ###################################################################

    #Dados patrimoniais do RPPS Segregado
    renda_fixa_valor_rpps_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Renda Fixa'}), required=False)
    renda_fixa_valor_rpps_apuracao_segregado = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data de apuração Renda Fixa'}), required=False)
    renda_variavel_rpps_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Renda variável'}), required=False)
    renda_variavel_rpps_apuracao_segregado = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data de apuração Renda variável'}), required=False)
    segmento_imobiliario_rpps_valor_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Segmento Imobiliário'}), required=False)
    segmento_imobiliario_rpps_apuracao_segregado = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data de apuração Segmento Imobiliário'}), required=False)
    segmento_fundo_imobiliario_rpps_valor_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Fundos Imobiliários'}), required=False)
    segmento_fundo_imobiliario_rpps_apuracao_segregado = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data de apuração Fundos Imobiliários'}), required=False)
    aplicacoes_enquadramento_valor_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Aplicações em Enquadramento'}), required=False)
    aplicacoes_enquadramento_apuracao_segregado = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data de apuração Aplicações em Enquadramento'}), required=False)
    titulos_valores_nao_sujeitos_enquadramento_valor_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Titulos e Valores não Sujeitos ao Enquadramento'}), required=False)
    titulos_valores_nao_sujeitos_enquadramento_apuracao_segregado = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data de apuração Titulos e Valores não Sujeitos ao Enquadramento'}), required=False)
    demais_bens_valor_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Demais Bens'}), required=False)
    demais_bens_apuracao_segregado = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data de apuração Demais Bens'}), required=False)

    #Alíquotas de contribuição previdenciária
    #Alíquota servidores ATIVOS
    aliquota_ativos_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aliquota ativos'}), required=False)
    base_calculo_ativos_segregado = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Base de Cálculo ativos'}), required=False)

    #Alíquota servidores APOSENTADOS
    aliquota_aposentados_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aliquota aposentados'}), required=False)
    base_calculo_aposentados_segregado = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Base de Cálculo aposentados'}), required=False)

    #Alíquota servidores PENSIONISTAS
    aliquota_pensionistas_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aliquota pensionistas'}), required=False)
    base_calculo_pensionistas_segregado = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Base De Cálculo Pensionistas'}), required=False)

    #Alíquota PATRONAL relativo aos servidores ativos (CUSTO NORMAL)
    aliquota_patronal_servidores_ativos_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aliquota patronal sobre servidores ativos'}), required=False)
    base_calculo_aliquota_patronal_segregado = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Base De Cálculo Patronal'}), required=False)

    #O ente contribui sobre os aposentados e pensionistas
    ente_contribui_segregado = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ente contribui?', 'id':'contribuicao_ente_segregado', 'oninput':'alterar_visibilidade("contribuicao_ente_segregado", "ente_contribui_segregado_space")', 'list':'sim_nao'}), required=False)
    base_calculo_patronal_sobre_aposentados_pensionistas_segregado = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Base de calculo patronal sobre aposentados e pensionistas', 'id':'base_calculos_id_segregado'}), required=False)

    #Administração do fundo previdenciário
    despesa_custeada_segregado = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'A DESPESA ADMINSTRATIVA É CUSTEADA...', 'id':'despesa_custeada_por_segregado', 'oninput':'alterar_visibilidade("despesa_custeada_por_segregado", "despesa_segregado_space")', 'list':'administradoras'}), required=False)
    numero_norma_define_custeio_despesas_administrativas_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número da norma que define o CUSTEIO das despesas administrativas'}), required=False)
    artigo_norma_define_custeio_despesas_administrativas_segregado = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Artigo da norma que define o CUSTEIO das despesas administrativas'}), required=False)
    aliquota_utilizada_calculo_limite_gastos_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alíquota utilizada para o cálculo do LIMITE de gastos com a despesa administrativa'}), required=False)
    aliquota_custeio_despesas_administrativas_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alíquota utilizada para o CUSTEIO das despesas administrativas (custeio administrativo)'}), required=False)
    aliquota_incluida_na_aliquota_patronal_segregado = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'A aliquota para o CUSTEIO das despesas administrativas está incluida na aliquota patronal informada no quadro anterior ?'}), required=False)

    #CALCULO DO LIMITE DE GASTOS COM AS DESPESAS ADMINISTRATITVAS			
    valor_remuneracao_servidores_ativos_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor da remuneração dos servidores ativos em 2022'}), required=False)
    valor_proventos_aposentados_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor dos proventos dos aposentados em 2022'}), required=False)
    valor_proventos_pensionistas_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor dos proventos dos Pensionistas em 2022'}), required=False)

    #LEVANTAMENTO DAS DESPESAS ADMINISTRATIVAS DOS ÚLTIMOS TRÊS ANOS
    base_calculo_taxa_administracao_2022_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Base de calculo da taxa de adminstração (para o LIMITE de gastos ) 2022'}), required=False)
    base_calculo_taxa_administracao_2021_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Base de calculo da taxa de adminstração (para o LIMITE de gastos ) 2021'}), required=False)
    base_calculo_taxa_administracao_2020_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Base de calculo da taxa de adminstração (para o LIMITE de gastos ) 2020'}), required=False)
    taxa_administracao_2022_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '% da taxa de administração 2022'}), required=False)
    taxa_administracao_2021_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '% da taxa de administração 2021'}), required=False)
    taxa_administracao_2020_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '% da taxa de administração 2020'}), required=False)
    gastos_despesas_administrativas_2022_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gastos com as despesas administrativas 2022'}), required=False)
    gastos_despesas_administrativas_2021_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gastos com as despesas administrativas 2021'}), required=False)
    gastos_despesas_administrativas_2020_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gastos com as despesas administrativas 2020'}), required=False)
    base_contribuicao_servidores_ativos_2022_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Base de contribuição dos servidores ativos 2022'}), required=False)
    base_contribuicao_servidores_ativos_2021_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Base de contribuição dos servidores ativos 2021'}), required=False)
    base_contribuicao_servidores_ativos_2020_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Base de contribuição dos servidores ativos 2020'}), required=False)

    #COMPENSAÇÃO PREVIDENCIÁRIA	SEGREGADO
    convenio_assinado_compensacao_previdenciaria_segregado = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Há convênio ASSINADO de COMPENSAÇÃO PREVIDENCIÁRIA, de servidores vinculados ao RPPS?', 'id':'convenio_assinado', 'list':'sim_nao', 'oninput':'ha_convenio_assinado("convenio_assinado")'}), required=True)
    informado_base_cadastral_aposentados_e_ou_pensionistas_segregado = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Foi informado na base cadastral dos aposentados e/ou pensionistas, o valor que este Ente Publico esta recebendo de compensação previdenciária?', 'list':'sim_nao', 'oninput':'func_base_cadastral("id_informado_base_cadastral_aposentados_e_ou_pensionistas")'}), required=False)
    informar_fluxo_mensal_valores_areceber_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Se NÃO, informar o fluxo mensal médio, sobre os valores a receber'}), required=False)
    informar_fluxo_mensal_a_pagar_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informar o fluxo mensal médio, sobre os valores a pagar'}), required=False)
    estoque_compensacao_previdenciaria_receber_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class  ': 'form-control', 'placeholder': 'Há ESTOQUE DE COMPENSAÇÃO PREVIDENCIÁRIA para receber?', 'list':'sim_nao'}), required=False)

    #EQUACIONAMENTO DO DÉFICIT ATUARIAL	
    ente_possui_plano_equacionamento_deficit_atuarial_segregado = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'O ENTE PÚBLICO POSSUI PLANO PARA EQUACIONAMENTO DO DÉFICIT ATUARIAL (CUSTO SUPLEMENTAR)?'}), required=False)
    mes_ano_inicio_plano_equacionamento_segregado = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'QUAL É O MÊS E ANO QUE DEU INÍCIO AO PLANO DE EQUACIONAMENTO'}), required=False)
    numero_norma_define_plano_amortizacao_segregado = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NÚMERO DA NORMA QUE DEFINE O PLANO DE AMORTIZAÇÃO'}), required=False)
    data_publicacao_lei_segregado = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'DATA DA PUBLICAÇÃO DA LEI'}), required=False)

    #Constituição fundo administrativo
    constituicao_fundo_administrativo_segregado = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Há a constituição de FUNDO ADMINISTRATIVO ? (também conhecida como RESERVA ADMINISTRATIVA)', 'list':'sim_nao', 'id':'consituicao_fundo_segregado', 'oninput':'alterar_visibilidade("consituicao_fundo_segregado")'}), required=True)
    
    #Dados patrimoniais do RPPS
    renda_fixa_valor_rpps_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Renda Fixa'}), required=False)
    renda_fixa_valor_rpps_apuracao_segregado = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data de apuração Renda Fixa'}), required=False)
    renda_variavel_rpps_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Renda variável'}), required=False)
    renda_variavel_rpps_apuracao_segregado = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data de apuração Renda variável'}), required=False)
    segmento_imobiliario_rpps_valor_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Segmento Imobiliário'}), required=False)
    segmento_imobiliario_rpps_apuracao_segregado = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data de apuração Segmento Imobiliário'}), required=False)
    segmento_fundo_imobiliario_rpps_valor_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Fundos Imobiliários'}), required=False)
    segmento_fundo_imobiliario_rpps_apuracao_segregado = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data de apuração Fundos Imobiliários'}), required=False)
    aplicacoes_enquadramento_valor_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Aplicações em Enquadramento'}), required=False)
    aplicacoes_enquadramento_apuracao_segregado = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data de apuração Aplicações em Enquadramento'}), required=False)
    titulos_valores_nao_sujeitos_enquadramento_valor_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Titulos e Valores não Sujeitos ao Enquadramento'}), required=False)
    titulos_valores_nao_sujeitos_enquadramento_apuracao_segregado = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data de apuração Titulos e Valores não Sujeitos ao Enquadramento'}), required=False)
    demais_bens_valor_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor Demais Bens'}), required=False)
    demais_bens_apuracao_segregado = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Data de apuração Demais Bens'}), required=False)

    #Acordo parcelamento de dividas
    existem_acordos_de_parcelamento_dividas_segregado = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'EXISTE(M) ACORDO(S) DE PARCELAMENTO DE DÍVIDAS DO ENTE COM O RPPS ENVIADOS PARA A SPREV ?', 'id':'acordos_parcelamentos_segregado', 'oninput':'alterar_visibilidade("acordos_parcelamentos_segregado", "acordo_segregado_space")', 'list':'sim_nao'}), required=False)

    class Meta:
        model = Formulario
        fields = '__all__'

class AcordoParcelamentoForm(forms.ModelForm):
        #Acordo parcelamento de dividas
    acordo_segregado = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ACORDO Nº (conforme DIPR)'}), required=False)
    data_aprovacao_segregado = forms.DateField(widget=DateForm(attrs={'class': 'form-control', 'placeholder': 'Lei / data de aprovação   '}), required=False)
    juros_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Juros ( % a.m.) '}), required=False)
    tipo_juros_segregado = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tipo de juros'}), required=False)
    numero_da_prestacao_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nº da prestação em 31/12/22'}), required=False)
    indice_atualizacao_segregado = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Índice de atualização'}), required=False)
    ano_acordo_segregado = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ano do acordo'}), required=False)
    valor_divida_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Valor da dívida (em R$)'}), required=False)
    valor_prestacao_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Valor prestação em 31/12/22'}), required=False)
    prazo_total_meses_segregado = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Prazo total em meses'}), required=False)
    saldo_devedor_segregado = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Saldo devedor em 31/12/22'}), required=False)
    acordo_adimplente_segregado = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Acordo adimplente?'}), required=False)

    class Meta:
        model = AcordoParcelamento
        fields = '__all__'