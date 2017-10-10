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
	juego = soup.find_all('span', itemprop="name")
	plataforma = soup.find_all('td' , itemprop="operatingSystem gamePlatform")
         
# Con [0] saco el primer elemento y con [1] el segundo
	print "juego :" +juego[19].text + "\n"+"plataforma :" + plataforma[19].text 
# Tiempo en segundos para ejecutarse nuevamente
	time.sleep(15)
# Boramos los datos viejos, para Windows es "cls"
	os.system("clear")
