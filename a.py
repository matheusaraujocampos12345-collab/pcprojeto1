Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import math
... import random
... import datetime
... import locale
... import statistics
... 
... locale.setlocale(locale.LC_ALL, 'pt-BR.UTF-8')
... 
... #Entrada
... capital = float(input('Capital inicial: '))
... aporte = float(input('Aporte Mensal: '))
... meses = int(input('Prazo em meses: '))
... cdi_anual = float(input('Cdi Anual(%): '))/100
... perc_cdb = float(input('Percentual CDI (%):'))/100
... perc_lci = float(input('Percentual LCI (%): '))/100
... taxa_fii = float(input('Rentabilidade mensal FII (%): '))/100
... Meta = float(input('Projeção financeira (R$): '))
... 
... #Processamento
... cdi_mensal = math.pow(1 + cdi_anual, 1/12) - 1
... 
... #Total investimento
... total_inv = capital + (aporte * meses)
... 
... #CDB
... taxa_cdb = cdi_mensal * perc_cdb
... montante_cdb = (capital * math.pow(1 + taxa_cdb, meses) + (aporte * meses))
... lucro_cdb = montante_cdb - total_inv
... montante_cdb_liquido = total_inv + (lucro_cdb * 0.85)
... 
... #LCI
... taxa_lci = cdi_mensal * perc_lci
... montante_lci = capital * math.pow((1 + taxa_lci), meses) + (aporte * meses)
... 
... #Poupança
... taxa_poup = 0.005
... montante_poup = capital * math.pow((1 + taxa_poup), meses) + (aporte * meses)

# FII (5 simulações com risco)
fii1 = (capital * math.pow(1 + taxa_fii, meses) + (aporte * meses)) * (1 + random.uniform(-0.03,0.03))
fii2 = (capital * math.pow(1 + taxa_fii, meses) + (aporte * meses)) * (1 + random.uniform(-0.03,0.03))
fii3 = (capital * math.pow(1 + taxa_fii, meses) + (aporte * meses)) * (1 + random.uniform(-0.03,0.03))
fii4 = (capital * math.pow(1 + taxa_fii, meses) + (aporte * meses)) * (1 + random.uniform(-0.03,0.03))
fii5 = (capital * math.pow(1 + taxa_fii, meses) + (aporte * meses)) * (1 + random.uniform(-0.03,0.03))

media_fii = statistics.mean([fii1,fii2,fii3,fii4,fii5])
mediana_fii = statistics.median([fii1,fii2,fii3,fii4,fii5])
desvio_fii = statistics.stdev([fii1,fii2,fii3,fii4,fii5])

# Datas
data_simulacao = datetime.date.today()
data_resgate = data_simulacao + datetime.timedelta(days = meses * 30)

# Meta
meta_atingida = media_fii >= Meta

# Gráficos ASCII
graf_cdb = "█" * int(montante_cdb_liquido / 1000)
graf_lci = "█" * int(montante_lci / 1000)
graf_poup = "█" * int(montante_poup / 1000)
graf_fii = "█" * int(media_fii / 1000)

# Relatório
print("\n===== RELATÓRIO PYINVEST =====")

print("Data da simulação:", data_simulacao)
print("Data de resgate:", data_resgate)

print("\nTotal investido:", locale.currency(total_inv, grouping=True))

print("\nCDB:", locale.currency(montante_cdb, grouping=True))
print(graf_cdb)

print("\nLCI/LCA:", locale.currency(montante_lci, grouping=True))
print(graf_lci)

print("\nPoupança:", locale.currency(montante_poup, grouping=True))
print(graf_poup)

print("\nFII:", locale.currency(media_fii, grouping=True))
print(graf_fii)

print("\nEstatísticas FII")
print("Média:", locale.currency(media_fii, grouping=True))
print("Mediana:", locale.currency(mediana_fii, grouping=True))
print("Desvio padrão:", locale.currency(desvio_fii, grouping=True))

