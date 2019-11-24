from socket import *
import _thread
from time import strftime
import random
import time


clientesObjeto = []
sockObj = socket(AF_INET, SOCK_STREAM)
meuHost = '192.168.2.14'
minhaPort = 5000

orig = (meuHost, minhaPort)
sockObj.bind(orig)
sockObj.listen(1)

matriz = None
linhaAnterior = None
colunaAnterior = None
fimJogo = False


class Cliente:
    def __init__(self, nomeCliente, conexaoCliente, cliente):
        self.nome = nomeCliente
        self.conexao = conexaoCliente
        self.cliente = cliente

    def getNomeCliente(self):
        return self.nome

    def getConexaoCliente(self):
        return self.conexao

    def getCliente(self):
        return self.cliente


class Matriz:

    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    lista5 = []
    lista6 = []
    lista7 = []
    lista8 = []
    lista9 = []
    lista10 = []
    valorInicial = None

    def __init__(self, valorInicial):
        self.valorInicial = valorInicial
        self.lista1 = [self.valorInicial] * 10
        self.lista2 = [self.valorInicial] * 10
        self.lista3 = [self.valorInicial] * 10
        self.lista4 = [self.valorInicial] * 10
        self.lista5 = [self.valorInicial] * 10
        self.lista6 = [self.valorInicial] * 10
        self.lista7 = [self.valorInicial] * 10
        self.lista8 = [self.valorInicial] * 10
        self.lista9 = [self.valorInicial] * 10
        self.lista10 = [self.valorInicial] * 10
        self.posicionarNavios()

    def get(self, posicaox, posicaoy):
        if posicaox == 0:
            return self.lista1[posicaoy]
        elif posicaox == 1:
            return self.lista2[posicaoy]
        elif posicaox == 2:
            return self.lista3[posicaoy]
        elif posicaox == 3:
            return self.lista4[posicaoy]
        elif posicaox == 4:
            return self.lista5[posicaoy]
        elif posicaox == 5:
            return self.lista6[posicaoy]
        elif posicaox == 6:
            return self.lista7[posicaoy]
        elif posicaox == 7:
            return self.lista8[posicaoy]
        elif posicaox == 8:
            return self.lista9[posicaoy]
        elif posicaox == 9:
            return self.lista10[posicaoy]

    def set(self, posicaox, posicaoy, valor):
        if posicaox == 0:
            self.lista1[posicaoy] = valor
        elif posicaox == 1:
            self.lista2[posicaoy] = valor
        elif posicaox == 2:
            self.lista3[posicaoy] = valor
        elif posicaox == 3:
            self.lista4[posicaoy] = valor
        elif posicaox == 4:
            self.lista5[posicaoy] = valor
        elif posicaox == 5:
            self.lista6[posicaoy] = valor
        elif posicaox == 6:
            self.lista7[posicaoy] = valor
        elif posicaox == 7:
            self.lista8[posicaoy] = valor
        elif posicaox == 8:
            self.lista9[posicaoy] = valor
        elif posicaox == 9:
            self.lista10[posicaoy] = valor

    def print(self):
        print("  | A B C D E F G H I J")
        print("-----------------------")
        print("0", end=' | ')
        for x in self.lista1:
            print(x, end=' ')
        print('')
        print("1", end=' | ')
        for x in self.lista2:
            print(x, end=' ')
        print('')
        print("2", end=' | ')
        for x in self.lista3:
            print(x, end=' ')
        print('')
        print("3", end=' | ')
        for x in self.lista4:
            print(x, end=' ')
        print('')
        print("4", end=' | ')
        for x in self.lista5:
            print(x, end=' ')
        print('')
        print("5", end=' | ')
        for x in self.lista6:
            print(x, end=' ')
        print('')
        print("6", end=' | ')
        for x in self.lista7:
            print(x, end=' ')
        print('')
        print("7", end=' | ')
        for x in self.lista8:
            print(x, end=' ')
        print('')
        print("8", end=' | ')
        for x in self.lista9:
            print(x, end=' ')
        print('')
        print("9", end=' | ')
        for x in self.lista10:
            print(x, end=' ')
        print('')
        print("-----------------------")
        print("  | A B C D E F G H I J")

    def isTodosNaviosAfundados(self):
        for x in range(0, 10, 1):
            for y in range(0, 10, 1):
                if self.get(x, y) != 'X' and self.get(x, y) != self.valorInicial:
                    return False
        return True

    def insertPortaAviao(self, xInicial, yInicial, HorizontalOrVertical):
        self.set(xInicial, yInicial, 'A')
        if HorizontalOrVertical == 0:
            self.set(xInicial, yInicial + 1, 'A')
            self.set(xInicial, yInicial + 2, 'A')
            self.set(xInicial, yInicial + 3, 'A')
            self.set(xInicial, yInicial + 4, 'A')
        else:
            self.set(xInicial + 1, yInicial, 'A')
            self.set(xInicial + 2, yInicial, 'A')
            self.set(xInicial + 3, yInicial, 'A')
            self.set(xInicial + 4, yInicial, 'A')

    def insertNavioTanque(self, xInicial, yInicial, HorizontalOrVertical):
        self.set(xInicial, yInicial, 'N')
        if HorizontalOrVertical == 0:
            self.set(xInicial, yInicial + 1, 'N')
            self.set(xInicial, yInicial + 2, 'N')
            self.set(xInicial, yInicial + 3, 'N')
        else:
            self.set(xInicial + 1, yInicial, 'N')
            self.set(xInicial + 2, yInicial, 'N')
            self.set(xInicial + 3, yInicial, 'N')

    def insertContratorpedeiro(self, xInicial, yInicial, HorizontalOrVertical):
        self.set(xInicial, yInicial, 'C')
        if HorizontalOrVertical == 0:
            self.set(xInicial, yInicial + 1, 'C')
            self.set(xInicial, yInicial + 2, 'C')
        else:
            self.set(xInicial + 1, yInicial, 'C')
            self.set(xInicial + 2, yInicial, 'C')

    def insertSubmarino(self, xInicial, yInicial, HorizontalOrVertical):
        self.set(xInicial, yInicial, 'S')
        if HorizontalOrVertical == 0:
            self.set(xInicial, yInicial + 1, 'S')
        else:
            self.set(xInicial + 1, yInicial, 'S')

    def verificarPosicoes(self, xInicial, yInicial, HorizontalOrVertical, numPosicoes):
        IsOk = True
        if HorizontalOrVertical == 0:
            for x in range(yInicial, yInicial + numPosicoes, 1):
                if self.get(xInicial, x) != self.valorInicial:
                    IsOk = False
            return IsOk
        else:
            for x in range(xInicial, xInicial + numPosicoes, 1):
                if self.get(x, yInicial) != self.valorInicial:
                    IsOk = False
            return IsOk

    def pegarPosicoes(self, x):
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)
        horizontalOrVertical = random.randint(0, 1)
        if horizontalOrVertical == 0:
            while (coluna + x) > 9:
                coluna = random.randint(0, 10)
        else:
            while (linha + x) > 9:
                linha = random.randint(0, 10)
        return linha, coluna, horizontalOrVertical

    def posicionarNavios(self):
        numeroNavios = 1
        for x in range(4, 0, -1):
            for y in range(1, numeroNavios + 1, 1):
                linha, coluna, horizontalOrVertical = self.pegarPosicoes(x)
                while not self.verificarPosicoes(linha, coluna, horizontalOrVertical, x + 1):
                    linha, coluna, horizontalOrVertical = self.pegarPosicoes(x)
                if x == 4:
                    self.insertPortaAviao(linha, coluna, horizontalOrVertical)
                elif x == 3:
                    self.insertNavioTanque(linha, coluna, horizontalOrVertical)
                elif x == 2:
                    self.insertContratorpedeiro(linha, coluna, horizontalOrVertical)
                elif x == 1:
                    self.insertSubmarino(linha, coluna, horizontalOrVertical)
            numeroNavios = numeroNavios + 1


