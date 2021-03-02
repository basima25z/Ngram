
import sys
import re
from nltk.tokenize import sent_tokenize
import nltk
import random
nltk.download('punkt')




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
    

def ngram_calc(fileContents, numGrams):
    #first you have to remove punctuation
    fileContents=punctuation_removal(fileContents)
    # print(fileContents)
    split_on_periods = re.split("\.", fileContents)
    #print(split_on_periods)
    # sequences=[]

    token_text =[]
    token_text = sent_tokenize(fileContents)
    #print(token_text)

    parts=[]
    parts = fileContents.split(".")
    #print(parts)




    #adds start and end tags per sentance
    sequences=[]
    for tags in parts:
        tags = "<start> " * (numGrams-1) + tags + " <end>"
        #sequences.append(tags)
        sequences.append(tags)
    #print("Sequences: ", sequences)



    #now need to split each tag into ngrams 
    # THIS WORKS NGRAMS SPLIT 
    spaced=[]
    finalSpaced=[]
    ngrams=[]
    for i in sequences:
        #print("I: ", i)
        spaced = i.split()
        
        #print("spaced word: ", spaced)
        finalSpaced.append(spaced)

        for i in range(len(spaced)-numGrams+1):
            temp=[spaced[j] for j in range(i,i+numGrams)]
            ngrams.append(" ".join(temp))
    #print("Spaced:", finalSpaced)
    print("ngrams: ", ngrams)

    return ngrams

def freq(ngrams):
    wordfreq = [ngrams.count(p) for p in ngrams]
    #print(wordfreq)
    return dict(list(zip(ngrams,wordfreq)))

def next_word(cur_word, grams, freq):

    # sequence = " ".join(cur_word.split()[(grams-1):])
    # print("Sequence: ", sequence)

    # print("Dictionary Freq: ", freq)

    # options = freq[sequence].items()

    # total = sum(weight for option, weight in options)
    # r= random.uniform(0,total)
    # k=0

    # for option, weight in options:
    #     if k+weight >r:
    #         return option
    #     k+=weight




   # print("Options:", options)




    #print("Dict = Freq", freq)

    #finding most frequent
    # v = list(freq.values())
    # k= list(freq.keys())

    # mostFreq= k[v.index(max(v))]
    # print(mostFreq) # do i have to return it and remove it from list?



    #maybe sort them first in order from highest to lowest frequency and return them one at a time
    
    #maybe take the frequency (count of each ngram) and find probability for each word and map it into a new dictionary
    #so the new dic would be word, prob and so on
    # then go thru and do k shit she said 

    # for key in freq:
    #     print(key, '-->', freq[key])


    ########################PROBABILITY DONE
    # total = sum(freq.values())
    # for key in freq:
    #     temp = freq[key]
    #     probs = temp/total
    #     freq[key]=probs


      ############################  

    #print("Probs", freq)

    #rand = random.uniform(0,1)
    #print("random number", rand)


    #Plan: loop thru and change frequency to probability, then do k shit 
    ########################################
    # rand = random.uniform(0,1)
    # k=0
    # for key, value in freq.items():
        
    #     #k = k + value

    #     if rand < k+value:
    #         return key
    #     k=k+value
    

        # else:
        #     continue


    #idea: may have to scrape start and end before

    #Trial 3
    # current = cur_word
    # print("Current", current)
     #sequence = " ".join(cur_word.split()[-(grams-1):])
    # print(sequence)


    # try:
    #     choices = freq[sequence].items()
    # except KeyError:
    #     return "<end>"
    
    # print(choices)


    # total= sum(chance for choose, chance in choices)
    # print("Total", total)
    # # create uniform random number between 0 total
    # rand = random.uniform(0,1)
    # until = 0

    # for choice, chance in choices:
    #     if until+chance > rand:
    #         return choice
    #     until = until+chance





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
            # for line in reader.readlines():
            #     contents = contents.replace("\n","")
            #     print(contents)
    frequency= freq(ngrams)
    #print("Dict: ", frequency)

    # for i in range(numOutputs):
    #     sentence= random.choice(
    #         list(filter(
    #                 lambda x: x.startswith("<start>"),
    #                 frequency.keys()

    #             )
    #         )
    #     )

    #     i=0
    #     while not sentence.endswith("<end>"):
    #         print(i)
    #         sentence = sentence + next_word(sentence, numGrams, frequency)

    #         # remove start and end tags before printing
    #     # for tags in sentence:
    #     #     sentence= re.sub("<start>", '', sentence)
    #     #     sentence = re.sub("<end>", '.', sentence)


    #     print(sentence)


    sentence =0
    rand_start = "<start>"

    while sentence < numOutputs:
        rand_start += " " + next_word(rand_start, numGrams, frequency)

        if rand_start.endswith(("<end>")):
            sentence +=1
    print(rand_start)

    for tags in rand_start:
        rand_start= re.sub("<start>", '', rand_start)
        rand_start = re.sub("<end>", '.', rand_start)

    print(rand_start)
    
    



if __name__ == "__main__":
    main(sys.argv)