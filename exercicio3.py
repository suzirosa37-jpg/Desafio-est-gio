valor = float(input("Digite o valor (R$): "))
dias_atraso = int(input("Digite a quantidade de dias em atraso: "))

if dias_atraso > 0:
    juros = valor * 0.025 * dias_atraso
    valor_total = valor + juros
    
    print("\n--- RESULTADO ---")
    print(f"Valor dos juros: R$ {juros:.2f}")
    print(f"Valor total a pagar: R$ {valor_total:.2f}")
else:
    print("\nConta em dia! Sem juros.")