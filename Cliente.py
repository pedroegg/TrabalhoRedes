from socket import *
import _thread
from time import strftime
import random

serverHost = '10.254.187.12'
serverPort = 5000
nickname = 'Pedro Egg'

sockObj = socket(AF_INET, SOCK_STREAM)


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

    def __init__(self, valorInicial):
        self.lista1 = [valorInicial] * 10
        self.lista2 = [valorInicial] * 10
        self.lista3 = [valorInicial] * 10
        self.lista4 = [valorInicial] * 10
        self.lista5 = [valorInicial] * 10
        self.lista6 = [valorInicial] * 10
        self.lista7 = [valorInicial] * 10
        self.lista8 = [valorInicial] * 10
        self.lista9 = [valorInicial] * 10
        self.lista10 = [valorInicial] * 10
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
        for x in self.lista1:
            print(x, end=' ')
        print('')
        for x in self.lista2:
            print(x, end=' ')
        print('')
        for x in self.lista3:
            print(x, end=' ')
        print('')
        for x in self.lista4:
            print(x, end=' ')
        print('')
        for x in self.lista5:
            print(x, end=' ')
        print('')
        for x in self.lista6:

            print(x, end=' ')
        print('')
        for x in self.lista7:
            print(x, end=' ')
        print('')
        for x in self.lista8:
            print(x, end=' ')
        print('')
        for x in self.lista9:
            print(x, end=' ')
        print('')
        for x in self.lista10:
            print(x, end=' ')
        print('')

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

    def posicionarNavios(self):
        arquivo = open("posicoes.txt", "r")
        for x in arquivo:
            texto = x.replace("\n", "")
            partesTexto = texto.split(" ")
            linha = int(partesTexto[0])
            coluna = int(partesTexto[1])
            isHorizontalOrVertical = int(partesTexto[2])
            navio = partesTexto[3]
            if navio == 'A':
                self.insertPortaAviao(linha, coluna, isHorizontalOrVertical)
            elif navio == 'N':
                self.insertNavioTanque(linha, coluna, isHorizontalOrVertical)
            elif navio == 'C':
                self.insertContratorpedeiro(linha, coluna, isHorizontalOrVertical)
            elif navio == 'S':
                self.insertSubmarino(linha, coluna, isHorizontalOrVertical)
        arquivo.close()


sockObj.connect((serverHost, serverPort))
matriz = Matriz(0)
matriz.print()
mensagem = 'ConectarCliente ' + nickname
sockObj.sendall(mensagem.encode('utf-8'))
print("Enviado -> " + mensagem)


def darTiro():
    print("Formato de entrada: 2,3 onde 2 = linha e 3 = coluna")
    local = str(input("Digite onde deseja atirar: ")).split(',')
    linha = int(local[0])
    coluna = int(local[1])
    while (linha > 9 or linha < 0) or (coluna > 9 or coluna < 0):
        print("Entrada inválida! Tente outra vez, por favor.")
        local = str(input("Digite onde deseja atirar: ")).split(',')
        linha = int(local[0])
        coluna = int(local[1])
    print("Atirando na posição {}, {}...".format(linha, coluna))
    sockObj.sendall("TIRO {},{}".format(linha, coluna).encode('utf-8'))


while True:
    try:
        data = sockObj.recv(1024)
        if data:
            mensagemRecebida = data.decode('utf-8')
            if 'StartGame' in mensagemRecebida:
                print("O Jogo Começou!")
                print("Sua vez de atirar!")
                darTiro()
            if 'HIT' in mensagemRecebida:
                print("Você acertou o tiro! Sua vez novamente!")
                darTiro()
            if 'MISS' in mensagemRecebida:
                print("Você errou o tiro :(\nVez do oponente!")
            if 'TIRO' in mensagemRecebida:
                params = mensagemRecebida.replace('TIRO ', '').split(',')
                linha = int(params[0])
                coluna = int(params[1])
                if str(matriz.get(linha, coluna)) != '0' and str(matriz.get(linha, coluna)) != 'X':
                    matriz.set(linha, coluna, 'X')
                    print("Servidor acertou o tiro! Posição {}, {}".format(linha, coluna))
                    print("Vez do servidor, novamente!")
                    sockObj.sendall("HIT".encode('utf-8'))
                else:
                    print("Servidor errou o tiro! Posicao {}, {}".format(linha, coluna))
                    print("Sua vez, Cliente!")
                    sockObj.sendall("MISS".encode('utf-8'))
                    darTiro()
    except:
        print('Finalizando thread de escutar mensagens')
        sockObj.close()
        break
