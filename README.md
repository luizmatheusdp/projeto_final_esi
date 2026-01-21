# Projeto Final ESI - Predição de Mudança em Arquivos

## Objetivo
Prever se um arquivo de código será modificado na próxima release utilizando Machine Learning.

## Estrutura do Projeto
- `dados/` - CSVs brutos e tratados
- `notebooks/` - Notebooks de análise e treino de modelo
- `modelos/` - Modelos treinados e binários
- `api/` - Serviço para consumir o modelo via API
- `requisitos.txt` - Dependências do projeto
- `Python 3.11.9` - Versão do python
## Como rodar
1. Instalar dependências:
   ```bash
   pip install -r requirements.txt

   
2. Ative o ambiente virtual:
   ```bash
   "venv/Scripts/Activate.ps1"


3. Inicie a API:
   ```bash
   python api/app.py

4. Enquanto a API estiver rodando, abra outro terminal e execute:
   ```bash
   python api/teste_api.py

Exemplo de sáida:
```yaml
   Status code: 200
   Resultado: {'mudanca_prevista': 1}


   

