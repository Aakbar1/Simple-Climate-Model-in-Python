import math
import matplotlib.pyplot as plt
import numpy as np
import EBMStatistics as EBM

""" 

    # Power_emitted = 4π * R^2 * σ * T^4
    # Solar irradiance = (power_emitted)/(Area)
    # Area = 4 * pi * (d)^2


    For the sun:
    r = 7.0 * (10**8)m 
    d = 150 * (10**9)m distance of sun from earth.
    star_surface_temperature = 5778K
    Average Albedo value of the Earth is: 
    """

class Star:

    def __init__(self, distance_from_planet, radius, star_surface_temperature ):
            self.distance_from_planet = distance_from_planet
            self.radius = radius
            self.star_surface_temperature = star_surface_temperature

            self.Stefan_Boltzman_constant = 5.6704*(10**-8)
            self.power_emmitted  = 4 * math.pi * (radius**2) * self.Stefan_Boltzman_constant * (star_surface_temperature**4) #[W]
            self.solar_irradiance  = self.power_emmitted/(4 * math.pi * (distance_from_planet**2)) # [Wm^-2]
            

 


class Planet: 

    def __init__(self, albedo, radius, solar_irradiance, B, T, CO2_forcing_coefficient, preindustrial_CO2, preindustrial_temperature, preindustrial_year, C):
        self.Temperatures = []
        self.Temperatures.append(T)
        self.Intervals = []
        self.Intervals.append(preindustrial_year)
        self.CO2_concentrations = []
        self.CO2_concentrations.append(preindustrial_CO2)

        self.solar_irradiance = solar_irradiance
        self.albedo = albedo
        self.radius = radius
        self.area = 4 * (math.pi) * ((radius)**2)
        self.preindustrial_temperature = preindustrial_temperature # 14

        
        self.B = B # B = Climate feedback parameter(helps stabilize temperature)
        self.T = T # Surface Temperature
        self.A = (self.solar_irradiance * (1-self.albedo))/4 + (B * self.preindustrial_temperature) # A = Pre-Industrial Radiation  

        self.CO2_forcing_coefficient = CO2_forcing_coefficient # CO2 forcing coeffecient
        self.preindustrial_CO2 = preindustrial_CO2 # [Parts per Million]
        self.preindustrial_year = preindustrial_year # Year prior to CO2 emissions

        self.C = C #Average Specific Heat Capacity of Earth
 

        
        




def abs_solar_radiation(solar_irradiance, albedo) -> float: #distance_from_planet, radius, star_surface_temperature
    absorbed_solar_radiation = solar_irradiance * (1 - albedo)
    return absorbed_solar_radiation/4 # [W/m^2]

def outgoing_thermal_radiation(T, A, B):
    return A - B*T

def greenhouse_effect(Current_CO2, CO2_Coefficent, Pre_industrial_CO2):
    """"
    a = 5.0 as it is the CO2 forcing coefficient [wm^-2]
    Pre_industrial_CO2  = 280 [Parts per million]
    """
    return CO2_Coefficent * math.log(Current_CO2/Pre_industrial_CO2)

def CO2_functional_increase(pre_industrial_CO2, year, preindustrial_year):
    return (pre_industrial_CO2 * (1 + (((year - preindustrial_year)/220)**3)))

def change_in_temp(Planet, change_in_time):
    return ((change_in_time/Planet.C) * (
      
      abs_solar_radiation(Planet.solar_irradiance, 
                          Planet.albedo) 


    - outgoing_thermal_radiation(Planet.Temperatures[len(Planet.Temperatures) - 1], 
                                 Planet.A, 
                                 Planet.B)  


    + greenhouse_effect(
        CO2_functional_increase(Planet.preindustrial_CO2, Planet.Intervals[len(Planet.Intervals) - 1], Planet.preindustrial_year),
        Planet.CO2_forcing_coefficient, 
        Planet.preindustrial_CO2)
    ))

def timestep(Planet):
    Planet.Temperatures.append((Planet.Temperatures[len(Planet.Temperatures)-1]) + change_in_temp(Planet, 1))
    Planet.Intervals.append((Planet.Intervals[len(Planet.Intervals) - 1]) + 1)
    Planet.CO2_concentrations.append(CO2_functional_increase(Planet.preindustrial_CO2, Planet.Intervals[len(Planet.Intervals) - 1], Planet.preindustrial_year))

def run_model(Year, Planet):
        for i in range(Year - (Planet.preindustrial_year)):
            timestep(Planet)
        print(Planet.Intervals)
        print(Planet.Temperatures)
 


Sun = Star((150 * (10**9)),(7.0 * (10**8)), (5778) ) # Star()
Earth = Planet(0.3, 7.0 * (10**8), Sun.solar_irradiance, -1.3, 14, 5, 280, 14, 1850, 51)
print(Sun.solar_irradiance)

run_model(2023, Earth)
EBM.Statistics.display_Temperature_Time_Graph(Earth)
EBM.Statistics.display_CO2_Time_Graph(Earth)

