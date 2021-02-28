
import sys
import re
from nltk.tokenize import sent_tokenize
import nltk
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
    print("Dict: ", frequency)

            # for line in reader.readlines():
            #     contents = contents.replace("\n","")
            #     print(contents)









if __name__ == "__main__":
    main(sys.argv)