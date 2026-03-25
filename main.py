import secrets
import string

def gerar_senha_segura(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    while True:
        senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
        
        if (any(c.isdigit() for c in senha) and
            any(c in string.punctuation for c in senha) and
            any(c.isupper() for c in senha)):
            return senha

def verificar_forca(senha):
    if len(senha) < 8:
        return "Fraca"
    elif any(c.isdigit() for c in senha) and any(c in string.punctuation for c in senha):
        return "Forte"
    else:
        return "Média"

def main():
    print("=== Gerador de Senhas ===")

    try:
        tamanho = int(input("Digite o tamanho da senha: "))

        if tamanho < 8:
            print("⚠️ O ideal é usar pelo menos 8 caracteres.")

        senha = gerar_senha_segura(tamanho)

        print(f"\nSenha gerada: {senha}")
        print(f"Força da senha: {verificar_forca(senha)}")

    except ValueError:
        print("Por favor, digite um número válido.")

if __name__ == "__main__":
    main()