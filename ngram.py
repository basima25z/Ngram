
import sys
import re

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
    print(fileContents)
    split_on_periods = re.split("\.", fileContents)
    print(split_on_periods)
    sequences=[]

    #sequences = ' '.join('<start> {} </start>'.format(l.strip()) for l in fileContents.split() if len(l.strip()))
    #print(sequences)

    for tags in split_on_periods:
        tags = "<start>" + tags + "<end>"
        sequences.append([tags.split()[i:] for i in range(numGrams)])
    
    print(sequences)


    # periodSplit = fileContents.split("\.")
    # sentances=[]

    # for tags in periodSplit:
    #     tags






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









if __name__ == "__main__":
    main(sys.argv)