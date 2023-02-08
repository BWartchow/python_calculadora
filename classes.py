import datetime

DATA = datetime.datetime.now()
data_str = DATA.strftime("%d/%m/%Y - %H:%M:%S")

# {f"operacao": "{num1} {operacao} {num2}", "resultado": 11, "data_hora": "{data_str}"}
# {"operacao": "{num1} {operacao} {num2}", "erro": "{erro}", "data_hora": "{data_str}"}

###############################################################################


class Calculadora:
    """ Classe Responsável pelas funções da calculadora """

    def __init__(self, entrada: str) -> None:
        """ Método construtor da classe """
        # único parâmetro obrigatório de construção a operação digitada pelo usuário
        # Manipula string digitada pelo usuário, separando por indices
        self.operacao = entrada.split()
        print(f"Operação recebida = {self.operacao}")
        self.num1 = self.operacao[0]
        print(f"Valor 01 = {self.num1}")

        self.operador = self.operacao[1]
        print(f"Operação solicitada = {self.operador}")

        self.num2 = self.operacao[-1]
        print(f"Valor 02 = {self.num2}")

        # Atributos da classe arquivo:
        self.acerto = Arquivo
        self.falha = Arquivo

    def verifica_operacao(self):
        """ Método que identifica qual é a operação requisitada pelo usuário"""
        try:
            if self.operacao[1] == "+":
                print("Operação de adição")
                resultado = Calculadora.somar(self.operacao)
                print(resultado)
                self.acerto.grava_acerto(str(resultado))

            elif self.operacao[1] == "-":
                print("Operação de subtração")
                resultado = Calculadora.subtrair(self.operacao)
                print(resultado)
                self.acerto.grava_acerto(str(resultado))

            elif self.operacao[1] == "*":
                print("Operação de multiplicação")
                resultado = Calculadora.multiplicacar(self.operacao)
                print(resultado)
                self.acerto.grava_acerto(str(resultado))

            elif self.operacao[1] == "**":
                print("Operação de potenciação")
                resultado = Calculadora.elevar(self.operacao)
                print(resultado)
                self.acerto.grava_acerto(str(resultado))

            elif self.operacao[1] == "/":
                print("Operação de divisão")
                resultado = Calculadora.dividir(self.operacao)
                print(resultado)
                self.acerto.grava_acerto(str(resultado))
            else:
                print("Entrada inválida")
        except IndexError:
            with open('erros.log', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f'Entrada Inválida!! data_hora: {data_str} \n')

    def somar(self):
        """ Método de adição """
        soma = int(self[0]) + int(self[-1])
        return soma

    def subtrair(self):
        """ Método de subtração """
        subtracao = int(self[0]) - int(self[-1])
        return subtracao

    def multiplicacar(self):
        """ Método de multiplicação """
        multiplicacao = int(self[0]) * int(self[-1])
        return multiplicacao

    def dividir(self):
        """ Método de divisão"""
        try:
            divisao = int(self[0]) / int(self[-1])
            return divisao
        except ZeroDivisionError:
            erro = "Não consigo dividir por zero... :("
            with open('erros.log', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f'{erro} \n')
            return print(erro)

    def elevar(self):
        """ Método de exponenciação """
        potenciacao = int(self[0]) ** int(self[-1])
        return potenciacao


###############################################################################

class Arquivo:
    """ Classe responsável por gerenciar o salvamento das operações """

    def __init__(self) -> None:
        self.acertou = "acertos.txt"
        self.errou = "erros.log"

    def grava_acerto(self):
        """ Método que grava as operações válidas em arquivo txt"""
        with open('acertos.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'Resultado: {self} data_hora: {data_str} \n')

    def grava_erro(self):
        """ Método que grava as operações inválidas em log de erros"""
        with open('erros.log', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'Resultado: {self} data_hora: {data_str} \n')
