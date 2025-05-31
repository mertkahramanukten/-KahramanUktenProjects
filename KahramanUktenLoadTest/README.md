
# KahramanUktenLoadTest 🔍

Bu proje, [n11.com](https://www.n11.com)'un arama modülüne yönelik Locust ile hazırlanmış bir yük testidir.

## 🔧 Kurulum

```
pip install -r requirements.txt
```

## 🚀 Çalıştırma

```
locust -f locustfile.py --headless -u 1 -r 1 --host=https://www.n11.com
```

## 🎯 Test Senaryosu

- Anasayfa açılır
- "telefon" kelimesi ile arama yapılır
- Arama sonucu sayfası kontrol edilir
