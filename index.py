salario = [5000, 6000, 4000, 5500, 3500, 1250, 7000]
salario = sorted(salario)


def busca_binaria(alvo):

    inicio = 0
    fim = len(salario) - 1
    meio = int((inicio + fim) / 2)

    while alvo != salario[meio]:
        meio = int((inicio + fim) / 2)
        if alvo == salario[meio]:
            
            return meio

        elif alvo < salario[meio]:
            fim = meio - 1

        elif alvo > salario[meio]:
            inicio = meio + 1


print(busca_binaria(4000))