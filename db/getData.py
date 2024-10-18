from selenium.webdriver.common.by import By
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get('https://www.google.com/search?q=redmi+note+13+pro+5g&gl=BR')

def getData():
	# GET DATA FROM GOOGLE 
	names = driver.find_elements(By.CSS_SELECTOR, 'div.gUf0b.uWvFpd.hP4iBf')
	links = driver.find_elements(By.CSS_SELECTOR, 'div.PshwNb a.P9159d.hMk97e.BbI1ub')
	imgs = driver.find_elements(By.CSS_SELECTOR, 'div.tLevwc img.YQ4gaf.zr758c')
	prices = driver.find_elements(By.CSS_SELECTOR, 'div.Xs9evb span.Pgbknd')
	descriptions = driver.find_elements(By.CSS_SELECTOR, 'div.Rp8BL.CpcIhb.rYkzq.vXtCo')

	# BUILD DATA LENGTH
	data = [{} for _ in range(len(names))]

	# SET NAMES IN DATA
	for name in enumerate(names):
		data[name[0]]['name'] = name[1].text

	# SET LINKS IN DATA
	for link in enumerate(links):
		data[link[0]]['link'] = link[1].get_attribute('href')

	# SET IMGS IN DATA
	for img in enumerate(imgs):
		data[img[0]]['img'] = img[1].get_attribute('src')

	# SET PRICES IN DATA
	for price in enumerate(prices):
		data[price[0]]['price'] = price[1].text

	# SET DESCRIPTIONS IN DATA
	for description in enumerate(descriptions):
		data[description[0]]['description'] = description[1].text

	return data