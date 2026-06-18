# Part 09

Topics Covered:

- What is a file?:
File is data stored in a storage device.

- Types of files:
1. Text file
2. Binary file

- Opening a file:
f = open("filename.txt", "mode"). Default mode is read mode. Apart from that we have w, a, +, rb, rt.

 - Reading a file:
Open the file in read mode. Read content using read(). Apart from read(), you can use readline()[reads one line at atime, and is a string] and readlines()[returns a list of lines in the file].

- Writing to a file:
Open the file either in write or append mode. Use f.write() to write the content.

- with statement:
This opens and closes the file automatically.

- Basic practice exercises:
1. Write a program to read the text from a given file ‘problem_01.txt’ and find out whether it contains the word 'twinkle'
2. The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'problem_02.txt' which is either blank or contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score
3. Write a program to generate multiplication tables from 2 to 20 and write it to the different files, and place them in a folder 'Tables'
4. A file contains a word 'Donkey' multiple times and you need to write a program which replaces this word with ###### by updating the same file
5. Repeat program 4 for a list of such words to be censored
6. Write a program to mine a log file and find out whether it contains 'python'
7. Write a program to find out the line number where python is present from ques 6
8. Write a program to make a copy of a text file 'problem_08.txt'
9. Write a program to find out whether a file is identical and matches the content of another file
10. Write a program to wipe out the content of a file using python
11. Write a python program to rename a file to 'problem_11.txt'

- Files added in order of the topics:
1. file.py
2. practice_set_09.py

Status: Completed
