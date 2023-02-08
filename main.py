from classes import Calculadora
import datetime

casos_de_teste_ok = ('1 + 41', '46 + -5', '32 - -10', '45 - 3',
                  '7 * 6', '42 / 1', '2 ** 10', '2 ** -5')

casos_de_teste_falha = ('1+8', '2 -9', 'a + 8', 'meu nome aqui', '19** 2', 'asdf - 5', '5--10')

DATA = datetime.datetime.now()
data_str = DATA.strftime("%d/%m/%Y - %H:%M:%S")

if __name__ == '__main__':
    # print("Estou no main")
    print("\n---------BEM VINDO À CALCULADORA À PROVA DE FALHAS--------- \n")
    while True:
        try:
            # vai tentar instanciar o objeto com o valor recebido no input:
            entrada_operacao = input("Digite Número Operação Número: ")

            obj_usuario = Calculadora(entrada_operacao)
            obj_usuario.verifica_operacao()

        except KeyboardInterrupt:
            # Não é permitido encerrar o programa por atalho de teclado
            msg = "Proibido parar por ctrl+C"
            txt = {"operacao":entrada_operacao, "resultado":msg, "data_hora":data_str}
            with open('erros.log', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f"{txt} \n")
            print(msg)

        except IndexError:
            # Quando são digitadas entradas fora do padrâo Número Operador Número
            msg = "Entrada Inválida!"
            txt = {"operacao":entrada_operacao, "resultado":msg, "data_hora":data_str}
            with open('erros.log', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f"{txt} \n")
            print(msg)

        except ValueError:
            # Quando são encontradas letras na entrada do usuário
            msg = "Eu só entendo números :("
            txt = {"operacao":entrada_operacao, "resultado":msg, "data_hora":data_str}
            with open('erros.log', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f"{txt} \n")
            print(msg)
