from validate_docbr import CPF, CNPJ

# aplicando factory

class Documento:

	@staticmethod
	def criar_documento(documento):
		if len(documento) == 11:
			return DocCpf(documento)
		elif len(documento) == 14:
			return DocCnpj(documento)
		else:
			raise ValueError("Documento Inválido")

class DocCpf:
	def __init__(self, documento):
		if self.validar(documento):
			self.cpf = documento
		else:
			raise ValueError("CPF Inválido")

	def validar(self, documento):
		validar = CPF() # instância objeto da classe CPF (import validate_docbr)
		return validar.validate(documento) # método de validação de cpf da classe CPF 

	def formatar(self):
		mascara = CPF()
		return mascara.mask(self.cpf) # método de aplicação de mascara da classe CPF

	def __str__(self):
		return self.formatar()

class DocCnpj:
	def __init__(self, documento):
		if self.validar(documento):
			self.cnpj = documento
		else:
			raise ValueError("CNPJ Inválido")

	def validar(self, documento):
		validar = CNPJ() # instância objeto da classe CNPJ (import validate_docbr)
		return validar.validate(documento) # método de validação de cnpj da classe CNPJ 

	def formatar(self):
		mascara = CNPJ()
		return mascara.mask(self.cnpj) # método de aplicação de mascara da classe CNPJ

	def __str__(self):
		return self.formatar()


'''
# sem factory
class CpfCnpj:
	def __init__(self, documento, tipo_documento):
		self.tipo_documento = tipo_documento
		documento = str(documento)

		if tipo_documento == 'cpf':
			if self.validar_cpf(documento):
				self.cpf = documento
			else:
				raise ValueError("CPF Inválido")
		elif tipo_documento == 'cnpj':
			if self.validar_cnpj(documento):
				self.cnpj = documento
			else:
				raise ValueError("CNPJ Inválido")
		else:
			raise ValueError("Documento Inválido")

	def __str__(self):
		if self.tipo_documento == 'cpf':
			return self.formatar_cpf()
		elif self.tipo_documento == 'cnpj':
			return self.formatar_cnpj()


	def validar_cpf(self, cpf):
		if len(cpf) == 11:
			validar = CPF() # instância objeto da classe CPF (import validate_docbr)
			return validar.validate(cpf) # método de validação de cpf da classe CPF 
		else:
			raise ValueError('CPF Incompleto')

	def formatar_cpf(self):
		mascara = CPF()
		return mascara.mask(self.cpf) # método de aplicação de mascara da classe CPF

	def validar_cnpj(self, cnpj):
		if len(cnpj)== 14:
			validar = CNPJ() # instância objeto da classe CNPJ (import validate_docbr)
			return validar.validate(cnpj)
		else:
			raise ValueError('CNPJ Incompleto')

	def formatar_cnpj(self):
		mascara = CNPJ()
		return mascara.mask(self.cnpj) # método de aplicação de mascara da classe CNPJ 
'''