import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os



# Nome completo = //*[text() = 'Texto exato']
# Nome incompleto = //*[contains(text(), 'texto parcial')]

def bot():
    chromedriver_path = os.path.abspath('chromedriver.exe')
    xpath_caixa_texto = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
   
    try:
        driver = webdriver.Chrome(chromedriver_path)
    except:
        print('chromedriver.exe não encontrado')
        return 0
    
    driver.get('https://web.whatsapp.com/')

    time.sleep(10)

    def busca_nome():
        nome = str(input('Digite o nome de um contato/grupo: '))
        xpath = f'//*[contains(text(), "{nome}")]'
        driver.find_element_by_xpath(xpath).click()
        mensagem = str(input('Digite a mensagem que deseja enviar: '))
        numero = int(input('Digite quantas vezes enviar: '))
        print(f'Enviar {mensagem} para {nome} {numero} vezes')
        return numero, mensagem

    try:
        numero, mensagem = busca_nome()
    except:
        print('\nContato/Grupo não encontrado :(\n')
        busca_nome()

    continuar = input('Tudo certo? Digite ENTER: ')
    
    for i in range(numero):
        texto = driver.find_element_by_xpath(xpath_caixa_texto)

        texto.send_keys(f'{mensagem}')
        texto.send_keys(Keys.ENTER)
        
    fim = input('Se deseja sair pressione ENTER, para tentar denovo digite 0: ')

    if (fim == ''):
        print('OBRIGADO :)')
        return 0
    else:
        return bot()

bot()