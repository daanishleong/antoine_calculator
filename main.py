#Used to calculate out vapor_pressure, composition, dew & bubble points + plot out a t-xy/p-xy graph
from Thermo.Antoine_Calculator import unique_vapor_pressure, vapor_pressure
from Thermo.composition import x_composition_raoults, y_composition_raoults
from Thermo.DewBubble import dew_pressure, bubble_pressure

def main():
    print('What do you need help calculating? (options 1-5): ')
    print('1. Vapor pressure')
    print('2. Liquid composition')
    print('3. Vapor composition')
    print('4. Dew pressure')
    print('5. Bubble pressure')
    query = input('Please enter an option: ')
    if query == '1':
        speciesA = input('Enter species A: ')
        speciesB = input('Enter species B: ')
        temp = float(input('Enter a temperature(°C): '))
        return print(f'The specific vapor pressure are: {vapor_pressure(speciesA, speciesB, temp)}')
    elif query == '2':
        pressure = float(input('Enter a pressure(kPa): '))
        temp = float(input('Enter a temperature(°C): '))
        speciesA = input('Enter species A: ')
        speciesB = input('Enter species B: ')
        return print(f'The liquid composition for A is: {x_composition_raoults(pressure, temp, speciesA, speciesB)} and for B: {1 - x_composition_raoults(pressure, temp, speciesA, speciesB)}')
    elif query == '3':
        pressure = float(input('Enter a pressure(kPa): '))
        temp = float(input('Enter a temperature(°C): '))
        speciesA = input('Enter species A: ')
        speciesB = input('Enter species B: ')
        return print(f'The liquid composition for A is: {y_composition_raoults(pressure, temp, speciesA, speciesB)} and for B: {1 - y_composition_raoults(pressure, temp, speciesA, speciesB)}')
    elif query == '4' or '5':
        temp = float(input('Enter a temperature(°C): '))
        speciesA = input('Enter species A: ')
        speciesB = input('Enter species B: ')
        compA = float(input('Enter known mixture composition(A): '))
        compB = float(input('Enter known mixture composition(B): '))
        return print(f'The bubble pressure is {bubble_pressure(temp, speciesA, speciesB, compA, compB)}kPa and the dew pressure is {dew_pressure(temp, speciesA, speciesB, compA, compB)}kPa')
    else:
        print('That is not a valid query.')

main()