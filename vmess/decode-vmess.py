import base64
import json

# Tautan V2Ray vmess
vmess_link = "vmess://eyJ2IjoiMiIsInBzIjoiRC1CUk9XTi0xMDI1IiwiYWRkIjoiMTU3LjI0NS40LjE3MCIsInBvcnQiOiI4ODgxIiwiaWQiOiJkYjVhZmFlNC1hYzIzLTQxYTYtODM3OC1mMzA3YTlhNDc0MzYiLCJhaWQiOiIwIiwic2N5IjoiYXV0byIsIm5ldCI6InRjcCIsInR5cGUiOiJodHRwIiwiaG9zdCI6Im1paGFud2ViaG9zdC5jb20iLCJwYXRoIjoiLyIsInRscyI6Im5vbmUiLCJzbmkiOiIiLCJhbHBuIjoiIn0="

# Fungsi untuk mengkonversi tautan vmess menjadi konfigurasi V2Ray
def decode_vmess(vmess_link):
    # Menghapus "vmess://" dari tautan
    vmess_data = vmess_link.replace("vmess://", "")
    
    # Mendekode base64
    decoded_data = base64.b64decode(vmess_data)
    
    # Mengkonversi ke format JSON
    vmess_config = json.loads(decoded_data)
    
    return vmess_config

# Menggunakan fungsi untuk mendapatkan konfigurasi V2Ray
v2ray_config = decode_vmess(vmess_link)

# Menampilkan hasilnya
print(json.dumps(v2ray_config, indent=4))
