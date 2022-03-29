from datetime import datetime, timedelta

class Cliente:
  def __init__(self, name, entrouNaFila, senha):
    self.name = name
    self.entrouNaFila = entrouNaFila
    self.saiuDaFila = None
    self.senha = senha
    self.startAtendimento = None
    self.endAtendimento = None

    self.tempoFila = None
    self.tempoAtendimento = None

  #Subtração de tempo
  def getIntervalo(self, starts, ends):
    start = starts.split(':')
    end = ends.split(':')
  
    time_1 = timedelta(hours= int(start[0]), minutes= int(start[1]), seconds= int(start[2]))
    time_2 = timedelta(hours= int(end[0]), minutes= int(end[1]), seconds= int(end[2]))
  
    return str(time_2 - time_1)

  def getName(self):
    return self.name

  def getEntrouNaFila(self):
    return self.entrouNaFila

  def getSaiuDaFila(self):
    return self.saiuDaFila

  def setSaiuDaFila(self, saiuDaFila):
    self.saiuDaFila = saiuDaFila

  def getSenha(self):
    return self.senha

  def getStartAtendimento(self):
    return self.startAtendimento

  def setStartAtendimento(self, startAtendimento):
    self.startAtendimento = startAtendimento

  def setEndAtendimento(self, endAtendimento):
    self.endAtendimento = endAtendimento
    
  def getEndAtendimento(self):
    return self.endAtendimento

  def setTempoAtendimento(self):
    start = self.getStartAtendimento()
    ends = self.getEndAtendimento()
    
    if (start != None) and (ends != None):
      self.tempoAtendimento = self.getIntervalo(start, ends)
      return self.tempoAtendimento
    else:
      return self.tempoAtendimento

  def getTempoAtendimento(self):
    self.setTempoAtendimento()
    return self.tempoAtendimento
    
  #Calcula o tempo em que o Cliente ficou na Fila
  #e atribui o resultado a variável 'self.tempoFila'
  def setTempoFila(self):
    entrouFila = self.getEntrouNaFila()
    saiuFila = self.getSaiuDaFila()
    
    if (entrouFila != None) and (saiuFila != None):
      self.tempoFila = self.getIntervalo(entrouFila, saiuFila)
      return self.tempoFila
    else:
      return self.tempoFila
      
  #Pega o Tempo em que o Cliente ficou na Fila
  def getTempoFila(self):
    self.setTempoFila()
    return self.tempoFila

  def toString(self):
    return "name:" + self.getName() + ", senha:" + self.getSenha() + ", entrouNaFila:" + self.getEntrouNaFila() + ", saiuDaFila:" + str(self.getSaiuDaFila()) + ", startAtendimento:" + str(self.getStartAtendimento()) + ", endAtendimento:" + str(self.getEndAtendimento()) + ", tempoFila:" + str(self.getTempoFila()) + ", tempoAtendimento:" + str(self.getTempoAtendimento())