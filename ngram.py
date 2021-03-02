#####################################
# Basima Zafar
# NLP Program 2
# 03/02/21
# V00825375
#####################################

import sys
import re
from nltk.tokenize import sent_tokenize
import nltk
import random
nltk.download('punkt')


#################################################
# The purpose of this program was to allow the user to input the number of ngrams wanted, the number of sentences,
# and a random number of text files to be used
# This works by first finding the ngrams, then finding the frequency of those ngrams and then finding the probability of them occuring
# The probability of them occuring will then be comapred to a random value and if it is less than the random value it will return the word needed
# Ngrams are used for a large number of things, the most popular is auto completion 
# Note: This progam may take more than 5 minutes to run, but it does run! 
##################################################


################################################
#Method: punctuation_removal
# Prior to calculating ngrams, we have to remove the punctuation
# This works by first delcaring a range of punctuation, in the first for loop, if the punctuation is found in fileContent
# it will replace it with a ""
# In the second for loop, we search for an exclamation point and a question mark and then replace that with a period
# we return fileContents after 
################################################

def punctuation_removal(fileContents):
    punc='''()-[];:'"\,/@#$%-^&*_"“”~'''
    for p in fileContents:
        if p in punc:
            fileContents=fileContents.replace(p,"")
    exclamationPoint ='''!?'''
    for i in fileContents:
        if i in exclamationPoint:
            fileContents=fileContents.replace(i,".")
    return fileContents

##############################################
# Method: ngram_calcu
# This takes in the filecontents, and the number of grams wanting to create
# The first thing to do when calculating Ngrams is to remove the punctuation, so that is the first method called and we pass it the fileContents
# After the punctation is removed, we split it into parts based off the period and put it into a list
##############################################
def ngram_calc(fileContents, numGrams):
    #first you have to remove punctuation
    fileContents=punctuation_removal(fileContents)
  
    parts=[]
    parts = fileContents.split(".")
    #print(parts)



    ########################################################################
    # After we split it into parts, we add start and end tags for each i in parts
    # We have to make sure the first word has (n-1) <start> tags hence we multiply start by (numGrams -1) and add the end tag
    # Once we've added the tags, we append it to a list called sequences
    ####################################################################
    #adds start and end tags per sentance
    sequences=[]
    for tags in parts:
        tags = "<start> " * (numGrams-1) + tags + " <end>"
        sequences.append(tags)
    #print("Sequences: ", sequences)



    ##################################################
    # After the tags have been added, we have to split them into ngrams
    # This works by spliting each i in sequence by space and putting it into a list called spaced
    # Then using the length of the spaced list - numGrams+1 to collect the ngrams
    ##################################################
    
    spaced=[]
    finalSpaced=[]
    ngrams=[]
    for i in sequences:
        spaced = i.split()
        
        #print("spaced word: ", spaced)
        finalSpaced.append(spaced)

        for i in range(len(spaced)-numGrams+1):
            temp=[spaced[j] for j in range(i,i+numGrams)] #nested for loop so the value of range appends
            ngrams.append(" ".join(temp)) #add each value into ngrams list 
    #print("ngrams: ", ngrams)

    return ngrams

##############################################
# Method: freq
# Once we have calculated the ngrams, we have to count the frequency of each ngram to calculate the probability of that ngram occuring
# We do this by using the built-in count function and appendning it to a list 
# And then puting that list into a dictionary, so the dictionary would contain the ngram along with the frequency
##############################################
def freq(ngrams):
    wordfreq = [ngrams.count(p) for p in ngrams]
    #print(wordfreq)
    return dict(list(zip(ngrams,wordfreq)))


###########################################
# Method: next_word
# This takes in the current word, the number of grams, and the frequency list
# First we have to calulcate the probability of that ngram occuring, so we do so by using a for loop
# We first find the sum of the total number of frequencies and then obtain the freq of the current word and divide it by the total
# Then we replace the frequency with the probability
# After that, I generate the next_word based off what we were taught in class. 
# We first had to generate a random number between 0 and 1
# We have to traverse through a list of words, and if rand < k+value, return the word
# if not then increment k to k= k + value
# This will be sent back to the main method and appened to a sentance, after this is generated, in the main method
# the regex will replace the <start> and <end> tag
############################################

def next_word(cur_word, grams, freq):

    ########################PROBABILITY DONE
    total = sum(freq.values())
    for key in freq:
        temp = freq[key]
        probs = temp/total
        freq[key]=probs

    ############################  




    ########################################
    rand = random.uniform(0,1)
    k=0
    for key, value in freq.items():
        
        #k = k + value

        if rand < k+value:
            return key
        k=k+value
    


#############Main Method##############
#This first takes in 3 or more agurments from the command line
#If ran in VS Code a command line argument would be: python ngram.py 2 10 harry.txt
#This would take 2 as the numGrams, 20 as the numOutputs, and harry.txt as the input file
#There is a range for the third argument, so you may enter more than one text file at the same time
#Once it takes in the arguments, it then splits it on \n and then sends the string contents and the number of grams to
#a method called ngram_calc (and the result appens to the ngram list)
#Once all the ngrams are calculated, it calculated the frequency of the ngram occuring by calling a method called freq and
# passing it ngram
#####################################


def main(argv):
    print(argv)
    numGrams = int(argv[1])
    numOutputs = int(argv[2])

    ngrams =[]

    for filename in argv[3:]:
        #r represents opening the file in read only mode
        with open(filename, "r") as reader:
            contents=reader.read()
            contents = contents.split('\n')
            contents = " ".join(contents)
            ngrams.extend(ngram_calc(contents,numGrams))
    frequency= freq(ngrams)

    ###################################################
    # This is where we start putting together are generated sentence
    # while sentence is less than the number of outputs, it calls the next_word function and passes the current word, numGrams and frequency list
    # This will only increment when the current word ends with end
    # Once the sentence is generated, with the use of regex, <start> is replaced with a space and <end> is replaced with a period
    # And then the sentance is printed
    ################################################

    sentence =0
    cur_word = "<start>"

    while sentence < numOutputs:
        cur_word += " " + next_word(cur_word, numGrams, frequency)

        if cur_word.endswith(("<end>")):
            sentence +=1
    #print(cur_word)

    for tags in cur_word:
        cur_word= re.sub("<start>", '', cur_word)
        cur_word = re.sub("<end>", '.', cur_word)

    print(cur_word)
    
    



if __name__ == "__main__":
    print('---------------------------------------------------------------------------------------------')
    print('Basima Zafar')
    print('This program learns an N-gram language model from a randum number of text files.')
    print('It then generates a number of sentences based on the N-gram model and the number of sentances inputted through command line.')
    print('---------------------------------------------------------------------------------------------')
    main(sys.argv)