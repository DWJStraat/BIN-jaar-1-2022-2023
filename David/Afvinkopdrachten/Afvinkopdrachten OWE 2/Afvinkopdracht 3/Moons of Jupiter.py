def moon(name):
    """
    This function returns information about a moon of Jupiter.

    Parameters
    ----------
    name : string
        Name of the moon.

    Returns
    -------
    radius: float
        Radius of the moon in km.
    gravity: float
        Gravity of the moon in m/s^2.
    period: float
        Period of the moon in days.
    """
    radius = {"Io": 1821.6, "Europa": 1560.8, "Ganymedes": 2634.1,
              "Callisto": 2410.3}
    gravity = {"Io": 1.796, "Europa": 1.314, "Ganymedes": 1.428,
               "Callisto": 1.235}
    period = {"Io": 1.769, "Europa": 3.551, "Ganymedes": 7.154,
              "Callisto": 16.689}
    return radius[name], gravity[name], period[name]


def main():
    moon_name = input("Which moon do you want to know about? ")
    radius, gravity, period = moon(moon_name)
    print(f'Radius: {radius} km')
    print(f'Gravity: {gravity} m/s^2')
    print(f'Period: {period} days')


main()
