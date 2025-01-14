import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Kullanıcıdan yayıncı adı al
channel_name = input("Yayıncı adını girin: ")

# Tarayıcı ayarları
chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--headless")  # Tarayıcıyı arka planda çalıştırmak için

# Tarayıcıyı başlat
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Yayıncının kanalına git
driver.get(f'https://www.twitch.tv/{channel_name}')

# Sayfanın tamamen yüklenmesini bekle
try:
    # İzleyici sayısını içeren öğenin tam yüklenmesini bekle
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'span.ScAnimatedNumber-sc-1iib0w9-0.hERoTc'))
    )
    
    # İzleyici sayısını almak için doğru elementin seçilmesi
    viewers_count = driver.find_element(By.CSS_SELECTOR, 'span.ScAnimatedNumber-sc-1iib0w9-0.hERoTc').text
    print(f"Yayıncı {channel_name} şu an {viewers_count} izleyiciye sahip.")

except Exception as e:
    print(f"Hata oluştu: {e}")

# Tarayıcıyı kapat
driver.quit()
