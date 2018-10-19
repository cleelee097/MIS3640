

def process_file(filename, skip_header):


    hist={}
    fp=open(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith():
            break
        
        strippables=string.punctuation+string.whiteapce 

        pass
        
        for word in line.split():
            word=word.strip(str)
            word=word.lower()

            # if word in hist:
            #     hist[word] += 1
            # else:
            #     hist[word] = 1
            
            hist[word] = hist.get(word,0)+1
    return hist

    def skip_gutenberg_header(fp):

        for linein fp:
            if line.startswith()


def total_words(hist):

    