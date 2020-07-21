print('*' * 40)
print('CAIXA ' * 7)
print('*' * 40)


#  Principais funções

#  calcula desconto
def calcula_desconto(tax, total):
    novo_valor = total - (total * tax / 100)
    return novo_valor


#  calcula novo valor com acréscimo
def calcula_acrecimo(tax, total):
    novo_valor = total + (total * tax / 100)
    return novo_valor


def parcelaCompra(qt_p, total_p):
    print('****COMPRA NO CARTÃO DE CRÉDITO***')
    print('COMPRA PARCELADAS EM.......... {}x'.format(qt_p))
    print('ACRÉSCIMO........... {}%'.format(qt_p))
    print('TOTAL: R${}'.format(total_p))

total = float(input('TOTAL: '))
tipo_pagamento = input(('TIPO DE PAGAMENTO >> CARTÃO/DINHEIRO: '))

if tipo_pagamento == 'DINHEIRO':
    entrada = float(input('Entrada: '))
    while entrada < total:
        print('Entrada insuficiente.')
        entrada = float(input('Entrada: '))

    if total >= 80:
        novo_total = calcula_desconto(15, total)
        print('TOTAL DA COMPRA ---------- {}'.format(total))
        print('DESCONTO ----------  -15%')
        print(f"TOTAL DA COMPRA COM DESCONTO ----------- {novo_total}")
        print("Troco: {:.2f}".format(entrada - total))

    else:
        print('TOTAL DA COMPRA ---------- {}'.format(total))
        print("Troco: {:.2f}".format(entrada - total))


elif tipo_pagamento == 'CARTÃO':
    if total < 80:
        print('Não foi possível parcelar esta compra')
    else:
        qt_parcelas = int(input('Parcelar em [2x - 3x - 5x]: '))
        if qt_parcelas < 2 or qt_parcelas > 5:
            while qt_parcelas < 2 or qt_parcelas > 5:
                print('<<OPÇÃO INVÁLIDA>>')
                qt_parcelas = int(input('Parcelar em [2x - 3x - 5x]: '))
                total_parcelamento = calcula_acrecimo(qt_parcelas, total)
                parcelaCompra(qt_parcelas, total_parcelamento)

        elif qt_parcelas == 2:
            total_parcelamento = calcula_acrecimo(qt_parcelas, total)
            parcelaCompra(qt_parcelas, total_parcelamento)

        elif qt_parcelas == 3:
            total_parcelamento = calcula_acrecimo(qt_parcelas, total)
            parcelaCompra(qt_parcelas, total_parcelamento)

        elif qt_parcelas == 5:
            total_parcelamento = calcula_acrecimo(qt_parcelas, total)
            parcelaCompra(qt_parcelas, total_parcelamento)

