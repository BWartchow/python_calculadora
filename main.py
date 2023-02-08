from classes import Calculadora
import datetime
import sys

DATA = datetime.datetime.now()
data_str = DATA.strftime("%d/%m/%Y - %H:%M:%S")

if __name__ == '__main__':
    # print("Estou no main")
    print("\n---------BEM VINDO À CALCULADORA À PROVA DE FALHAS--------- \n")
    while True:
        entrada_operacao = "Vazio"
        try:
            entrada_operacao = input("Digite Número Operação Número (ex.: 2 + 2): ")

        except KeyboardInterrupt:
            # Não é permitido encerrar o programa por atalho de teclado
            msg = "Tentativa de interrupção do programa"
            txt = {"operacao":entrada_operacao, "resultado":msg, "data_hora":data_str}
            with open('erros.log', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f"{txt} \n")
            print(msg)
            print('digite "sair" para sair do programa!')
        else:
            # vai instanciar o objeto com o valor recebido no input:
            if entrada_operacao == 'sair':
                print('\n Programa encerrado!!')
                sys.exit()
            obj_usuario = Calculadora(entrada_operacao)
            obj_usuario.verifica_operacao()
