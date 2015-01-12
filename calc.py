import pandas as pd
import matplotlib.pyplot as plt
import datetime

Location = '/home/qwe/Документы/python/result.txt'

df = pd.read_csv(Location, names=['Names', 'Author', 'Start', 'End', 'Answer', 'Review'], sep=';;')

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

# Удаляем лишние столбцы

del df['Names']
del df['Author']
del df['Start']
del df['End']
del df['Answer']
del df['Review']

# Добавляем поле count. По нему будем считать кол-во повторяющихся значений
df['Count'] = 1


# Create a groupby object
name = df.groupby('Delta')

# Apply the sum function to the groupby object
df = name.sum()
df



#Sorted = df.sort(['Delta'], ascending=False)



# Суммируем хайпы по кол-ву прожитых дней
#name = df.groupby('Delta')
#df1 = name.sum()




#Добавляем через pandas колонку Howmuch
#df['Howmuch'] = 0

# Рассчитываем сколько каждый день осталось хайпов
#hyips = 17640
#for i in range(17640):
#df['Howmuch'][0] =





# Save results to excel

#df.to_excel('/home/qwe/Документы/python/result.xlsx', index=False)
#print 'Done'

