
from utils import readinput

lines = readinput()

OUTCOMES = {
    'A': {  # they play rock
        'X': None,  # rock (draw)
        'Y': True,  # paper
        'Z': False,  # scissors
    },
    'B': {  # paper
        'X': False,
        'Y': None,  # paper (draw)
        'Z': True,
    },
    'C': {  # scissors
        'X': True,
        'Y': False,
        'Z': None,  # scissors (draw)
    },
}


def part1():
    total_score = 0
    for game in lines:
        opponent_move, your_move = game.split()
        iwin = OUTCOMES[opponent_move][your_move]
        score = 0
        if your_move == 'X':
            score = 1
        elif your_move == 'Y':
            score = 2
        elif your_move == 'Z':
            score = 3

        if iwin is None:
            score += 3
        elif iwin:
            score += 6

        total_score += score

    return total_score


DESIRED_OUTCOMES = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
}

OUTCOMES2 = {
    'A': {  # they play rock
        'lose': 'scissor',
        'draw': 'rock',
        'win': 'paper',
    },
    'B': {  # they play paper
        'lose': 'rock',
        'draw': 'paper',
        'win': 'scissor',
    },
    'C': {  # they play scissor
        'lose': 'paper',
        'draw': 'scissor',
        'win': 'rock',
    },
}

def part2():
    total_score = 0
    for game in lines:
        opponent_move, desired_outcome = game.split()
        desired_outcome = DESIRED_OUTCOMES[desired_outcome]
        your_move = OUTCOMES2[opponent_move][desired_outcome]
        score = 0
        if your_move == 'rock':
            score = 1
        elif your_move == 'paper':
            score = 2
        elif your_move == 'scissor':
            score = 3

        if desired_outcome == 'draw':
            score += 3
        elif desired_outcome == 'win':
            score += 6

        total_score += score

    return total_score


print(part1())
print(part2())
