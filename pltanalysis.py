from collections import Counter
import spacy

nlp= spacy.en.English()

f=open('plot2006_2016.txt','r')
doc=f.read()

plots=doc.split('-----------------------------------------------------------')
cleanplots=[]

'''for plot in plots:
    clean=plot.split()
    for word in clean:
        if '(' in word or ')' in word:
            clean.remove(word)
    cleanplots.append(' '.join(clean))'''

    

parseplot=[]
names=[]

for plot in plots:
    parseplot.append(nlp(plot))

for plot in parseplot:
    n=[]
    ents=list(plot.ents)
    for ent in ents:
        if ent.label_=='GPE' and ' '.join(t.orth_ for t in ent) not in n :
            n.append(' '.join(t.orth_ for t in ent))
    for name in n:
        names.append(name)
    



'''ents=list(doc.ents)

names=[]

for ent in ents:
    if ent.label_=='PERSON':
        names.append(' '.join(t.orth_ for t in ent))


#words=plots.split()
#print(words.count("-----------------------------------------------------------"))'''
print(Counter(names).most_common(50))

