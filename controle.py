from src.modelo import *

# renomeia os estados
def renomeia_estados(incremento, automato2):
        automato = Automato()

        # adiciona transicao (origem estado destino)
        for i in automato2.lista_transicao:
            automato.addTransicao(automato.letra_estado+str(incremento + int(i.origem[1:])), i.nome, automato.letra_estado+str(incremento + int(i.destino[1:])))
        
        automato.inicio = automato.letra_estado + str(incremento + int(automato2.lista_estado[0][1:]))
        
        return automato

# upload do automato
def organizar(automato):
    j = 0
    n = max(automato.lista_transicao, key=lambda t: max(int(t.origem[1:]), int(t.destino[1:])))
    n = int(max(n.origem, n.destino)[1:])

    # filtra o automato (ficar bonitin)
    for i in range(n+1):
        filtrado = [t for t in automato.lista_transicao if t.origem == automato.letra_estado+str(i) or t.destino == automato.letra_estado+str(i)]
        if filtrado:
            if j == i:
                continue
            for t in filtrado:
                if (t.origem == automato.letra_estado+str(i)):
                    t.origem = automato.letra_estado+str(j)
                if (t.destino == automato.letra_estado+str(i)):
                    t.destino = automato.letra_estado+str(j)
            j += 1
    
    automato.lista_estado = [automato.letra_estado+str(i) for i in range(j)]
    automato.inicio = automato.lista_estado[0]
    automato.lista_fim[0] = automato.lista_estado[-1]

# caso seja o fecho de Kleene
def fecho_kleene(automato1):
    if(type(automato1) is Automato):
        automato = Automato()
        automato1 = renomeia_estados(1, automato1)
        automato.addTransicao(automato.inicio, automato.epsilon(), automato1.inicio)

        for i in automato1.lista_transicao:
            automato.addTransicao(i.origem, i.nome, i.destino)
        
        automato.addTransicao(automato1.lista_fim[0], automato.epsilon(), automato1.inicio)
        automato.addEstado(automato.letra_estado + str(1+(int(automato1.lista_fim[0][1:]))))
        automato.addTransicao(automato1.lista_fim[0], automato.epsilon(), automato.lista_fim[0])
        automato.addTransicao(automato.inicio, automato.epsilon(), automato.lista_fim[0])
        return automato
    print("\nOops, esse nao e um automato\n")
    return False

# caso seja concatenacao
def concatenacao(automato1, automato2):
    if(type(automato1) is Automato) and (type(automato2) is Automato):
        automato = Automato()

        for i in automato1.lista_transicao:
            automato.addTransicao(i.origem, i.nome, i.destino)
        
        automato2 = renomeia_estados(len(automato.lista_estado), automato2)
        automato.addTransicao(automato1.lista_fim[0], automato.epsilon(), automato2.inicio)

        for i in automato2.lista_transicao:
            automato.addTransicao(i.origem, i.nome, i.destino)
        
        return automato
    print("\nOops, esse nao e um automato\n")
    return False

# caso seja uniao
def uniao(automato1, automato2): 
    if(type(automato1) is Automato) and (type(automato2) is Automato):
        automato = Automato()
        automato1 = renomeia_estados(1,automato1)
        automato.addTransicao(automato.inicio, automato.epsilon(), automato1.inicio)

        for i in automato1.lista_transicao:
            automato.addTransicao(i.origem, i.nome, i.destino)

        automato2 = renomeia_estados(len(automato.lista_estado), automato2)
        automato.addTransicao(automato.inicio, automato.epsilon(),automato2.inicio)

        for i in automato2.lista_transicao:
            automato.addTransicao(i.origem, i.nome, i.destino)
        
        automato.addEstado(automato.letra_estado + str(1+int(automato2.lista_fim[0][1:])))
        automato.addTransicao(automato1.lista_fim[0], automato.epsilon(), automato.lista_fim[0])
        automato.addTransicao(automato2.lista_fim[0], automato.epsilon(), automato.lista_fim[0])            
        return automato
    print("\nOops, esse nao e um automato\n")
    return False