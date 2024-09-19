from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializar o WebDriver (supondo que o chromedriver está no PATH)
driver = webdriver.Chrome()

# Abrir a página de login
driver.get('https://mentorweb.unifecaf.edu.br/fecafMentorWebG5/')

# Encontrar o campo de login e preencher
username = driver.find_element(By.NAME, "j_username")
username.send_keys("45286")

# Encontrar o campo de senha e preencher
password = driver.find_element(By.NAME, "senha")
password.send_keys("Luigikat1@")

# Simular o clique no botão de login
login_button = driver.find_element(By.NAME, "btnLogin")
login_button.click()

# Espera para o carregamento da página
time.sleep(10)

# Verificar se o login foi bem-sucedido
if "dashboard" in driver.current_url:
    print("Login realizado com sucesso!")
else:
    print("Falha no login.")

# Fechar o WebDriver
driver.quit()