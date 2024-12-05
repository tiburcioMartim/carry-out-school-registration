from selenium import webdriver # importando webdriver do Selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from password_generator import gerar_senha, gerar_log # importando a função do gerador



##########[   LÓGICA SELENIUM   ]##########
var_service = Service(ChromeDriverManager().install())
navegator = webdriver.Chrome(service = var_service)



##########[   FUNÇÕES   ]##########
def cadastro_de_responsavel(nome_do_responsavel, email_do_responsavel, senha):
    navegator.find_element('xpath', '//*[@id="input-15"]').send_keys(nome_do_responsavel)                       # Nome do responsável 
    navegator.find_element('xpath', '//*[@id="input-18"]').send_keys(email_do_responsavel)                      # E-mail
    navegator.find_element('xpath', '//*[@id="input-21"]').send_keys(senha)                                     # Gerar uma senha forte
    navegator.find_element('xpath', '//*[@id="input-26"]').send_keys(senha)                                     # Copiar senha de cima e colar aqui
    navegator.find_element('xpath', '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div[2]/button').click()       # Clicar em prosseguir pop-up
    navegator.find_element('xpath', '//*[@id="app"]/div/div[2]/div/div/div/div/div/div[2]/div/button').click()  # Clicar em prosseguir

def dados_aluno(nome_do_aluno, data_nascimento, filiacao_1, 
                cpf_da_filiacao_1, filiacao_2, CPF_da_filiacao_2, 
                email_do_aluno, cor, nacionalidade, uf_nascimento, 
                municipio_nascimento, fator_rh, procedencia_escola):
    time.sleep(ESPERAR)
    navegator.find_element('xpath', '//*[@id="input-140"]').send_keys(nome_do_aluno)                # Preenche nome do aluno
    navegator.find_element('xpath', '//*[@id="input-143"]').send_keys(data_nascimento)              # Preenche data de nascimento
    
    if (sexo == 'm'):
        navegator.find_element('xpath', '//*[@id="app"]/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/span/div/div[3]/span/div/div/div/div/div[2]/div/div/div/div/div').click()     # Clica no gênero desejado
        navegator.find_element('xpath', '//*[@id="input-155"]').send_keys(filiacao_1)               # Filiação 1*
        navegator.find_element('xpath', '//*[@id="input-158"]').send_keys(cpf_da_filiacao_1)        # CPF da Filiação 1*
        navegator.find_element('xpath', '//*[@id="input-161"]').send_keys(filiacao_2)               # Filiação 2
        navegator.find_element('xpath', '//*[@id="input-164"]').send_keys(CPF_da_filiacao_2)        # CPF da Filiação 2
        navegator.find_element('xpath', '//*[@id="input-167"]').send_keys(email_do_aluno)           # E-mail do aluno
        navegator.find_element('xpath', '//*[@id="input-170"]').send_keys(cor)                      # Raça/Cor
        navegator.find_element('xpath', '//*[@id="input-170"]').send_keys(Keys.ENTER)               # Pressionar ENTER            
        navegator.find_element('xpath', '//*[@id="input-176"]').send_keys(nacionalidade)            # Nacionalidade
        navegator.find_element('xpath', '//*[@id="input-176"]').send_keys(Keys.ENTER)               # Pressionar ENTER 
        navegator.find_element('xpath', '//*[@id="input-229"]').send_keys(uf_nascimento)            # UF Nascimento
        navegator.find_element('xpath', '//*[@id="input-229"]').send_keys(Keys.ENTER)               # Pressionar ENTER 
        navegator.find_element('xpath', '//*[@id="input-235"]').send_keys(municipio_nascimento)     # Municipio Nascimento
        navegator.find_element('xpath', '//*[@id="input-235"]').send_keys(Keys.ENTER)               # Pressionar ENTER 
        navegator.find_element('xpath', '//*[@id="input-182"]').send_keys(fator_rh)                 # Grupo sanguíneo / Fator RH
        navegator.find_element('xpath', '//*[@id="input-182"]').send_keys(Keys.ENTER)               # Pressionar ENTER 
        navegator.find_element('xpath', '//*[@id="input-188"]').send_keys(procedencia_escola)       # Procedência escola
        navegator.find_element('xpath', '//*[@id="input-188"]').send_keys(Keys.ENTER)               # Pressionar ENTER 
        navegator.find_element('xpath', '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/span/div/div[15]/span/div/div/div/div/div[2]/div/div/div/div/div').click() # É pessoa com deficiência? NÃO
        navegator.find_element('xpath', '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div/div[2]/button').click() # Próximo
        
    elif (sexo == 'f'):
        navegator.find_element('xpath', '//*[@id="app"]/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/span/div/div[3]/span/div/div/div/div/div[1]/div/div/div/div/div').click()     # Clica no gênero desejado
        navegator.find_element('xpath', '//*[@id="input-155"]').send_keys(filiacao_1)               # Filiação 1*
        navegator.find_element('xpath', '//*[@id="input-158"]').send_keys(cpf_da_filiacao_1)        # CPF da Filiação 1*
        navegator.find_element('xpath', '//*[@id="input-161"]').send_keys(filiacao_2)               # Filiação 2
        navegator.find_element('xpath', '//*[@id="input-164"]').send_keys(CPF_da_filiacao_2)        # CPF da Filiação 2
        navegator.find_element('xpath', '//*[@id="input-167"]').send_keys(email_do_aluno)           # E-mail do aluno
        navegator.find_element('xpath', '//*[@id="input-170"]').send_keys(cor)                      # Raça/Cor
        navegator.find_element('xpath', '//*[@id="input-170"]').send_keys(Keys.ENTER)               # Pressionar ENTER            
        navegator.find_element('xpath', '//*[@id="input-176"]').send_keys(nacionalidade)            # Nacionalidade
        navegator.find_element('xpath', '//*[@id="input-176"]').send_keys(Keys.ENTER)               # Pressionar ENTER 
        navegator.find_element('xpath', '//*[@id="input-229"]').send_keys(uf_nascimento)            # UF Nascimento
        navegator.find_element('xpath', '//*[@id="input-229"]').send_keys(Keys.ENTER)               # Pressionar ENTER 
        navegator.find_element('xpath', '//*[@id="input-235"]').send_keys(municipio_nascimento)     # Municipio Nascimento
        navegator.find_element('xpath', '//*[@id="input-235"]').send_keys(Keys.ENTER)               # Pressionar ENTER 
        navegator.find_element('xpath', '//*[@id="input-182"]').send_keys(fator_rh)                 # Grupo sanguíneo / Fator RH
        navegator.find_element('xpath', '//*[@id="input-182"]').send_keys(Keys.ENTER)               # Pressionar ENTER 
        navegator.find_element('xpath', '//*[@id="input-188"]').send_keys(procedencia_escola)       # Procedência escola
        navegator.find_element('xpath', '//*[@id="input-188"]').send_keys(Keys.ENTER)               # Pressionar ENTER 
        navegator.find_element('xpath', '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/span/div/div[15]/span/div/div/div/div/div[2]/div/div/div/div/div').click() # É pessoa com deficiência? NÃO
        navegator.find_element('xpath', '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div/div[2]/button').click() # Próximo

