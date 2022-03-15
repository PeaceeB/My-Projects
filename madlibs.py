# madlib generator is a fun game where the user has to enter substitutes for
#blanks in the story without knowing the story.

# Example excercise - subscribe to youtube channel
# variable name = youtuber

#youtuber = "Peace Benson"
# method 1 : concaternate string with youtuber
#print("subscribe to " + youtuber)
# method 2 : use the curly brackets. We call the string.format() into youtuber
#this will put whatever the value of yotuber is into the curly brackets
#print("subscribe to {}".format(youtuber))
# method 2 : f string
#print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Gaming is so {adj}! It makes me so siked all the time \
I love to {verb1}. Stay loyal and {verb2} like you are {famous_person}!"

print(madlib)
