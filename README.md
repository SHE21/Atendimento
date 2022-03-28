# Atendimento
Programa de gerenciamneto de atendimento presencial

Sistema de gerenciamento de Atendimento

Cada Atendimento tem uma Fila

<h2>Documentação</h2><br>
  <i>Class <code>Atendimento</code></i> <br>
  <p><i>Classe usada para criar um objeto do tipo Atendimento.</i></p>
  <b>Propriedades:</b>
  <ul>
    <li><code>fila:Cliente[]</code> - fila do tipo Cliente</li>
    <li><code>atendimentoId:String</code> - id do objeto atendimento.</li>
    <li><code>clienteEmAtendimento:Cliente</code> - armazena o status de atendimento.</li>
    <li><code>historicoAtendidos:Cliente[]</code> - armazena o histórico de atendimentos finalizados.</li>
  </ul>
  <b>Metódos</b><br>
  <code>Atendimento(atendimentoId:string)</code><br>
  <p>O construtor recebe um id como paramentro</p>
  
<code>tamanhoFila():int</code><br>
  <p>Método público que retorna um inteiro que corresponde ao tamanho da fila.</p>
  
<code>getFila():Cliente[]</code><br>
  <p>Método público que retorna um array de <code>Cliente</code> que corresponde a fila.</p>
  
<code>getClienteEmAtendimento():Cliente</code><br>
  <p>Método público que retorna um objeto do tipo <code>Cliente</code> que corresponde ao cliente em atendimento nomento.</p>
  
<code>getHistoricoAtendidos():Cliente[]</code><br>
  <p>Método público que retorna um array de objetos do tipo <code>Cliente</code> que corresponde ao histórico de clientes cujo atendimento foi concluído.</p>
  
  <code>gerarRelatorio():void</code><br>
  <p>Método público que que gera um relatório e o salva em um aquivo <code>relatorio.txt</code>.</p>
  
  <code>adicionarCliente(cliente:Cliente):void</code><br>
  <p>Método público que adiciona um <code>Cliente</code> na fila.</p>
<code>iniciarAtendimento():void</code><br>
  <p>Método público que incia o atendimento do primeiro <code>Cliente</code> da fila.</p>
  
  <i>Class <code>Cliente</code></i> <br>
  <p><i>Classe usada para criar um objeto do tipo Cliente. No nível de abstração essa classe representa um cliente.</i></p>

  <b>Propriedades:</b><br>
  <ul>
    <li><code>name:String</code> - nome do cliente</li>
    <li><code>entrouNaFila:String</code> - horário em que o cliente entrou na fila.</li>
    <li><code>saiuDaFila:String</code> - horário em que o cliente saiu da fila.</li>
    <li><code>senha:String</code> - senha do cliente.</li>
    <li><code>startAtendimento:String</code> - horário em que o cliente começa a ser atendido.</li>
    <li><code>endAtendimento:String</code> - horário em que o cliente termina o atendimento.</li>
    <li><code>tempoFila:String</code> - o tempo que o cliente ficou na fila.</li>
    <li><code>tempoAtendimento:String</code> - o tempo que o cliente ficou no atendimento.</li>
  </ul>
    <b>Metódos</b><br>
  <code>Cliente(name:string, entrouNaFila:string, senha:string)</code><br>
  <p>O construtor recebe três paramentros: nome do cliente, horário que entrou na fila e senha de atendimento.</p>
  <code>getName():string</code><br>
  <p>Método público retorna o nome do cliente.</p>
  
  <code>getEntrouNaFila():string</code><br>
  <p>Método público retorna o horário em que o cliente entrou na fila.</p>
  
  <code>getSaiuDaFila():string</code><br>
  <p>Método público retorna o horário em que o cliente saiu da fila.</p><code>setSaiuDaFila():void</code><br>
  <p>Método público put o horário em que o cliente saiu da fila.</p>
<code>getSenha():string</code><br>
  <p>Método público retorna a senha do cliente.</p>
  <code>getStartAtendimento():string</code><br>
  <p>Método público retorna horário em que o cliente iniciou o atendimento.</p>
    <code>setStartAtendimento():void</code><br>
  <p>Método privado seta horário em que o cliente iniciou o atendimento.</p>
  <code>setEndAtendimento():void</code><br>
  <p>Método privado seta horário em que o cliente finalizou o atendimento.</p>
    <code>getEndAtendimento():string</code><br>
  <p>Método privado retorna horário em que o cliente finalizou o atendimento.</p>
      <code>setTempoAtendimento():void</code><br>
  <p>Método privado que seta o calculo de tempo em que o cliente durou no atendimento.</p>
