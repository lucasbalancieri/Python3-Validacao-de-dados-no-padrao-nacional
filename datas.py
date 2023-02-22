from datetime import datetime, timedelta


class DatasBr:
	def __init__(self):
		self.momento_cadastro = datetime.today()

	def __str__(self):
		return self.formatar_data()

	def mes_cadastro(self):
		meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dec"]
		mes_cadastro = self.momento_cadastro.month - 1
		return meses[mes_cadastro]

	def dia_semana(self):
		semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]
		dia_semana = self.momento_cadastro.weekday()
		return semana[dia_semana]

	def formatar_data(self):
		data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
		return data_formatada

	def tempo_cadastro(self):
		tempo_cadastro = (datetime.today() + timedelta(days = 15, minutes = 20, seconds = 30)) - self.momento_cadastro
		return tempo_cadastro