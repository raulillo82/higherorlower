from art import logo, vs
from game_data import data
from random import sample, choice
from os import system

def clear():
    """Clear the screen in unix-like systems
    """
    system('clear')

def dict_to_string(dict):
    """Returns a human readable friendly string version of 'dict'"""
    return (dict["name"] + ", a(n) " + dict["description"] + ", from " +
dict["country"] + ".")

def print_question(options):
    """Print each of the two expected questions in the list given by
    'options'"""
    print(f"Compare A: {dict_to_string(options[0])}")
    print(vs)
    print(f"Against B: {dict_to_string(options[1])}")

def get_answer(question, a, b):
    """Returns the answer to 'question' between two possible answers, 'a' and
    'b'. Loops till the answer is one of the two values. Uses lowercases"""
    answer = ""
    while answer != a.lower() and answer != b.lower():
        answer = input(question).lower()
    return answer

def answer_is_right(options, answer):
    """Checks whether 'answer' is correct or not within the two values of the
    expected list from 'options'. 'answer' should be either 'a' (first) or 'b'
    (second)"""
    if answer == "a":
        if options[0]["follower_count"] > options[1]["follower_count"]:
            is_correct = True
        else:
            is_correct = False
    elif answer == "b":
        if options[1]["follower_count"] > options[0]["follower_count"]:
            is_correct = True
        else:
            is_correct = False
    return is_correct

def play():
    """Function with the game flow, looped for continuos play if desired"""
    play_again = True
    #right_answer = True
    score = 0
    while play_again:# and right_answer:
        clear()
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}")
            removed_item = options.pop(0)
            new_item = removed_item.copy()
            while new_item == removed_item:
                new_item = choice(data).copy()
            options.append(new_item)
        else:
            options = sample(data, k = 2)
        print_question(options)
        answer = get_answer("Who has more followers? Type 'A' or 'B': ", "A",
        "B")
        if answer_is_right(options, answer):
            score += 1
        else:
            play_again = False
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            answer_play_again = get_answer("Play again? Type 'y' or 'n': ", "y", "n")
            if answer_play_again == "y":
                play_again = True
                score = 0
play()
