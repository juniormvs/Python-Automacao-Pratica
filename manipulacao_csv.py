import csv
import os

# Define o nome do arquivo a ser lido, usando o caminho relativo
NOME_ARQUIVO = 'dados/vendas_brutas.csv'

# 1. FUNÇÃO PRINCIPAL DE PROCESSAMENTO
def gerar_relatorio_pendente_sudeste(nome_arquivo):
    pedidos_filtrados = []
    valor_total_pendente = 0.0

    try:
        # Abre o arquivo para leitura
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv)

            for linha in leitor:
                # 1.1. TRATAMENTO DE VALOR FALTANTE (Limpeza de Dados)
                valor_str = linha.get('Valor')
                # Se o campo Valor estiver vazio, definimos como 0.0
                valor = float(valor_str) if valor_str else 0.0 

                # 1.2. FILTRO (Lógica de Negócio)
                status = linha.get('Status_Pagamento')
                regiao = linha.get('Regiao')

                # Filtra apenas pedidos PENDENTES na região SUDESTE
                if status == 'PENDENTE' and regiao == 'Sudeste':
                    pedidos_filtrados.append(linha)
                    valor_total_pendente += valor

    except FileNotFoundError:
        print(f"ERRO: Arquivo {nome_arquivo} não encontrado. Certifique-se do caminho.")
        return None, 0.0

    return pedidos_filtrados, valor_total_pendente

# 2. EXECUÇÃO
print(f"--- Processando dados do arquivo: {NOME_ARQUIVO} ---")
relatorio, total = gerar_relatorio_pendente_sudeste(NOME_ARQUIVO)

# 3. SAÍDA FINAL (O Relatório)
if relatorio is not None:
    print(f"\nRelatório Final (Pedidos PENDENTES na região Sudeste):")
    if relatorio:
        for pedido in relatorio:
            # Demonstração da extração de dados
            print(f"  - Pedido ID {pedido['ID_Pedido']} | Cliente: {pedido['Cliente']} | Valor: R$ {float(pedido['Valor'] if pedido['Valor'] else 0.0):.2f}")
        
        print(f"\nVALOR TOTAL PENDENTE NO SUDESTE: R$ {total:.2f}")
    else:
        print("Nenhum pedido pendente encontrado para a região Sudeste.")
