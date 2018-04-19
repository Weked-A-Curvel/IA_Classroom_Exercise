from Player import Logic
import Edubot

options = {
    'screenSize': {
        'width': 1200,
        'height': 500
    },
    'gameVelocity': 4,
    'enemies': ['FullStaticFire'],
    'customPositions': [
            ['0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','!','0'],
            ['0','0','!','!','t','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','!','0','0'],
            ['0','0','0','!','0','!','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0'],
            ['0','!','0','0','0','0','0','0','!','0'],
            ['0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','x','0','0','0','0','0','0'],
        ],
    'enemiesCount': 4,
    'maxItems': 0,
    'matrixSquares': {
        'x': 10,
        'y': 10
    },
    'usingSensors': {
        'vision': False,
        'temperature': True,
        'target': True
    },
    'usingTarget': True,
    'endGame': {
        'type': 'target', # 'rounds', 'life', 'target'
        'params': [100] # array of params
    }
}

logic = Logic.Logic()
Edubot.run(logic, options)
