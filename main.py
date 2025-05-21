import hashlib

def gerar_hash(senha):
    """Gera um hash SHA-256 da senha"""
    return hashlib.sha256(senha.encode()).hexdigest()

# Senha original definida
senha_original = "minhaSenhaSegura123"
hash_senha_original = gerar_hash(senha_original)

# Tentativa de alterar a senha
tentativa_senha = str(input("Digite uma senha: "))

# Verificando a tentativa
hash_tentativa = gerar_hash(tentativa_senha)

if hash_tentativa == hash_senha_original:
    print("A senha permanece inalterada.")
else:
    print("Tentativa de modificar a senha detectada! Alteração não permitida.")