<code>getTempoAtendimento():string</code><br>
  <p>Método publico que retorna o tempo em que o cliente durou no atendimento.</p>
  <code>setTempoFila():void</code><br>
  <p>Método privado que seta o calculo de tempo em que o cliente durou na fila</p>
    <code>getTempoFila():void</code><br>
  <p>Método publico que retorna o calculo de tempo em que o cliente durou na fila</p>
      <code>toString():string</code><br>
  <p>Método publico que retorna dados concatenados das propriedades da classe.</p>
  
  <h2>Guia de Uso</h2><br>
  <p>Primeiramente é preciso criar uma instâcia da classe <code>Atendimento</code>. Uma intancia dessa classe representa um atendimento:</p>
  <p><code>
    atendimentoA = Atendimento('A')<br>
  </code></p>
  <p>Feito isso, é preciso também criar uma instâcia da classe <code>Cliente</code>fornecendo parâmetros no método construtor. Uma vez criado um objeto deste tipo o metodo <code>adicionarCliente(cliente:Cliente):void</code> deverá ser invocado para adicionar um cliente na fila do atendimento:</p>

  <p>
    <code>
      cliente = Cliente('Jack', '12:30:00', '123')<br>
      atendimentoA = Atendimento('A')<br>
      atendimentoA.adicionarCliente(cliente)
    </code>
  </p>
  <p>
    É possivel criar um número ilimitado de Atendimentos bem como de clientes:
  </p>

  <p>
    <code>
        cliente0 = Cliente('Jack', '12:30:00', '121')<br>
        cliente1 = Cliente('May', '12:31:00', '122')<br>
        cliente2 = Cliente('Paulo', '12:40:00', '123')<br>
        cliente3 = Cliente('José', '13:10:00', '124')
    </code>
  </p>
  <p>
    <code>
      atendimentoA = Atendimento('A')
      atendimentoA.adicionarCliente(cliente0)
      atendimentoB = Atendimento('B')<br>
      atendimentoB.adicionarCliente(cliente1)
      atendimentoC = Atendimento('C')<br>
      atendimentoC.adicionarCliente(cliente2)
      atendimentoC.adicionarCliente(cliente3)
    </code>
  </p>

  <p>Ao adicionar clientes em um atendimento, é possivel inicar o atendimento de um cliente invocando o método <code>iniciarAtendimento():void</code></p>
  <p><code>
    atendimentoA.iniciarAtendimento()
  </code>
  </p>
  <p>
    A partir desse momento o cliente deixa a fila e passa a ser atendido. O Horário de incio é armazenado na propridade <code>startAtendimento:String </code>
  </p>
  <p>
    Para finalizar uma atendimento o método <code>finalizarAtendimento()</code> precisa ser invocado:<br>
    <code>atendimentoA.finalizarAtendimento()</code>
  </p>
  <p>Quando um atendimento e finalizado é criado um historico de atendimento que pode ser obtido pelo metodo <code>getHistoricoAtendidos()</code></p>
    <p>Invocando o metodo <code>gerarRelatorio('teste')</code> de um atendimento é possivel obter dados desse atendimento em um aquivo txt com a seguinte saída:</p>
    <p><i>
      ------ Histórico de Atendimento ------<br>
name:Cliente1, senha:1, entrouNaFila:11:1:51, saiuDaFila:23:50:54, startAtendimento:23:50:54, endAtendimento:23:50:54, tempoFila:12:49:03, tempoAtendimento:0:00:00<br>
------ Media de Atendimento ------<br>
0.0<br>
------ Média de Tempo na Fila ------<br>
49.05<br>
------ Clientes na Fila ------<br>
name:Cliente1, senha:1, entrouNaFila:11:1:51, saiuDaFila:None, startAtendimento:None, endAtendimento:None, tempoFila:None, tempoAtendimento:None
name:Cliente1, senha:1, entrouNaFila:11:1:51, saiuDaFila:None, startAtendimento:None, endAtendimento:None, tempoFila:None, tempoAtendimento:None<br>
------ Tamanho da Fila ------<br>
2<br>
------ Status ------<br>
Não há cliente sendo atendido!<br>
------ Total de Atendimento ------<br>
1
    </i>
  </p>
    
  
