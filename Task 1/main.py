probability = float(input('Enter the percentage chance of rain (from 0 to 100): '))

if (probability < 0) or (probability > 100):
    print('Please, enter a value between 0 and 100')
    
else:
    probability = probability / 100

    print('On the scale from 0 to 10, where 0 - very bad, 5 - satisfactory, 10 - very good, estimate your state, when:')
    forest_raining = int(input('- it is raining and you are in the forest: '))
    home_raining = int(input('- it is raining and you are at home: '))
    forest_sunny = int(input('- it is sunny and you are in the forest: '))
    home_sunny = int(input('- it is sunny and you are at home: '))

    forest_efficiency = probability * forest_raining + (1 - probability) * forest_sunny
    home_efficiency = probability * home_raining + (1 - probability) * home_sunny
    
    print(f"Decision Efficiency (Forest): {forest_efficiency}")
    print(f"Decision Efficiency (Home): {home_efficiency}")

    if (forest_efficiency > home_efficiency):
        print('Decision to go to the forest has a higher efficiency.')

    elif (forest_efficiency < home_efficiency):
        print('Decision to stay at home has a higher efficiency.')

    else:
        print('Both decisions have the same efficiency.')
