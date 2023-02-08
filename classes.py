""" Módulo com as Classes Calculadora e Arquivo"""

import datetime

DATA = datetime.datetime.now()
data_str = DATA.strftime("%d/%m/%Y - %H:%M:%S")

###############################################################################


class Calculadora:
    """ Classe Responsável pelas funções da calculadora """

    def __init__(self, entrada: str) -> None:
        """ Método construtor da classe """
        self.entrada = entrada.strip()
        # Atributos para uso no salvamento de arquivos:
        self.resultado = ""
        self.txt = dict
        self.arq = Arquivo()

    def valida_entrada(self):
        # Manipula string digitada pelo usuário, separando por indices:
        verificador: str = self.entrada.split()
        print(f"Operação recebida = {verificador}")
        # testa tamanho, qualquer coisa diferente de 3 é errado
        if len(verificador) < 3:
            msg: str = 'Você digitou poucos termos'
            print(msg)
            # Grava erro da operação:
            self.txt = {"operacao":self.entrada, "resultado":msg, "data_hora":data_str}
            self.arq.grava_erro(self.txt)
            return False
        if len(verificador) > 3:
            msg: str = 'Você digitou termos demais'
            print(msg)
            # Grava erro da operação:
            self.txt = {"operacao":self.entrada, "resultado":msg, "data_hora":data_str}
            self.arq.grava_erro(self.txt)
            return False
        # valida os 3 termos:
        try:
            # não pode receber float, por isso invalida números com ponto
            # Verificação primeiro número:
            if '.' in verificador[0]:
                raise ValueError
            num1 = int(verificador[0])
            print(f"Valor 01 = {num1}")
        except ValueError:
            msg: str = 'O primeiro termo não é um número válido'
            print(msg)
            self.txt = {"operacao":self.entrada, "resultado":msg, "data_hora":data_str}
            self.arq.grava_erro(self.txt)
            return False
        try:
            # Verificação segundo número:
            if '.' in verificador[2]:
                raise ValueError
            num2 = int(verificador[2])
            print(f"Valor 02 = {num2}")
        except ValueError:
            msg: str = 'O terceiro termo não é um número válido'
            print(msg)
            self.txt = {"operacao":self.entrada, "resultado":msg, "data_hora":data_str}
            self.arq.grava_erro(self.txt)
            return False
        # valida operador
        operador = verificador[1]
        print(f"Operação solicitada = {operador}")
        if not operador in ['+', '-', '*', '/', '**']:
            msg: str = 'operador inválido'
            print(msg)
            self.txt = {"operacao":self.entrada, "resultado":msg, "data_hora":data_str}
            self.arq.grava_erro(self.txt)
            return False
        # se todos os testes deram ok, retorna para realizar a conta na
        # verifica_operacao
        return True

    def verifica_operacao(self):
        """ Método que identifica qual é a operação requisitada pelo usuário"""
        # A validação da entrada é realizada e só executa se for válido (True)
        if self.valida_entrada():
            entrada = self.entrada.split()
            # Verifica se há operador de adição:
            if entrada[1] == "+":
                print("Operação de adição")
                # Faz a operação requisitada (soma segundo número ao primeiro):
                self.resultado = Calculadora.somar(Calculadora, entrada)
                print(self.resultado)
            # Verifica se há operador de subtração:
            elif entrada[1] == "-":
                print("Operação de subtração")
                # Faz a operação requisitada (subtrai segundo número do primeiro):
                self.resultado = Calculadora.subtrair(Calculadora, entrada)
                print(self.resultado)
            # Verifica se há operador de multiplicação:
            elif entrada[1] == "*":
                print("Operação de multiplicação")
                # Faz a operação requisitada (multiplica os dois números):
                self.resultado = Calculadora.multiplicacar(Calculadora, entrada)
                print(self.resultado)
            # Verifica se há operador de potenciação:
            elif entrada[1] == "**":
                print("Operação de potenciação")
                # Faz a operação requisitada (primeiro número elevado ao segundo):
                self.resultado = Calculadora.elevar(Calculadora, entrada)
                print(self.resultado)
            # Verifica se há operador de divisão:
            elif entrada[1] == "/":
                print("Operação de divisão")
                # Faz a operação requisitada (divide o primeiro número pelo segundo):
                self.resultado = Calculadora.dividir(Calculadora, entrada)
                print(self.resultado)

    def somar(self, conta):
        """ Método de adição """
        self.conta = conta
        soma = int(self.conta[0]) + int(self.conta[-1])
        # Grava resultado da operação:
        self.txt = {"operacao":conta, "resultado":soma, "data_hora":data_str}
        self.arq.grava_acerto(Arquivo, self.txt)
        return soma

    def subtrair(self, conta):
        """ Método de subtração """
        self.conta = conta
        subtracao = int(self.conta[0]) - int(self.conta[-1])
        # Grava resultado da operação:
        self.txt = {"operacao":conta, "resultado":subtracao, "data_hora":data_str}
        self.arq.grava_acerto(Arquivo, self.txt)
        return subtracao

    def multiplicacar(self, conta):
        """ Método de multiplicação """
        self.conta = conta
        multiplicacao = int(self.conta[0]) * int(self.conta[-1])
        # Grava resultado da operação:
        self.txt = {"operacao":conta, "resultado":multiplicacao, "data_hora":data_str}
        self.arq.grava_acerto(Arquivo, self.txt)
        return multiplicacao

    def dividir(self, conta):
        """ Método de divisão"""
        self.conta = conta
        try:
            if int(self.conta[-1] == 0):
                raise ZeroDivisionError
        except ZeroDivisionError:
            erro = "Não consigo dividir por zero... :("
            txt = {"operacao":conta, "resultado":erro, "data_hora":data_str}
            Arquivo.grava_erro(Arquivo, txt)
        else:
            divisao = int(self.conta[0]) / int(self.conta[-1])
            if divisao == None: # Por exemplo 0 / 0
                msg= "0"
                # Grava resultado da operação:
                self.txt = {"operacao":conta, "resultado":msg, "data_hora":data_str}
                self.arq.grava_acerto(Arquivo, self.txt)
                return divisao
            else:
                # Grava resultado da operação:
                self.txt = {"operacao":conta, "resultado":divisao, "data_hora":data_str}
                self.arq.grava_acerto(Arquivo, self.txt)
                return divisao

    def elevar(self, conta):
        """ Método de exponenciação """
        self.conta = conta
        potenciacao = int(self.conta[0]) ** int(self.conta[-1])
        # Grava resultado da operação:
        self.txt = {"operacao":conta, "resultado":potenciacao, "data_hora":data_str}
        self.arq.grava_acerto(Arquivo, self.txt)
        return potenciacao


###############################################################################


class Arquivo(Calculadora):
    """ Classe responsável por gerenciar o salvamento das operações """

    def __init__(self) -> None:
        self.acertou = "acertos.txt"
        self.errou = "erros.log"

    def grava_acerto(self, txt):
        """ Método que grava as operações válidas em arquivo txt"""
        with open('acertos.txt', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f"{txt} \n")

    def grava_erro(self, txt):
        """ Método que grava as operações inválidas em log de erros"""
        with open('erros.log', 'a', encoding='utf-8') as arquivo:
            arquivo.write(f"{txt} \n")

###############################################################################

if __name__ == '__main__':
    # casos de teste
    casos_de_teste_ok = ('1 + 41', '46 + -5', '32 - -10', '45 - 3',
                        '7 * 6', '42 / 1', '2 ** 10', '2 ** -5')

    casos_de_teste_falha = ('1+8', '2 -9', 'a + 8', 'meu nome aqui',
                            '19** 2', 'asdf - 5', '5--10')

#for caso in casos_de_teste_ok:
for caso in casos_de_teste_falha:
        if caso == 'sair':
            print('\n Programa encerrado!!')
            sys.exit()
        else:
            obj_usuario = Calculadora(caso)
            obj_usuario.verifica_operacao()
