from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
now = timezone.now()


class Formulario(models.Model):
    #Teto remuneratório begin
    executivo = models.FloatField(verbose_name='EXECUTIVO', null=False, blank=False, default=0)
    legislativo = models.FloatField(verbose_name='LEGISLATIVO', null=False, blank=False, default=0)
    judiciario = models.FloatField(verbose_name='JUDICIARIO', null=False, blank=False, default=0)

    #Dados de cadastro do ente federativo Begin ('Adicionar foreign key')
    tipo_ente_federativo = models.CharField(verbose_name='TIPO_ENTE_FEDERATIVO', max_length=14, null=True, blank=False, default='None') #Puxar de unidade gestora
    nome_ente = models.CharField(verbose_name='NOME_ENTE', max_length=50, null=False, blank=False, default=None)

    #Dados de cadastro da unidade gestora
    nome_dirigente = models.CharField(verbose_name='NOME DO DIRIGENTE', max_length=50, null=False, blank=False, default='Nenhum') #Puxar de unidade gestora
    telefone = models.CharField(verbose_name='Telefone', max_length=11, null=True, blank=True, default=00000000000) #Puxar de unidade gestora
    e_mail = models.EmailField(verbose_name='E-mail', null=False, blank=False, default='noemailreceived@gmail.com') #Puxar de unidade gestora

    #Informações de meta de rentabilidade
    meta_de_taxa_de_juros = models.FloatField(verbose_name='TAXA DE JUROS', null=False, blank=False, default=0)
    indexador_de_inflação = models.CharField(verbose_name='INDEXADOR DA INFLAÇAO', max_length=15, null=False, blank=False, default=None, choices=(('INPC', 'INPC'),('IPCA', 'IPCA'),('IGPM', 'IGPM'),('SELIC', 'SELIC')))

    #Informações de outros benefícios
    tesouro_responsavel_por_pagar_algum_beneficio = models.CharField(verbose_name='TRPAB', max_length=3, null=True, blank=True, default='Não')
    numero_da_lei_transfere_o_pagamento = models.FloatField(verbose_name='NLTP', null=False, blank=False, default=0)
    dispositivo_lei_transfere_pagamento = models.CharField(verbose_name='DLTP', null=True, blank=True, max_length=50, default='Não transfere')
    data_publicacao_lei_transfere_pagamento = models.DateField(verbose_name='Data Publicação', null=True, blank=True)

    #Parametros de segregação de massa
    atuario_responsavel_pela_criacao = models.CharField(verbose_name='Atuario Responsável', null=True, blank=True, max_length=50)
    miba = models.IntegerField(verbose_name='MIBA', null=True, blank=True)
    tipo_documento = models.CharField(verbose_name='Tipo do documento', null=True, blank=True, max_length=25)
    numero_documento = models.IntegerField(verbose_name='Numero do documento', null=True, blank=True)
    data_documento = models.DateField(verbose_name='Data do documento', null=True, blank=True)
    nome_plano = models.CharField(verbose_name='Nome do plano', null=True, blank=True, max_length=50)
    criterio_segregacao = models.CharField(verbose_name='Criterio segregação de massa', null=True, blank=True, max_length=25)

    #Leis vigente no ente
    numero_lei_criacao_rpps = models.IntegerField(verbose_name='Numero da lei de criação do RPPS', null=True, blank=True)
    data_publicacao_lei_rpps = models.DateField(verbose_name='Data publicação da lei', null=True, blank=True)
    numero_lei_reestrutura_rpps = models.IntegerField(verbose_name='Numero da lei que reestrutura o RPPS', null=True, blank=True)
    data_publicacao_reestruturou_rpps = models.DateField(verbose_name='Data publicação da lei que reestruturou o RPPS', null=True, blank=True)
    numero_lei_define_aliquotas = models.IntegerField(verbose_name='Numero da lei que define aliquotas de contribuição', null=True, blank=True)
    publicacao_lei_define_aliquotas = models.DateField(verbose_name='Data publicação da lei que define aliquotas de contribuição', null=True, blank=True)
    numero_lei_define_aliquotas_contribuicao = models.IntegerField(verbose_name='Numero da lei que define as aliquotas de contribuição de aliquotas suplementares', null=True, blank=True)
    data_lei_define_aliquotas_contribuicao = models.DateField(verbose_name='Data publicação da lei que define aliquotas de contribuição de aliquotas suplementares', null=True, blank=True)

    #Atualização base cadastral
    #Ativos
    ativos_base_cadastral = models.CharField(verbose_name='Ativos base cadastral', null=True, blank=True, max_length=3, default='Não')
    data_ultimo_recenseamento_ativos = models.DateField(verbose_name='Data do Último Recenseamento Previdenciário', null=True, blank=True)
    percentual_cobertura_ativos = models.FloatField(verbose_name='Percentual de cobertura', null=True, blank=True, default=0)
    
    #Aposentados
    aposentados_base_cadastral = models.CharField(verbose_name='Aposentados base cadastral', null=True, blank=True, max_length=3, default='Não')
    data_ultimo_recenseamento_aposentados = models.DateField(verbose_name='Data do Último Recenseamento Previdenciário', null=True, blank=True)
    percentual_cobertura_aposentados = models.FloatField(verbose_name='Percentual de cobertura', null=True, blank=True, default=0)

    #Ativos garantidores dos compromissos do plano de benefícios do fundo previdenciário
    #Renda fixa
    renda_fixa_valor = models.FloatField(verbose_name='Valor', null=True, blank=True, default=0)
    renda_fixa_apuracao = models.DateField(verbose_name='Data de apuração', null=True, blank=True)

    #Renda variável
    renda_variavel_valor = models.FloatField(verbose_name='Valor', null=True, blank=True, default=0)
    renda_variavel_apuracao = models.DateField(verbose_name='Data de apuração', null=True, blank=True)

    #Segmento Imobiliário (Bens Imóveis)
    imobiliario_valor_imoveis = models.FloatField(verbose_name='Valor', null=True, blank=True, default=0)
    imobiliario_apuracao_imoveis = models.DateField(verbose_name='Data de apuração', null=True, blank=True)

    #Segmento Imobiliário (Fundos Imobiliários)
    fundos_valor_imoveis = models.FloatField(verbose_name='Valor', null=True, blank=True, default=0)
    fundos_apuracao_imoveis = models.DateField(verbose_name='Data de apuração', null=True, blank=True)

    #Aplicações em enquadramento
    enquadramento_valor = models.FloatField(verbose_name='Valor', null=True, blank=True, default=0)
    enquadramento_apuracao = models.DateField(verbose_name='Data de apuração', null=True, blank=True)

    #Titulos e Valores não sujeitos ao enquadramento
    titulos_valores_nao_enquadramento_valor = models.FloatField(verbose_name='Valor', null=True, blank=True, default=0)
    titulos_valores_nao_enquadramento_apuracao = models.DateField(verbose_name='Data de apuração', null=True, blank=True)

    #Demais bens, direitos e ativos
    bens_direitos_ativos_valor = models.FloatField(verbose_name='Valor', null=True, blank=True, default=0)
    bens_direitos_ativos_apuracao = models.DateField(verbose_name='Data de apuração', null=True, blank=True)

    #Alíquotas de contribuição previdenciária
    #Alíquota servidores ATIVOS
    aliquota_ativos = models.FloatField(verbose_name='Valor', null=True, blank=True, default=0)
    base_calculo_ativos = models.CharField(verbose_name='Base de cálculo Ativos', null=True, blank=True, max_length=50)

    #Alíquota servidores APOSENTADOS
    aliquota_aposentados = models.FloatField(verbose_name='Valor', null=True, blank=True, default=0)
    base_calculo_aposentados = models.CharField(verbose_name='Base de cálculo Aposentados', null=True, blank=True, max_length=50)

    #Alíquota servidores PENSIONISTAS
    aliquota_pensionistas = models.FloatField(verbose_name='Valor', null=True, blank=True, default=0)
    base_calculo_pensionistas = models.CharField(verbose_name='Base de cálculo Pensionistas', null=True, blank=True, max_length=50)

    #Alíquota PATRONAL relativo aos servidores ativos (CUSTO NORMAL)
    aliquota_patronal_servidores_ativos = models.FloatField(verbose_name='Valor', null=True, blank=True, default=0)
    base_calculo_aliquota_patronal = models.CharField(verbose_name='Base de cálculo Patronal', null=True, blank=True, max_length=50)

    #O ente contribui sobre os aposentados e pensionistas
    ente_contribui = models.CharField(verbose_name='Ente contribui?', null=True, blank=True, max_length=3)
    base_calculo_patronal_sobre_aposentados_pensionistas = models.CharField(verbose_name='Base de patronal sobre aposentados e pensionistas', null=True, blank=True, max_length=50)

    ################# A partir daqui n tem o HTML criar ele ##############################

    #Administração do fundo previdenciário
    despesa_custeada = models.CharField(verbose_name='Despesa custeada ...', null=True, blank=True, max_length=50)
    numero_norma_define_custeio_despesas_administrativas = models.FloatField(verbose_name='Numero da norma que define o custeio', null=True, blank=True)
    artigo_norma_define_custeio_despesas_administrativas = models.CharField(verbose_name='Artigo que define o custeio', null=True, blank=True, max_length=50)
    aliquota_utilizada_calculo_limite_gastos = models.FloatField(verbose_name='Alíquota utilizada para cálculo do LIMITE de gastos com a despesa administrativa', null=True, blank=True)
    aliquota_custeio_despesas_administrativas = models.FloatField(verbose_name='Alíquota utilizada para o CUSTEIO das despesas administrativas (custeio administrativo)', null=True, blank=True)
    aliquota_incluida_na_aliquota_patronal = models.CharField(verbose_name='Artigo que define o custeio', null=True, blank=True, max_length=3)

    #CALCULO DO LIMITE DE GASTOS COM AS DESPESAS ADMINISTRATITVAS			
    valor_remuneracao_servidores_ativos = models.FloatField(verbose_name='Valor da remuneração dos servidores ativos em 2022', null=True, blank=True)
    valor_proventos_aposentados = models.FloatField(verbose_name='Valor dos proventos dos aposentados em 2022', null=True, blank=True)
    valor_proventos_pensionistas = models.FloatField(verbose_name='Valor dos proventos dos Pensionistas em 2022	', null=True, blank=True)

    #LEVANTAMENTO DAS DESPESAS ADMINISTRATIVAS DOS ÚLTIMOS TRÊS ANOS			
    base_calculo_taxa_administracao_2022 = models.FloatField(verbose_name='Base de calculo da taxa de adminstração (para o LIMITE de gastos ) 2022', null=True, blank=True)
    base_calculo_taxa_administracao_2021 = models.FloatField(verbose_name='Base de calculo da taxa de adminstração (para o LIMITE de gastos ) 2021', null=True, blank=True)
    base_calculo_taxa_administracao_2020 = models.FloatField(verbose_name='Base de calculo da taxa de adminstração (para o LIMITE de gastos ) 2020', null=True, blank=True)
    taxa_administracao_2022 = models.FloatField(verbose_name='% da taxa de administração 2022', null=True, blank=True)
    taxa_administracao_2021 = models.FloatField(verbose_name='% da taxa de administração 2021', null=True, blank=True)
    taxa_administracao_2020 = models.FloatField(verbose_name='% da taxa de administração 2020', null=True, blank=True)
    gastos_despesas_administrativas_2022 = models.FloatField(verbose_name='Gastos com as despesas administrativas 2022', null=True, blank=True)
    gastos_despesas_administrativas_2021 = models.FloatField(verbose_name='Gastos com as despesas administrativas 2021', null=True, blank=True)
    gastos_despesas_administrativas_2020 = models.FloatField(verbose_name='Gastos com as despesas administrativas 2020', null=True, blank=True)
    base_contribuicao_servidores_ativos_2022 = models.FloatField(verbose_name='Base de contribuição dos servidores ativos 2022', null=True, blank=True)
    base_contribuicao_servidores_ativos_2021 = models.FloatField(verbose_name='Base de contribuição dos servidores ativos 2021', null=True, blank=True)
    base_contribuicao_servidores_ativos_2020 = models.FloatField(verbose_name='Base de contribuição dos servidores ativos 2020', null=True, blank=True)
    
    #COMPENSAÇÃO PREVIDENCIÁRIA			
    convenio_assinado_compensacao_previdenciaria = models.CharField(verbose_name='Há convênio ASSINADO de COMPENSAÇÃO PREVIDENCIÁRIA, de servidores vinculados ao RPPS?	', null=True, blank=True, max_length=3) # Adicionar condicional
    informado_base_cadastral_aposentados_e_ou_pensionistas = models.CharField(verbose_name='Foi informado na base cadastral dos aposentados e/ou pensionistas, o valor que este Ente Publico esta recebendo de compensação previdenciária?	', null=True, blank=True, max_length=3) # Adicionar condicional
    informar_fluxo_mensal_valores_areceber = models.FloatField(verbose_name='Se NÃO, informar o fluxo mensal médio, sobre os valores a receber', null=True, blank=True)
    informar_fluxo_mensal_a_pagar = models.FloatField(verbose_name='Informar o fluxo mensal médio, sobre os valores a pagar', null=True, blank=True)
    estoque_compensacao_previdenciaria_receber = models.FloatField(verbose_name='Há ESTOQUE DE COMPENSAÇÃO PREVIDENCIÁRIA para receber?', null=True, blank=True)

    #EQUACIONAMENTO DO DÉFICIT ATUARIAL			
    ente_possui_plano_equacionamento_deficit_atuarial = models.CharField(verbose_name='O ENTE PÚBLICO POSSUI PLANO PARA EQUACIONAMENTO DO DÉFICIT ATUARIAL (CUSTO SUPLEMENTAR)?', null=True, blank=True, max_length=25)

    #FUNDO PREVIDENCIARIO
    mes_ano_inicio_plano_equacionamento = models.DateField(verbose_name='QUAL É O MÊS E ANO QUE DEU INÍCIO AO PLANO DE EQUACIONAMENTO', null=True, blank=True)
    numero_norma_define_plano_amortizacao = models.CharField(verbose_name='NÚMERO DA NORMA QUE DEFINE O PLANO DE AMORTIZAÇÃO', null=True, blank=True, max_length=25)
    data_publicacao_lei = models.DateField(verbose_name='DATA DA PUBLICAÇÃO DA LEI', null=True, blank=True)

    #Constituição fundo administrativo
    constituicao_fundo_administrativo = models.CharField(verbose_name='Há constituição de Fundo Administrativo', null=True, blank=True, max_length=3) # Adicionar condicional / Adicionar choice field

    #Dados patrimoniais do RPPS
    renda_fixa_valor_rpps = models.FloatField(verbose_name='Valor renda fixa', null=True, blank=True)
    renda_fixa_valor_rpps_apuracao = models.DateField(verbose_name='Data de apuração', null=True, blank=True)
    renda_variavel_rpps = models.FloatField(verbose_name='Valor renda variável', null=True, blank=True)
    renda_variavel_rpps_apuracao = models.DateField(verbose_name='Data de apuração', null=True, blank=True)
    segmento_imobiliario_rpps_valor = models.FloatField(verbose_name='Valor segmento imobiliario', null=True, blank=True)
    segmento_imobiliario_rpps_apuracao = models.DateField(verbose_name='Data de apuração', null=True, blank=True)
    segmento_fundo_imobiliario_rpps_valor = models.FloatField(verbose_name='Valor fundos imobiliarios', null=True, blank=True)
    segmento_fundo_imobiliario_rpps_apuracao = models.DateField(verbose_name='Data de apuração', null=True, blank=True)
    aplicacoes_enquadramento_valor = models.FloatField(verbose_name='Valor aplicações em enquadramento', null=True, blank=True)
    aplicacoes_enquadramento_apuracao = models.DateField(verbose_name='Data de apuração', null=True, blank=True)
    titulos_valores_nao_sujeitos_enquadramento_valor = models.FloatField(verbose_name='Valor titulos e valores não sujeitos ao enquadramento', null=True, blank=True)
    titulos_valores_nao_sujeitos_enquadramento_apuracao = models.DateField(verbose_name='Data de apuração', null=True, blank=True)
    demais_bens_valor = models.FloatField(verbose_name='Valor demais bens', null=True, blank=True)
    demais_bens_apuracao = models.DateField(verbose_name='Data de apuração', null=True, blank=True)

    #Acordo parcelamento de dividas
    existem_acordos_de_parcelamento_dividas = models.CharField(verbose_name='Existe(m) acordo(s) de parcelamento de dívidas do ente com o RPPS?', null=True, blank=True, max_length=3) # Implementar botão de adicionar
    acordo = models.CharField(verbose_name='Acordo N°', null=True, blank=True, max_length=15)
    data_aprovacao = models.DateField(verbose_name='Data de aprovação', null=True, blank=True)
    juros = models.FloatField(verbose_name='Valor juros', null=True, blank=True)
    tipo_juros = models.CharField(verbose_name='Tipo de juros°', null=True, blank=True, max_length=15)
    numero_da_prestacao = models.CharField(verbose_name='Numero da prestação em 31/12/22', null=True, blank=True, max_length=15)
    indice_atualizacao = models.CharField(verbose_name='Indice de atualização', null=True, blank=True, max_length=15)
    ano_acordo = models.DateField(verbose_name='Ano do acordo', null=True, blank=True)
    valor_divida = models.FloatField(verbose_name='Valor da dívida', null=True, blank=True)
    valor_prestacao = models.FloatField(verbose_name='Valor da prestação em 31/12/22', null=True, blank=True)
    prazo_total_meses = models.FloatField(verbose_name='Prazo total em meses', null=True, blank=True)
    saldo_devedor = models.FloatField(verbose_name='Saldo devedor em 31/12/22', null=True, blank=True)
    acordo_adimplente = models.CharField(verbose_name='Acordo adimplente', null=True, blank=True, max_length=3)

    ####################################################################################
    ################################ SEGREGADO #########################################
    ####################################################################################

    #Dados patrimoniais do RPPS Segregado
    renda_fixa_valor_rpps_segregado = models.FloatField(verbose_name='Valor renda fixa', null=True, blank=True)
    renda_fixa_valor_rpps_apuracao_segregado = models.DateField(verbose_name='Data de apuração', null=True, blank=True)
    renda_variavel_rpps_segregado = models.FloatField(verbose_name='Valor renda variável', null=True, blank=True)
    renda_variavel_rpps_apuracao_segregado = models.DateField(verbose_name='Data de apuração', null=True, blank=True)
    segmento_imobiliario_rpps_valor_segregado = models.FloatField(verbose_name='Valor segmento imobiliario', null=True, blank=True)
    segmento_imobiliario_rpps_apuracao_segregado = models.DateField(verbose_name='Data de apuração', null=True, blank=True)
    segmento_fundo_imobiliario_rpps_valor_segregado = models.FloatField(verbose_name='Valor fundos imobiliarios', null=True, blank=True)
    segmento_fundo_imobiliario_rpps_apuracao_segregado = models.DateField(verbose_name='Data de apuração', null=True, blank=True)
    aplicacoes_enquadramento_valor_segregado = models.FloatField(verbose_name='Valor aplicações em enquadramento', null=True, blank=True)
    aplicacoes_enquadramento_apuracao_segregado = models.DateField(verbose_name='Data de apuração', null=True, blank=True)
    titulos_valores_nao_sujeitos_enquadramento_valor_segregado = models.FloatField(verbose_name='Valor titulos e valores não sujeitos ao enquadramento', null=True, blank=True)
    titulos_valores_nao_sujeitos_enquadramento_apuracao_segregado = models.DateField(verbose_name='Data de apuração', null=True, blank=True)
    demais_bens_valor_segregado = models.FloatField(verbose_name='Valor demais bens', null=True, blank=True)
    demais_bens_apuracao_segregado = models.DateField(verbose_name='Data de apuração', null=True, blank=True)

    #Alíquotas de contribuição previdenciária
    #Alíquota servidores ATIVOS
    aliquota_ativos_segregado = models.FloatField(verbose_name='Valor', null=True, blank=True, default=0)
    base_calculo_ativos_segregado = models.CharField(verbose_name='Base de cálculo Ativos', null=True, blank=True, max_length=50)

    #Alíquota servidores APOSENTADOS
    aliquota_aposentados_segregado = models.FloatField(verbose_name='Valor', null=True, blank=True, default=0)
    base_calculo_aposentados_segregado = models.CharField(verbose_name='Base de cálculo Aposentados', null=True, blank=True, max_length=50)

    #Alíquota servidores PENSIONISTAS
    aliquota_pensionistas_segregado = models.FloatField(verbose_name='Valor', null=True, blank=True, default=0)
    base_calculo_pensionistas_segregado = models.CharField(verbose_name='Base de cálculo Pensionistas', null=True, blank=True, max_length=50)

    #Alíquota PATRONAL relativo aos servidores ativos (CUSTO NORMAL)
    aliquota_patronal_servidores_ativos_segregado = models.FloatField(verbose_name='Valor', null=True, blank=True, default=0)
    base_calculo_aliquota_patronal_segregado = models.CharField(verbose_name='Base de cálculo Patronal', null=True, blank=True, max_length=50)

    #O ente contribui sobre os aposentados e pensionistas
    ente_contribui_segregado = models.CharField(verbose_name='Ente contribui?', null=True, blank=True, max_length=3)
    base_calculo_patronal_sobre_aposentados_pensionistas_segregado = models.CharField(verbose_name='Base de patronal sobre aposentados e pensionistas', null=True, blank=True, max_length=100)
    #descreva_base_calculo_segregado = models.TextField(verbose_name='Descreva a base de cálculo relativo a contribuição PATRONAL', null=True, blank=True)

    #Administração do fundo previdenciário
    despesa_custeada_segregado = models.CharField(verbose_name='Despesa custeada ...', null=True, blank=True, max_length=50)
    numero_norma_define_custeio_despesas_administrativas_segregado = models.FloatField(verbose_name='Numero da norma que define o custeio', null=True, blank=True)
    artigo_norma_define_custeio_despesas_administrativas_segregado = models.CharField(verbose_name='Artigo que define o custeio', null=True, blank=True, max_length=50)
    aliquota_utilizada_calculo_limite_gastos_segregado = models.FloatField(verbose_name='Alíquota utilizada para cálculo do LIMITE de gastos com a despesa administrativa', null=True, blank=True)
    aliquota_custeio_despesas_administrativas_segregado = models.FloatField(verbose_name='Alíquota utilizada para o CUSTEIO das despesas administrativas (custeio administrativo)', null=True, blank=True)
    aliquota_incluida_na_aliquota_patronal_segregado = models.CharField(verbose_name='Artigo que define o custeio', null=True, blank=True, max_length=3)

    #CALCULO DO LIMITE DE GASTOS COM AS DESPESAS ADMINISTRATITVAS			
    valor_remuneracao_servidores_ativos_segregado = models.FloatField(verbose_name='Valor da remuneração dos servidores ativos em 2022', null=True, blank=True)
    valor_proventos_aposentados_segregado = models.FloatField(verbose_name='Valor dos proventos dos aposentados em 2022', null=True, blank=True)
    valor_proventos_pensionistas_segregado = models.FloatField(verbose_name='Valor dos proventos dos Pensionistas em 2022	', null=True, blank=True)

    #LEVANTAMENTO DAS DESPESAS ADMINISTRATIVAS DOS ÚLTIMOS TRÊS ANOS			
    base_calculo_taxa_administracao_2022_segregado = models.FloatField(verbose_name='Base de calculo da taxa de adminstração (para o LIMITE de gastos ) 2022', null=True, blank=True)
    base_calculo_taxa_administracao_2021_segregado = models.FloatField(verbose_name='Base de calculo da taxa de adminstração (para o LIMITE de gastos ) 2021', null=True, blank=True)
    base_calculo_taxa_administracao_2020_segregado = models.FloatField(verbose_name='Base de calculo da taxa de adminstração (para o LIMITE de gastos ) 2020', null=True, blank=True)
    taxa_administracao_2022_segregado = models.FloatField(verbose_name='% da taxa de administração 2022', null=True, blank=True)
    taxa_administracao_2021_segregado = models.FloatField(verbose_name='% da taxa de administração 2021', null=True, blank=True)
    taxa_administracao_2020_segregado = models.FloatField(verbose_name='% da taxa de administração 2020', null=True, blank=True)
    gastos_despesas_administrativas_2022_segregado = models.FloatField(verbose_name='Gastos com as despesas administrativas 2022', null=True, blank=True)
    gastos_despesas_administrativas_2021_segregado = models.FloatField(verbose_name='Gastos com as despesas administrativas 2021', null=True, blank=True)
    gastos_despesas_administrativas_2020_segregado = models.FloatField(verbose_name='Gastos com as despesas administrativas 2020', null=True, blank=True)
    base_contribuicao_servidores_ativos_2022_segregado = models.FloatField(verbose_name='Base de contribuição dos servidores ativos 2022', null=True, blank=True)
    base_contribuicao_servidores_ativos_2021_segregado = models.FloatField(verbose_name='Base de contribuição dos servidores ativos 2021', null=True, blank=True)
    base_contribuicao_servidores_ativos_2020_segregado = models.FloatField(verbose_name='Base de contribuição dos servidores ativos 2020', null=True, blank=True)

    #COMPENSAÇÃO PREVIDENCIÁRIA	SEGREGADO
    convenio_assinado_compensacao_previdenciaria_segregado = models.CharField(verbose_name='Há convênio ASSINADO de COMPENSAÇÃO PREVIDENCIÁRIA, de servidores vinculados ao RPPS?	', null=True, blank=True, max_length=3) # Adicionar condicional
    informado_base_cadastral_aposentados_e_ou_pensionistas_segregado = models.CharField(verbose_name='Foi informado na base cadastral dos aposentados e/ou pensionistas, o valor que este Ente Publico esta recebendo de compensação previdenciária?	', null=True, blank=True, max_length=3) # Adicionar condicional
    informar_fluxo_mensal_valores_areceber_segregado = models.FloatField(verbose_name='Se NÃO, informar o fluxo mensal médio, sobre os valores a receber', null=True, blank=True)
    informar_fluxo_mensal_a_pagar_segregado = models.FloatField(verbose_name='Informar o fluxo mensal médio, sobre os valores a pagar', null=True, blank=True)
    estoque_compensacao_previdenciaria_receber_segregado = models.FloatField(verbose_name='Há ESTOQUE DE COMPENSAÇÃO PREVIDENCIÁRIA para receber?', null=True, blank=True)

    #EQUACIONAMENTO DO DÉFICIT ATUARIAL			
    ente_possui_plano_equacionamento_deficit_atuarial_segregado = models.CharField(verbose_name='O ENTE PÚBLICO POSSUI PLANO PARA EQUACIONAMENTO DO DÉFICIT ATUARIAL (CUSTO SUPLEMENTAR)?', null=True, blank=True, max_length=25)
    mes_ano_inicio_plano_equacionamento_segregado = models.DateField(verbose_name='QUAL É O MÊS E ANO QUE DEU INÍCIO AO PLANO DE EQUACIONAMENTO', null=True, blank=True)
    numero_norma_define_plano_amortizacao_segregado = models.CharField(verbose_name='NÚMERO DA NORMA QUE DEFINE O PLANO DE AMORTIZAÇÃO', null=True, blank=True, max_length=25)
    data_publicacao_lei_segregado = models.DateField(verbose_name='DATA DA PUBLICAÇÃO DA LEI', null=True, blank=True)

    #Constituição fundo administrativo
    constituicao_fundo_administrativo_segregado = models.CharField(verbose_name='Há constituição de Fundo Administrativo', null=True, blank=True, max_length=3) # Adicionar condicional / Adicionar choice field

    #Dados patrimoniais do RPPS
    renda_fixa_valor_rpps_segregado = models.FloatField(verbose_name='Valor renda fixa', null=True, blank=True)
    renda_fixa_valor_rpps_apuracao_segregado = models.DateField(verbose_name='Data de apuração', null=True, blank=True)
    renda_variavel_rpps_segregado = models.FloatField(verbose_name='Valor renda variável', null=True, blank=True)
    renda_variavel_rpps_apuracao_segregado = models.DateField(verbose_name='Data de apuração', null=True, blank=True)
    segmento_imobiliario_rpps_valor_segregado = models.FloatField(verbose_name='Valor segmento imobiliario', null=True, blank=True)
    segmento_imobiliario_rpps_apuracao_segregado = models.DateField(verbose_name='Data de apuração', null=True, blank=True)
    segmento_fundo_imobiliario_rpps_valor_segregado = models.FloatField(verbose_name='Valor fundos imobiliarios', null=True, blank=True)
    segmento_fundo_imobiliario_rpps_apuracao_segregado = models.DateField(verbose_name='Data de apuração', null=True, blank=True)
    aplicacoes_enquadramento_valor_segregado = models.FloatField(verbose_name='Valor aplicações em enquadramento', null=True, blank=True)
    aplicacoes_enquadramento_apuracao_segregado = models.DateField(verbose_name='Data de apuração', null=True, blank=True)
    titulos_valores_nao_sujeitos_enquadramento_valor_segregado = models.FloatField(verbose_name='Valor titulos e valores não sujeitos ao enquadramento', null=True, blank=True)
    titulos_valores_nao_sujeitos_enquadramento_apuracao_segregado = models.DateField(verbose_name='Data de apuração', null=True, blank=True)
    demais_bens_valor_segregado = models.FloatField(verbose_name='Valor demais bens', null=True, blank=True)
    demais_bens_apuracao_segregado = models.DateField(verbose_name='Data de apuração', null=True, blank=True)

    #Acordo parcelamento de dividas
    existem_acordos_de_parcelamento_dividas_segregado = models.CharField(verbose_name='Existe(m) acordo(s) de parcelamento de dívidas do ente com #o RPPS?', null=True, blank=True, max_length=3) # Implementar botão de adicionar
    #acordo_segregado = models.CharField(verbose_name='Acordo N°', null=True, blank=True, max_length=15)
    #data_aprovacao_segregado = models.DateField(verbose_name='Data de aprovação', null=True, blank=True)
    #juros_segregado = models.FloatField(verbose_name='Valor juros', null=True, blank=True)
    #tipo_juros_segregado = models.CharField(verbose_name='Tipo de juros°', null=True, blank=True, max_length=15)
    #numero_da_prestacao_segregado = models.CharField(verbose_name='Numero da prestação em 31/12/22', null=True, blank=True, max_length=15)
    #indice_atualizacao_segregado = models.CharField(verbose_name='Indice de atualização', null=True, blank=True, max_length=15)
    #ano_acordo_segregado = models.DateField(verbose_name='Ano do acordo', null=True, blank=True)
    #valor_divida_segregado = models.FloatField(verbose_name='Valor da dívida', null=True, blank=True)
    #valor_prestacao_segregado = models.FloatField(verbose_name='Valor da prestação em 31/12/22', null=True, blank=True)
    #prazo_total_meses_segregado = models.FloatField(verbose_name='Prazo total em meses', null=True, blank=True)
    #saldo_devedor_segregado = models.FloatField(verbose_name='Saldo devedor em 31/12/22', null=True, blank=True)
    #acordo_adimplente_segregado = models.CharField(verbose_name='Acordo adimplente', null=True, blank=True, max_length=3)


