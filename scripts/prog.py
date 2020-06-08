###############################################
word = "This sentence has two lines.\nI wanna be a single line."
word_modified  = word.replace( "\n", "" )

print( word )
print( word_modified )
###############################################

###############################################
word = "This sentence has two lines.\nI wanna be stored in array."
word_modified  = word.split("\n")

print( word )
print( word_modified )
###############################################

###############################################
words = ["I am first line", "I am second line"]
words_modified = ", ".join( words )

print( words )
print( words_modified )
###############################################

###############################################
import re

word = " This sentence has a blank at the leading."
word_modified = re.sub( r'^\s+', "", word )

print( f"[{word}]" )
print( f"[{word_modified}]" )
###############################################

###############################################
import re

word = "This sentence has a blank at the ending. "
word_modified = re.sub( r'\s+$', "", word )

print( f"[{word}]" )
print( f"[{word_modified}]" )
###############################################

###############################################
import re

word = " This sentence has blanks at the leading and ending. "
word_modified = re.sub( r'^\s+|\s+$', "", word )

print( f"[{word}]" )
print( f"[{word_modified}]" )
###############################################


###############################################
arr = list( open("./data1.csv", "r") )
print( arr )
###############################################

###############################################
word = "I am a sentence."
print( word )
open( "./data2.csv", "w" ).write( word+"\n" )
###############################################

###############################################
import re

arr = [[re.sub( r'^\s+|\s+$', "", d ) for d in data.replace("\n","").split(",")] for data in open("./data1.csv","r")]
arr_modified = "\n".join([", ".join( data ) for data in arr])

print( arr )
print( arr_modified )

open("./data3.csv","w").write( arr_modified+"\n" )
###############################################