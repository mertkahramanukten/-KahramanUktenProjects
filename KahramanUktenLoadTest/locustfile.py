from locust import HttpUser, task, between

class N11User(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        self.headers = {
            "authority": "www.n11.com",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "referer": "https://www.n11.com/",
            "cookie": "__hapc=e22244b4-31b5-4037-b817-195da0763013; _cfuvid=m1Xr00SbULRdvLk631nasl54trdXTGmh9KSRKFZZke4-1748652989161-0.0.1.1-604800000; _ATHENA_SID=11911308-08e7-48a4-9174-69af936b6a7f; n11_cookie_ver_1=true; locationInfoPopup=true; SID=1459cf9c-e618-4ba7-8b36-71950c008e3c8256883b-6784-4c01-870b-6d52c5386366; __hausc=855f4783-6618-41e0-a26f-5c531eccff20; __apc=e22244b4-31b5-4037-b817-195da0763013; _gcl_au=1.1.168839671.1748652990; _dn_sid=60baaa7f-6d27-44a0-8c43-7fc69848b744; _ga=GA1.1.918076562.1748653100; _hjSessionUser_196222=eyJpZCI6ImQxZjRlZTc0LTgzNjUtNTJhYy1iMTI5LTBiYmVhYmZkOTc0NiIsImNyZWF0ZWQiOjE3NDE2MDM5MzMxODEsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_196222=eyJpZCI6ImIxMDQ4ZWIyLTljYmYtNGY3OS05NjkzLTNjNGYxNDlhNDU3ZiIsImMiOjE3NDg2NTMxMDAwODYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; cebs=1; _p2s_cc=grant; _ce.clock_data=-981%2C195.142.166.105%2C1%2C0fe6feb54289f4c67027ec06cc2131f8%2CChrome%2CTR; _pin_unauth=dWlkPU9ESXpaRFEzTVRjdE5EUTVZaTAwTURoakxXSTNZamd0WVdOa1pXTTNNamMyTldObQ; _tt_enable_cookie=1; _ttp=01JWHXHM29PDM0PYJK2AEC8MH2_.tt.1; _dn_data=e22244b4-31b5-4037-b817-195da0763013||||||; _ATHENA_DID=e22244b4-31b5-4037-b817-195da0763013; __cf_bm=GNvhWvT60pK9NBxby7d2Kloqz2466.tAlDqZZltwNLY-1748653968-1.0.1.1-Mihpk2UHkXAi.U_c2X68tdSLJMQ4YwcTCNe5OVpsZcQqnQPPG3tk_VCa5j1uIn3g6p7nI2G4qxVPimliakzTtawTH6p3jaRlYMNW5Dwx7DQ; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22undefined%22%2C%22expiryDate%22%3A%222026-05-31T01%3A12%3A48.680Z%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22Rvv8tnlIQR9EYgv6DL0Q%22%2C%22expiryDate%22%3A%222026-05-31T01%3A12%3A48.680Z%22%7D; _ga_CR868RESVB=GS2.1.s1748653099$o1$g1$t1748653968$j43$l0$h0; cto_bundle=_qO_iF9wQkZNRkFsUkd4MHB1eFh2YVBsRTVRY2ZWU05NckVhMGRURUVtTCUyQmJWS0hCRk5KMEs2UFB2MEczU1QyT21zVHQwZTdNOTdFSzYlMkYwRXJxazlJQ0Fnckh0cG5hJTJGTlE3MTJQaElnRkkwZnZ6WDlNT1BpY2lNc0JrUUMxOWpaSm42JTJGYVI3c215WGtlamIyeUs1RVZaeXBMZyUzRCUzRA; ttcsid=1748653101146::FR6Kb7vWIemLefK3oTGQ.1.1748653969365; _derived_epik=dj0yJnU9MGpkVDdCUkU2XzcxZ3RzZ3BfNndRXzNlTEl2bTdNOUYmbj1QN25WMXg4amhvY2g3cTVGMUh5VnZRJm09MSZ0PUFBQUFBR2c2VjVJJnJtPTEmcnQ9QUFBQUFHZzZWNUkmc3A9Mg; cebsp_=4; _ce.s=v~ae7b81f04997e32cfbf85896cca396b5d7b4b893~lcw~1748653795806~vir~new~lva~1748653969542~vpv~0~as~false~v11.cs~409307~v11.s~5881fa50-3dba-11f0-8932-531d8ec0e620~v11.vs~ae7b81f04997e32cfbf85896cca396b5d7b4b893~v11.ss~1748653100666~v11ls~5881fa50-3dba-11f0-8932-531d8ec0e620~lcw~1748653969543; ttcsid_C7ENAUKHG7L4JU6R0HQG=1748653101146::mJGuKYEpYEyGRx1jN2HO.1.1748653969580; citrix_ns_id=AAs7p1Y6aDsI97cqAAAAADta2UAs0IoTFqmDO9LKUr8qaYaIJBgU2_HHbTMfQebqOw==vlg6aA==8v5e5z36Fnx63EjHes6QwcVmdNk=; _ATHENA_SID_TIMEOUT=1748655770351; ADRUM=s~1748654405288&r~aHR0cHMlM0ElMkYlMkZ3d3cubjExLmNvbSUyRg=="
        }

    @task
    def search_product(self):
        with self.client.get("/", headers=self.headers, name="Ana Sayfa", catch_response=True) as response:
            if "n11" in response.text.lower():
                response.success()
            else:
                response.failure("Ana sayfa açılmadı")

        with self.client.get("/arama?q=telefon", headers=self.headers, name="Ürün Arama", catch_response=True) as response:
            if "ürün" in response.text.lower() or "sonuç" in response.text.lower():
                response.success()
            else:
                response.failure("Beklenmeyen yanıt: 403 veya içerik yok.")
