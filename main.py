# Car types and their conditions
car_conditions = {
    'compact': {
        'fuel_efficiency': 'high',
        'space': 'compact',
        'power': 'low'
    },
    'sedan': {
        'fuel_efficiency': 'moderate',
        'space': 'moderate',
        'power': 'moderate'
    },
    'SUV': {
        'fuel_efficiency': 'low',
        'space': 'high',
        'power': 'high'
    },
    'sports': {
        'fuel_efficiency': 'moderate',
        'space': 'low',
        'power': 'very_high'
    },
    'hybrid': {
        'fuel_efficiency': 'very_high',
        'space': 'moderate',
        'power': 'moderate'
    }
}

# Questions
questions = {
    'fuel_efficiency': 'How important is fuel efficiency to you?',
    'space': 'How much space do you need?',
    'power': 'How important is high power for you?'
}

# Answers
answers = {
    'low': 'Low',
    'moderate': 'Moderate',
    'very_high': 'Very High',
    'compact': 'Compact',
    'high': 'High'
}

cars = {
    "compact": {
        "description": "Compact Car\nSmall and fuel-efficient, perfect for city driving."
    },
    "sedan": {
        "description": "Sedan\nA practical choice for families with a balance of space, fuel efficiency, and power."
    },
    "SUV": {
        "description": "SUV\nSpacious and powerful, ideal for off-road adventures and large families."
    },
    "sports": {
        "description": "Sports Car\nHigh-performance and stylish, best for those who love speed and handling."
    },
    "hybrid": {
        "description": "Hybrid Car\nEnvironmentally friendly and fuel-efficient, combining electric and gasoline power."
    }
}


def introduction():
    print('What type of car best suits your needs?')
    print()


# Ask a question
def ask(question, options):
    print(questions[question])
    for i, option in enumerate(options):
        print(f'{i + 1}. {answers[option]}')
    answer = input()
    while not answer.isdigit() or int(answer) < 1 or int(answer) > len(options):
        print('Invalid answer, please try again')
        answer = input()
    return options[int(answer) - 1]


def find_car():
    fuel_efficiency = ask('fuel_efficiency', ['low', 'moderate', 'high', 'very_high'])
    space = ask('space', ['compact', 'moderate', 'high'])
    power = ask('power', ['low', 'moderate', 'high', 'very_high'])

    car2score = {}
    for car, conditions in car_conditions.items():
        score = 0
        if conditions['fuel_efficiency'] == fuel_efficiency:
            score += 1
        if conditions['space'] == space:
            score += 1
        if conditions['power'] == power:
            score += 1
        car2score[car] = score

    best_score = max(car2score.values())
    return [car for car, score in car2score.items() if score == best_score][0]


def main():
    introduction()
    car = find_car()
    print(f"You should consider a {car}!")


if __name__ == "__main__":
    main()