def getHorario():
    return strftime("%d/%m/%Y %H:%M:%S")


def convertColunaToInt(caractere):
    return int(ord(caractere) - 65)


def convertColunaToChar(numero):
    return chr(numero + 65)


def darTiro(conexao, HIT):
    global linhaAnterior
    global colunaAnterior

    # Se o HIT for True, significa que acertei o tiro anterior. Logo, vou tentar atirar em uma posicao vizinha
    if HIT:
        orientacao = random.randint(0, 1)
        somarOUsubtrair = random.randint(0, 1)
        erro = False

        # Verificacao para ver se ira ocorrer problemas de indice ao somar ou subtrair a coluna ou linha

        # Verificacao do caso em que a orientacao seja horizontal
        if orientacao == 0 and ((somarOUsubtrair == 0 and colunaAnterior == 9) or (somarOUsubtrair == 1 and colunaAnterior == 0)):
            # Caso va ocorrer o problema se for horizontal, tento trocar a orientacao para vertical
            orientacao = 1

        # Verificacao do caso em que a orientacao seja vertical
        if orientacao == 1 and ((somarOUsubtrair == 0 and linhaAnterior == 9) or (somarOUsubtrair == 1 and linhaAnterior == 0)):
            # Caso va ocorrer o problema se for vertical, tento ver se o mesmo ocorre com a orientacao horizontal
            if (somarOUsubtrair == 0 and colunaAnterior == 9) or (somarOUsubtrair == 1 and colunaAnterior == 0):
                # Se o mesmo ocorre com a orientacao horizontal, ou seja, o problema ocorre independente da orientacao
                # Entao eu sorteio as posicoes ao inves de usar as antigas para atirar em quadrados vizinhos
                linha = random.randint(0, 9)
                linhaAnterior = linha
                coluna = random.randint(0, 9)
                colunaAnterior = coluna
                erro = True # Sinalizo que nao devo fazer as operacoes de soma ou subtracao, para fugir do erro
            else:
                orientacao = 0

        # Verificacoes da orientacao. Se horizontal, devo somar ou subtrair da coluna, caso contrario, da linha
        if orientacao == 0 and erro is False: # Horizontal
            linha = linhaAnterior
            if somarOUsubtrair == 0: # Somar
                coluna = colunaAnterior + 1
            else: # Subtrair
                coluna = colunaAnterior - 1
            colunaAnterior = coluna
        else: # Vertical
            coluna = colunaAnterior
            if somarOUsubtrair == 0: # Somar
                linha = linhaAnterior + 1
            else: # Subtrair
                linha = linhaAnterior - 1
            linhaAnterior = linha

        print("Atirando na posicao {}, {}...".format(linha, convertColunaToChar(coluna)))
        conexao.sendall("TIRO {},{}".format(linha, coluna).encode('utf-8'))
    else:
        linha = random.randint(0, 9)
        linhaAnterior = linha
        coluna = random.randint(0, 9)
        colunaAnterior = coluna
        print("Atirando na posicao {}, {}...".format(linha, convertColunaToChar(coluna)))
        conexao.sendall("TIRO {},{}".format(linha, coluna).encode('utf-8'))


