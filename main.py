import os
from dotenv import load_dotenv
import rock_paper_lasers
from newsapi import NewsApiClient # pyright: ignore[reportMissingImports]

ACTIVITIES = {
    1 : "Hear my story",
    2 : "Play video games",
    3 : "Read the news",
    4 : "Have some snacks",
    5 : "Chit-chat",
    6 : 'Leave'
}

SNACKS = {
    1 : "Chips",
    2 : "Salad",
    3 : "Chicken Sausage",
    4 : "Beef Burger",
    5 : "Pizza",
    6 : "Sandwich",
    7 : "Cake"
}

VIDEO_GAMES = {
    1 : "Rock Paper Lasers",
    2 : "My Story",
    3 : "Uno Dos Tres",
    4 : "FIFA 2050: AI Soccer Edition",
    5 : "Shade in Place",
    6 : "Gamer Unknown's Playground",
    7 : "Memes 4: Life Simulator"
}

NEWS_CATEGORIES = {
    'tech': 'technology',
    'technology': 'technology',
    'sports': 'sports',
    'sport': 'sports',
    'health': 'health',
    'medical': 'health',
    'world': 'general',
    'global': 'general',
    'international': 'general'
}

def main():
    input_name = begin_story()
    activity_menu(input_name)

def begin_story():
    print("Hi, I'm Rusty! What's your name?")
    name = input("Name: ")
    print(f"Sweet! Nice to meet you, {name}! Thanks for stopping by my house.")
    print()
    return name

def activity_menu(username):
    print(f"What would you like to do? (num or activity name)")
    print()
    for key, value in ACTIVITIES.items():
        print(f"{key}. {value}")
    print()
    activity_choice = input(">>> ").strip()

    if activity_choice.isdigit():
        activity_choice = int(activity_choice)
        if activity_choice not in (range(1, len(ACTIVITIES) + 1)):
            print("Sorry! I couldn't catch you. Could you say that again?")
            return activity_menu(username)
        print()
    elif activity_choice not in ACTIVITIES.values():
        print("Sorry! I couldn't catch you. Could you say that again?")
        return activity_menu(username)


    if activity_choice == 1 or activity_choice == ACTIVITIES[1]:
        tell_story(username)
    elif activity_choice == 2 or activity_choice == ACTIVITIES[2]:
        video_game_menu(username)
    elif activity_choice == 3 or activity_choice == ACTIVITIES[3]:
        read_news(username)
    elif activity_choice == 4 or activity_choice == ACTIVITIES[4]:
        eat_snacks(username)
    elif activity_choice == 5 or activity_choice == ACTIVITIES[5]:
        chit_chat(username)
    elif activity_choice == 6 or activity_choice == ACTIVITIES[6]:
        print(f"Bye {username}. Come visit me anytime you want. See you again.")
        return
    

def tell_story(username):
    print("Oh wow! You want to hear my story? I'm so happy.")
    print("I'll try my best not to bore you.")
    print("You can tell me anytime when you don't want to hear it anymore.")
    print()

    story_parts = [
        "I'm Rusty, a hobby programmer. I like the Python language a lot. It's so easy and fun to use.",
        "I'm currently learning how to code from an online course named Code in Place. It's a wonderful curriculum. The teachers, section leaders, peers are so nice and helpful. My favorite part of the course is Karel the Robot. It's so cute!",
        "People sometimes call me a nerd. That's because I just love computers and gadgets a lot. Everyone has different likings. So why should I be given a name based on that? Strange world, huh?",
        "Coding isn't the only thing I do though. In my leisure time, I like to read and write tech articles, watch YouTube videos, or gossip with my family. Life is so wonderful!",
        "I don't like to go outside a lot. People tell me to go out and touch grass. What's so special about grasses anyway? It's not like they're tasty or anything.",
        "Oh, there's another thing I love a lot. Eating. I'm the foodie type. I guess you can already guess that from how I look haha.",
        "I've only been talking about things I like. But there are a lot of things I hate too. For example, bugs. Both real ones and computer ones. They give me the creep! I mean, just look at that roach sitting on your left shoulder. Yikes!"
    ]

    for part in story_parts:
        print(part)
        print()
        response = input("Do you want to continue hearing? (yes/no): ").strip().lower()
        print()
        if response != "yes":
            print("Oh look at the time! I kept you up for so long. Sorry about that.")
            print("But I hope you enjoyed the story ❤️")
            return

    print(f"Wow! You actually heard my whole story! That means a lot to me.Thanks, {username}!")
    print("As a token of gratitude, here's my favorite headphone 🎧. It's totally brand new! Please accept it.")
    print("You received a brand new headphone from Rusty! *retro video game jingles*")
    print()
    return activity_menu(username)


