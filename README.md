# Article Fetch Bot

**Article Fetch Bot** projesi, web üzerindeki makale sayfalarındaki yazarlara ait e-posta adreslerini toplamak için geliştirilmiş iki önemli Python betiği içeriyor:

1. **article_archive_url_fetch.py**: Bu betik, belirli bir arşiv sayfasındaki makale sayfalarının URL'lerini toplar.
2. **mail_cekme_script.py**: Bu betik, topladığı URL'leri kullanarak her bir makale sayfasına gidip, yazarlara ait e-posta adreslerini çeker.

## Özellikler

- **URL Toplama**: Arşiv sayfalarındaki makale linklerini toplar.
- **Makale E-posta Çekme**: Her makale sayfasında yazarların e-posta adreslerini çıkarır.
- **Sonuçları Kaydetme**: Elde edilen e-posta adreslerini ve makale başlıklarını bir Excel dosyasına kaydeder.

## Gereksinimler

Bu projeyi çalıştırabilmek için aşağıdaki yazılımların ve kütüphanelerin yüklü olması gerekmektedir:

- Python 3.x
- Selenium
- Pandas
- Openpyxl (Excel dosyasına veri yazabilmek için)

Gerekli Python kütüphanelerini yüklemek için şu komutu çalıştırabilirsiniz:

```bash
pip install -r requirements.txt
```

## Kurulum ve Çalıştırma

### 1. Projeyi Klonlayın

GitHub'dan projeyi bilgisayarınıza klonlayın:

```bash
git clone https://github.com/muhammedaydiiinn/article_fetch_bot.git
cd article_fetch_bot
```

### 2. Gereksinimleri Yükleyin

`requirements.txt` dosyasındaki kütüphaneleri yükleyin:

```bash
pip install -r requirements.txt
```

### 3. URL Listesini Hazırlayın

**`sayi_url_listesi.txt`** dosyasına, arşiv sayfalarındaki makale linklerinin bulunduğu URL'leri ekleyin. Her URL yeni bir satıra yerleştirilmelidir.

### 4. URL Toplama: `article_archive_url_fetch.py`

Arşiv sayfalarındaki makale URL'lerini toplamak için **`article_archive_url_fetch.py`** betiğini çalıştırın:

```bash
python article_archive_url_fetch.py
```

Bu betik, arşiv sayfalarındaki makale sayfalarının URL'lerini çeker ve **`sayi_url_listesi.txt`** dosyasına kaydeder.

### 5. E-posta Çekme: `mail_cekme_script.py`

Makale sayfalarındaki yazarlara ait e-posta adreslerini toplamak için **`mail_cekme_script.py`** betiğini çalıştırın:

```bash
python mail_cekme_script.py
```

Bu betik, **`sayi_url_listesi.txt`** dosyasındaki her URL'yi işler ve makalelerdeki başlıkları ve yazarlara ait e-posta adreslerini **`makale_mailler.xlsx`** dosyasına kaydeder.

### 6. Sonuçları Görüntüleyin

Bot çalıştıktan sonra, tüm makale başlıkları ve e-posta adresleri **`makale_mailler.xlsx`** dosyasına kaydedilecektir.

---

## Kullanım Örneği

Örneğin, **`sayi_url_listesi.txt`** dosyasına şu URL'leri eklediyseniz:

```
https://malque.pub/ojs/index.php/mr/issue/view/46
https://malque.pub/ojs/index.php/mr/issue/view/47
```

1. **`article_archive_url_fetch.py`** betiği çalıştırıldığında bu URL'leri toplar.
2. Sonrasında, **`mail_cekme_script.py`** betiği çalıştırılarak, her bir URL'nin içindeki makale başlıkları ve e-posta adresleri çekilir ve kaydedilir.

---

## Başka Bir Bilgi

- **Headless Mod**: Bu bot, tarayıcıyı gizli (headless) modda çalıştırarak, görsel arayüzü göstermeden işlemi gerçekleştirir. Tarayıcıyı görsel olarak görmek isterseniz, `chrome_options.add_argument("--headless")` satırını kaldırabilirsiniz.
  
---

## Katkı

Bu proje açık kaynaklıdır ve katkılara açıktır. Eğer bir hata bulduysanız ya da geliştirmek için bir öneriniz varsa, lütfen bir **Pull Request** açın veya **Issue** oluşturun.
