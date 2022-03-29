from Atendimento import Atendimento
from util import buscarMenor, mediaTest

#Cria um Atendimentos e adicionar em um lista
atendimentos = list()
atendimentos.append(Atendimento('A'))
atendimentos.append(Atendimento('B'))
atendimentos.append(Atendimento('C'))
atendimentos.append(Atendimento('D'))

#Gerar clientes de forma dinamica
while True:
  comm = input()
  if comm == "ok":
    break
  else:
    buscarMenor(atendimentos)
    
    for atendimento in atendimentos:
      print(atendimento.tamanhoFila())

atendimentos[0].iniciarAtendimento()
atendimentos[0].finalizarAtendimento()


print(atendimentos[0].gerarRelatorio('teste'))

#arrayDeTempo = ['00:08:21', '00:08:21', '00:08:12']
#'00:12:50' => 12 x 60 = 720 + 50s restantes = 770s
#'00:04:21' => 4 x 60 = 240 + 21s restantes = 261s
#media = 770 + 261 = 1031s / 2 = 515.5s
#media em minutos = 515.5 / 60s = 8.5 minutos
#SERÁ QUE PODE ESTAR CERTO? 
#result = mediaTest(arrayDeTempo)
#print(str(result))
