#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
#
#	Autor:	Adrian Martinez
#	GitHub: https://github.com/ame97
#
"""

import Adafruit_BMP.BMP085 as BMP 
import Adafruit_DHT as DHT
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
	
def tweetea(text, pic):
	CONSUMER_KEY = ''		# Refill with your own twitter API keys
	CONSUMER_SECRET = ''		#
	ACCESS_KEY = ''			#
	ACCESS_SECRET = ''		#
	
	auth = tweepy.OauthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	
	x = tweepy.API(auth)
	x.update_with_media(pic, text)
	
def camera():
	path = "/Path to the folder where you want to temporarily save the photo/" + time.strftime("%d-%m-%Y_%X") + ".jpg"
	os.system("fswebcam -d /dev/video0 -r 640x480 --no-banner " + path)
	
	return path
	
def main():
	#Obtaining data
	hum, temp = sensorDHT()
	press, alt = sensorBMP()
			
	#Taking the picture
	pic = camera()
			
	#Build tweet
	twit = 'Temperature= {0:0.2f} ºC'.format(temp) + '\Humidity= {0:0.2f} %'.format(hum)\
			+ '\nPressure= {0:0.2f} hPa'.format(press) + '\nAltitude= {0:0.2f} m'.format(alt)\
			+ '\n#RPiWeather'
		
	#Send tweet
	tweetea(twit, pic)
		
	#Remove the picture
	os.system("rm " + pic)


if __name__ == '__main__':
	main()
