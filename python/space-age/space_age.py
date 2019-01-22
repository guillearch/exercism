class SpaceAge(object):

    EARTH_YEAR = 31557600

    ORBITAL_PERIODS = {'earth':1,
                       'mercury':.2408467,
                       'venus':.61519726,
                       'mars':1.8808158,
                       'jupiter':11.862615,
                       'saturn':29.447498,
                       'uranus':84.016846,
                       'neptune':164.79132
                       }

    def __init__(self, seconds):
        self.seconds = seconds
        self.years = seconds/self.EARTH_YEAR
        for planet in self.ORBITAL_PERIODS:
            setattr(self, "on_" + planet, self.conversion(planet))

    def conversion(self, planet):
        return lambda: round(self.years/self.ORBITAL_PERIODS[planet] ,2)
