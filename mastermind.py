# mastermind
from itertools import product


BLACK_RESPONSE = 1
WHITE_RESPONSE = 0
NO_RESPONSE = -1


# CODE = [int(elem) for elem in input("Give me a code separating each element by a -: ").split("-")]
CODE = [0,1,2,5]
LENGTH_OF_CODE = len(CODE)
NUMBER_OF_COLOURS = int(max(CODE)) + 1

def get_feedback(guess, solution):
    whites = [WHITE_RESPONSE if guess_single in solution else NO_RESPONSE for guess_single in guess]
    blacks_and_whites = [BLACK_RESPONSE if guess[i] == solution[i] else whites[i] for i in range(LENGTH_OF_CODE)]
    return blacks_and_whites

def get_all_combinations():
    return [list(combination) for combination in list(product(list(range(0, NUMBER_OF_COLOURS)), repeat=LENGTH_OF_CODE))]

def update_remaining_combinations(previous_guess, previous_feedback, remaining_combinations):
    return list(filter(lambda combination: get_feedback(previous_guess, combination) == previous_feedback, remaining_combinations))

def solution(code=""):
    if len(code):
        CODE = code
        LENGTH_OF_CODE = len(CODE)
        NUMBER_OF_COLOURS = int(max(CODE)) + 1
    print(f"CODE = {CODE}")
    remaining_combinations = get_all_combinations()
    guess = [0]*(LENGTH_OF_CODE//2) + [1]*(LENGTH_OF_CODE - LENGTH_OF_CODE//2)
    remaining_combinations.remove(guess)
    tries = 0
    if guess == CODE:
        return 1
    while guess != CODE:
        previous_feedback = get_feedback(guess, CODE)
        tries += 1
        remaining_combinations = update_remaining_combinations(guess, previous_feedback, remaining_combinations)
        guess = remaining_combinations.pop(0)

    print(f"Solved {guess} in {tries} attempts")
    return tries

def benchmark():
    attempts = []
    for code in get_all_combinations():
        attempts.append(solution(code))
    print(sum(attempts))



print(benchmark())
print(NUMBER_OF_COLOURS)

