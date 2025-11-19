import pandas as pd

class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.df_filtrado = None

    def carregar_csv(self):
        """Carrega o arquivo CSV em um DataFrame do pandas."""
        self.df = pd.read_csv(self.file_path)
        return self.df
    
    def filtrar_por(self, coluna: str, atributo: str):
        """Filtra o DataFrame com base em uma coluna e um atributo."""
        if len(coluna) != len(atributo):
            raise ValueError("A coluna e o atributo devem ter o mesmo tamanho.")
        if len(coluna) == 0:
            return self.df
        
        coluna_atual = coluna[0]
        atributo_atual = atributo[0]
        
        df_filtrado = self.df[self.df[coluna_atual] == atributo_atual]

        if len(coluna) == 1:
            return df_filtrado
        else:
            return self.filtrar_por(coluna[1:], atributo[1:])