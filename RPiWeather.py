# -*- coding: utf-8 -*-

"""
#
#	Autor:	Adrian Martinez Espinosa
#
#	Codigo para RPiWeather, una estacion meteorologica con 
#	Raspberry Pi que twittea los datos que recogen los sensores
#	junto a una foto del cielo tomada en ese instante con la 
#	camara P3 Eye
#
"""

import Adafruit_BMP.BMP085 as BMP 
import Adafruit_DHT as DHT
import subprocess as sub
import tweepy
import time
import os

def sensorBMP():
	sensor = BMP.BMP085()
	p = sensor.read_pressure()/100.0
	a = sensor.read_altitude()
	
	return p,a 

def sensorDHT():
	sensor = DHT.DHT11
	h, t = read_retry(sensor, 5)
	
	return h,t
	
def tweetea(texto, foto):
	CONSUMER_KEY = ''
	CONSUMER_SECRET = ''
	ACCESS_KEY = ''
	ACCESS_SECRET = ''
	
	auth = tweepy.OauthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	
	x = tweepy.API(auth)
	x.update_with_media(foto, texto)
	
def camara():
	path = "/home/pi/Desktop/RPiWeather/" + time.strftime("%d-%m-%Y_%X") + ".jpg"
	os.system("fswebcam -d /dev/video0 -r 640x480 --no-banner " + path)
	
	return path
	
def main():
	
	while True:
		try:
			print "\nObteniendo datos..."
			hum, temp = sensorDHT()
			press, alt = sensorBMP()
			
			print "\nObteniendo la foto..."
			photo = camara()
			
			print "\nEnviando tweet..."
			twit = 'Temperatura= {0:0.2f} ยบC'.format(temp) + '\Humedad= {0:0.2f} %'.format(hum)\
					+ '\nPresion= {0:0.2f} hPa'.format(press) + '\nAltitud= {0:0.2f} m'.format(alt)\
					+ '\n#Granada #RPiweather'
			
			tweetea(twit, photo)
			
			os.system("rm " + photo)
			
			print "Hecho! \nHasta dentro de 15 min..."
			time.sleep(900)
		
		except KeyboardInterrupt:
			print "Saliendo del programa..."
			print "Hasta la proxima!"
			break


if __name__ == '__main__':
	main()
