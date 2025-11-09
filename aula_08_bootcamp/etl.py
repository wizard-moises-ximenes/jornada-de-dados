import glob
import os

import pandas as pd

# uma função de extract que le e consolida os json


def extract_json_files(path: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(path, "*.json"))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


# uma função de transform que limpa e transforma os dados
def calcular_kpi_de_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df_novo = df.copy()
    df_novo["Total"] = df_novo["Quantidade"] * df_novo["Venda"]
    return df_novo


# uma função de load em csv ou parquet
def carregar_dados(df: pd.DataFrame, format_saida: list) -> None:
    for formato in format_saida:
        if formato == "csv":
            df.to_csv("dados.csv", index=False)
        if formato == "parquet":
            df.to_parquet("dados.parquet", index=False)


def pipeline_calcular_kpi_total_vendas(path: str, format_saida: list) -> None:
    df = extract_json_files(path)
    df = calcular_kpi_de_total_vendas(df)
    carregar_dados(df, format_saida=format_saida)
