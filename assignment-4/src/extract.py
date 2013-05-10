from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import pos_tag
from nltk import ne_chunk
from nltk import Tree

waste = ['physics','chemistry','physiology','literature','wikipedia']

class NEExtract:
    def __init__(self,data):
        self.text = data
    def main(self):
        text = self.text

        nmli = []
        try:
            for sentence in sent_tokenize(text):
                #print '\nSentence:\n', sentence
                tokens = word_tokenize(sentence)
                pos_tagged_tokens = pos_tag(tokens)
                phrase_chunks = ne_chunk(pos_tagged_tokens)
                #print 'tokens:\n', tokens
                #print 'tokens with part of speech tags:\n', pos_tagged_tokens
                for chunk in [chunk for chunk in phrase_chunks if hasattr(chunk, 'node')]:
                    nmli.append(  Tree(
                        chunk.node, [(' '.join(c[0] for c in chunk.leaves()))] ).__str__() )
        except :
            pass

        neli = []    
        for j in nmli:
            temp = dict()
            j = j.strip('()')
            nl = j.split()
            k = 1
            ntype = nl[0]
            nname = ' '.join(nl[1:])
            j = -1
            ntyp = ''
            while j<len(ntype):
                j += 1 
                try:
                    ntyp += str(ntype[j])
                except:
                    pass
            j = -1 
            nnam = ''
            while j<len(nname):
                j += 1 
                try:
                    nnam += str(nname[j])
                except:
                    pass
            print ntyp, nnam
            if ntyp == 'PERSON' or ntyp == 'GPE':
                temp['type'] = ntyp
                temp['name'] = nnam
                if temp not in neli and nnam.lower() not in waste:
                    neli.append(temp)
        printd = ''
        printd += '<table border="1"><tbody>'
        for j in neli:
            printd  += '<tr>'
            ntype = j['type']
            nname = j['name']            
            printd +=  '<td>'+ntype+'</td><td>'+nname+'</td></tr>'
        printd += '</tbody></table>'
        return printd