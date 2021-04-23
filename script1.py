import xlsxwriter
from selenium import webdriver
import time

div = 1
row = 0


navegador = webdriver.Chrome()
navegador.get('https://www.magazineluiza.com.br/iphone-12/celulares-e-smartphones/s/te/ip12?page=2')

file = xlsxwriter.Workbook('projeto4.xlsx')
table = file.add_worksheet()
table.write(row + 0, 0, 'produto')
table.write(row + 0, 1, 'Preço')


while div < 24:

    produto = navegador.find_element_by_xpath('//*[@id="showcase"]/ul[1]/a[{}]/div[3]/h3'.format(div)).text;
    preco = navegador.find_element_by_xpath('//*[@id="showcase"]/ul[1]/a[{}]/div[3]/div/div[2]'.format(div)).text;

    table.write(row + div, 0, produto)
    table.write(row + div, 1, preco)
    div = div + 1
    time.sleep(3)
    print('Produto regitrado')

file.close()




