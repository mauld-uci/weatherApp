#weatherdata.py

class WeatherData:
    def __init__(self, feel: int, temperature: float, apparent: float, humidity: float ,
    precipitation: int, wind: float, cloud: int, sun:int , time:int ) -> None:
        self.feel = feel #[0-4]:freezing-burning; [-1]: is a weather check
        self.temperature = temperature
        self.apparent = apparent
        self.humidity = humidity
        self.precipitation = precipitation
        self.wind = wind
        self.cloud = cloud
        self.sun = sun
        self.time = time

    def __str__(self):
        return 'feel: ' + feel + ', temperature: ' + temperature + ', feels_like: ' + feels_like + ', humidity: ' + humidity + ', precipitation: ' + precipitation + ', wind speed: ' + wind + ', cloud coverage: ' + ', sun position: ' + ', time (min): ' + time
