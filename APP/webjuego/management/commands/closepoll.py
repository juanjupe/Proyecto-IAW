from django.core.management.base import BaseCommand, CommandError
from webjuego.models import *
from bs4 import BeautifulSoup
import requests


class Command(BaseCommand):
	def handle(self, *args, **options):

		url = "http://www.vandal.net/lanzamientos/0/videojuegos"
		r  = requests.get(url)
		data = r.text
		soup = BeautifulSoup(data, 'lxml')
		juegos = soup.find_all('span', itemprop="name")
		plataformas = soup.find_all('td' , itemprop="operatingSystem gamePlatform")
		cont=0

		cont=0

		for juego in juegos :
			#pla=str(plataformas[0])[44:-5]
			print (str(juego)[22:-7])  
			#print pla  
			
			a=Juego(nombre=str(juego)[22:-7])
			a.save()
			print ("datos insertados")
			
			cont=cont+1

