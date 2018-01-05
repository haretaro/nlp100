import pandas
table = pandas.read_csv('hightemp.txt', delimiter='\t', header=None)
csv1 = table.iloc[:, 0]
csv2 = table.iloc[:, 1]
csv1.to_csv('col1.txt', index=False)
csv2.to_csv('col2.txt', index=False)
