# 1. AŞAMA - TÜM nth-child(kart) LİNKLERİNİ TOPLA

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Chrome başlat
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=chrome_options)

# Arşiv sayfaları
archive_pages = [
    'https://malque.pub/ojs/index.php/mr/issue/archive',
    'https://malque.pub/ojs/index.php/mr/issue/archive/2'
]

issue_urls = []

for archive_url in archive_pages:
    driver.get(archive_url)
    time.sleep(3)

    # Tahmini kart sayısı (fazla ver, sorun olmaz)
    max_cards = 100  

    for i in range(1, max_cards):
        try:
            selector = f"#pageWrapper > div.uk-margin-large-top.uk-margin-large-bottom.uk-container.uk-container-large > div > div > div:nth-child({i}) > div > div > div > a"
            link_element = driver.find_element(By.CSS_SELECTOR, selector)
            href = link_element.get_attribute('href')
            if href:
                issue_urls.append(href)
                print(f"🔗 Kart {i}: {href}")
        except Exception as e:
            # Kart yoksa devam et
            continue

driver.quit()

# Linkleri txt'ye yaz
with open('sayi_url_listesi.txt', 'w', encoding='utf-8') as f:
    for url in issue_urls:
        f.write(url + '\n')

print(f"\n🎯 Tüm sayı linkleri 'sayi_url_listesi.txt' dosyasına kaydedildi. Toplam: {len(issue_urls)} link.")
