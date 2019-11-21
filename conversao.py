from infixa_posfixa import *
from estruturas.pilha import *
from estruturas.modelo import Automato
from src.controle import *

# faz a conversao do alfabeto
def conversao1(alfabeto_entrada):
    pilha_alfabeto = Pilha()    
    alfabeto_pos_fixo = conversao(alfabeto_entrada)    

    # percorre ele todo
    for i in range(len(alfabeto_pos_fixo)):
        # se n for um operador
        if(alfabeto_pos_fixo[i] != '.' and alfabeto_pos_fixo[i] != '+' and alfabeto_pos_fixo[i] != '*'):
            automato = Automato(alfabeto_pos_fixo[i])
            pilha_alfabeto.inserir_pilha(automato)
        # se for operador
        else:
            if(alfabeto_pos_fixo[i] == '.'):
                dado2 = pilha_alfabeto.get_pilha()
                dado1 = pilha_alfabeto.get_pilha()
                pilha_alfabeto.inserir_pilha(concatenacao(dado1, dado2))
            if(alfabeto_pos_fixo[i] == '+'):
                dado2 = pilha_alfabeto.get_pilha()
                dado1 = pilha_alfabeto.get_pilha()
                pilha_alfabeto.inserir_pilha(uniao(dado1,dado2))
            if(alfabeto_pos_fixo[i] == '*'):
                dado = pilha_alfabeto.get_pilha()
                pilha_alfabeto.inserir_pilha(fecho_kleene(dado))

    return pilha_alfabeto.get_pilha()