# Library imports
import argparse


# Temperature conversion formulas
def celsius_to_fahrenheit(temp):
    return (temp * 9 / 5) + 32


def celsius_to_kelvin(temp):
    return temp + 273.15


def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5 / 9


def fahrenheit_to_kelvin(temp):
    return celsius_to_kelvin(fahrenheit_to_celsius(temp))


def kelvin_to_celsius(temp):
    return temp - 273.15


def kelvin_to_fahrenheit(temp):
    return kelvin_to_celsius(celsius_to_fahrenheit(temp))


# Main function
if __name__ == '__main__':
    # Set arguments
    parser = argparse.ArgumentParser(prog='Thermometer')
    parser.add_argument('-t', '--temperature', type=float, required=True, dest='temp', metavar='Temperature', action='store', help='Specify a temperature to convert to other units.')
    parser.add_argument('-rt', '--room-temperature', type=float, nargs='?', default=20, dest='room', metavar='Room Temperature', action='store', help='Specify the current room temperature in the same units as the input. Default=20° Celsius')
    parser.add_argument('-v', '--verbose', action='store_true', help='Toggle verbosity.')

    # Add unit conversions
    conversions = parser.add_mutually_exclusive_group()
    conversions.add_argument('-cf', '--celsius-to-fahrenheit', action='store_false')
    conversions.add_argument('-ck', '--celsius-to-kelvin', action='store_true')
    conversions.add_argument('-fc', '--fahrenheit-to-celsius', action='store_true')
    conversions.add_argument('-fk', '--fahrenheit-to-kelvin', action='store_true')
    conversions.add_argument('-kc', '--kelvin-to-celsius', action='store_true')
    conversions.add_argument('-kf', '--kelvin-to-fahrenheit', action='store_true')

    # Parse arguments
    args = parser.parse_args()

    if args.celsius_to_fahrenheit:
        print(celsius_to_fahrenheit(args.temp))
    elif args.celsius_to_kelvin:
        print(celsius_to_kelvin(args.temp))
    elif args.fahrenheit_to_celsius:
        print(fahrenheit_to_celsius(args.temp))
    elif args.fahrenheit_to_kelvin:
        print(fahrenheit_to_kelvin(args.temp))
    elif args.kelvin_to_celsius:
        print(kelvin_to_celsius(args.temp))
    else:
        print(kelvin_to_fahrenheit(args.temp))

    # Check if room temperature is hot
    if args.verbose:
        if args.room > args.temp:
            print("Less than room temperature")
        else:
            print("Greater than or equal to room temperature")
