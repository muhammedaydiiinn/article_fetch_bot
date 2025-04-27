from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

# Chrome ayarları
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--headless=new")  # HEADLESS MOD
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=chrome_options)

# TXT dosyasından sayı URL'lerini oku
with open('sayi_url_listesi.txt', 'r', encoding='utf-8') as f:
    issue_urls = [line.strip() for line in f if line.strip()]

results = []

BATCH_SIZE = 20  # Aynı anda açılacak sekme sayısı

# Her sayı (issue) URL'si için çalış
for issue_url in issue_urls:
    print(f"\n📂 Sayı açılıyor: {issue_url}")
    driver.get(issue_url)
    time.sleep(3)  # Sayfa tam yüklensin

    # Makale linklerini çek
    try:
        article_links = driver.find_elements(By.CSS_SELECTOR, '#issue-articles > div > div > div > div.uk-flex > div.uk-width-4-5 > h3 > a')
        article_urls = [link.get_attribute('href') for link in article_links]
        print(f"🔎 {len(article_urls)} makale bulundu.")
    except:
        print("⚠️ Bu sayıda makale bulunamadı.")
        continue

    # Makale URL'lerini grupla
    for i in range(0, len(article_urls), BATCH_SIZE):
        batch = article_urls[i:i+BATCH_SIZE]

        # Her makale için sekme aç
        for url in batch:
            driver.execute_script(f"window.open('{url}', '_blank');")
            time.sleep(0.2)

        windows = driver.window_handles

        # Sadece yeni açılan sekmelere geç
        for window in windows[1:]:  # windows[0] ana sayı sayfası
            driver.switch_to.window(window)
            time.sleep(1)

            try:
                title_element = driver.find_element(By.CSS_SELECTOR, '#articleHeaderTitle > h1')
                title = title_element.text.strip()
            except:
                title = "Başlık Bulunamadı"

            try:
                mail_elements = driver.find_elements(By.CSS_SELECTOR, '#articleAuthors a.ico-mail-solid')
                emails = []

                for mail_element in mail_elements:
                    mailto_link = mail_element.get_attribute('href')
                    if mailto_link and mailto_link.startswith('mailto:'):
                        email = mailto_link.replace('mailto:', '')
                        emails.append(email)

                if emails:
                    email_text = " || ".join(emails)
                else:
                    email_text = "Mail Bulunamadı"

            except:
                print("⚠️ Bu makalede mail bulunamadı.")
                email_text = "Mail Bulunamadı"

            results.append({"Makale Başlığı": title, "E-Postalar": email_text})

            # Sekmeyi kapat
            driver.close()

        # Ana pencereye dön
        driver.switch_to.window(windows[0])

# Tarayıcıyı kapat
driver.quit()

# Sonuçları kaydet
df = pd.DataFrame(results)
df.to_excel('makale_mailler.xlsx', index=False)

print("\n🎯 Tüm işlemler tamamlandı! 'makale_mailler.xlsx' dosyası oluşturuldu.")
