"""
Classificador de meia-entrada de cinema
Regras:
- Menor de 12 anos: gratuito
- 12 a 17 anos com carteirinha: meia-entrada
- Demais casos: entrada inteira
"""

resposta_carteirinha = ""
while resposta_carteirinha not in ("s", "n"):
    resposta_carteirinha = input("Possui carteirinha de estudante? (s/n): ").strip().lower()

possui_carteirinha = resposta_carteirinha == "s"

while True:
    try:
        idade_pessoa = int(input("Digite sua idade: "))
        if idade_pessoa < 0:
            print("Idade não pode ser negativa. Tente novamente.")
            continue
        break
    except ValueError:
        print("Entrada inválida! Digite um número inteiro para a idade.")

if idade_pessoa < 12:
    situacao, resultado_msg = "gratuito", "Entrada gratuita"
elif idade_pessoa <= 17 and possui_carteirinha:
    situacao, resultado_msg = "meia", "Meia-entrada liberada"
else:
    situacao, resultado_msg = "inteira", "Entrada inteira"

print(f"\nIdade: {idade_pessoa} | Carteirinha: {'Sim' if possui_carteirinha else 'Não'}")
print(f"Status: {resultado_msg.upper()}")

motivos = {
    "gratuito": "Menores de 12 anos não pagam.",
    "meia": "Idade entre 12 e 17 anos com carteirinha válida.",
    "inteira": "Não se enquadra nas condições de meia-entrada."
}
print(f"Motivo: {motivos[situacao]}")
