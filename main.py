from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

var_service = Service(ChromeDriverManager().install())
navegator = webdriver.Chrome(service = var_service)

navegator.get('https://matricula.semed.novaiguacu.rj.gov.br/#/inscricaoUsuario')
navegator.find_element('xpath', '//*[@id="input-15"]').send_keys(...) # Nome do responsável 
navegator.find_element('xpath', '//*[@id="input-18"]').send_keys(...) # E-mail
navegator.find_element('xpath', '//*[@id="input-21"]').send_keys(...) # Gerar uma senha forte
navegator.find_element('xpath', '//*[@id="input-26"]').send_keys(...) # Copiar senha de cima e colar aqui
navegator.find_element('xpath', '//*[@id="app"]/div/div[3]/div/div[2]/div/div/div[2]/button').click() # Clicar em prosseguir
# navegator.find_element('xpath', '')

input('Para encerrar pressione qualquer tecla.')