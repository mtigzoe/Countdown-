#Upload a transcript and count characters.
import sys 
import io

input_file = input("Type your file name: ")

file = open(input_file,"r")

count_characters= file.read()
count_characters.replace(" ","")

characters = len(count_characters)
print(characters, "characters")
words = count_characters.split()
print(len(words), "words")

file.close()