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
for juego in juegos:
	print juego
print juegos
plataformas = soup.find_all('td' , itemprop="operatingSystem gamePlatform")
print plataformas     

