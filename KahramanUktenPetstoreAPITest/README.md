# KahramanUktenPetstoreAPITest

Bu proje, https://petstore.swagger.io/ üzerindeki "pet" endpoint'lerini kullanarak CRUD (Create, Read, Update, Delete) işlemleri için pozitif ve negatif senaryoları test eder.

## Kullanım Kuralları

- Tüm testler `pytest` ile yazılmıştır.
- Ortak bir `PET_ID` (`999999`) kullanılmaktadır.
- Testler birbirine bağımlı değildir. Ancak `create_pet()` fonksiyonu ile bazı testler öncesinde test pet'i sisteme eklenir.
- Swagger API, eksik body içeren isteklere karşı bazen 200 dönebilmektedir. Bu nedenle `create_pet_negative` ve `update_pet_negative` testlerinde `200` kabul edilmektedir.

## Gereksinimler

- Python 3.7+
- `requests`
- `pytest`

## Kurulum

```bash
pip install -r requirements.txt
```

## Testleri Çalıştırmak

```bash
pytest tests/test_pet_api.py
```
