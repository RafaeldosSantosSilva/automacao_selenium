from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time
# Configurando web driver

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Abrindo site

driver.get('https://www.youtube.com/')

# Executando ações no site 

busca = driver.find_element(By.NAME, "search_query")


busca.send_keys('likin park')
time.sleep(5)
busca.send_keys(Keys.RETURN)

# Carregamento dos resultados "video-title"

try:
    video = WebDriverWait(driver, 10).until(EC.
    presence_of_element_located((By.ID, 'video-title')))
    video.click()
    input('ola')
finally:
    # Saindo do site
    driver.quit()