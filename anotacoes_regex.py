from telefones import TelefonesBr
import re
'''
# exemplo
# padrao = "[0-9][a-z]{2}[0-9]" # busca o padrão de um numero de 0 a 9, 2 letras, um numero de 0 a 9 ex: num letra letra num
# texto = "123 1a22 1cc aa1 2cb3"
# resposta = re.search(padrao, texto) # .search busca a primeira ocorrência do padrão
# print(resposta.group()) 
'''

'''
# exemplo email
# padrao ="\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}" # "\w" numero de 0-9 ou letras de a-z A-Z{de x, a y caracteres}
# texto = "aaaabbbccc TeSTe@hotmail.com.br aaabb aacc"
# resposta = re.search(padrao, texto)
# print(resposta.group())
'''
#exemplo telefone (xx) xxxx-xxxx
padrao ="[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto = "aa bbb ddd cc ee ff 1432323231 abd 143232 asdas 1432323233"

resposta = re.findall(padrao, texto) # busca todas as ocorrências do padrão e retorna uma lista com os resultados 
print(resposta)