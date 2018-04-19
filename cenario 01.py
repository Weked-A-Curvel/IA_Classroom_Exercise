from Player import Logic
import Edubot

options = {
    'screenSize': {
        'width': 1200,
        'height': 500
    },
    'gameVelocity': 5,
    'enemies': ['StaticFire'],
    'enemiesCount': 50,
    'maxItems': 0,
    'matrixSquares': {
        'x': 10,
        'y': 10
    },
    'usingTarget': False,
    'usingSensors': {
        'vision': True,
        'temperature': False,
        'target': False
    },
    'endGame': {
        'type': 'rounds', # 'rounds' or 'life'
        'params': [100] # array of params
    }
}

logic = Logic.Logic()
Edubot.run(logic, options)
