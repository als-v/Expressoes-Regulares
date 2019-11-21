from estruturas.pilha import Pilha
import re

def busca_dados(pilha):
    return len(pilha) and pilha[len(pilha) - 1]

# todos os operadores possiveis
operadores = {'+': 0,'.': 1,'*': 2}

# analisa a expressao
def analise_expressao(expressao):
    pilha_expressao1 = Pilha()
    pilha_expressao2 = Pilha()
    expressao = list(re.sub("[a-zA-Z0-9][a-zA-Z0-9]+", lambda x: '.'.join(x.group()), expressao))

    # passa por toda ela, e verifica os ()
    for i in expressao:
        if i == '(':
            pilha_expressao1.inserir_pilha(i)
        if i == ')':
            pilha_expressao2.inserir_pilha(i)
    
    resultado = pilha_expressao1.tamanho - pilha_expressao2.tamanho

    # enquanto nao tiver nada sobrando em nenhuma das pilhas
    while(1):
        if resultado == 0:
            break
        if resultado > 0:
            expressao.append(')')
            resultado -=1
        if resultado < 0:
            expressao.insert(0,'(')
            resultado +=1
    
    return ''.join(expressao)

# conversao
def conversao(expressao):
    expressao = analise_expressao(expressao)
    saida = ''
    operador_pilha = []

    # verifica o operador
    for token in expressao:
        # se for operacao
        if (token == '.' or token == '+' or token == '*'):
            while(len(operador_pilha) and busca_dados(operador_pilha) != '(' and operadores[busca_dados(operador_pilha)] >= operadores[token]):
                saida += operador_pilha.pop()
            operador_pilha.append(token)
        # se terminar
        elif (token == '(' or token == ')'):
            if(token == '('):
                operador_pilha.append(token)
            else:
                while(busca_dados(operador_pilha) != '('):
                    saida += operador_pilha.pop()
                operador_pilha.pop()
        else:
            saida += token
    while(len(operador_pilha)):
        saida += operador_pilha.pop()
    return saida

