pedido = {
    "produto": "Cálculo no carrinho de compras",
    "preco": 35.00,
    "quantidade": 2,
    "desconto": 10.00
}

valor_bruto = pedido["preco"] * pedido["quantidade"]
valor_pago = valor_bruto - pedido["desconto"]

print(f"\n{pedido['produto']}")
print(f"Um cliente comprou {pedido['quantidade']} livros, cada um por: R$ {pedido['preco']:.2f}")
print(f"E recebeu um desconto de: R$ {pedido['desconto']:.2f}")
print("Quanto ele gastou?")
print(f"Ele gastou: R$ {valor_pago:.2f}")
