import requests

ip = "139.192.20.158"  # Ganti dengan IP yang mau dicek (atau ambil otomatis)
url = f"http://ip-api.com/json/{ip}"

response = requests.get(url).json()

if response["status"] == "success":
    print(f"IP: {response['query']}")
    print(f"Kota: {response['city']}")
    print(f"Negara: {response['country']}")
    print(f"ISP: {response['isp']}")
    print(f"Koordinat: {response['lat']}, {response['lon']}")
else:
    print("Gagal mendapatkan lokasi.")
