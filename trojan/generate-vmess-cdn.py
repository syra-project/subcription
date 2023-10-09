import base64
import json
import yaml

def parse_vmess_url(vmess_url):
    try:
        vmess_data = base64.urlsafe_b64decode(vmess_url.replace("vmess://", "")).decode("utf-8")
        vmess_json = json.loads(vmess_data)
        return vmess_json
    except Exception as e:
        print(f"Failed to parse Vmess URL: {str(e)}")
        return None

def convert_to_x2ray_proxy(vmess_list):
    proxies = []
    for vmess_url in vmess_list:
        vmess_data = parse_vmess_url(vmess_url)
        if vmess_data:
            proxy = {
                "name": f"{vmess_data['ps']}-{vmess_data['add']}-{vmess_data['port']}",
                "server": '104.16.51.111',
                "port": vmess_data['port'],
                "type": "vmess",
                "uuid": vmess_data['id'],
                "alterId": vmess_data.get('aid', 64),
                "cipher": "auto",
                "tls": True,
                "skip-cert-verify": True,
                "servername": vmess_data['host'],
                "network": "ws",
                "ws-opts": {
                    "path": vmess_data.get('path', '/'),
                    "headers": {
                        "Host": vmess_data['host']
                    }
                },
                "udp": True
            }
            proxies.append(proxy)
    return proxies

vmess_list_file = []
with open('subcription/vmess-list.txt', 'r') as vmess_file:
    vmess_list = vmess_file.read().splitlines()

proxies = convert_to_x2ray_proxy(vmess_list)

# Simpan ke dalam file proxies.yaml dengan format yang diinginkan
with open('proxies-cdn.yaml', 'w', encoding='utf-8') as yaml_file:
    yaml_file.write("proxies:\n")
    for proxy in proxies:
        yaml_file.write(f"  - {{name: {proxy['name']}, server: {proxy['server']}, port: {proxy['port']}, type: {proxy['type']}, uuid: {proxy['uuid']}, alterId: {proxy['alterId']}, cipher: {proxy['cipher']}, tls: {proxy['tls']}, skip-cert-verify: {proxy['skip-cert-verify']}, servername: {proxy['servername']}, network: {proxy['network']}, ws-opts: {proxy['ws-opts']}, udp: {proxy['udp']}}}\n")

print("Proxies telah disimpan dalam proxies-cdn.yaml")
