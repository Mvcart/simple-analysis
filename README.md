# GlobalTech Sales Analysis

**Autor:** Marcos Cota

Script PySpark para consolidar a performance de vendas por país, incluindo continente, valor total, média e avaliação. Atividade 1 do RocketLab.

## Estrutura do Projeto
```text
├── analysis.py
├── continents.csv
├── README.md
└── sales_data_sample.csv
```

## Como Executar
O arquivo `.py` verifica automaticamente se está rodando no Databricks (edite o caminho hardcoded para o local correto).
Caso seja local:
```bash
# Localmente
python analysis.py
```

## Saída Esperada
DataFrame consolidado com as colunas:
- `COUNTRY`
- `CONTINENT`
- `valor_total_vendas`
- `media_vendas`
- `avaliacao_performance`