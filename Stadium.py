class Stadium:
    security_at_the_stadium = "Safely"

    def __init__(self, number_of_spectators=None, name_stadium=None, lighting_power_in_suites=None,
                 year_building=None, country=None, price=None):
        self.number_of_spectators = number_of_spectators
        self.name_stadium = name_stadium
        self.lighting_power_in_suites = lighting_power_in_suites
        self.year_building = year_building
        self.country = country
        self.price = price

    def __str__(self):
        print("\nNumber_of_spectators =", self.number_of_spectators,
              "\nName:", self.name_stadium,
              "\nLighting power (in suites) =", self.lighting_power_in_suites,
              "\nYear_building =", self.year_building,
              "\nCountry:", self.country,
              "\nPrice =", self.price, "\n")

    @staticmethod
    def security():
        print("Level of security at the stadium =", Stadium.security_at_the_stadium)

    def __del__(self):
        pass
