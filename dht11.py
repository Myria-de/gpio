import Python_DHT
sensor = Python_DHT.DHT11
pin = 4
feuchtigkeit, temperatur = Python_DHT.read_retry(sensor, pin)
print('Temperatur = '+str(temperatur) + 'C Feuchtigkeit = '+str( feuchtigkeit)+'%')