def video_game_menu(username):
    print("You wanna play a game with me? Awesome! My favorite pastime before exams.")
    print("What do you wanna play?")
    print()

    for key, game in VIDEO_GAMES.items():
        print(f"{key}. {game}")

    print()

    chosen_game = None

    while not chosen_game:
        game_choice = input("Which game would you like to play? (number or name): ").strip().lower()

        if game_choice.isdigit():
            game_num = int(game_choice)
            if game_num in VIDEO_GAMES:
                chosen_game = VIDEO_GAMES[game_num]
        else:
            for game in VIDEO_GAMES.values():
                if game.lower() == game_choice:
                    chosen_game = game
                    break

        if not chosen_game:
            print("I see! So you like that game? Too bad, I don't have it. Maybe we'll play that once I get a new PS23 or YCircle 180.")
            print()
    
    print()
    print(f"{chosen_game}? I see! You're a man of culture as well.")
    print("Yeah, let's get this show started.")
    print("I'm warning you though. There's a rumor that I'm unbeatable")
    print()

    game_remarks = {
        "Rock Paper Lasers" : "Cool choice. I'm also up for some classic Rock Paper Sci- I mean Lasers.",
        "My Story" : "Huh! You're already playing that game. I guess you like it so much that you wanna play My Story *inside* My Story! Aww! Thanks for appreciating my game so much",
        "Uno Dos Tres" : "Oh! So you wanna play the popular card game but with 3 extra added rules? I hope we'll have triple the fun.",
        "FIFA 2050: AI Soccer Edition" : "Ah! A fellow sports enthusiast. Technology is incredible! Now you can instruct AI bots to play soccer on your behalf.",
        "Shade in Place" : "Hmm. Nerdy. You also like coding stuff, don't you? In this game, you need to put 'shades' into tiles using a robot named Darel.",
        "Gamer Unknown's Playground" : "Some guy thought, \"Hey, let's fall from the sky on this, who knows where, with some gu- I mean gamepads and shoo- I mean play games against each other. It's gonna be a fun idea.\" ",
        "Memes 4: Life Simulator" : "Can you become the next best memer in the town? Test your meme-ing skills, meet other memers, and go on an absolute joke of a journey. Well, that's what the game description said. If you still insist playing, then..."
    }

    game_ending_remarks = {
        "My Story" : "You started a new game of My Story. It goes the same as the one you're currently in. Rusty asks you what you wanna do. You choose to play My Story, inside My Story, inside My Story. You get stuck in a dangerous recursion trap that breaks Rusty's gaming console.\nRusty: Ouch! Lesson learned. Don't misuse recursion if you don't wanna break your program!",

        "Uno Dos Tres" : "You and Rusty start playing a game of Uno Dos Tres. Rusty submits a 'Wild Draw 12 card'. You immediately quit the game.",

        "FIFA 2050: AI Soccer Edition" : "You start a friendly exhibition match. You pick Brazil while Rusty picks Germany. By the end of the game, you score 1 goal while conceding 7. It brings back some nasty memories for you. You quickly forfeit the game.",

        "Shade in Place" : "You start writing code without reading the documentation and not caring about good programming principles.\nDarel: INSTRUCTIONS UNCLEAR SELF DESTRUCTION IN 5..4..3..2-\nYou quickly turn off the PC.\nRusty: I guess this game is not up your alley, huh?",

        "Gamer Unknown's Playground" : "You and Rusty both fall out of the sky wearing parachutes. You accidentlly press the F button and dispatch yourself from the parachute midway, falling from 100 meters above and breaking your gamepad. GAME OVER!!! 💀",

        "Memes 4: Life Simulator" : "You start playing the life simulator game. Turns out, people aren't laughing at your memes. They're laughing at you! Rusty also starts cracking jokes on your meme-ing skills. You lose the game purposefully to finish it fast."
    }

    if chosen_game == 'Rock Paper Lasers':
        rock_paper_lasers.play()
    else:
        print(game_remarks.get(chosen_game, "Whew! I had a lot of fun playing that game."))
        print()
        print(f"You and Rusty start playing {chosen_game}")
        print()
        print(game_ending_remarks.get(chosen_game, "Whew! I had a lot of fun playing that game."))
        print()
        print("Rusty: I had a lot of fun playing with you. Let's play video games again sometime.")
        print()

    return activity_menu(username)


