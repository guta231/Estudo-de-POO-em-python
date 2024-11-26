

class Conta_bancaria:

    def __init__(self, titular, saldo, senha, logado):

        self.titular = titular
        self.saldo = saldo
        self.senha = senha
        self.logado = logado
        
    
    def __str__(self):
        return f"Conta bancaria - Titular: {self.titular} / saldo: {self.saldo}"
    
    
    
class Operacoes_bancarias:

    def __init__(self):

        self.lista_de_contas = []

    
    def login(self, nome, senha):
        for conta in self.lista_de_contas:
            if conta.titular == nome:
                if conta.senha == senha:
                    print(f"{conta} \n logada com sucesso")
                    conta.logado = True
                    return
                else:
                    print("senha incorreta")
                    return
            print("Nome de usuario incorreto")
            

    def criar_conta(self, nome, senha):
        conta = Conta_bancaria(nome, 0, senha, False)
        self.lista_de_contas.append(conta)

    def depositar(self):
        
        for conta in self.lista_de_contas:
            if conta.logado == True:
                valor = float(input("qual o valor que deseja depositar? "))
                conta.saldo = conta.saldo + valor
     
    
    def sacar(self):
       
        for conta in self.lista_de_contas:
            if conta.logado == True:
                valor = float(input("Quanto voce deseja sacar? "))
                conta.saldo = conta.saldo - valor
               
    def extrato(self):

        for conta in self.lista_de_contas:
            if conta.logado == True:
                print(f"Seu saldo atual: {conta.saldo}")
    def transferencia(self, nome):
        for conta in self.lista_de_contas:
            if conta.titular == nome:
                conta_destinatario = conta
                
                for conta in self.lista_de_contas:
                    if conta.logado == True:
                        valor = float(input("Valor da transferencia: "))
                        if valor <= conta.saldo:
                            conta_destinatario.saldo = conta_destinatario.saldo + valor
                            conta.saldo = conta.saldo - valor
                            return
                        else:
                            print("Saldo insuficiente")
                            return
        print("Essa conta não existe")
banco = Operacoes_bancarias()

while True:

    user_choice = int(input("Bem vindo ao banco, como deseja prosseguir? \n 1-Entrar em uma conta \n 2-Criar conta \n 3-Sair \n "))

    match user_choice:
        
        case 1:
            nome = str(input("Nome do usuario: "))
            senha = str(input("Digite a senha: "))
            banco.login(nome, senha)
        case 2:
            nome = str(input("Nome da conta que deseja criar: "))
            senha = str(input("Crie uma senha: "))
            banco.criar_conta(nome, senha)
        case 3:
            break

    for conta in banco.lista_de_contas:
        while conta.logado == True:
            print(conta)
            user_choice = int(input(f"{conta} \n Como deseja prosseguir? \n 1-Ver extrato \n 2-Fazer deposito \n 3-Sacar dinheiro \n 4-Realizar transferencia \n 5-Sair da conta \n"))
            match user_choice:

                case 1:
                    banco.extrato()
                case 2:
                    banco.depositar()
                case 3:
                    banco.sacar()
                case 4:
                    nome = str(input("Nome do titular da conta para qual deseja transferir: "))
                    banco.transferencia(nome)
                case 5:
                    conta.logado = False
                    