letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#1 Using a list comprehension and zip, create a dictionary called letter_to_points that has the elements of letters as the keys and the elements of points as the values:
letter_to_points = {key:value for key, value in zip(letters, points)}

#2 Our letters list did not take into account blank tiles. Add an element to the letter_to_points dictionary that has a key of " " and a point value of 0
letter_to_points[" "] = 0
print(letter_to_points)

#3,4,5,6 We want to create a function that will take in a word and return how many points that word is worth. Define a function called score_word that takes in a parameter word:
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter.upper(), 0) # changes letters to uppercase and add 0 points if letter do not exist in dictionary
  return point_total

#7 Let's chceck if it works (should retunr 14 point because '!' is not in dict)
brownie_points = score_word("Browni!")
print(brownie_points)

word = input("Please type your word to count score points: ")
print("Your word's score is: " + str(score_word(word)))

# Bonus - let's input or own word in terminal and check its score:
word = input("Please type your word to count score points: ")
print("Your word's score is: " + str(score_word(word)))

# 9,10 Create a dictionary called player_to_words that maps players to a list of the words they have played. This table represents the data to transcribe into your dictionary:
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"],
                   "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
                   "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}

# 11 Iterate through the items in player_to_words. Call each player player and each list of words words. Within your loop, create a variable called player_points and set it to 0:
for player, words in player_to_words.items():
    player_points = 0

    # 11 Within the loop, create another loop that goes through each word in words and adds the value of score_word() with word as an input:
    for word in words:
        player_points += score_word(word)

        # 12 fter the inner loop ends, set the current player value to be a key of player_to_points, with a value of player_points
        player_to_points[player] = player_points

print(player_to_points)
