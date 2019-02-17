#from models import WeatherData, UserDataPoint

'''

allPoints = UserDataPoint.objects.all()
zeroPoints = UserDataPoint.objects.filter(feeling = 0)
print(zeroPoints)

'''

'''

tempDict = dict{}
for everyPoint in allPoints:
    feel = everyPoint.feeling
    real_temp = everyPoint.recordedWeather.apparent_temp
    tempDict[feel] = real_temp

#find Ave of temps
sumTemps = sum(list(tempDict.values()))
totalTemps = len(tempDict.values())
aveTemp = sumTemps/totalTemps

#input aveTemp
def find_closest_feeling(temperature :float): -> 'number 0 -4'
    for every_temp in tempDict:
        if temperature


'''

def find_closest_feeling(temperature :float):
    return 2