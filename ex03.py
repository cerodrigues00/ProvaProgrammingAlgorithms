import locale

def preparar_formatador():
    try:
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    except locale.Error:
        locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')
    return lambda v: locale.currency(v, grouping=True, symbol='R$ ')

formatar = preparar_formatador()

print("=" * 50)
print("         SISTEMA DE VENDAS - PADARIA")
print("=" * 50)

cliente = input("Nome do cliente: ")
item = input("Nome do produto: ")
valor_unit = float(input("Preco unitario (R$): "))
qtd = int(input("Quantidade: "))
perc_desconto = float(input("Percentual de desconto (%): "))

valor_bruto = valor_unit * qtd
desconto_calculado = valor_bruto * perc_desconto / 100
valor_liquido = valor_bruto - desconto_calculado

print("\n" + "=" * 50)
print("         RECIBO DA COMPRA")
print("=" * 50)
print(f"Cliente:          {cliente}")
print(f"Produto:          {item}")
print(f"Quantidade:       {qtd} unidade(s)")
print(f"Preco unitario:   {formatar(valor_unit)}")
print(f"Subtotal:         {formatar(valor_bruto)}")
print(f"Desconto:         {perc_desconto:.0f}% ({formatar(desconto_calculado)})")
print(f"TOTAL A PAGAR:    {formatar(valor_liquido)}")
print("=" * 50)
