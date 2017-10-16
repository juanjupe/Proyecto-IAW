#!/usr/bin/python
# -*- coding: utf-8 -*-
# Sitio: http://www.vandal.net/lanzamientos/0/videojuegos
 

from bs4 import BeautifulSoup
import requests

 

url = "http://www.vandal.net/lanzamientos/0/videojuegos"
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'lxml')
juegos = soup.find_all('span', itemprop="name")
plataformas = soup.find_all('td' , itemprop="operatingSystem gamePlatform")

for juego in juegos :
	print (str(juego)[22:-7])    

for plataforma in plataformas:
	print (str(plataforma)[44:-5])
