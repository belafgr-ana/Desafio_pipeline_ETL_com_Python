# Desafio_pipeline_ETL_com_Python
Desafio Explorando IA Generativa em um Pipeline de ETL com Python - Santander Bootcamp 2º semestre 2025

# 📊 Desafio de Projeto: Pipeline de ETL com Python

**Bootcamp Santander 2025 - Ciência de Dados com Python**

Este repositório contém a resolução do desafio de construção de um pipeline de ETL (Extract, Transform, Load), demonstrando habilidades de manipulação de dados e lógica de programação.

## 🚀 Sobre o Projeto

O objetivo foi criar um script que automatiza o processo de:
1.  **Extração:** Leitura de dados tabulares (CSV).
2.  **Transformação:** Aplicação de lógica de negócios (Enriquecimento de dados).
3.  **Carregamento:** Disponibilização dos dados processados.

### 🛠️ Tecnologias Utilizadas
* **Python 3.14**
* **Pandas:** Para manipulação de DataFrames.
* **OS:** Para gerenciamento robusto de caminhos de arquivos (File Paths).
* **Random:** Para simulação de lógica geradora de conteúdo.

## 📂 Estrutura do Pipeline

### 1. Extract (Extração)
Utilizei a biblioteca `pandas` para ler o arquivo `SDW2025.csv`.
* **Destaque Técnico:** Implementei a biblioteca `os` para identificar dinamicamente o diretório do script. Isso soluciona o erro comum de `FileNotFoundError` ao executar o código em diferentes terminais ou IDEs, tornando o script "portátil".

### 2. Transform (Transformação)
Criei uma lógica de transformação que simula uma IA Generativa simples.
* O script lê o nome de cada usuário.
* Aplica uma função personalizada `gerar_mensagem_marketing`.
* Utiliza o método `.apply()` do Pandas para iterar sobre as linhas de forma otimizada (vetorizada), evitando loops `for` desnecessários.

### 3. Load (Carregamento)
O resultado é um DataFrame enriquecido com uma nova coluna de mensagens personalizadas ("news"), pronto para ser salvo ou exportado.

## 💻 Como Executar

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/belafgr-ana/Desafio_pipeline_ETL_com_Python.git](https://github.com/belafgr-ana/Desafio_pipeline_ETL_com_Python.git)

2. **Instale as dependências:**
   pip install pandas

3. **Execute o script:**
Certifique-se de que o arquivo SDW2025.csv está na mesma pasta do script e execute:
   python pipeline_ETL.py
### 
