from selenium import webdriver # importando webdriver do Selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from password_generator import gerar_senha, gerar_log # importando a função do gerador

# Lógica do Selenium
var_service = Service(ChromeDriverManager().install())
navegator = webdriver.Chrome(service = var_service)

# Gerador de senha
tamanho = 12
usar_maiusculo = True
usar_numeros = True
usar_especiais = True
esta_rede_ensino = True # implementar vinculo com excel para ser dinâmico

senha = gerar_senha(tamanho, usar_maiusculo, usar_numeros, usar_especiais)
gerar_log(tamanho, usar_maiusculo, usar_numeros, usar_especiais, senha)

try:
    navegator.get('https://matricula.semed.novaiguacu.rj.gov.br/#/inscricaoUsuario')
    navegator.find_element('xpath', '//*[@id="input-15"]').send_keys('Martim Tiburcio')                         # Nome do responsável 
    navegator.find_element('xpath', '//*[@id="input-18"]').send_keys('tiburcio.contato@gmail.com')              # E-mail
    navegator.find_element('xpath', '//*[@id="input-21"]').send_keys(senha)                                     # Gerar uma senha forte
    navegator.find_element('xpath', '//*[@id="input-26"]').send_keys(senha)                                     # Copiar senha de cima e colar aqui
    navegator.find_element('xpath', '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div[2]/button').click()       # Clicar em prosseguir pop-up
    navegator.find_element('xpath', '//*[@id="app"]/div/div[2]/div/div/div/div/div/div[2]/div/button').click()  # Clicar em prosseguir
    WebDriverWait(navegator, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/div/div[2]/div/span/div/span/div/div/div/div/div[1]/div/div/div/div/div'))) # Aguarda o botão carregar

    if esta_rede_ensino:    # Faz parte do sistema de ensino? SIM SIM SIM
        navegator.find_element('xpath', '//*[@id="app"]/div/div[2]/div/div/div/div/div[2]/div/span/div/span/div/div/div/div/div[1]/div/div/div/div/div').click() # Aperta sim
        navegator.find_element('xpath', '//*[@id="app"]/div/div[2]/div/div/div/div/div[2]/div/span/div[2]/span/div/div/div/div/div[3]/div/div/div/div/div').click() # Clica em Nome
        navegator.find_element('xpath', '//*[@id="input-104"]').send_keys('João Paulo Ferreira')        # Preenche nome do aluno
        navegator.find_element('xpath', '//*[@id="input-107"]').send_keys('Carolina Da Silva Erreira')  # Preenche nome da filiação 1
        navegator.find_element('xpath', '//*[@id="input-101"]').send_keys('12022011')                   # Preenche data de nascimento
        # navegator.find_element('xpath', '//*[@id="recaptcha-anchor"]/div[1]').click() # Clica no eu não sou um robô   ********** QUEBRAR CAPTCHA **********
        input('Para encerrar pressione qualquer tecla.')
        # navegator.find_element('xpath', '')
        # navegator.find_element('xpath', '')
        
    else:                   # Faz parte do sistema de ensino? NÃO NÃO NÃO
        navegator.find_element('xpath', '//*[@id="app"]/div/div[2]/div/div/div/div/div[2]/div/span/div/span/div/div/div/div/div[2]/div/div/div/div/div').click() # Aperta não
        navegator.find_element('xpath', '//*[@id="app"]/div/div[2]/div/div/div/div/div[2]/div/button').click()  # Aperta prosseguir
        navegator.find_element('xpath', '//*[@id="input-140"]').send_keys('João Paulo Ferreira')                # Preenche nome do aluno
        navegator.find_element('xpath', '//*[@id="input-143"]').send_keys('12022011')                           # Preenche data de nascimento
        
        
        
    # navegator.find_element('xpath', '')

except Exception as e:
    print(f'Erro: {e}')