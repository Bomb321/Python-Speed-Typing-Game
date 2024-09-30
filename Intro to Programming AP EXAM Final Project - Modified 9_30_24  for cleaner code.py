import random
import time

# A sample list of 50 random 5-letter words
words_list = [
    "apple", "grape", "pearl", "brick", "spoon", "flame", "beach", "tiger", "train", "piano", 
    "table", "chair", "plant", "sound", "stone", "brain", "track", "sheep", "horse", "light", 
    "flock", "movie", "clock", "ocean", "place", "heart", "snake", "climb", "party", "alarm", 
    "shirt", "drink", "glass", "mouse", "lunch", "bread", "cloud", "field", "river", "house", 
    "plant", "punch", "smile", "brick", "flute", "curve", "stand", "grill", "flash", "pouch",
    "white", "black", "green", "pizza", "salad", "treat", "great", "right", "wrong", "loved",
    "guess", "joint", "human", "giant", "small", "happy", "sadly", "scary", "music", "brave", 
    "sunny", "storm", "drink", "teach", "group", "fight", "laugh", "round", "steal", "trust",
    "lucky", "stone", "rider", "loose", "tight", "bread", "shout", "clear", "drive", "quiet",
    "first", "flame", "grape", "apple", "slice", "table", "brick", "broom", "flute", "grill", 
    "grove", "horse", "quick", "trace", "alarm", "climb", "brick", "smile", "curve", "laugh",
    "piano", "brain", "heart", "grass", "light", "river", "ocean", "sheep", "stone", "place"]

def speed_typing_game():
    print("Welcome to the Speed Typing Game!")
    num_words = 10  # Number of words to type in one round
    correct_words = 0
    total_time = 0

    for i in range(num_words):
        word_to_type = random.choice(words_list)
        print(f"Word {i + 1}: {word_to_type}")
        
        start_time = time.time()
        user_input = input("Type the word: ")
        end_time = time.time()

        time_taken = end_time - start_time
        total_time += time_taken

        if user_input == word_to_type:
            print(f"Correct! Time taken: {time_taken:.2f} seconds.\n")
            correct_words += 1
        else:
            print(f"Incorrect! The correct word was '{word_to_type}'. Time taken: {time_taken:.2f} seconds.\n")
    
    average_time = total_time / num_words
    accuracy = (correct_words / num_words) * 100

    print(f"Game Over!\nYou typed {correct_words}/{num_words} words correctly.")
    print(f"Your average time per word: {average_time:.2f} seconds.")
    print(f"Your accuracy: {accuracy:.2f}%.")

if __name__ == "__main__":
    speed_typing_game()
