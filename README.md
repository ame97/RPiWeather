# RPiWeather
Weather station with Raspberry Pi

###INTRODUCTION
The station tweets every 15 minutes the temperature, humidity, pressure and altitude data recorded by the sensors and, in addition, upload a photo taken by a webcam. In order to read the temperature and humidity it uses the DHT11 sensor of Adafruit, next to lMBP180 for the atmospheric pressure and the altitude

###INSTALATION
Connect the sensors to the raspberry in the following or an equivalent way:

|  BMP180 |         |  DHT11  |         |
|---------|---------|---------|---------|
| Sensor  |Raspberry| Sensor  |Raspberry|
|  VIN    |  3V3    |  VIN    |  3V3    |
|  GND    |  GND    |  GND    |  GND    |
|  SCL    |  SCL    |  DATA   |  GPIO5  |
|  SDA    |  SDA    |

Once the sensors are connected to the Raspberry Pi we must make some adjustments to allow communication between the two parts. First, let's update the software using the following commands:
```bash
sudo apt-get update
sudo apt-get upgrade
```

Next, we will need to install the libraries to control the I2C interface, which we will do with the following command. In addition, we must activate the I2C interface, since it is disabled by default.
```bash
sudo apt-get install build-essential python-dev
```

Now, we have to install the libraries for the sensors and the camera (I used the P3 Eye):
```bash
sudo apt-get install git

git clone https://github.com/adafruit/Adafruit_Python_BMP.git 
cd Adafruit_Python_BMP
sudo python setup.py install

git clone https://github.com/adafruit/Adafruit_Python_DHT.git 
cd Adafruit_Python_DHT
sudo python setup.py install

sudo apt-get install fswebcam
```

Finally, execute this command:
```
git clone https://github.com/ame97/RPiWeather.git
```

###SCRIPT EXECUTION
To run the script every 15 minutes, we can use crontab. To do this, we will put the command
```bash
crontab -e
```
And we will add to the file this line:
```
15 * * * * /path_to_the_script/RPiWeather.py
```
