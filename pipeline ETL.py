import pandas as pd
import random
import os

# --- ETAPA 1: EXTRACT (Extração) ---
# Lendo os dados do arquivo CSV que criamos
print("Iniciando o processo de ETL...")

# 1. Obtém o caminho absoluto da pasta onde este script (.py) está salvo
diretorio_script = os.path.dirname(os.path.abspath(__file__))

# 2. Constrói o caminho para o CSV (independente de onde você rode o script)
caminho_csv = os.path.join(diretorio_script, 'SDW2025.csv')

try:
    # Usamos a variável 'caminho_csv' que criamos acima
    df = pd.read_csv(caminho_csv)
    print(f"Arquivo encontrado em: {caminho_csv}")
    print("Dados extraídos com sucesso!")
    print(df.head()) 
except FileNotFoundError:
    print(f"Erro: O arquivo não foi encontrado no caminho: {caminho_csv}")
    exit()

    import random

# --- ETAPA 2: TRANSFORM (Transformação) ---
print("\nIniciando a transformação dos dados...")

# Vamos criar uma função simples que simula uma IA gerando texto
# No seu dia a dia no orçamento, isso poderia ser uma função que classifica despesas automaticamente!
def gerar_mensagem_marketing(nome):
    mensagens = [
        f"Olá {nome}, invista no seu futuro com nossos planos especiais!",
        f"{nome}, você viu as novas vantagens do seu cartão? Confira no app.",
        f"Dica de hoje para {nome}: Organize suas finanças com a nossa nova ferramenta."
    ]
    return random.choice(mensagens)

# Aqui aplicamos a lógica linha por linha no DataFrame
# Verifique se a coluna de nomes no seu CSV se chama 'Nome' ou 'name'. 
# Se for diferente, ajuste abaixo (ex: df['Nome_Cliente'])
try:
    # O método .apply() é super poderoso no Pandas. Ele executa a função para cada linha.
    df['news'] = df['Nome'].apply(gerar_mensagem_marketing)
    
    print("Transformação concluída! Veja como ficou:")
    print(df[['Nome', 'news']].head())
    
except KeyError as e:
    print(f"Erro: Não encontrei a coluna de nome. Verifique o nome correto no seu CSV. Erro: {e}")
    print("Colunas disponíveis:", df.columns)