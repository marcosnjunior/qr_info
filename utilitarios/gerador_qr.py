import qrcode
import argparse
import os

def gerar_qrcode(url, nome_arquivo="qrcode.png"):
    """
    Gera um QR Code a partir de uma URL e salva como imagem.
    
    Args:
        url (str): URL para codificar no QR Code
        nome_arquivo (str): Nome do arquivo de saída (padrão: qrcode.png)
    """
    try:
        # Criar o QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        # Gerar a imagem
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Salvar a imagem
        img.save(nome_arquivo)
        print(f"QR Code gerado com sucesso e salvo como '{nome_arquivo}'")
        print(f"URL codificada: {url}")
        
    except Exception as e:
        print(f"Erro ao gerar QR Code: {e}")

def main():
    # Configurar o parser de argumentos
    parser = argparse.ArgumentParser(description='Gerador de QR Code a partir de URL')
    parser.add_argument('url', help='URL para gerar o QR Code')
    parser.add_argument('-o', '--output', help='Nome do arquivo de saída (padrão: qrcode.png)', default="qrcode.png")
    
    # Obter os argumentos
    args = parser.parse_args()
    
    # Verificar se a URL começa com http:// ou https://
    if not args.url.startswith(('http://', 'https://')):
        args.url = 'https://' + args.url
    
    # Gerar o QR Code
    gerar_qrcode(args.url, args.output)

if __name__ == "__main__":
    main()