
from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains 

import time

class TotalCorner_Live_Stats:
	"""docstring for TotalCorner"""
	def __init__(self):

		url = 'https://www.totalcorner.com/match/live-stats/96415983'

		self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')

		self.driver.get(url)

		time.sleep(2)
		

	def obterValores(self,nome_grafico):

		dic_graf = {'Attack':[[2,3,4],2],'Dangerous Attack':[[1,3,4],4],'Shoot off target':[[1,2,4],6],'Shoot on target':[[1,2,3],8]}
		
		elementos =  self.driver.find_elements_by_tag_name(f'#highcharts-0 > svg > g.highcharts-series-group > g:nth-child({dic_graf[nome_grafico][1]}) > path')


		for num in dic_graf[nome_grafico][0]:

			self.action = ActionChains(self.driver)

			desabilitar_botao = self.driver.find_element_by_tag_name(f'#highcharts-0 > svg > g.highcharts-legend > g > g > g:nth-child({num})')

			self.action.move_to_element(desabilitar_botao).click().perform()


		self.action = ActionChains(self.driver)

		# Movendo o ponteiro do mouse para cima do ponto, tornar visível o valor do ponto 

		self.action.move_to_element(elementos[0]).perform()
										
		valores = []


		for elemento in elementos:

			self.action = ActionChains(self.driver)

			# Movendo o ponteiro do mouse para cima do ponto, tornar visível o valor do ponto 

			self.action.move_to_element(elemento).perform()

			valor = self.driver.find_element_by_tag_name('#highcharts-0 > svg > g.highcharts-tooltip > text > tspan:nth-child(4)')

			valores.append(valor.text)


		return nome_grafico, valores


	


		
x = TotalCorner_Live_Stats()

nome_grafico, valores = x.obterValores('Shoot off target')

print(f'As estatísticas do gráfico {nome_grafico}, são: {valores}')


