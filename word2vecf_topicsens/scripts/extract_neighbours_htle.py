import sys
from collections import defaultdict
vocab_file = sys.argv[1]
train_file = sys.argv[2] #doc per line
try:
   THR = int(sys.argv[3])
except IndexError: THR=0

lower = True
window = 10

def read_vocab(fh):
   v = {}
   for line in fh:
      if lower: line = line.lower()
      line = line.strip().split()
      if len(line) != 2: continue
      if int(line[1]) >= THR:
         v[line[0]] = int(line[1]) 
   return v

vocab = set(read_vocab(file(vocab_file)).keys())
print >> sys.stderr,"vocab:",len(vocab)

positions = [(x,"l%s_" % x) for x in xrange(-window, +window+1) if x != 0]
trainfile = file(train_file)

for line in trainfile:
   if lower: line = line.lower()
   toks = ['<s>']
   toks.extend(line.strip().split())
   for i,tok in enumerate(toks):
      if tok not in vocab: continue
      for j,s in positions:
         if i+j < 0: continue
         if i+j >= len(toks): continue
         c = toks[i+j]
         #print i+j 
         tmp = c.split("___")
         if c not in vocab: continue
         print tok,"%s" % (tmp[0])
