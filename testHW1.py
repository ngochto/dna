#Claire To
#10/29/2019
#testHW1.py

#Part1: Codons
'''This function takes a string as its argument and return a list containing
the string split up into three-letter words of the orginial string'''
def codons(string):
    if len(string)==3:
        return [string]
#This 'if' is used to return the list containing three-letter if the length
#of the string is 3. This is the base case.
    else:
        return [string[:3]]+ codons(string[3:])
#If the length of the string is not 3 (0 or 1 or 2), we take those characters,in
#the mean time, use recursion until the length of the string is 3, in order to
#form a new split three-letter word (codon.) We also assumed that the length of
#the provided string is divisible by 3 so recursion always occur to form codons
#(not stop when the length is 1 or 2.)

#Part2: Point Mutations
'''This function takes two equal-lenth strings representing two DNA sequences
and returns a list that has possible elements of 0 or 1 or an empty string.
If 2 strings have the same character, return a number 0 in the list. If 2 strings
do not have the same character, return a number 1 in the list. Go through every
character of the two string, when it reachs the end, return an empty string
in the list.'''
def pointMutationsHelper(string1,string2):
    if [string1]==[''] and [string2]==['']:
        return ['']
#I use an empty string to signify when the function has gone through all the
#character in the string1 and string2. Return a list containing an empty string
# at the end so the program will stop running after reaching the end of string1
#and string2. This is the base case.
    if string1[0]==string2[0]:
        return [0] + pointMutationsHelper(string1[1:],string2[1:])
#This 'if' happens when 2 strings have the same character. It returns an element
#of 0 in the final list. After that, use recursion of this function
#to check for the next character of 2 strings.
    else:
        return [1] + pointMutationsHelper(string1[1:],string2[1:])
#This happens when 2 strings do not have the same character. It returns an element
#of 1 in the final list. After that, use recursion of this function to check
#for the next character of 2 strings.



'''This function takes two equal-length strings representing two DNA sequences
as arguments and returns the number of the point muations between 2 strings.
This function basically is based on the pointMutationsHelper function,
how it works is it sums all of the elements (Ones and Zeros) in the list created
previously,excluding the empty string, to count for the point mutations.'''
def pointMutations(string1,string2):
    if pointMutationsHelper(string1,string2)=='':
        return ''
#This works as the base case, signifying when it reaches the end of the two
#strings, so the program will stop running.
    else:
        return sum(pointMutationsHelper(string1,string2)[:-2])
#This works as summing the Ones and Zeros in the list created after running the
#pointMutationsHelper function. I use [:-2] in the program to exclude the empty
#string at the end of the list.

#Part3: Transcription
'''This function takes a string representing a DNA template and returns the
transcribed RNA sequences.'''
def transcribe(string):
    if string=='':
        return ''
#This works as the base case. Using an empty string to signify the end of the
#string, in order for the program to stop running after reaching the end of the
#string.
    elif string[0]=='G':
        return 'C' + transcribe(string[1:])
#If the character of the string we're executing is 'G', return 'C' so as to
#replace 'G', then use recursion of the function transcribe to check to the
#next character of the string.
    elif string[0]=='C':
        return 'G' + transcribe(string[1:])
#If the character of the string we're executing is 'C', return 'G' so as to
#replace 'C', then use recursion of the function transcribe to check to the
#next character of the string.
    elif string[0]=='T':
        return 'A' + transcribe(string[1:])
#If the character of the string we're executing is 'T', return 'A' so as to
#replace 'T', then use recursion of the function transcribe to check to the
#next character of the string.
    elif string[0]=='A':
        return 'U' + transcribe(string[1:])
#If the character of the string we're executing is 'A', return 'U' so as to
#replace 'A', then use recursion of the function transcribe to check to the
#next character of the string.

