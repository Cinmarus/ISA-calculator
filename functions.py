def print_menu():
    print("*** ISA calculator ***\n")
    print("1. Calculate ISA for altitude in meters")
    print("2. Calculate ISA for altitude in feet")
    print("3. Calculate ISA for altitude in FL")
    # print("4. Calculate altitude for given pressure")
    # print("5. Calculate altitude for given density")

def get_temperature():
    while True:
        temperature_input = input("Set sea-level temperature (default 288.15 K): ").strip()
        if temperature_input:
            try:
                temperature = float(temperature_input)
                if temperature > 0:
                    return temperature
                else:
                    print("Please enter a temperature greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a valid floating-point number.")
        else:
            return 288.15  # Default temperature

def get_pressure():
    while True:
        pressure_input = input("Set sea-level pressure (default 101325 Pa): ").strip()
        if pressure_input:
            try:
                pressure = float(pressure_input)
                if pressure > 0:
                    return pressure
                else:
                    print("Please enter a pressure grater then 0.")
            except ValueError:
                print("Invalid input. Please enter a valid floating-point number.")
        else:
            return 101325  # Default pressure

def get_alttitude(mode):
    while True:
        altitude_input = input("You have choose the unit mode correctly, now enter altitude: ").strip()
        if altitude_input:
            try:
                altitude = float(altitude_input)
                altitude_meters = altitude * altitude_factors[mode]
                if 86000 >= altitude_meters > 0:
                    return altitude_meters
                else:
                    print("Please enter a altitude grater then 0 or in atmosphere range.")
            except ValueError:
                print("Invalid input. Please enter a valid floating-point number.")
def get_user_input():
    print_menu()
    while True:
        try:
            mode = input("Select mode: ")
            if mode in altitude_factors:
                altitude = get_alttitude(mode)
                return altitude
            else:
                print("wal się na łep")
        except ValueError:
            print("to nie liczba cepie")

def calculate_temperature(altitude_m, base_temp, base_pressure):
    pressure = base_pressure
    temperature = base_temp

    for layer in range(len(base_altitudes)):
        if altitude_m < base_altitudes[layer]:
            break
        if altitude_m > base_altitudes[layer+1]:
            delta_altitute = base_altitudes[layer+1] - base_altitudes[layer]
        else:
            delta_altitute = altitude_m - base_altitudes[layer]

        if lapse_rates[layer] != 0:
            temperature_1 = temperature + lapse_rates[layer] * delta_altitute
            pressure *= (temperature / temperature_1) ** ( g / (lapse_rates[layer] * R))
            temperature = temperature_1
        else:
            pressure *= 2.71828 ** (-g / (R * temperature) * delta_altitute)
    rho = pressure / (R * temperature)
    return temperature, pressure, rho

def run():
    base_temp = get_temperature()
    base_pressure = get_pressure()
    altitude_m = get_user_input()
    temperature, pressure, rho = calculate_temperature(altitude_m, base_temp, base_pressure)
    print(f"Temperature at {altitude_m} is {temperature}, and pressure is {pressure}, and density is {rho}")

# Constants
g = 9.80665
R = 287.05
base_altitudes = [0, 11000, 20000, 32000, 47000, 51000, 71000, 86000]
lapse_rates = [-0.0065, 0, 0.001, 0.0028, 0, -0.0028, -0.002, 0]
altitude_factors = {"1": 1, "2": 0.3048, "3": 30.48}