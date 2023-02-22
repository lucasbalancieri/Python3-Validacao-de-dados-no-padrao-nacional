import requests


class BuscaEndereco:

	def __init__(self, cep):
		cep = str(cep)
		if self.cep_e_valido(cep):
			self.cep = cep
		else:
			raise ValueError ("CEP Inválido")

	def __str__(self):
		return self.formatar_cep()

	def cep_e_valido(self, cep):
		if len(cep) == 8:
			return True
		else:
			return False

	def formatar_cep(self):
		return "{}-{}".format(self.cep[0:5], self.cep[5:])

	def acessa_via_cep(self):
		url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
		r = requests.get(url)
		dados = r.json()
		return (dados['bairro'], dados['localidade'], dados['uf'])