def documentos(cpf_do_aluno, nis, rg, rg_digito, orgao_expedidor, uf, data_de_emissao):
    navegator.find_element('xpath', '//*[@id="input-113"]').send_keys(cpf_do_aluno)
    navegator.find_element('xpath', '//*[@id="input-205"]').send_keys(nis)
    navegator.find_element('xpath', '//*[@id="input-208"]').send_keys(rg)
    navegator.find_element('xpath', '//*[@id="input-211"]').send_keys(rg_digito)
    navegator.find_element('xpath', '//*[@id="input-214"]').send_keys(orgao_expedidor)
    navegator.find_element('xpath', '//*[@id="input-214"]').send_keys(Keys.ENTER)
    navegator.find_element('xpath', '//*[@id="input-220"]').send_keys(uf)
    navegator.find_element('xpath', '//*[@id="input-220"]').send_keys(Keys.ENTER)
    navegator.find_element('xpath', '//*[@id="input-226"]').send_keys(data_de_emissao)
    navegator.find_element('xpath', '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/button').click() # Aperta próximo

def responsavel(vResponsavel, data_nascimento_responsavel_1, email_do_responsavel_1, 
                data_nascimento_responsavel_2, email_do_responsavel_2, cpf_responsavel_outro, 
                nome_do_responsavel_outro, data_nascimento_responsavel_outro, email_do_responsavel_outro):
    
    navegator.find_element('xpath', '//*[@id="input-121"]').send_keys(vResponsavel) # Escolhe o responsável
    navegator.find_element('xpath', '//*[@id="input-121"]').send_keys(Keys.ENTER)  # Aperta ENTER
    
    match vResponsavel:
        case 'filiação 1':
            navegator.find_element('xpath', '//*[@id="input-450"]').send_keys(data_nascimento_responsavel_1)
            navegator.find_element('xpath', '//*[@id="input-453"]').send_keys(email_do_responsavel_1)
            navegator.find_element('xpath', '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div[3]/div/div[2]/button').click() # Aperta próximo
        
        case 'filiação 2':
            navegator.find_element('xpath', '//*[@id="input-450"]').send_keys(data_nascimento_responsavel_2)
            navegator.find_element('xpath', '//*[@id="input-453"]').send_keys(email_do_responsavel_2)
            navegator.find_element('xpath', '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div[3]/div/div[2]/button').click() # Aperta próximo
        
        case 'outro':
            navegator.find_element('xpath', '//*[@id="input-449"]').send_keys(cpf_responsavel_outro)
            navegator.find_element('xpath', '//*[@id="input-452"]').send_keys(nome_do_responsavel_outro)
            navegator.find_element('xpath', '//*[@id="input-455"]').send_keys(data_nascimento_responsavel_outro)
            navegator.find_element('xpath', '//*[@id="input-458"]').send_keys(email_do_responsavel_outro)
            navegator.find_element('xpath', '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div[3]/div/div[2]/button').click() # Aperta próximo
        
        case 'próprio aluno':
            navegator.find_element('xpath', '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div[3]/div/div[2]/button').click() # Aperta próximo

