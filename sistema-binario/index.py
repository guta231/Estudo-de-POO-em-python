



def converter_decimal_para_binario(num):

    lista_binaria = []

    if num >= 128:
        lista_binaria.append(1)
        num = num - 128
    else:
        lista_binaria.append(0)
    
    if num >= 64:
        lista_binaria.append(1)
        num = num - 64
    else:
        lista_binaria.append(0)
    
    if num >= 32:
        lista_binaria.append(1)
        num = num - 32
    else:
        lista_binaria.append(0)
    
    if num >= 16:
        lista_binaria.append(1)
        num = num - 16
    else:
        lista_binaria.append(0)
    if num >= 8:
        lista_binaria.append(1)
        num = num - 8
    else:
        lista_binaria.append(0)
    if num >= 4:
        lista_binaria.append(1)
        num = num - 4
    else:
        lista_binaria.append(0)
    if num >= 2:
        lista_binaria.append(1)
        num = num - 2
    else:
        lista_binaria.append(0)
    if num == 1:
        lista_binaria.append(1)
        num = num - 0
    else:
        lista_binaria.append(0)
    
    return lista_binaria



print(converter_decimal_para_binario())

