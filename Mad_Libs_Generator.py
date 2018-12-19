"""Takes random words that the user enters in and makes a silly story
out of the words the user gave."""

from numpy import random
game = True
print("Welcome to the Mad Libs Generator")

while game:

    # Created a dictionary to store more than one word for the game so the game can choose random words from the lists of word types to implement into the stories.

    game_words = {"singluar_noun": [], "adjective": [], "verb": []}

# This for loop enables the user to put in 5 words for each word type for each of the stories that will be randomly chosen. This way it will choose a random word from the stored list each time.

    for word_type, word_list in game_words.items():
        while len(word_list) < 5:
            word = input("Enter a {} : ".format(word_type))
            word_list.append(word)

# The variables, which include the names of the main subjects of the story, put each word of the user input into the sentence to display for the user. The format function is used for this to happen.

    david_story = "David had a {} that was very {} and it would always {} around.".format(random.choice(game_words["singluar_noun"]), random.choice(game_words["adjective"]), random.choice(game_words["verb"]))

    lucus_story = "Lucus went to the store and bought a {} that was {} and he was happy with it. When he was alone he would {} when no one was watching him.".format(random.choice(game_words["singluar_noun"]), random.choice(game_words["adjective"]), random.choice(game_words["verb"]))

    sams_story = "Sam was a kind person who always wanted a {} that was always {}. One day for his birthday his sister {} to the store and got him a {}. Sam  was overjoyed. ".format(random.choice(game_words["singluar_noun"]), random.choice(game_words["adjective"]), random.choice(game_words["verb"]), random.choice(game_words["singluar_noun"]))

    marys_story = "Mary wanted to get a puppy so she went to see a {}. After she did that she decided she wanted to see if the puppy was {}. The very next day Mary {} and got her puppy.".format(random.choice(game_words["singluar_noun"]), random.choice(game_words["adjective"]), random.choice(game_words["verb"]))
# The random_story vaiable will pick a random story to implement all the random words into.

    random_story = [david_story, lucus_story, sams_story]
    print('\n\n')

    print(random.choice(random_story))

    print('\n\n')

    play_again = input("Play Again?")

# This if statement is to give a proper end to the game or if the user wants to play again if gives the option to contiue the while loop and start everything over again.

    if play_again in ["Yes", "y", "yes"]:
        game = True
    else:
        print("Bye Bye!")
        game = False
