class ConversionUtility:

    @staticmethod
    def GramsPounds(float):
        us_weight = (float(gram_weight) * 0.002216)
        return ("{} lbs".format(us_weight))

    @staticmethod
    def MilesKilometres(float):
        kenya_distance = (float(miles) * 1.6)
        return ("{} km".format(kenya_distance))

    @staticmethod
    def LitresOZ(float):
        foreign_fluid = (float(litres) * 33.814)
        return("{} fl oz".format(foreign_fluid))

    @staticmethod
    def InchCentimetre(float):
        smaller_measurement = (float(inches) * 2.54)
        return("{} cm".format(smaller_measurement))

    @staticmethod
    def FarenheitCelsius(float):
        foreign_temperature = input("Temperature in Farenheit?:")
        normal_temperature = (float(foreign_temperature) *
                              (foreign_temperature - 32) * 0.5556)
        return("{} degrees celsius".format(normal_temperature))

gram_weight = input("What is the weight in grams?:")
print(ConversionUtility.GramsPounds(float))

miles = input("Distance in miles?: ")
print(ConversionUtility.MilesKilometres(float))

litres = input("Litre of milk?: ")
print(ConversionUtility.LitresOZ(float))

inches = input("Height in inches?:")
print(ConversionUtility.InchCentimetre(float))

inches = input("Height in inches?:")
print(ConversionUtility.FarenheitCelsius(float))

# Do reverse conversion.
