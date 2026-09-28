#inserir o valor da compra
valor = float(input("Digite o valor total da compra: R$ "))
# se o valor for menor que 200, ira aplicar um desconto de 0.05 porcento
if valor < 200:
    desconto = valor * 0.05
 #se o valor for maior igual a  200 e menor que 300 ira aplicar um desconto de 0.010 porcento
elif valor >= 200 and valor < 300:
    desconto = valor * 0.10
# senao, valor sera maior igual a 300 e ira aplicar um desconto de 0.15 porcento
else:
    desconto = valor * 0.15
    
#realiza o calculo com a procentagem de desconto aplicada
valor_final = valor - desconto


#apresenta o valor informado sem o desconto aplicado
print(f"\nValor da compra: R$ {valor:.2f}")
#apresenta o total de desconto
print(f"Desconto: R$ {desconto:.2f}")
#apresenta o valor final com o desconto aplicado
print(f"Valor final: R$ {valor_final:.2f}")