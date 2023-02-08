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

        self.resultado = ""
        # Atributos da classe arquivo:
        self.acerto = Arquivo
        self.falha = Arquivo
        self.txt = dict

    def verifica_operacao(self):
        """ Método que identifica qual é a operação requisitada pelo usuário"""
        entrada = self.operacao
        if entrada[1] == "+":
            print("Operação de adição")
            self.resultado = Calculadora.somar(Calculadora, entrada)
            print(self.resultado)
            self.txt = {"operacao":entrada, "resultado":self.resultado, "data_hora":data_str}
            self.acerto.grava_acerto(Arquivo, self.txt)

        elif entrada[1] == "-":
            print("Operação de subtração")
            self.resultado = Calculadora.subtrair(Calculadora, entrada)
            print(self.resultado)
            self.txt = {"operacao":entrada, "resultado":self.resultado, "data_hora":data_str}
            self.acerto.grava_acerto(Arquivo, self.txt)

        elif entrada[1] == "*":
            print("Operação de multiplicação")
            self.resultado = Calculadora.multiplicacar(Calculadora, entrada)
            print(self.resultado)
            self.txt = {"operacao":entrada, "resultado":self.resultado, "data_hora":data_str}
            self.acerto.grava_acerto(Arquivo, self.txt)

        elif entrada[1] == "**":
            print("Operação de potenciação")
            self.resultado = Calculadora.elevar(Calculadora, self.operacao)
            print(self.resultado)
            self.txt = {"operacao":entrada, "resultado":self.resultado, "data_hora":data_str}
            self.acerto.grava_acerto(Arquivo, self.txt)

        elif entrada[1] == "/":
            print("Operação de divisão")
            self.resultado = Calculadora.dividir(Calculadora, entrada)
            if self.resultado == None:
                print("Resultado inválido")
            else:
                print(self.resultado)
                self.txt = {"operacao":entrada, "resultado":self.resultado, "data_hora":data_str}
                self.acerto.grava_acerto(Arquivo, self.txt)

        else:
            print("Não entendi a operação... :(")


    def somar(self, conta):
        """ Método de adição """
        self.conta = conta
        soma = int(self.conta[0]) + int(self.conta[-1])
        return soma

    def subtrair(self, conta):
        """ Método de subtração """
        self.conta = conta
        subtracao = int(self.conta[0]) - int(self.conta[-1])
        return subtracao

    def multiplicacar(self, conta):
        """ Método de multiplicação """
        self.conta = conta
        multiplicacao = int(self.conta[0]) * int(self.conta[-1])
        return multiplicacao

    def dividir(self, conta):
        """ Método de divisão"""
        self.conta = conta
        try:
            divisao = int(self.conta[0]) / int(self.conta[-1])
            return divisao
        except ZeroDivisionError:
            erro = "Não consigo dividir por zero... :("
            txt = {"operacao":conta, "resultado":erro, "data_hora":data_str}
            Arquivo.grava_erro(Arquivo, txt)

    def elevar(self, conta):
        """ Método de exponenciação """
        self.conta = conta
        potenciacao = int(self.conta[0]) ** int(self.conta[-1])
        return potenciacao


###############################################################################

class Arquivo(Calculadora):
    """ Classe responsável por gerenciar o salvamento das operações """

    def __init__(self) -> None:
        self.acertou = "acertos.txt"
        self.errou = "erros.log"

    def grava_acerto(self, txt):
        """ Método que grava as operações válidas em arquivo txt"""
        #txt = {"operacao":self.operacao, "resultado":self.resultado, "data_hora":data_str}
        with open('acertos.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f"{txt} \n")

    def grava_erro(self, txt):
        """ Método que grava as operações inválidas em log de erros"""
        with open('erros.log', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f"{txt} \n")
