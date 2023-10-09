import yaml
from tqdm import tqdm

# Membaca daftar alamat IP dari file txt
ip_list_filename = "bug.txt"
with open(ip_list_filename, "r") as ip_file:
    ip_list = ip_file.read().splitlines()

# Prefix untuk nama akun
name_prefix = "TRojan"

# Inisialisasi struktur konfigurasi
config = {"proxies": []}

# Fungsi untuk menghasilkan konfigurasi berdasarkan IP
def generate_config(ip):
    config_entry = {
        "name": f"{name_prefix}-{ip.replace('.', '-')}",
        "server": ip,
        "port": 443,
        "type": "trojan",
        "password": "c86863ab-6277-447b-b386-f73b8518e904",
        "network": "ws",
        "sni": "id8.fastvpn.biz.id",
        "skip-cert-verify": True,
        "udp": True,
        "ws-opts": {"path": "/trojan-ws"},
        "headers": {"Host": "id8.fastvpn.biz.id"},
    }
    return config_entry

# Generate konfigurasi untuk setiap IP dan tambahkan ke daftar konfigurasi
for ip in tqdm(ip_list, desc="Generating Configuration", unit="IP"):
    config["proxies"].append(generate_config(ip))

# Simpan konfigurasi dalam berkas YAML
print("Mulai menyimpan konfigurasi dalam berkas YAML")
with tqdm(total=1, desc="Saving Configuration", unit="File") as pbar:
    with open("config.yaml", "w") as config_file:
        yaml.dump(config, config_file, default_flow_style=False, sort_keys=False)
        pbar.update(1)
print("Konfigurasi berhasil disimpan dalam berkas YAML")

# Pesan ketika proses selesai
print("Proses telah selesai")
