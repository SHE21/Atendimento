from datetime import timedelta
from Cliente import Cliente


def buscarMenor(lst):
    i = float("inf")
    atendimento = None
    for nr in lst:
        if nr.tamanhoFila() < i:
            i = nr.tamanhoFila()
            atendimento = nr
    cliente = Cliente('Cliente' + str(1), '11:'+str(1)+':51', str(1))
    atendimento.adicionarCliente(cliente)
    return i


  
#media de tempo dos atendimentos
#o tempo vai estar assim: ['00:12:50', '00:04:21']
#essa é a entrada do metodo, é desses dados que vão extrair a media. Esse calculo já é feito na classe Cliente
arrayDeTempo = ['00:12:50', '00:04:21']

def mediaTest(arrayDeTempo):
  media = 0
  arrayResults = []
  for tempo in arrayDeTempo:
    #aqui é a logica, que vai converter '00:12:50' em segundos, ou milisegundos
    #adiconar todos no array
    minutes = tempo.split(':')#transforma em um array: ['00', '12', '50']
    segundos = (int(minutes[1]) * 60) + int(minutes[2]) #transforma tudo sem segundo
    arrayResults.append(segundos)#adionar resultado em um array
  #calcula a media
  media = sum(arrayResults) / len(arrayResults)#pega aqui o tamanho do array

  #retorna a media
  return media / 60 #e depois transfroma tudo em segundos novamente. PODERIAMOS FAZER O CALCULO APENAS COM OS MINUTOS, NO ENTANTO PERDERIMOS OS SEGUNDOS, DAI A NECESSIDADE DE CONVERTER EM SEGUNDOS
  

