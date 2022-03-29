from datetime import datetime
from util import buscarMenor, mediaTest

class Atendimento:
  def __init__(self, atendimentoId):
    self.fila = []
    self.atendimentoId = atendimentoId
    self.clienteEmAtendimento = None
    self.historicoAtendidos = []

  #Tamnho da Fila
  def tamanhoFila(self):
    return len(self.fila)

  #Obtem o horário.
  def timeNow(self):
   return datetime.now().strftime("%H:%M:%S")

  #Pegar Fila
  def getFila(self):
    clientes = []
    for cliente in self.fila:
      clientes.append(cliente.toString())
    return clientes
    
  #Pega o Cliente que está sendo atendido
  def getClienteEmAtendimento(self):
    if self.clienteEmAtendimento != None:
      return self.clienteEmAtendimento
    else:
      return "Não há cliente sendo atendido!"

  #Pega o nome do Atendimento
  def getAtendimentoId(self):
    return self.atendimento

  #Pega o histórico de Atendimento
  def getHistoricoAtendidos(self):
    if len(self.historicoAtendidos) != 0:
      return self.historicoAtendidos
    else:
      return "Nenhum Cliente foi atendido!"

  def gerarArquivo(self, content):
    file = open("relatorio.txt", 'w')
    file.writelines(content)

  #Gerar relatório
  def gerarRelatorio(self, file):
    listContent = list()
    
    #Tamanho da fila
    tamanhoFila = self.tamanhoFila()
    
    #Status do atendimento (Quem está sendo atendido)
    status = self.getClienteEmAtendimento()

    #Histórico de atendimento
    mediaTempoAtendimento = []
    mediaTempoNaFila = []
    
    listContent.append("------ Histórico de Atendimento ------\n")
    historico = self.getHistoricoAtendidos()
    for cliente in historico:
      timeAtendimento = cliente.getTempoAtendimento()
      timeNaFila = cliente.getTempoFila()
      
      mediaTempoAtendimento.append(timeAtendimento)
      mediaTempoNaFila.append(timeNaFila)
      listContent.append(cliente.toString() + '\n')

    listContent.append("------ Media de Atendimento ------\n")
    listContent.append(str(mediaTest(mediaTempoAtendimento)) + '\n')

    listContent.append("------ Média de Tempo na Fila ------\n")
    listContent.append(str(mediaTest(mediaTempoNaFila)) + '\n')

    listContent.append("------ Clientes na Fila ------\n")
    if len(self.fila) != 0:
      for cliente in self.fila:
        listContent.append(cliente.toString() + '\n')
    else:
      listContent.append('Nenhum Cliente na fila \n')
    
    #Total de Clientes atendidos
    totalAtendidos = len(historico)

    listContent.append("------ Tamanho da Fila ------\n")
    listContent.append(str(tamanhoFila) + '\n')
    listContent.append("------ Status ------\n")
    listContent.append(str(status) + '\n')

    listContent.append('------ Total de Atendimento ------\n')
    listContent.append(str(totalAtendidos) + '\n')

    self.gerarArquivo(listContent)

    return listContent
    
    
  #Adicionar um Cliente na Fila do Atendimento
  def adicionarCliente(self, cliente):
    self.fila.append(cliente)
    
  #Iniciar um Atendimento
  def iniciarAtendimento(self):
    startAtendimento = self.timeNow()
    cliente = self.fila[0]

    cliente.setStartAtendimento(startAtendimento)
    cliente.setSaiuDaFila(startAtendimento)

    self.clienteEmAtendimento = cliente
    
    #Remove o Cliente da Fila ao iniciar o Atendimento.
    self.fila.pop(0)

    
  #Finaliza um Atendimento
  def finalizarAtendimento(self):
    cliente = self.clienteEmAtendimento
    #armazena horário de encerramento do atendimento
    cliente.setEndAtendimento(self.timeNow())

    #Adicionar Cliente a historico de atendimentos
    self.historicoAtendidos.append(cliente)

    #Agora o atendimento está livre
    self.clienteEmAtendimento = None
    
    return "Atendimento finalizado!"