from conversao import *
from infixa_posfixa import *
import time
import subprocess

def main():
    expressao_regular = ''
    automato = ''
    opcao = -1
    arquivo = 'AFND.txt'
    flag = False

    while(opcao != '0'):
        if (flag == False):
            expressao_regular = input('\nDigite a expressao regular: ')    
            expressao_regular = analise_expressao(expressao_regular)
            automato = conversao(expressao_regular)
            automato.makeFile(arquivo,'NDFA')
            flag = True
    
        print("\nOPCOES:")
        print("Mostrar a expressao regular (1)")
        print("Mostrar o automato finito nao deterministico resultante (2)")
        print("Digitar outra expressao regular (3)")
        print("Sair (0)")

        opcao = input("\n  >> ")

        if (opcao == '1'):
            print("\n ESPRESSÃO: ",expressao_regular)

        if (opcao == '2'):
            print("\nAutomato:\n")
            automato.imprimir()
            resposta = input('\nDeseja testar o automato? (s/n): ')
            if (resposta == "s"):
                testar_automato(arquivo, expressao_regular, automato)
        
        if (opcao == '3'):
            flag = False

# funcao para testar o automato criado
def testar_automato(arquivo_automato, exp_reg, automato):
    arquivo_resposta_aceitacao = 'resposta.txt'
    criar_arq = open(arquivo_resposta_aceitacao,'w')
    criar_arq.close()
    testar_novamente = 's'

    while(testar_novamente == 's'):
        print("\nEspressao: ",exp_reg)

        palavra_teste = verificar_teste(automato)
        processo = subprocess.Popen(['python3', 'fla/main.py', arquivo_automato, palavra_teste, ' >',arquivo_resposta_aceitacao])

        if processo.wait() != 0:
            print("Erro!")
    
        arquivo = open(arquivo_resposta_aceitacao,'r')
        resposta = arquivo.readlines()
        print()

        for i in resposta:
            print(i)

        arquivo.close()

        testar_novamente = input("Deseja testar novamente? (s/n): ")

# verifica o teste para o input do usuario
def verificar_teste(automato):
    palavra_teste = ''
    continuar = True

    while(continuar):
        palavra_teste = input("Insira a palavra: ") 

        for i in range(len(palavra_teste)):
            if palavra_teste[i] in automato.alfabeto:
                continuar = False
            else:
                continuar = True
                print("\nPalavra não aceita!")
                break

    return palavra_teste

if __name__ == '__main__':
	main()