def endereco_telefone(cep, uf_atual, municipio_atual, bairro_atual, endereço_atual, numero_atual, complemento_atual, ddd_atual_1, telefone_atual_1, ddd_atual_2, telefone_atual_2):
    navegator.find_element('xpath', '//*[@id="input-462"]').send_keys(cep)
    navegator.find_element('xpath', '//*[@id="input-467"]').send_keys(uf_atual)
    navegator.find_element('xpath', '//*[@id="input-467"]').send_keys(Keys.ENTER)
    navegator.find_element('xpath', '//*[@id="input-473"]').send_keys(municipio_atual)
    navegator.find_element('xpath', '//*[@id="input-473"]').send_keys(Keys.ENTER)
    navegator.find_element('xpath', '//*[@id="input-479"]').send_keys(bairro_atual)
    navegator.find_element('xpath', '//*[@id="input-482"]').send_keys(endereço_atual)
    navegator.find_element('xpath', '//*[@id="input-485"]').send_keys(numero_atual)
    navegator.find_element('xpath', '//*[@id="input-488"]').send_keys(complemento_atual)
    navegator.find_element('xpath', '//*[@id="input-491"]').send_keys(ddd_atual_1)
    navegator.find_element('xpath', '//*[@id="input-494"]').send_keys(telefone_atual_1)
    navegator.find_element('xpath', '//*[@id="input-497"]').send_keys(ddd_atual_2)
    navegator.find_element('xpath', '//*[@id="input-500"]').send_keys(telefone_atual_2)
    navegator.find_element('xpath', '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div[4]/div/div[2]/button').click() # Aperta próximo

def dados_de_cadastro_da_matricula(curso, serie, possui_irmao_na_escola):
    ######################     DADOS DE CADASTRO DA MATRÍCULA
    navegator.find_element('xpath', '//*[@id="input-585"]').send_keys(curso)
    navegator.find_element('xpath', '//*[@id="input-585"]').send_keys(Keys.ENTER)
    navegator.find_element(By.XPATH, '//*[@id="input-591"]').send_keys(serie)           
    navegator.find_element(By.XPATH, '//*[@id="input-591"]').send_keys(Keys.ARROW_DOWN) 
    navegator.find_element(By.XPATH, '//*[@id="input-591"]').send_keys(Keys.ENTER)
    navegator.find_element('xpath', '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div/div[3]/div[2]/div/span/div[3]/div[1]/div[2]/button').click() # PESQUISAR ESCOLA
    
    
    ########### Escolher a escola em uma variedade de escolas ###########
    try:        # Aguardar que o usuário escolha uma escola
        if possui_irmao_na_escola == 's': # SIM     ############# IMPLEMENTAR LÓGICA SEMELHANTE À ELIF ABAIXO
            navegator.find_element('xpath', '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div/div[3]/div[2]/div/span/div[5]/span/div/div/div/div/div[1]/div/div/div/div/div').click() # SIM
        
        elif possui_irmao_na_escola == 'n': # NÃO
            elemento_escola_selecionada = WebDriverWait(navegator,600).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div/div[3]/div[2]/div/span/div[5]/span/div/div/div/div/div[2]/div/div/div/div/div')))  # Colocar o XPath do botão ou elemento que aparece após a seleção da escola    # BOTÃO NÃO
            elemento_escola_selecionada.click() # Clicar na escola escolhida
            quebra_de_captcha = WebDriverWait(navegator, 600).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[3]/div/div/div[3]/div[2]/div/div[4]/div[2]/button')))  # Colocar o XPath do botão ou elemento que aparece após a quebra do captcha      # Botão Continuar
            time.sleep(ESPERAR * 3)
            quebra_de_captcha.click()
            time.sleep(ESPERAR * 3)
            navegator.find_element('xpath', '//*[@id="app"]/div[16]/div/div/div[2]/button[1]').click() # CLICAR EM CONFIRMAR
            
            input()
            
    except TimeoutException as e:
        print(f'{e} | Tempo esgotado.')