class AcordoParcelamento(models.Model):
    formulario = models.ForeignKey(Formulario, verbose_name='Formulario', on_delete=models.CASCADE)
    acordo_segregado = models.CharField(verbose_name='Acordo N°', null=True, blank=True, max_length=15)
    data_aprovacao_segregado = models.DateField(verbose_name='Data de aprovação', null=True, blank=True)
    juros_segregado = models.FloatField(verbose_name='Valor juros', null=True, blank=True)
    tipo_juros_segregado = models.CharField(verbose_name='Tipo de juros°', null=True, blank=True, max_length=15)
    numero_da_prestacao_segregado = models.CharField(verbose_name='Numero da prestação em 31/12/22', null=True, blank=True, max_length=15)
    indice_atualizacao_segregado = models.CharField(verbose_name='Indice de atualização', null=True, blank=True, max_length=15)
    ano_acordo_segregado = models.DateField(verbose_name='Ano do acordo', null=True, blank=True)
    valor_divida_segregado = models.FloatField(verbose_name='Valor da dívida', null=True, blank=True)
    valor_prestacao_segregado = models.FloatField(verbose_name='Valor da prestação em 31/12/22', null=True, blank=True)
    prazo_total_meses_segregado = models.FloatField(verbose_name='Prazo total em meses', null=True, blank=True)
    saldo_devedor_segregado = models.FloatField(verbose_name='Saldo devedor em 31/12/22', null=True, blank=True)
    acordo_adimplente_segregado = models.CharField(verbose_name='Acordo adimplente', null=True, blank=True, max_length=3)