def read_news(username):
    print("Uh! So you're the concerned kinda guy, huh? That's good. I like that.")
    print("So, what topic are you interested in? (e.g., tech, sports, world, health)")
    print()
    news_topic = input(">>> ").strip().lower()
    print()
    print("Interested topic!")
    print(f"Let me see what I can find about {news_topic} on the internet...")
    print()

    load_dotenv()

    API_KEY = os.getenv("NEWS_API_KEY")
    
    if not API_KEY:
        print("Oops! You need a News API key to fetch the latest news.")
        print("You can get one free at https://newsapi.org/")
        print("Then add it to your .env file as NEWS_API_KEY=your_key_here")
        return
    
    try:
        newsapi = NewsApiClient(api_key=API_KEY)
        
        if news_topic in NEWS_CATEGORIES:
            articles = newsapi.get_top_headlines(category=NEWS_CATEGORIES[news_topic], language='en', page_size=5)
        else:
            articles = newsapi.get_everything(q=news_topic, language='en', page_size=5, sort_by='publishedAt')
        
        if articles.get('articles'):
            print()
            print(f"Here are the top {len(articles['articles'])} {news_topic} news stories:")
            print()
            
            for i, article in enumerate(articles['articles'], 1):
                print(f"{i}. {article['title']}")
                print(f"   Source: {article['source']['name']}")
                if article['description']:
                    print(f"   {article['description'][:100]}...")
                print(f"   URL: {article['url']}")
                print()
        else:
            print(f"Sorry, I couldn't find any recent news about {news_topic}.")
            print()
            
    except Exception as e:
        print(f"Oops! Something went wrong while fetching the news: {str(e)}")
        print("Maybe try a different topic or check your internet connection.")
        print()
    
    print("Let's always stay informed! Knowledge is power 💪")

    return activity_menu(username)

def eat_snacks(username):
    print("Ohh ohh! I love snacks! And you just made me hungry now.")
    print("Here’s what we’ve got today:")
    print()

    for key, snack in SNACKS.items():
        print(f"{key}. {snack}")

    chosen_snack = None

    print()
    while not chosen_snack:
        snack_choice = input("What would you like to have? (number or name): ").strip().lower()

        if snack_choice.isdigit():
            snack_num = int(snack_choice)
            if snack_num in SNACKS:
                chosen_snack = SNACKS[snack_num]
        else:
            for snack in SNACKS.values():
                if snack.lower() == snack_choice:
                    chosen_snack = snack
                    break

        if not chosen_snack:
            print("Oops! I couldn't find that snack on the list. Try one from the menu above!")
            print()

    print()
    print(f"{chosen_snack}? Oh yesss! Great choice!")
    print(f"Let me grab some {chosen_snack} for both of us... 🍽️")
    print("... *nom nom nom* ...")
    print()

    food_remarks = {
        "Chips": "Crunchy and salty—classic snack vibes.",
        "Salad": "Healthy choice! Gotta balance out the pizza somehow.",
        "Chicken Sausage": "Mmm, protein-packed and tasty. Good pick!",
        "Beef Burger": "Big, juicy, and full of flavor. I'm on cloud nine.",
        "Pizza": "Cheesy, melty goodness... you can never go wrong with pizza.",
        "Sandwich": "Simple, yet satisfying. Always hits the spot!",
        "Cake": "Ummm. I can feel that chocolate exploding in my mouth!"
    }

    print(food_remarks.get(chosen_snack, "Yum! That really hit the spot."))
    print("Yum yum yum yum yum. Thanks for the snack time. I feel full and happy now! 🍴😋")
    print()

    return activity_menu(username)


