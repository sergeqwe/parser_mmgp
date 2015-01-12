import pandas as pd
import matplotlib.pyplot as plt
import datetime

Location = '/home/qwe/Документы/python/result.txt'

df = pd.read_csv(Location, names=['Name', 'Author', 'Start', 'End', 'Answer', 'Review'], sep=';;')

# Добавляем через pandas колонку Delta
df['Delta'] = 0


# Находим разницу между датой закрытия хайпы и датой открытия (сколько просуществовал хайп)
for i in range(17640):
	start = df.Start[i]
	start = datetime.datetime.strptime(start, '%d.%m.%Y')

	end = df.End[i]
	end = datetime.datetime.strptime(end, '%d.%m.%Y')

	delta = end-start
	delta = delta.days
	
	df['Delta'][i] = delta

 





# Save results to excel
'''
df.to_excel('/home/qwe/Документы/python/result.xlsx', index=False)
print 'Done'
'''
