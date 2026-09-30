# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 22:01:01 2026

@author: Pammie Lynn
"""
import string
import unicodedata


# Open the file in read mode
file1 = open("words.txt", "r")
file2 = open("sample.txt", "r", encoding='utf-8-sig')
outputFile = open("output.txt", "a")

outputFile2 = open("words1.txt", "w")

# Remove punctuation
#translator = str.maketrans('', '', string.punctuation)


def remove_punctuation(text):      				
    return ''.join(						
        ch for ch in text					
        if not unicodedata.category(ch).startswith('P')		
    )


basic_words = []
new_words = set()

# Read the entire content of the file
for line in file2:
    line = line.strip()
    # Remove punctuation
    line = remove_punctuation(line)
    #line = line.translate(translator)
    line = line.lower()
    
    words = line.split()
    basic_words.extend(words)
    #basic_words.append(line)


word_set = set(basic_words)



# for i in word_set:
#     #outputFile2.write(i + "\n")
#     print(i)




# for line in file2:
#     new_line = line.split(' ')
    
    

# for i in new_line:
#     # Remove punctuation
#     i = i.translate(translator)
#     i = i.lower()
    
#     if i not in word_set:
#         new_words.add(i)
#         #print(i)
        

# for i in new_words:
#     outputFile.write(i + "\n")


print(word_set)
        

#print(new_words)





# Close the file
#file1.close()
file2.close()
outputFile.close()
outputFile2.close()
