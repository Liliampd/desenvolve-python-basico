'''# Lista de URLs fornecidas
urls = ["www.google.com", "www.facebook.com", "www.twitter.com", "www.linkedin.com"]
# Extrair os nomes dos domínios usando fatiamento
dominios = [url[4:-4] for url in urls]
# Exibir o resultado
print("Lista de domínios:", dominios)
'''


urls = ["www.google.com", "www.facebook.com", "www.twitter.com", "www.linkedin.com"]


dominios = [url[4:-4] for url in urls]

print("Lista de domínios:", dominios)
