
import sys
import re
from nltk.tokenize import sent_tokenize
import nltk
import random
nltk.download('punkt')

def punctuation_removal(fileContents):
    punc='''()-[];:'"\,/@#$%^&*_~'''
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
    print(split_on_periods)
    # sequences=[]

    token_text =[]
    token_text = sent_tokenize(fileContents)
    print(token_text)

    parts=[]
    parts = fileContents.split(".")
    print(parts)


    #sequences = ' '.join('<start> {} </start>'.format(l.strip()) for l in fileContents.split() if len(l.strip()))
    #print(sequences)
#sequences.append([tags.split()[i:] for i in range(numGrams)])

    #adds start and end tags per sentance
    sequences=[]
    for tags in parts:
        tags = "<start> " * (numGrams-1) + tags + " <end>"
        #sequences.append(tags)
        sequences.append(tags)
    print("Sequences: ", sequences)



    #now need to split each tag into ngrams 
    # THIS WORKS NGRAMS SPLIT 
    spaced=[]
    finalSpaced=[]
    ngrams=[]
    for i in sequences:
        print("I: ", i)
        spaced = i.split()
        
        print("spaced word: ", spaced)
        finalSpaced.append(spaced)

        for i in range(len(spaced)-numGrams+1):
            temp=[spaced[j] for j in range(i,i+numGrams)]
            ngrams.append(" ".join(temp))
    print("Spaced:", finalSpaced)
    print("ngrams: ", ngrams)

    return ngrams

def freq(ngrams):
    wordfreq = [ngrams.count(p) for p in ngrams]
    print(wordfreq)
    return dict(list(zip(ngrams,wordfreq)))

def next_word(cur_word, grams, freq):

    sequence = " ".join(cur_word.split()[-(grams-1):])
    print("Sequence: ", sequence)

    print("Dict = Freq", freq)

    #finding most frequent
    v = list(freq.values())
    k= list(freq.keys())

    mostFreq= k[v.index(max(v))]
    print(mostFreq) # do i have to return it and remove it from list?



    #maybe sort them first in order from highest to lowest frequency and return them one at a time
    
    #maybe take the frequency (count of each ngram) and find probability for each word and map it into a new dictionary
    #so the new dic would be word, prob and so on
    # then go thru and do k shit she said 

    for key in freq:
        print(key, '-->', freq[key])


    #PROBABILITY DONE
    total = sum(freq.values())
    for key in freq:
        temp = freq[key]
        probs = temp/total
        freq[key]=probs
    
    
    
    print("Probs", freq)


    #Plan: loop thru and change frequency to probability, then do k shit 





    # try:
    #     choices = freq[sequence].items()
    # except KeyError:
    #     return "<end>"
    # # make a weighted choice for the next word
    # total= sum(chance for choose, chance in choices)
    
    # print("Total", total)
    # # create uniform random number between 0 total
    # rand = random.uniform(0, total)
    # until = 0

    # for choice, chance in choices:
    #     until += chance
    #     if until > rand:
    #         return choice





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
    print("Dict: ", frequency)

    for i in range(numOutputs):
        sentence= random.choice(
            list(filter(
                    lambda x: x.startswith("<start>"),
                    frequency.keys()

                )
            )
        )

        while not sentence.endswith("<end>"):
            sentence = sentence + next_word(sentence, numGrams, frequency)

            # remove start and end tags before printing
        for tags in sentence:
            sentence= re.sub("<start>", '', sentence)
            sentence = re.sub("<end>", '.', sentence)

        print(sentence)
        

  









if __name__ == "__main__":
    main(sys.argv)