# Problem 1 -
print('''
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.
      ''')

# Problem 2 -
# Printing 5 table using REPL

# Problem 3 -
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

# Problem 4 -
import os
# Specifying the path
path = "/"
contents = os.listdir(path)
# Printing the directory contents
print("Directory contents:")
for item in contents:
    print(item)

# Problem 5 - 
# Adding comments