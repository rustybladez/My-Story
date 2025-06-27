import random

def play():

    print("Okay. Here are the rules. Paper beats Lasers. Laser beats Rock. Rock beats Paper.")
    print("Using invalid moves mean your opponent gets a point.")
    print("Sorry. My game, my rules!")
    print("How many rounds do you wanna play?")

    while True:
        try:
            game_rounds = int(input(">>> "))
            break
        except ValueError:
            print("Please enter a valid number.")

    print()


    moves = ['Rock', 'Paper', 'Lasers']

    my_score, player_score = 0, 0

    rounds = 1

    while rounds <= game_rounds:

        print(f"Round {rounds}/{game_rounds}")
        print()
        rounds += 1

        my_move = random.choice(moves)

        print("Play your move: Rock, Paper, Lasers")
        print()
        player_move = input(">>> ").strip().lower()
        print()

        if player_move.capitalize() not in moves:
            print("Sorry. Wrong Move! I get a point as a penalty.")
            player_score += 1
        else:
            print(f"Rusty played {my_move}")
            print(f"You played {player_move.capitalize()}")
            print()

            if my_move == 'Rock' and player_move == 'paper' or my_move == 'Paper' and player_move == 'lasers' or my_move == 'Lasers' and player_move == 'rock':
                my_score += 1
                print(f"{my_move.capitalize()} beats {player_move.capitalize()}!")
                print()
                print("Rusty: Haha! I got you.")
                print("Rusty gets 1 point.")
                print()
                print("Current Score:")
                print(f"Rusty: {my_score}, You: {player_score}")
                print()

            elif player_move == 'rock' and my_move == 'Paper' or player_move == 'paper' and my_move == 'Lasers' or player_move == 'lasers' and my_move == 'Rock':
                player_score += 1
                print(f"{player_move.capitalize()} beats {my_move.capitalize()}!")
                print("Rusty: Oops! I wasn't concentrating. You got me.")
                print("You get 1 point.")
                print("Current Score:")
                print(f"Rusty: {my_score}, You: {player_score}")
                print()
            else:
                print("Rusty: Huh! We both have the same thinking process.")
                print("It's a draw. Nobody gets any points.")
                print("Current Score:")
                print(f"Rusty: {my_score}, You: {player_score}")
                print()

    print("Final Score:")
    print(f"Rusty: {my_score}, You: {player_score}")

    if my_score > player_score:
        print("Rusty Wins!")
        print("Rusty: Yep! Told you I'm unbeatable!")
    elif player_score > my_score:
        print("You Win!")
        print("Rusty: What! Can't be! What kind of sorcery did you use!")
        print("Haha! Just kidding. You're good at this! Congrats mate.")
    else:
        print("Rusty: Welp. I couldn't get you this time. But next time I sure will.")