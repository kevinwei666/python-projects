"""
Asks the user for the temperature and wind speed and
gives them a wind chill temperature.  Rounds to two decimal places.

If the user enters a temperature or a wind speed for which the formula
is not applicable, give them a message that politely tells them why
it does not make sense to calculate wind chill (too hot and/or no wind).

Allows for input of float values but checks the user’s input.

"""

#Get user input
temp = input("Enter temperature: ")
wind_speed = input("Enter wind speed: ")

try:
    temp = float(temp)
    wind_speed = float(wind_speed)

    if (temp < 50 and wind_speed > 5):
        T = temp
        v = wind_speed

        #National Weather Service formula:
        Twc = 35.74 + (0.6215 * T) - (35.75 * (v ** 0.16)) + (0.4275 * T * (v ** 0.16))

        print("Feels like", round(Twc, 2))

    else:
        too_hot = ""
        no_wind = ""
        if (temp >= 50):
            too_hot = "Too hot"

        if (wind_speed <= 5):
            no_wind = "No wind"

        print(too_hot, no_wind)

except:
    print("Input is not valid")
    
