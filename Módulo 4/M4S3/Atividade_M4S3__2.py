'''
1 -> __________________________________________________________________ <- 1

def test_Desc_095():
    desconto = 1 - 0.95
    desconto = f'{desconto:.2f}'

    assert desconto == str(0.05)

def test_Desc_090():
    desconto = 1 - 0.90
    desconto = f'{desconto:.1f}'

    assert desconto == str(0.1)

def test_Desc_085():
    desconto = 1 - 0.85
    desconto = f'{desconto:.2f}'

    assert desconto == str(0.15)

def test_valor_com_desconto(valor_unitario = float(2.00),desconto = int(1), quantidade = int(10) ):
    resultado = valor_unitario * desconto * quantidade

    assert resultado == 20

def test_valor_sem_desconto(valor_unitario = 3.00, quantidade = 10):
    resultado = valor_unitario * quantidade

    assert resultado == 30
1 -> __________________________________________________________________ <- 1
'''


'''
2 -> __________________________________________________________________ <- 2

def test_itens_Carrinho():
    itens = []
    while True:
        codigo = int(input('Digite um valor: ')) #colocar o -s no terminal pra rodar o input

        if codigo == 100:
            itens.append('cachorro_quente')
            total = 9
        elif codigo == 101:
            itens.append('cachorro_quenteD')    
            total1 = 11
        else:
            print(f'<<ERROR: Item Não Encontrado>>\nSeu Total foi de: R${total + total1} Reais')
            break

    assert 'cachorro_quente'  in itens
    assert 'cachorro_quenteD' in itens
    assert total + total1 == 20
2 -> __________________________________________________________________ <- 2
'''    