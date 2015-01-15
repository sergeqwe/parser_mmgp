# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

%pylab inline

# <codecell>

import pandas as pd
import matplotlib.pyplot as plt
import datetime

# <codecell>

#Location = '/home/qwe/Документы/python/result.txt'
Location = '/home/lepinskiy.s.v/python/parser_mmgp/result.txt'
df = pd.read_csv(Location, names=['Names', 'Author', 'Start', 'End', 'Answer', 'Review'], sep=';;')

# <codecell>

df[0:3]

# <codecell>

# Добавляем через pandas колонку Delta (разница между датой закрытия и открытия) 
df['Delta'] = 0
# Добавляем столбцы Month для сезонной статистики открытия и закрытия
df['Month_Start'] = 0
df['Month_End'] = 0

# <codecell>

df[0:3]

# <codecell>

# Находим разницу между датой закрытия хайпа и датой открытия (сколько просуществовал хайп)
# Сезонная статистика закрытия хайпов (в какой месяц больше всего и меньше всего закрываются и открываются)
for i in range(17640):
	start = df.Start[i]
	start = datetime.datetime.strptime(start, '%d.%m.%Y')
	end = df.End[i]
	end = datetime.datetime.strptime(end, '%d.%m.%Y')
	delta = end-start
	delta = delta.days
	df['Delta'][i] = delta
	df['Month_Start'][i] = start.month
	df['Month_End'][i] = end.month

# <codecell>

df[0:3]

# <codecell>

# Создаем новую таблицу из колонки Delta, чтобы подсчитать кол-во
df1 = pd.DataFrame(data = df['Delta'], columns=['Delta'])

# <codecell>

df1.head()

# <codecell>

# Добавляем поле count. По нему будем считать кол-во повторяющихся значений
df1['Count'] = 1

# <codecell>

df1[0:3]

# <codecell>

# Выполняем группировку
name = df1.groupby('Delta')

# Высчитываем сумму сгруппированных объектов
df1 = name.sum()

# <codecell>

df1[0:3]

# <codecell>

# Строим график сколько в среднем дней живут хайпы
df1[:365].plot(kind='bar', figsize=(70, 10))
grid(True)
title(u'Срок жизни хайпов')
ylabel(u'Кол-во соскамившихся хайпов')
xlabel(u'Кол-во дней')
#df[100:200].plot(kind='bar', figsize=(20, 5))

# <codecell>

# Добавляем колонку сколько хайпов осталось. По этим даннм будем смотреть сколько за период времени хайпов соскамилось.
df1['Residue'] = 0

# <codecell>

# Добавляем в таблицу колонку индексов
df1= df1.reset_index()

# <codecell>

df1[:4]

# <codecell>

print 'Столбцов в диаграмме: ', len(df1)

# <codecell>

# Подсчитываем остаток хайпов на текущий день и записываем их в колоку Residue
s = 17640
for i in range(0,585):
    s = s-df1['Count'][i]
    df1['Residue'][i] = s
    

# <codecell>

df1[:4]

# <codecell>

#df1.to_excel('/home/lepinskiy.s.v/python/parser_mmgp/Residue.xlsx', index=False)

# <codecell>

# График оставшихся хайпов
days = 365
plt.plot(df1['Delta'][:days], df1['Residue'][:days], linewidth=2.0)
plt.title(u'График оставшихся хайпов')
plt.xlabel(u'Дни')
plt.ylabel(u'Хайпов осталось')
plt.grid(True)
#plt.axis([0, 5, 0, 20])
plt.show()

# <codecell>

df[:3]

# <codecell>

# Создаем новые таблицы из колонок Month_Start и Month_end для подсчета кол-ва открытия и закрытия хайпов по месяцам (сезонность)
df_month_start = pd.DataFrame(data = df['Month_Start'], columns=['Month_Start'])
df_month_end = pd.DataFrame(data = df['Month_End'], columns=['Month_End'])

# <codecell>

# Добавляем столбцы Count
df_month_start['Count'] = 1
df_month_end['Count'] = 1

# <codecell>

# Выполняем группировку для Month_Start
name = df_month_start.groupby('Month_Start')
# Высчитываем сумму сгруппированных объектов
df_month_start = name.sum()

# Выполняем группировку для Month_Start
name = df_month_end.groupby('Month_End')
# Высчитываем сумму сгруппированных объектов
df_month_end = name.sum()

# <codecell>

df_month_start.plot(kind='bar')
grid(True)
title(u'Кол-во открывающихся хайпов по месяцам')
ylabel(u'Кол-во открывшихся хайпов')
xlabel(u'Месяц')

# <codecell>

df_month_end.plot(kind='bar')
grid(True)
title(u'Кол-во закрывшихся хайпов по месяцам')
ylabel(u'Кол-во соскамившихся хайпов')
xlabel(u'Месяц')

# <codecell>

# Кол-во постов на автора
df_author = pd.DataFrame(data = df['Author'], columns=['Author'])

# <codecell>

# Добавляем колонку Count
df_author['Count'] = 1

# <codecell>

# Выполняем группировку для Author
name = df_author.groupby('Author')
# Высчитываем сумму сгруппированных объектов
df_author = name.sum()

# <codecell>

# Сортируем по кол-ву постов
author_sorted = df_author.sort(['Count'], ascending=False)

# <codecell>

# Строим график
author_sorted[:30].plot(kind='bar')

# <headingcell level=3>

# РАСЧЕТ ВЛОЖЕНИЙ

# <codecell>

# Задаем дату инвестирования
date = '01.01.2010'
date_of_investing = datetime.datetime.strptime(date, '%d.%m.%Y')

# Задаем кол-во хайпов в которые инвестируем
hyip = 10

# <codecell>


# <codecell>


