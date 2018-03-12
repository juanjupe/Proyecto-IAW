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

		for juego in juegos :
				print (str(juego)[22:-7])				
				a=Juego(nombre=str(juego)[22:-7])
				a.save()
