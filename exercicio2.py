import json
import uuid

with open('estoque.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

codigo = int(input("Digite o código do produto (ex: 101): "))
tipo = input("Digite o tipo (entrada ou saida): ")
qtd = int(input("Digite a quantidade: "))
descricao = input("Digite a descrição da movimentação: ")

for produto in dados["estoque"]:
    if produto["codigoProduto"] == codigo:
        
        id_movimentacao = str(uuid.uuid4())[:8]
    
        if tipo == "entrada":
            produto["estoque"] = produto["estoque"] + qtd
        elif tipo == "saida":
            produto["estoque"] = produto["estoque"] - qtd
            
        print("\n--- MOVIMENTAÇÃO REALIZADA ---")
        print("ID da Movimentação:", id_movimentacao)
        print("Descrição:", descricao)
        print("Produto:", produto["descricaoProduto"])
        print("Quantidade Final no Estoque:", produto["estoque"])