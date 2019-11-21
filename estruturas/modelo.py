from transicao import Transicao
from itertools import chain

# classe automato
object Automato:
    # construtor
    def __init__(self, nome=None):
        self.letra_estado = 'q'
        self.inicio = self.letra_estado+(str(0))

        if(nome != None):
            self.lista_fim = [self.letra_estado+(str(1))]
            self.lista_estado = [self.inicio, self.lista_fim[0]]
            transicao = Transicao(self.inicio, nome, self.lista_fim[0])
            self.lista_transicao = [transicao]
            self.alfabeto = [transicao.nome]
        else:
            self.lista_estado = []
            self.lista_transicao = list()
            self.alfabeto = list()
            self.lista_fim = list()

    @staticmethod
    def epsilon():
        return 'E'

    # cria arquivo
    def makeFile(self, nome_arquivo, titulo):
        arquivo = open(nome_arquivo,'w')
        arquivo.write(titulo+'\n')
        arquivo.write(' '.join(self.alfabeto) + '\n')
        arquivo.write(self.epsilon()+'\n')
        arquivo.write(' '.join(self.lista_estado) + '\n')
        arquivo.write(self.inicio + '\n')
        arquivo.write(' '.join(self.lista_fim) + '\n')

        for i in self.lista_transicao:
            arquivo.write(i.origem +' ')
            arquivo.write(i.nome +' ')
            arquivo.write(i.destino +'\n')
        
        arquivo.close()

    # adiciona estado
    def addEstado(self, nome_estado):
        if(nome_estado in self.lista_estado):
            return False
        
        self.lista_estado.append(nome_estado)
        self.lista_fim = [nome_estado]
    
        return True

# adiciona transicao
    def addTransicao(self, origem, nome, destino):
        if isinstance(origem, int):
            origem = self.letra_estado+str(origem)
        if isinstance(destino, int):
            destino = self.letra_estado+str(destino)
        if(self.origem_destino(origem, nome, destino) == False):
            if(self.getEstado(origem) == False):
                self.addEstado(origem)
            if(self.getEstado(destino) == False):
                self.addEstado(destino)
            transicao = Transicao(origem, nome, destino)
            self.lista_transicao.append(transicao)
            if(transicao.nome != self.epsilon()):
                if(transicao.nome not in self.alfabeto):
                    self.alfabeto.append(transicao.nome)                
            return True
        return False

    # pega estado
    def getEstado(self, nome_estado):
        for estado in self.lista_estado:
            if estado == nome_estado:
                return estado
    
        return False

    # pega transicao
    def getTransicao(self):
        transicoes = {}

        for i in range(len(self.lista_transicao)):
            origem = self.lista_transicao[i].origem
            destino = self.lista_transicao[i].destino
            nome = self.lista_transicao[i].nome

            if not transicoes.get(origem):
                transicoes[origem] = {}
            if not transicoes[origem].get(nome):
                transicoes[origem][destino] = {nome}
            else:
                transicoes[origem][destino].update([nome])
        return transicoes

    # origem e destino da transicao
    def origem_destino(self, origem, nome, destino):
        for transicao in self.lista_transicao:
            if ((transicao.origem == origem) and (transicao.destino == destino) and (transicao.nome == nome)):
                return True
        
        return False
    
    # pega a transicao destino
    def getTransicao_destino(self, estado, palavra):
        transicoes = self.getTransicao()

        # LISTA
        if isinstance(estado, int):
            estado = [estado]

        todos_estados = set()

        for estado in estado:
            if estado in transicoes:
                for transicao in transicoes[estado]:
                    if palavra in transicoes[estado][transicao]:
                        todos_estados.add(transicao)
        return set(todos_estados)

    #imprime automato
    def imprimir(self):
        print(self.alfabeto)
        print(self.epsilon())
        print(self.inicio)
        for i in self.lista_fim:
            print(f'{i} ',end='')
        print() 
        for estados in self.lista_estado:
            print(estados, end =" ")
        print("")
        for i in self.lista_transicao:
            print(f'[{i.origem} {i.nome} {i.destino}]')
        print("\n")