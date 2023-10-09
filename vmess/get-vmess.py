import requests
import base64
import json

# Membaca daftar URL dari file sub.txt
with open('subcription\sub.txt', 'r') as file:
    url_list = file.read().splitlines()

# Membuat list baru untuk menyimpan hanya link vmess dengan port 443 dari semua file
filtered_vmess_list = []

# Loop melalui semua URL dan mengambil daftar akun dari masing-masing URL
for url in url_list:
    response = requests.get(url)
    if response.status_code == 200:
        akun_list = response.text.splitlines()
        for akun in akun_list:
            if akun.startswith("vmess://"):
                # Mengurai link vmess
                vmess_data = json.loads(base64.urlsafe_b64decode(akun[8:]))
                # Memeriksa jika port adalah 443
                if "port" in vmess_data and vmess_data["port"] == 443:
                    filtered_vmess_list.append(akun)

# Menyimpan semua link vmess dengan port 443 ke dalam file vmess-list.txt (mengganti isi sebelumnya)
with open('subcription/vmess-list.txt', 'w') as vmess_file:
    for vmess in filtered_vmess_list:
        vmess_file.write(vmess + '\n')