def conectado(clienteConectado):
    nomeCliente = clienteConectado.getNomeCliente()
    conexaoCliente = clienteConectado.getConexaoCliente()
    print('{}: Server conectado por {}'.format(getHorario(), nomeCliente))

    # Inicio do jogo!

    conexaoCliente.sendall('StartGame'.encode('utf-8'))
    print("O Jogo Comecou!")

    while True:
        try:
            mensagem = conexaoCliente.recv(1024)
            mensagem = mensagem.decode('utf-8')
            if not mensagem:
                print('{}: Cliente {} finalizou a conexao.'.format(getHorario(), nomeCliente))
                clientesObjeto.remove(clienteConectado)
                for p in clientesObjeto:
                    p.getConexaoCliente().sendall('Cliente {} desconectou-se!'.format(nomeCliente).encode('utf-8'))
                break
            # print('{}: Cliente {} enviou -> {}'.format(getHorario(), nomeCliente, mensagem))
            if "FIMJOGO" in mensagem:
                print("PARABENS!! VOCE GANHOU O JOGO! :)")
                clientesObjeto.remove(clienteConectado)
                break
            if "TIRO" in mensagem:
                params = mensagem.replace('TIRO ', '').split(',')
                linha = int(params[0])
                coluna = int(params[1])
                if matriz.get(linha, coluna) != matriz.valorInicial and matriz.get(linha, coluna) != 'X':
                    valorPosicao = matriz.get(linha, coluna)
                    matriz.set(linha, coluna, 'X')
                    print("Cliente acertou o tiro! Na posicao {}, {}".format(linha, convertColunaToChar(coluna)))
                    matriz.print()
                    if matriz.isTodosNaviosAfundados():
                        print("FIM DE JOGO! Cliente ganhou! :(")
                        global fimJogo
                        fimJogo = True
                        conexaoCliente.sendall("FIMJOGO".encode('utf-8'))
                    else:
                        print("Vez do Cliente, novamente!")
                        conexaoCliente.sendall("HIT {}".format(valorPosicao).encode('utf-8'))
                else:
                    print("Cliente errou o tiro! Na posicao {}, {}".format(linha, convertColunaToChar(coluna)))
                    print("Sua vez, Servidor!")
                    conexaoCliente.sendall("MISS".encode('utf-8'))
                    time.sleep(1.5)
                    darTiro(conexaoCliente, False)
            if "HIT" in mensagem:
                print("Voce acertou o tiro! Sua vez novamente!")
                time.sleep(1)
                darTiro(conexaoCliente, True)
            if "MISS" in mensagem:
                print("Voce errou o tiro :(\nVez do Cliente!")
        except Exception as e:
            print('{}: Deu erro na conexao com o cliente {}.'.format(getHorario(), nomeCliente))
            print('Mensagem do erro : ' + str(e))
            clientesObjeto.remove(clienteConectado)
            for p in clientesObjeto:
                p.getConexaoCliente().sendall('Cliente {} desconectou-se!'.format(nomeCliente).encode('utf-8'))
            break

    print('Finalizando conexao do cliente', nomeCliente)
    conexaoCliente.close()
    _thread.exit()


def receberConexao():
    while True and not fimJogo:
        con, cliente = sockObj.accept()
        msg = con.recv(1024).decode('utf-8')
        # print("MensagemRecebida = " + msg)
        if 'ConectarCliente' in msg:
            global matriz
            matriz = Matriz(0)
            matriz.print()
            clienteNovo = Cliente(msg.split(' ', 1)[1], con, cliente)
            clientesObjeto.append(clienteNovo)
            for x in clientesObjeto:
                x.getConexaoCliente().sendall('Cliente {} conectado!'.format(clienteNovo.getNomeCliente()).encode('utf-8'))
            _thread.start_new_thread(conectado, tuple([clienteNovo]))
        else:
            print("Ocorreu um problema ao tentar conectar o Cliente {} ao Servidor".format(cliente[1]))
            con.sendall('Seu Cliente tentou se conectar, mas ocorreu um problema.'.encode('utf-8'))
            con.close()
            print('Conexao com cliente {} finalizada'.format(cliente[1]))

    sockObj.close()


receberConexao()
