from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import pos_tag
from nltk import ne_chunk
from nltk import Tree
 
text = """
A multi-agency manhunt is under way across several states and Mexico after
police say the former Los Angeles police officer suspected in the murders of a
college basketball coach and her fiance last weekend is following through on
his vow to kill police officers after he opened fire Wednesday night on three
police officers, killing one.
"In this case, we're his target," Sgt. Rudy Lopez from the Corona Police
Department said at a press conference.
The suspect has been identified as Christopher Jordan Dorner, 33, and he is
considered extremely dangerous and armed with multiple weapons, authorities
say. The killings appear to be retribution for his 2009 termination from the
 Los Angeles Police Department for making false statements, authorities say.
Dorner posted an online manifesto that warned, "I will bring unconventional
and asymmetrical warfare to those in LAPD uniform whether on or off duty."
"""
nmli = []
for sentence in sent_tokenize(text):
    print '\nSentence:\n', sentence
    tokens = word_tokenize(sentence)
    pos_tagged_tokens = pos_tag(tokens)
    phrase_chunks = ne_chunk(pos_tagged_tokens)
    print 'tokens:\n', tokens
    print 'tokens with part of speech tags:\n', pos_tagged_tokens
    for chunk in [chunk for chunk in phrase_chunks if hasattr(chunk, 'node')]:
        nmli.append(  Tree(
            chunk.node, [(' '.join(c[0] for c in chunk.leaves()))]).__str__() )

print '#'*70+'\nNamed entities\n'+'#'*70
for j in nmli:
	j = j.strip('()')
	nl = j.split()
	k = 1
	ntype = nl[0]
	nname = ' '.join(nl[1:])
	print ntype+',    '+nname