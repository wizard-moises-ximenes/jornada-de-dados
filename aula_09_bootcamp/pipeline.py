from etl import pipeline_calcular_kpi_total_vendas

pasta: str = "data"
format_saida: list = ["parquet"]

pipeline_calcular_kpi_total_vendas(path=pasta, format_saida=format_saida)
