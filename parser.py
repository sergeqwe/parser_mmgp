# -*- coding: utf-8 -*-
import requests
import lxml.html
import re

# На какой странице в данный момент находимся
pages_all = 1
pages = [0, 10]
sep = "^" # Разделитель в SCV файле

'''
proxies = {
  "http": "http://test:IRRAa0BA@87.118.113.157:8972",
  "https": "http://test:IRRAa0BA@87.118.113.157:8972",
}
'''

# Открываем файл для записи результатов
f = open('result.txt', 'w')

# Стартовая станица
base_url = base_url_my = 'http://mmgp.ru/forumdisplay.php?f=344'

while pages_all < pages[1]:
	# Загружаем страницу
	# session = requests.session()
	url = requests.get(base_url)#, proxies=proxies)
	
	# Если статус при загрузке страницы не равен 200, то останавливаем скрипт
	if url.status_code != 200:
		print "FAILED! Status code is:", url.status_code
		f.close()
		exit
	
	doc = lxml.html.document_fromstring(url.text)
	 
	# Если мы находимся на первой странице, то получаем кол-во страниц. Они будут в переменной pages[1]
	if pages_all == 1:
		pages = doc.xpath('//td[@class="vbmenu_control"]/text()')
		pages = [int(s) for s in pages[0].split() if s.isdigit()]
		print u'Всего старниц: ', pages[1]
	 
	# Выводим номер страницы на которой мы находимся
	print u"Страница", pages_all, u"из", pages[1]

	# Получаем названия хайпов на странице
	hyip = doc.xpath('//tr/td/div/a[@id]/text()')
	count = len(hyip)
	print u"На станице хайпов: ", count

	# Получаем ссылки на хайпы
	# ref = doc.xpath('//tr/td/div/a[@id]/@href')

	# Получаем имена тех кто постил
	nickname = doc.xpath('//div[@class="smallfont"]/span[@title]/text()')

	# Получаем дату создания темы
	posting_date = doc.xpath('//div[@class="smallfont"]/span/@title')

	# Получаем дату последнего сообщения в теме. При этом вытаскиваем значения через posting_date_end[0].text
	posting_date_end = doc.xpath('//div[@class="smallfont"][@style="text-align:right; white-space:nowrap"]')

	# Получаем кол-во ответов на пост (т.к. в переменной много разных символов, то вытаскиваем только число)
	answer = doc.xpath('//td[@class="alt1"][@align="center"]/text()')
	i=0
	answer1 = []
	while i < len(answer):
		answer1.append (re.sub("\D", "", answer[i]))
		i = i + 1
	
	# Кол-во просмотров
	review = doc.xpath('//td[@class="alt2"][@align="center"]/text()')
	i=0
	review1 = []
	while i < len(review):
		review1.append (re.sub("\D", "", review[i]))
		i = i + 1

	# Записываем информацию в файл
	i=0
	while i < count:
		result = (hyip[i] + sep +
		nickname[i] + sep +
		re.findall("\d{2}.\d{2}.\d{2,4}", posting_date[i])[0] + sep +
		re.findall("\d{2}.\d{2}.\d{2,4}", posting_date_end[i].text)[0] + sep +
		answer1[i] + sep +
		review1[i] # + sep +
		# 'http://mmgp.ru/'+ref[i]
		)
		f.write(result.encode('cp1251') + '\n')
		i=i+1

	pages_all = pages_all + 1
	base_url = base_url_my + '&order=desc&page=' + str(pages_all)
	# print '***separator********************************************************'

# Закрываем файл
f.close()
print '*****successful*****'