def main():
    try:
        navegator.get('https://matricula.semed.novaiguacu.rj.gov.br/#/inscricaoUsuario')
        
        cadastro_de_responsavel(nome_do_responsavel, email_do_responsavel, senha)
        WebDriverWait(navegator, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/div/div[2]/div/span/div/span/div/div/div/div/div[1]/div/div/div/div/div'))) # Aguarda o botão carregar
        if esta_na_rede_ensino:    # Faz parte do sistema de ensino? SIM SIM SIM
            navegator.find_element('xpath', '//*[@id="app"]/div/div[2]/div/div/div/div/div[2]/div/span/div/span/div/div/div/div/div[1]/div/div/div/div/div').click() # Aperta sim
            navegator.find_element('xpath', '//*[@id="app"]/div/div[2]/div/div/div/div/div[2]/div/span/div[2]/span/div/div/div/div/div[3]/div/div/div/div/div').click() # Clica em Nome
            navegator.find_element('xpath', '//*[@id="input-104"]').send_keys('João Paulo Ferreira')        # Preenche nome do aluno
            navegator.find_element('xpath', '//*[@id="input-107"]').send_keys('Carolina Da Silva Erreira')  # Preenche nome da filiação 1
            navegator.find_element('xpath', '//*[@id="input-101"]').send_keys('12022011')                   # Preenche data de nascimento
            # navegator.find_element('xpath', '//*[@id="recaptcha-anchor"]/div[1]').click() # Clica no eu não sou um robô   ********** QUEBRAR CAPTCHA **********
            time.sleep(ESPERAR)
            
        else: ######## Faz parte do sistema de ensino? NÃO NÃO NÃO
            navegator.find_element('xpath', '//*[@id="app"]/div/div[2]/div/div/div/div/div[2]/div/span/div/span/div/div/div/div/div[2]/div/div/div/div/div').click() # Aperta não
            navegator.find_element('xpath', '//*[@id="app"]/div/div[2]/div/div/div/div/div[2]/div/button').click()  # Aperta prosseguir
            
            dados_aluno(nome_do_aluno, data_nascimento, filiacao_1, cpf_da_filiacao_1, filiacao_2, CPF_da_filiacao_2, email_do_aluno, cor, nacionalidade, uf_nascimento, municipio_nascimento, fator_rh, procedencia_escola)        
            documentos(cpf_do_aluno, nis, rg, rg_digito, orgao_expedidor, uf, data_de_emissao)
            responsavel(vResponsavel, data_nascimento_responsavel_1, email_do_responsavel_1, data_nascimento_responsavel_2, email_do_responsavel_2, cpf_responsavel_outro, nome_do_responsavel_outro, data_nascimento_responsavel_outro, email_do_responsavel_outro)
            endereco_telefone(cep, uf_atual, municipio_atual, bairro_atual, endereço_atual, numero_atual, complemento_atual, ddd_atual_1, telefone_atual_1, ddd_atual_2, telefone_atual_2)
            dados_de_cadastro_da_matricula(curso, serie, possui_irmao_na_escola)
            
        time.sleep(ESPERAR)
        
    except TypeError as e:
        print(f'Erro: {e}')



##########[   CONSTANTES   ]##########
ESPERAR = 1     # segundos



##########[   GERADOR DE SENHA   ]##########
tamanho = 12
usar_maiusculo = True
usar_numeros = True
usar_especiais = True
senha = gerar_senha(tamanho, usar_maiusculo, usar_numeros, usar_especiais)
gerar_log(tamanho, usar_maiusculo, usar_numeros, usar_especiais, senha)



##########[   CADASTRO DE RESPONSÁVEL   ]##########
nome_do_responsavel = 'Martim Tiburcio'      # Campo obrigatório
email_do_responsavel = 'tiago@gmail.com'     # Campo obrigatório



##########[   DADOS DINÂMICOS   ]##########
esta_na_rede_ensino = False                     # implementar vinculo com excel para ser dinâmico   # Campo obrigatório



##########[   DADOS DO ALUNO   ]##########
nome_do_aluno = 'João Paulo Ferreira'.lower()   # implementar vinculo com excel para ser dinâmico   # Campo obrigatório
data_nascimento = '12022011'                    # implementar vinculo com excel para ser dinâmico   # Campo obrigatório
sexo = 'F'.lower()                              # implementar vinculo com excel para ser dinâmico   # Campo obrigatório
filiacao_1 = 'Martim Tiburcio'.lower()          # implementar vinculo com excel para ser dinâmico   # Campo obrigatório
cpf_da_filiacao_1 = '11278784411'.lower()       # implementar vinculo com excel para ser dinâmico   # Campo obrigatório
filiacao_2 = ''.lower()                         # implementar vinculo com excel para ser dinâmico           # NÃO obrigatório
CPF_da_filiacao_2 = ''.lower()                  # implementar vinculo com excel para ser dinâmico           # NÃO obrigatório
email_do_aluno = 'aluno@gmail.com'.lower()      # implementar vinculo com excel para ser dinâmico           # NÃO obrigatório
cor = 'Parda'.lower()                           # implementar vinculo com excel para ser dinâmico   # Campo obrigatório
nacionalidade = 'Brasileira'.lower()            # implementar vinculo com excel para ser dinâmico   # Campo obrigatório
uf_nascimento = 'RJ'.lower()                    # implementar vinculo com excel para ser dinâmico   # Campo obrigatório
municipio_nascimento = 'Nova Iguaçu'.lower()    # implementar vinculo com excel para ser dinâmico   # Campo obrigatório
fator_rh = 'o+'.lower()                         # implementar vinculo com excel para ser dinâmico           # NÃO obrigatório
procedencia_escola = 'Outro'.lower()            # implementar vinculo com excel para ser dinâmico           # NÃO obrigatório
pessoa_com_deficiencia = False                  # ATENÇÃO  |  Lógica condicional NÃO implementada   # Campo obrigatório  |  default = Não



##########[   DOCUMENTOS   ]##########
cpf_do_aluno = '39463982604'                              # implementar vinculo com excel para ser dinâmico         # NÃO obrigatório
nis = '15375845'                                          # implementar vinculo com excel para ser dinâmico         # NÃO obrigatório
rg = '52876857'                                           # implementar vinculo com excel para ser dinâmico         # NÃO obrigatório
rg_digito = '3'                                           # implementar vinculo com excel para ser dinâmico         # NÃO obrigatório
orgao_expedidor = 'corpo de bombeiros militar'.lower()    # implementar vinculo com excel para ser dinâmico         # NÃO obrigatório
uf = 'Rj'.lower()                                         # implementar vinculo com excel para ser dinâmico         # NÃO obrigatório
data_de_emissao = '22052023'                              # implementar vinculo com excel para ser dinâmico         # NÃO obrigatório



##########[   RESPONSÁVEL   ]##########
vResponsavel = 'filiação 1'.lower()                                 # Campo obrigatório
data_nascimento_responsavel_1 = '02101999'      # filiação 1        # Campo obrigatório
email_do_responsavel_1 = 'tiago@gmail.com'      # filiação 1                # NÃO obrigatório
data_nascimento_responsavel_2 = '02101999'      # filiação 2        # Campo obrigatório
email_do_responsavel_2 = 'tiago@gmail.com'      # filiação 2                # NÃO obrigatório
cpf_responsavel_outro = '12176567711'           # responsável outro
nome_do_responsavel_outro = 'Maria Conceição'   # responsável outro
data_nascimento_responsavel_outro = '02101999'  # responsável outro
email_do_responsavel_outro = 'tiago@gmail.com'  # responsável outro



##########[   ENDEREÇO / TELEFONE   ]##########
cep = '26253789'                    # Campo obrigatório
uf_atual = 'Rj'                     # Campo obrigatório
municipio_atual = 'Nova Iguaçu'     # Campo obrigatório
bairro_atual = 'Posse'              # Campo obrigatório
endereço_atual = 'Rua do bobo'      # Campo obrigatório
numero_atual = '0'                  # Campo obrigatório
complemento_atual = ''                      # NÃO obrigatório
ddd_atual_1 = '21'                  # Campo obrigatório
telefone_atual_1 = '988880239'      # Campo obrigatório
ddd_atual_2 = ''                            # NÃO obrigatório
telefone_atual_2 = ''                       # NÃO obrigatório



##########[   DADOS DE CADASTRO DA MATRÍCULA   ]##########
curso = 'EDUCAÇÃO DE JOVENS E ADULTOS - EJA'  # Campo obrigatório
serie = 'FASE II'                             # Campo obrigatório
possui_irmao_na_escola = 'N'.lower()          # Campo obrigatório



if __name__ == '__main__':
    main()