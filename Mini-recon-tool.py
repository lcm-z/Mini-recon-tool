# Codigo reorganizado por: @MarkDevBrasil
# Adorei o projeto e quis dar uma melhorada!
# TMJ


import requests
import socket

PORTAS =  [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 5432, 8080, 8443]

HEADERS_SEGURANCA = [
    "Strict-Transport-Security",
    "X-Frame-Options",
]


def menu():
    print("\n=== Mini Recon Tool ===")
    print("1 - Escanear portas")
    print("2 - Verificar headers de segurança")
    print("3 - Sair")
    
def scan_portas(site):
    print(f"\n[+] Escaneando {site}...\n")

    for porta in PORTAS:
        conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conexao.settimeout(1)

        resultado = conexao.connect_ex((site, porta))

        if resultado == 0:
            print(f"[+] Porta {porta}: ABERTA")
        else:
            print(f"[-] Porta {porta}: fechada")

        conexao.close()
        
def verificar_headers(site):
    try:
        reposta = requests.get(site, timeout=5)
        print(f"\n[+] Verificando headers de segurança em {site}...\n")
        
        for header in HEADERS_SEGURANCA:
            if header in reposta.headers:
                print(f"[+] Header {header}: PRESENTE")
            else:
                print(f"[-] Header {header}: AUSENTE")
    except requests.exceptions.RequestException as erro:
        print(f"[-] Erro ao verificar headers: {erro}")
        

def main():
    while True:
        menu()
        opçao = input("\nEscolha uma opção:").strip()
        
        if opçao == "1":
            site = input("Digite o domínio ou IP: ").strip()

            scan_portas(site)
        elif opçao == "2":
            site = input("Digite a URL: ").strip()

            if not site.startswith(("http://", "https://")):
                site = "https://" + site

            verificar_headers(site)
        elif opçao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

        continuar = input("\nQuer verificar outro site? [S/N]: ").strip().lower()

        if continuar != "s":
            break


if __name__ == "__main__":
    main()