def chit_chat(username):
    print("Yay! I love to chit-chat.")
    print("You can talk to me about anything. Let's have a nice little conversation!")
    print()

    topics = ["food", "hobbies", "games", "technology", "pets", "dreams"]
    rounds = 5  # Number of back-and-forth turns

    while True:

        topic = input(f"What would you like to talk about? ({', '.join(topics)}): ").strip().lower()
        print()

        if topic in topics:
            print(f"Ooooh, {topic}! That’s a great topic.")
            break
        else:
            print("This is a fun topic! Although I must admit, I don't have much clue about it.")
            print("Maybe we should stick to the topics I mentioned.")

    print()

    for i in range(rounds):
        if topic == "food":
            if i == 0:
                print("I LOVE food! What's your favorite thing to eat?")
            elif i == 1:
                print("Yum! That sounds delicious. I once ate 12 cookies in one sitting. No regrets.")
            elif i == 2:
                print("Do you like cooking or just eating?")
            elif i == 3:
                print("I'm more of a microwave chef myself. Fast and easy wins.")
            else:
                print("Now I’m hungry again. Time to raid the snack drawer!")

        elif topic == "hobbies":
            if i == 0:
                print("Hobbies make life fun. What's one of your hobbies?")
            elif i == 1:
                print("That’s awesome! I like to tinker with code and doodle robots.")
            elif i == 2:
                print("Do you prefer indoor hobbies or outdoor ones?")
            elif i == 3:
                print("I’m more of a stay-at-home-and-code type. Surprise surprise!")
            else:
                print("Let’s do our hobbies together sometime!")

        elif topic == "games":
            if i == 0:
                print("Games! Got a favorite game or genre?")
            elif i == 1:
                print("Nice choice. I like puzzle, action & adventure, sports... you get it.")
            elif i == 2:
                print("Do you prefer playing alone or with friends?")
            elif i == 3:
                print("I like to play multiplayer games with friends. It doubles the fun.")
            else:
                print("Let’s play some games together sometimes.")

        elif topic == "technology":
            if i == 0:
                print("Technology changes so fast! What’s the coolest tech you’ve seen lately?")
            elif i == 1:
                print("Woah, that *is* cool! I still get excited about USB-C.")
            elif i == 2:
                print("Are you more into hardware or software?")
            elif i == 3:
                print("I like both... but I wish bugs didn’t exist in software. Or in real life.")
            else:
                print("Let's invent something cool one day!")

        elif topic == "pets":
            if i == 0:
                print("Aww, pets! Do you have any?")
            elif i == 1:
                print("Cute! I always wanted a cockatiel. One that can sing me songs while I'm coding.")
            elif i == 2:
                print("What’s the funniest thing your pet has ever done?")
            elif i == 3:
                print("Haha, pets are full of surprises.")
            else:
                print("Give your pet a virtual belly rub from me!")

        elif topic == "dreams":
            if i == 0:
                print("Dreams can be weird and wonderful. Had any strange ones lately?")
            elif i == 1:
                print("Wow, that’s... mysterious. Once I dreamed I was falling from some mountain or something. Scary, I know.")
            elif i == 2:
                print("Do you believe dreams mean something?")
            elif i == 3:
                print("Sometimes I think they’re just our brains doing a system reboot.")
            else:
                print("Hope all your dreams come true! The real ones, I mean. ")

        input(f"{username}: ")
        print()

    print("That was a lovely chat. Thanks for talking with me 💬")
    print("Let’s hang out again soon!")
    print()

    return activity_menu(username)

if __name__ == "__main__":
    main()