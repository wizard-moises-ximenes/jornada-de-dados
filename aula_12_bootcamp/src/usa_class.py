from interface.classes.csv_class import CsvProcessor

arquivo = './exemplo.csv'
filtro = ['estado', 'preco']
atributo = ['SP', '22,00']

arquivo_CSV = CsvProcessor(arquivo)
arquivo_CSV.carregar_csv()
resultado = arquivo_CSV.filtrar_por(filtro, atributo)
print(resultado)