#Part4: Pattern Matching
'''This function takes two argumetns, a string and a string containing only one
single character of the previous string and returns a list that has possible
elements of 0 or 1 or an empty string. If the character of the string matches
the single character, return a number 0 in the list. If the character of the
string does not match the single character, return a number 1 in the list.
Go through every character of the string, when it reachs the end, return an empty
string in the list.'''
def findHelper(string,single_character):
    if string=='':
        return ['']
#An empty string is used to signify when the function has gone through all the
#character in the string. Return a list containing an empty string in the end so
#the program will stop running after reaching the end of the string. This happens
#when no matching is found. This is the base case.
    elif string[0]==single_character:
        return [0]
#This happens when the single_character matches the element of the string.
#It returns a 0 element in the final list. And the program stops running after
#it has found the matching.
    elif string[0]!=single_character:
        return [1] + findHelper(string[1:],single_character)
#This happens when the single_character does not match the element of the string.
#It returns an 1 element in the final list. After that, use recursion to check to
#the next element of the string.



'''This function takes a string and a single character as its two arguments and
returns the index of a single character in the string.This function basically is
based on the findHelper function, how it works is it sums all of the elements
(Ones and Zeros) in the list created previously to find the index. If the list
created previously contains an empty string at the end, meaning that no matching
was found, returns -1'''
def find(string,single_character):
    if findHelper(string,single_character)[-1]=='':
        return -1
#This happens when the list created after using the findHelper function has
#an empty string at the end, meaning no matching was found. This returns -1.
    else:
        return sum(findHelper(string,single_character))
#If there's a match, this works to sum all of the elements (Ones and Zeros) in
#the list to return the index of the character in the string.



'''This function takes a short pattern and a long sequence as its two arguments
and returns a list of elements 1 or 0. If the short pattern does not appear in
the long sequence, return a element 1 on the list. If the short pattern appears
in the long sequence, return a element 0 on the list. If the programs runs untill
the end of the long sequence and the short pattern is not found in the long sequence,
returns an empty string.'''
def matchHelper(short_pattern,long_seq):
    if long_seq=='':
        return ['']
#An empty string is used to signify when the function has gone through all the
#characters in the long sequence and no short pattern is found in the long sequence.
#Return a list containing an empty string in the end so the program will stop
#running after reaching the end of the long sequence.
#This is the base case.
    elif short_pattern==long_seq[0:(len(short_pattern))]:
        return [0]
#This happens when the short pattern appears in the long sequence. It returns
#an element of 0 in the list. The program then stops running.
#I use long_seq[0:(len(short_pattern))] to look for patterns in the long sequence
#that has the same length as the short pattern.
    elif short_pattern!=long_seq[0:(len(short_pattern))]:
        return [1] + matchHelper(short_pattern,long_seq[1:])
#This happens when the short pattern has not appeared in the long sequence.
#It returns an element of 1 in the final list and use recursion to continue to check
#for the next character to see if the short pattern appears.
#I use long_seq[0:(len(short_pattern))] to look for patterns in the long sequence
#that has the same length as the short pattern.



'''This function takes a short pattern and a long sequence as its two elements
to return the index of the pattern's first occurrence in the sequence. This function
basically works based on the find function. How this works is it sums the elements
(Zeros and Ones of the list created after executing the matchHelper function to find the index.
If the list created previously contains an empty string at the end, meaning that no matching
was found, returns -1'''
def match(short_pattern,long_seq):
    if matchHelper(short_pattern,long_seq)[-1]=='':
        return -1
##This happens when the list created after using the matchHelper function has
#an empty string at the end, meaning no matching of the short pattern
#was found in the long sequence. This returns -1.
    else:
        return sum(matchHelper(short_pattern,long_seq))
#If there is a match, this works to sum all of the elements (Zeros and Ones) of
#the final list of matchHelper, to return the index if the pattern's first occurrence
#in the sequence.

#NOTE: MY CODE DOES NOT NEED THE 'FIND','FINDHELPER' FUNCTIONS TO RUN. I WANT TO INCLUDE IT
#HERE ANYWAY.
