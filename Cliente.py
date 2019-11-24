from socket import *
import _thread
from time import strftime
import random
import time

serverHost = '192.168.2.14'
serverPort = 5000
nickname = 'ClienteBatalhaNaval'

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
    valorInicial = None

    def __init__(self, valorInicial, posicionarNavios):
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
        if posicionarNavios:
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
        print("  | A B C D E F G H I J\n")

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
matriz = Matriz(0, True)
matrizInimiga = Matriz('?', False)
linhaAnterior = None
colunaAnterior = None
mensagem = 'ConectarCliente ' + nickname
sockObj.sendall(mensagem.encode('utf-8'))


def darTiro():
    local = str(input("Digite onde deseja atirar ou sua opcao: ")).upper().replace(" ", "").split(',')
    if local[0] == 'P':
        print("Sua Matriz: ")
        matriz.print()
        time.sleep(1)
        print("Matriz Inimiga: ")
        matrizInimiga.print()
        time.sleep(1)
        darTiro()
    else:
        try:
            global linhaAnterior
            global colunaAnterior
            linha = int(local[0])
            if local[1] is not int:
                coluna = convertColunaToInt(local[1])
            else:
                coluna = int(local[1])
            while (linha > 9 or linha < 0) or (coluna > 9 or coluna < 0):
                print("Entrada invalida! Tente outra vez, por favor.")
                local = str(input("Digite onde deseja atirar: ")).split(',')
                linha = int(local[0])
                if local[1] is not int:
                    coluna = convertColunaToInt(local[1])
                else:
                    coluna = int(local[1])
            linhaAnterior = linha
            colunaAnterior = coluna
            print("Atirando na posicao {}, {}...".format(linha, convertColunaToChar(coluna)))
            time.sleep(1)
            sockObj.sendall("TIRO {},{}".format(linha, coluna).encode('utf-8'))
        except:
            print("Entrada invalida! Tente outra vez, por favor.")
            darTiro()


def convertColunaToInt(caractere):
    return int(ord(caractere) - 65)


def convertColunaToChar(numero):
    return chr(numero + 65)


while True:
    try:
        data = sockObj.recv(1024)
        if data:
            mensagemRecebida = data.decode('utf-8')
            if 'StartGame' in mensagemRecebida:
                print("O Jogo Começou!")
                print("Sua vez de atirar!")
                print("Formato de entrada: 2,D onde 2 = linha e D = coluna\n"
                      "Voce pode tambem digitar P caso queira ver sua matriz\n")
                darTiro()
            if 'HIT' in mensagemRecebida:
                navio = mensagemRecebida.split(" ")[1]
                print("Voce ACERTOU o tiro! :) Atingiu um navio {}. Sua vez novamente!".format(navio))
                matrizInimiga.set(linhaAnterior, colunaAnterior, navio)
                darTiro()
            if 'MISS' in mensagemRecebida:
                print("Voce ERROU o tiro :( Vez do oponente!")
            if 'FIMJOGO' in mensagemRecebida:
                print("PARABENS!! VOCE GANHOU O JOGO! :)")
                sockObj.close()
                break
            if 'TIRO' in mensagemRecebida:
                params = mensagemRecebida.replace('TIRO ', '').split(',')
                linha = int(params[0])
                coluna = int(params[1])
                if matriz.get(linha, coluna) != matriz.valorInicial and matriz.get(linha, coluna) != 'X':
                    matriz.set(linha, coluna, 'X')
                    print("Servidor ACERTOU o tiro! Posicao {}, {}. Vez do servidor, novamente!".format(linha, convertColunaToChar(coluna)))
                    if matriz.isTodosNaviosAfundados():
                        print("FIM DE JOGO! Servidor ganhou! :(")
                        sockObj.sendall("FIMJOGO".encode('utf-8'))
                        break
                    else:
                        sockObj.sendall("HIT".encode('utf-8'))
                else:
                    print("Servidor ERROU o tiro! Posicao {}, {}. Sua vez, Cliente!".format(linha, convertColunaToChar(coluna)))
                    sockObj.sendall("MISS".encode('utf-8'))
                    darTiro()
    except Exception as e:
        print('Ocorreu um erro! Finalizando thread de escutar mensagens')
        print('Erro: {}'.format(str(e)))
        sockObj.close()
        break

sockObj.close()
