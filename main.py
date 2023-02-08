from classes import Calculadora
import datetime

casos_de_teste = ('1 + 41', '46 + -5', '32 - -10', '45 - 3',
                  '7 * 6', '42 / 1', '2 ** 10', '2 ** -5')

DATA = datetime.datetime.now()
data_str = DATA.strftime("%d/%m/%Y - %H:%M:%S")

if __name__ == '__main__':
    # print("Estou no main")
    print("\n---------BEM VINDO À CALCULADORA À PROVA DE FALHAS--------- \n")
    while True:
        try:
            # vai tentar instanciar o objeto com o valor recebido no input:
            obj_usuario = Calculadora(input("Digite Número Operação Número: "))
            obj_usuario.verifica_operacao()
        except IndexError:
            # Quando são digitadas entradas fora do padrâo Número Operador Número
            with open('erros.log', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f'Entrada Inválida!!  data_hora: {data_str} \n')
        except KeyboardInterrupt:
            # Não é permitido encerrar o programa por atalho de teclado
            print("Proibido parar por ctrl+C")
        except ValueError:
            # Quando são encontradas letras na entrada do usuário
            with open('erros.log', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f'Entrada Inválida!!  data_hora: {data_str} \n')
