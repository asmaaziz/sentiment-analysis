from nltk.sentiment.vader import SentimentIntensityAnalyzer
dir= 'C:\\Users\\asmazi01\\dir_path'
commentfile= 'yellow.txt'
delim ='\t'

fname = dir + '\\' + commentfile
with open(fname, encoding='utf-8', errors='ignore') as f:
   sentences = f.readlines()
sid = SentimentIntensityAnalyzer()

totalCompoundScore = 0.0
totalNegativeScore = 0.0
totalNeutralScore = 0.0
totalPositiveScore = 0.0
totalNumOfSentences = 0.0
outfpath = fname + '.sentiment.txt'
outf = open(outfpath,'wb')
outf.write("Sentence\tcompound score\tnegative score\tneutral score\tpositive score\n".encode('utf-8'))
for sentence in sentences:
   if sentence.strip() == "":
       continue
   totalNumOfSentences += 1.0
   print(sentence)
   ss = sid.polarity_scores(sentence)
   outline = "\"" + sentence.strip() + "\""
   compScore = 0.0
   negScore = 0.0
   neuScore = 0.0
   posScore = 0.0
   for k in sorted(ss):
       print('{0}: {1}, '.format(k, ss[k]), end='')
       if k == "compound":
           compScore = ss[k]
       if k == "neg":
           negScore = ss[k]
       if k == "neu":
           neuScore = ss[k]
       if k == "pos":
           posScore = ss[k]
   outline = outline + delim \
             + str(compScore) + delim \
             + str(negScore) + delim \
             + str(neuScore) + delim \
             + str(posScore) + "\n"
   totalCompoundScore += compScore
   totalNegativeScore += negScore
   totalNeutralScore += neuScore
   totalPositiveScore += posScore
   print()
   outf.write(outline.encode('utf-8'))

avgCompoundScore = str(totalCompoundScore/totalNumOfSentences)
avgNegativeScore = str(totalNegativeScore/totalNumOfSentences)
avgNeutralScore = str(totalNeutralScore/totalNumOfSentences)
avgPositiveScore = str(totalPositiveScore/totalNumOfSentences)
outline = "total sentence=" + str(int(totalNumOfSentences))\
         + delim + avgCompoundScore\
         + delim + avgNegativeScore\
         + delim + avgNeutralScore\
         + delim + avgPositiveScore + "\n"
print(outline)
#outf.write(outline.encode('utf-8'))
outf.close()

