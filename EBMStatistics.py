import math
import matplotlib.pyplot as plt
import numpy as np

class Statistics :
    def __init__(self, Planet):
        self.Planet = Planet

    def display_Temperature_Time_Graph(Planet):
        xpoints = np.array(Planet.Intervals)
        ypoints = np.array(Planet.Temperatures)

        plt.plot(xpoints, ypoints)

        plt.xlabel("Time(Years)")
        plt.ylabel("Average Temperature ($^\circ$C )")
        plt.show()

    def display_CO2_Time_Graph(Planet):
        xpoints = np.array(Planet.Intervals)
        ypoints = np.array(Planet.CO2_concentrations)

        plt.plot(xpoints, ypoints)
        
        plt.xlabel("Time(Years)")
        plt.ylabel("Average CO2 Concentration")
        plt.show()