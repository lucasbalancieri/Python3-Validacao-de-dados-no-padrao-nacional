import re


class TelefonesBr:
	def __init__(self, telefone):
		if self.validar_telefone(telefone):
			self.numero = telefone
		else:
			raise ValueError('Número Inválido')

	def __str__(self):
		return self.formatar_numero()
		
	def validar_telefone(self, telefone):
		padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})" # país (2 ou 3 números) dd (2 numeros) numero(4 ou 5) numero
		resposta = re.findall(padrao, telefone)
		if resposta:
			return True
		else:
			return False

	def formatar_numero(self):
		padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
		resposta = re.search(padrao, self.numero)
		numero_formatado = "+{}({}){}-{}".format(resposta.group(1), resposta.group(2), resposta.group(3), resposta.group(4))
		return numero_formatado


