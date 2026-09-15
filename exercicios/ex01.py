# Guarda o texto e calcula a expressão antes de qualquer print
usuario = "Edson"
calculo = 2 + 3 * 4
operacao = "2 + 3 * 4"

print(usuario)
# Edson

print(calculo)
# 14

saudacao = "Olá," + usuario + "!"
print(saudacao)
# Olá,Edson!

print(operacao)
# 2 + 3 * 4 (aqui é só texto, o Python não calcula)

# Duas formas de juntar texto com número: concatenação e f-string
resultado_concat = operacao + " = " + str(calculo)
print(resultado_concat)

resultado_fstring = f"{operacao} = {calculo}"
print(resultado_fstring)
