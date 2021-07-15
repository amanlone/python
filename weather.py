
import pyowm
def report(country):
        owm = pyowm.OWM("1c3938cd971b64b8e3d796d59deb4cbb")
        mgr = owm.weather_manager()
        #country = input("Enter a country or a city\n")
        observation = mgr.weather_at_place(country)
        weth = observation.weather
        temp = weth.temperature("celsius")
        status = weth.detailed_status

        print(int(temp["temp"]))
        print(status)
country = ["Malaysia", "Germany", "United Kingdom"]
#report()
#while True:
    #leave = input("Would you like to find weather forecast for another country? (y/n)\n")
    #if leave == "n":
     #   report()

    #else:
     #   exit()
for i in country:
    print(i)
    report(i)
