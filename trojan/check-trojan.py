import os
import urllib.parse
import json

# Mendapatkan path relatif ke file "list-active.txt"
file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "subcription", "list-active.txt")

# Membaca daftar tautan Trojan dari file
trojan_links = []
with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        if line.startswith("trojan://"):
            trojan_links.append(line)

# Membuat list untuk menyimpan konfigurasi Clash
clash_configs = []

# Loop melalui tautan Trojan
for trojan_link in trojan_links:
    # Menghapus "trojan://" dari tautan
    trojan_link = trojan_link[len("trojan://"):]

    # Memisahkan tautan berdasarkan "@" untuk mendapatkan host dan port (jika ada)
    parts = trojan_link.split("@")

    # Inisialisasi port dengan None
    port = None

    # Mengekstrak port jika ada
    if len(parts) > 1:
        port_str = parts[1]
        # Mencari indeks tanda titik dua (":") dan tanda tanya ("?")
        colon_index = port_str.find(":")
        question_index = port_str.find("?")
        if colon_index != -1:
            # Jika ada tanda titik dua, ekstrak port dari string
            port_str = port_str[colon_index + 1:question_index] if question_index != -1 else port_str[colon_index + 1:]
            try:
                port = int(port_str)
            except ValueError:
                pass

    # Memeriksa apakah port adalah 443 sebelum menambahkannya ke konfigurasi Clash
    if port == 443:
        # Mengekstrak host
        host = parts[0]

        # Membuat konfigurasi Clash
        clash_config = {
            "name": host,
            "server": host,
            "port": port,
            "type": "trojan",
            "password": "",  # Anda dapat menambahkan logika untuk mengekstrak kata sandi jika diperlukan
            "skip-cert-verify": True,
            "sni": "",
            "network": "",
            "udp": True,
            "ws-opts": {
                "path": "",
                "headers": {
                    "Host": host
                }
            }
        }

        clash_configs.append(clash_config)

# Mencetak hasil dalam format JSON
clash_config_json = json.dumps({"proxies": clash_configs}, indent=2)
print(clash_config_json)
