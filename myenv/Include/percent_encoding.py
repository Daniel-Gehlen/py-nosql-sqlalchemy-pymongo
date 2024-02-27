import urllib.parse

# Lendo a senha do arquivo password.txt
with open('password.txt', 'r') as file:
    password = file.readline().strip()

# Convertendo a senha usando percent encoding
encoded_password = urllib.parse.quote(password, safe="")

print("Senha codificada:", encoded_password)
