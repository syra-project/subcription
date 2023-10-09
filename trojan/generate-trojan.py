import urllib.parse
import json

# Membaca daftar tautan Trojan dari file
trojan_links = []
with open("C:/Users/IJD/Videos/oc/New folder/New folder/New folder/subcription/list-active.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line.startswith("trojan://"):
            trojan_links.append(line)

# Membuat list untuk menyimpan konfigurasi Clash
clash_configs = []

# Loop melalui tautan Trojan
for trojan_link in trojan_links:
    parsed_url = urllib.parse.urlparse(trojan_link)
    
    # Memeriksa jika tautan menggunakan port 443
    if parsed_url.port == 443:
        query_params = urllib.parse.parse_qs(parsed_url.query)
        
        # Memeriksa jika kunci 'host' ada dalam query_params
        if 'host' in query_params:
            # Membuat konfigurasi Clash
            clash_config = {
                "name": query_params["host"][0],
                "server": parsed_url.hostname,
                "port": parsed_url.port,
                "type": "trojan",
                "password": parsed_url.username,
                "skip-cert-verify": True,
                "sni": query_params.get("sni", [""])[0],
                "network": query_params.get("type", [""])[0],
                "udp": True,
                "ws-opts": {
                    "path": urllib.parse.unquote(query_params.get("path", [""])[0]),
                    "headers": {
                        "Host": query_params["host"][0]
                    }
                }
            }
        
            clash_configs.append(clash_config)

# Mencetak hasil dalam format JSON
clash_config_json = json.dumps({"proxies": clash_configs}, indent=2)
print(clash_config_json)
