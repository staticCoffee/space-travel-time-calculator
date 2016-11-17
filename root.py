newHorizons = 36000
light = 670616629

planets = {
    'mercury': 35000000, 'venus': 67000000, 'earth': 93000000,
    'mars': 142000000, 'jupiter': 484000000, 'saturn': 889000000,
    'uranus': 1790000000, 'neptune': 2800000000
    }

def calculateDistance(planet):
    distance = planets[planet]
    probeSpeed = float(newHorizons)
    lightSpeed = float(light)

    hourTime = distance / probeSpeed

    lightHourTime = distance / lightSpeed
    minTime = lightHourTime * 60

    return hourTime, minTime

def main():
    print 'Space Travel Time Calculator'
    print

    print 'Speed of New Horizon Probe: ~36,000 mph.'
    print 'Speed of Light: ~670,616,629 mph.'
    print

    for k in planets:
        print k.title()
    print
    inp = raw_input('Which planet would you like to travel to?: ').lower()
    while inp not in planets.keys():
        print 'Not a valid planet.'
        inp = raw_input('Which planet would you like to travel to?: ').lower()

    hourTime, minTime = calculateDistance(inp)

    print '''
If you were travelling in the New Horizons probe, it would take you {} hours to
reach {}. If you were travelling at the speed of light, it would only take {} minutes.
'''.format(hourTime, inp, minTime)

    print
    inp = raw_input('Press [Y] to travel to a different planet, or [N] to exit. ').lower()
    if inp == 'y':
        os.system('cls')
        os.system('clear')
        main()

    else:
        return
