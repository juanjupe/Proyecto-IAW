#!/usr/bin/python
# -*- coding: utf-8 -*-
# Sitio: http://www.vandal.net/lanzamientos/0/videojuegos
 
# Importamos las librerias
from bs4 import BeautifulSoup
import requests
import time
import os
 
# Creamos el Bucle infinito
while True:
# Capturamos la url
	url = "http://www.vandal.net/lanzamientos/0/videojuegos"
# Capturamos el hml de la pagina web y creamos un objeto Response
	r  = requests.get(url)
	data = r.text
# Creamos el objeto soup y le pasamos lo capturado con request
	soup = BeautifulSoup(data, 'lxml')
# Buscamos el div para sacar los grados
	temp = soup.find_all('div', class_="fblanco froboto_real mt1")
# Buscamos el div para sacar la sensacion termica
#	sTerm = soup.find_all('div', class_="table table-striped froboto_real")
         
# Con [0] saco el primer elemento y con [1] el segundo
	print temp[0].text
#	print "La sesacion termica: " + sTerm[0].text
# Tiempo en segundos para ejecutarse nuevamente
	time.sleep(15)
# Boramos los datos viejos, para Windows es "cls"
	os.system("clear")
