import requests
import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from colorama import Fore
from pystyle import Center, Colors, Colorate
import os
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

warnings.filterwarnings("ignore", category=DeprecationWarning)

def güncellemeleri_kontrol_et():
    try:
        r = requests.get("")
        remote_version = r.content.decode('utf-8').strip()
        local_version = open('version.txt', 'r').read().strip()
        if remote_version != local_version:
            
            time.sleep(3)
            return False
        return True
    except:
        return True


def botu_çalıştır():
    if not güncellemeleri_kontrol_et():
        return

    os.system(f"ChatGpt viewer tool xd ")

    print(Colorate.Vertical(Colors.green_to_cyan, Center.XCenter("""           
 ____  _______  _______ ____   ___  
|  _ \| ____\ \/ /_   _|  _ \ / _ \ 
| | | |  _|  \  /  | | | |_) | | | |
| |_| | |___ /  \  | | |  _ <| |_| |
|____/|_____/_/\_\ |_| |_| \_\\___/  

                selam
                             """ )))

    proxy_sunuculari = {
        1: "https://www.blockaway.net",
        2: "https://www.croxyproxy.com",
        3: "https://www.croxyproxy.rocks",
        4: "https://www.croxy.network",
        5: "https://www.croxy.org",
        6: "https://www.youtubeunblocked.live",
        7: "https://www.croxyproxy.net",
    }

    print(Colors.green, "Proxy Sunucusu 1 Tavsiye Edilir")
    print(Colorate.Vertical(Colors.green_to_blue, "Bir proxy sunucusu seçin (1,2,3..):"))
    for i in range(1, 7):
        print(Colorate.Vertical(Colors.red_to_blue, f"Proxy Sunucusu {i}"))
    proxy_secimi = int(input("> "))
    proxy_url = proxy_sunuculari.get(proxy_secimi)

    twitch_kullanici_adi = input(Colorate.Vertical(Colors.green_to_blue, "Kanal adınızı girin (örnek: dextroriyalbaba): "))
    bot_sayisi = int(input(Colorate.Vertical(Colors.cyan_to_blue, "Kaç proxy sitesi açmak istersiniz? (Gönderilecek izleyici sayısı)")))

    os.system("cls")

    print(Colorate.Vertical(Colors.green_to_cyan, Center.XCenter("""           
 ____  _______  _______ ____   ___  
|  _ \| ____\ \/ /_   _|  _ \ / _ \ 
| | | |  _|  \  /  | | | |_) | | | |
| |_| | |___ /  \  | | |  _ <| |_| |
|____/|_____/_/\_\ |_| |_| \_\\___/  

 Bot başlatıldı, izleyici gönderimi başlıyor...
                             """ )))

    print(Colors.red, Center.XCenter("İzleyici sayısı çekiliyor..."))

    izleyici_sayisi = get_current_viewers(twitch_kullanici_adi)  # Bu fonksiyon izleyici sayısını alacak

    print(f"Güncel izleyici sayısı: {izleyici_sayisi}")
    print("Botlar gönderilmeye başlıyor...")

    chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    driver_path = 'chromedriver.exe'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument('--disable-dev-shm-usage')
    extension_path = 'adblock.crx'
    chrome_options.add_extension(extension_path)
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(proxy_url)

    for i in range(bot_sayisi):
        driver.execute_script("window.open('" + proxy_url + "')")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(proxy_url)

        text_box = driver.find_element(By.ID, 'url')
        text_box.send_keys(f'www.twitch.tv/{twitch_kullanici_adi}')
        text_box.send_keys(Keys.RETURN)
        print(f"Bot gönderildi {i + 1}")

    # Dinamik olarak bot gönderme hızını ayarlayacağız
    while True:
        time.sleep(40)  # 40 saniye bekleyerek izleyici sayısını tekrar kontrol ediyoruz
        izleyici_sayisi = get_current_viewers(twitch_kullanici_adi)  # İzleyici sayısını tekrar alıyoruz

        print(f"Güncel izleyici sayısı: {izleyici_sayisi}")
        
        if izleyici_sayisi < bot_sayisi:
            print("İzleyici sayısında azalma tespit edildi, botları yeniden gönderiyorum...")
            for i in range(bot_sayisi - izleyici_sayisi):
                driver.execute_script("window.open('" + proxy_url + "')")
                driver.switch_to.window(driver.window_handles[-1])
                driver.get(proxy_url)

                text_box = driver.find_element(By.ID, 'url')
                text_box.send_keys(f'www.twitch.tv/{twitch_kullanici_adi}')
                text_box.send_keys(Keys.RETURN)
                print(f"Bot gönderildi {i + 1}")

        # Eğer izleyici sayısı 50'yi geçmişse, bot gönderme hızını yavaşlatıyoruz
        if izleyici_sayisi >= bot_sayisi:
            print("İzleyici sayısı yeterli, bot gönderme hızını yavaşlatıyorum...")
            time.sleep(30)  # Hızlı bot göndermeyi yavaşlatıyoruz

        if izleyici_sayisi >= bot_sayisi:
            break

    input(Colorate.Vertical(Colors.red_to_blue, "Tüm izleyiciler gönderildi. Çıkmak için Enter'a basın."))
    driver.quit()


def get_current_viewers(twitch_username):
    # Tarayıcı ayarları
    chrome_options = Options()
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")  # Tarayıcıyı arka planda çalıştırmak için

    # Tarayıcıyı başlat
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Yayıncının kanalına git
        driver.get(f'https://www.twitch.tv/{twitch_username}')

        # İzleyici sayısını içeren öğenin yüklenmesini bekle
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@data-a-target="animated-channel-viewers-count"]'))
        )

        # İzleyici sayısını al
        viewers_count = driver.find_element(By.XPATH, '//*[@data-a-target="animated-channel-viewers-count"]').text
        
        # Sayıyı işleyip integer olarak döndür
        viewers_count = viewers_count.replace(',', '')  # Virgülleri kaldır
        return int(viewers_count)

    except Exception as e:
        print(f"Hata oluştu: {e}")
        return 0  # İzleyici sayısı hatalıysa 0 döndürüyoruz

    finally:
        driver.quit()


botu_çalıştır()
