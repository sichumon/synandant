#!/usr/bin/python
import string  
import random                                    
import urllib
import json


llist=[[['steady', 'regular']], [['stupid', 'silly']], [['substantially', 'considerably']], [['suggest', 'propose']], [['sundown', 'sunset']], [['sunrise', 'dawn']], [['sure', 'certain']], [['surroundings', 'environment']], [['survive', 'outlive']], [['symbolise', 'represent']], [['tailored', 'tailor-made']], [['temper', 'mood']], [['testament', 'testimony']], [['today', 'nowadays']], [['torpid', 'lethargic']], [['touchdown', 'landing']], [['touchy', 'sensitive']], [['transform', 'convert']], [['transitory', 'temporary']], [['transparent', 'obvious']], [['trustworthy', 'reliable']], [['twister', 'tornado']], [['twosome', 'pair']], [['ultimate', 'final']], [['uncared-for', 'neglected']], [['uncommon', 'unusual']], [['uncooked', 'raw']], [['undeniable', 'indisputable']], [['understandable', 'comprehensible']], [['unforeseen', 'unexpected']], [['unfortunate', 'unlucky']], [['unhurt', 'unharmed']], [['uninjured', 'unhurt']], [['unlawful', 'illegal']], [['unmarried', 'single']], [['untimely', 'premature']], [['untrue', 'unfaithful']], [['unusual', 'strange']], [['uprising', 'rebellion']], [['usually', 'generally']], [['vacuum', 'hoover']], [['vague', 'indistinct']], [['vain', 'useless']], [['valueless', 'worthless']], [['vanquish', 'conquer']], [['vary', 'differ']], [['vast', 'huge']], [['virtue', 'advantage']], [['visualize', 'imagine']], [['warranty', 'guarantee']]]
nlist=[['steady', 'regular'], ['stupid', 'silly'], ['substantially', 'considerably'], ['suggest', 'propose'], ['sundown', 'sunset'], ['sunrise', 'dawn'], ['sure', 'certain'], ['surroundings', 'environment'], ['survive', 'outlive'], ['symbolise', 'represent'], ['tailored', 'tailor-made'], ['temper', 'mood'], ['testament', 'testimony'], ['today', 'nowadays'], ['torpid', 'lethargic'], ['touchdown', 'landing'], ['touchy', 'sensitive'], ['transform', 'convert'], ['transitory', 'temporary'], ['transparent', 'obvious'], ['trustworthy', 'reliable'], ['twister', 'tornado'], ['twosome', 'pair'], ['ultimate', 'final'], ['uncared-for', 'neglected'], ['uncommon', 'unusual'], ['uncooked', 'raw'], ['undeniable', 'indisputable'], ['understandable', 'comprehensible'], ['unforeseen', 'unexpected'], ['unfortunate', 'unlucky'], ['unhurt', 'unharmed'], ['uninjured', 'unhurt'], ['unlawful', 'illegal'], ['unmarried', 'single'], ['untimely', 'premature'], ['untrue', 'unfaithful'], ['unusual', 'strange'], ['uprising', 'rebellion'], ['usually', 'generally'], ['vacuum', 'hoover'], ['vague', 'indistinct'], ['vain', 'useless'], ['valueless', 'worthless'], ['vanquish', 'conquer'], ['vary', 'differ'], ['vast', 'huge'], ['virtue', 'advantage'], ['visualize', 'imagine'], ['warranty', 'guarantee']]



def goodchoice(a,b,ll):
   if a==b:
      return True
   else:
      for i in ll:
         if a in i and b in i:
            return True
      return False

def chooseanelem(a,ll):
   while True:
      x=random.sample(ll,1)

      if not goodchoice(x,a,ll):
         return x
         break
def mrandomsample(ll):
   while True:
      x,y,z,w,h=random.sample(nlist, 5)
      if not goodchoice(x,y,ll) and not goodchoice(x,z,ll) and not goodchoice(x,w,ll) and not goodchoice(x,h,ll):
         return x,y,z,w,h
         break

print len(nlist)
for x in nlist:
   for j in nlist:
      if set(x).issubset(set(j)) and set(x)<>set(j):
         nlist.remove(x)
         break
print len(nlist)
def choose(score):
   x,y,z,w,h=mrandomsample(nlist)
   s=score
   x= [x[0], x[random.randrange(1,len(x))]]
   i=random.randrange(5)

  #-------------------------------
#   hyphen = " ----- "
#   xtitle = x[0]
#   xurl = 'http://glosbe.com/gapi/translate?from=eng&dest=eng&format=json&phrase='+xtitle+'&pretty=true'
#   xresultx = json.load(urllib.urlopen(xurl))
#   xresul = xresultx["tuc"][0]["meanings"][0]["text"]
#   xresult = hyphen+xresul
   #-------------------------------

   ll=[y[0],z[0],w[0],h[0]]
   ll.insert(i,x[1])
#   print "choose a synonym for "+x[0], xresult
   print "choose a synonym for "+x[0]
   for a in range(5):
      print str(a)+")"+ll[a]

   res=raw_input()
   if str(res) and str(res)==str(i):

      s=s+1
   else:
      print "No! the answer is "+ll[i]+"\n\n"

   return s
score=0
for i in range(1,51):
   print "Question number "+str(i)+"/50"
   score=choose(score)

print "You scored "+str(100*score/50.0)+"%"
