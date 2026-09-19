import json
with open('vendas.json', 'r', encoding="utf-8") as arquivo:
    dados = json.load(arquivo)
comissoes_totais = {}

for venda in dados["vendas"]:
    vendedor = venda["vendedor"]
    valor = venda["valor"]
   
    if valor <100:
        comissao = 0.0
    elif valor <= 500: 
        comissao = valor * 0.01
    else:
        comissao = valor * 0.05  
        
    if vendedor in comissoes_totais:
        comissoes_totais[vendedor] += comissao      
    else:
        comissoes_totais[vendedor] = comissao
        
print("---Comissões Totais por Vendedor---")
for vendedor, comissao in comissoes_totais.items():
    print(f"Vendedor: {vendedor} | Comissão Total: R$ {comissao:.2f}")
    
    