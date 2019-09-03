#!/usr/bin/python
import string  
import random                                    
import urllib
import json



llist=[[['about', 'approximately']], [['abstract', 'summary']], [['accomplish', 'achieve']], [['accumulate', 'build-up']], [['administer', 'manage']], [['admit', 'confess']], [['almost', 'nearly']], [['animated', 'lively']], [['annoy', 'irritate']], [['answer', 'reply']], [['anyway', 'besides']], [['apparent', 'obvious']], [['appear', 'seem']], [['applicable', 'relevant']], [['appreciable', 'considerable']], [['ardour', 'passion']], [['arise', 'occur']], [['aromatic', 'fragrant']], [['arrive', 'reach']], [['artful', 'crafty']], [['association', 'organisation']], [['assure', 'guarantee']], [['attractive', 'appealing']], [['away', 'absent']], [['awful', 'terrible']], [['backbone', 'spine']], [['ballot', 'poll']], [['beat', 'defeat']], [['begin', 'start']], [['believable', 'plausible']], [['belly', 'stomach']], [['beneficial', 'favourable']], [['bid', 'tender']], [['bizarre', 'weird']], [['blameless', 'innocent']], [['branch', 'department']], [['brave', 'courageous']], [['brow', 'forehead']], [['business', 'commerce']], [['busy', 'engaged']], [['categorise', 'classify']], [['charter', 'constitution']], [['chiefly', 'mainly']], [['choosy', 'picky']], [['chop', 'cut']], [['chorus', 'refrain']], [['citation', 'quotation']], [['cite', 'quote']], [['class', 'lesson']], [['clerk', 'receptionist']], [['', '']], [['clever', 'intelligent']], [['close', 'shut']], [['collect', 'gather']], [['comfort', 'consolation']], [['comic', 'comedian']], [['complete', 'total']], [['completely', 'totally']], [['concord', 'harmony']], [['condemn', 'sentence']], [['confine', 'restrict']], [['conflict', 'clash']], [['conform', 'comply']], [['considerate', 'thoughtful']], [['constant', 'fixed']], [['constitution', 'structure']], [['consult', 'refer']], [['contemporary', 'modern']], [['continuous', 'continual']], [['contrary', 'opposite']], [['convention', 'conference']], [['convey', 'communicate']], [['cope', 'manage']], [['correct', 'right']], [['couch', 'sofa']], [['crusade', 'campaign']], [['cube', 'dice']], [['curative', 'healing']], [['dash', 'sprint']], [['daybreak', 'dawn']], [['deceptive', 'misleading']], [['decontrol', 'deregulate']], [['dedicated', 'committed']], [['deduce', 'infer']], [['defective', 'faulty']], [['deliberate', 'planned']], [['deliberately', 'intentionally']], [['delicate', 'fragile']], [['demonstrate', 'protest']], [['denote', 'indicate']], [['deprave', 'corrupt']], [['depraved', 'wicked,']], [['desert', 'abandon']], [['deserted', 'abandoned']], [['destiny', 'fate']], [['detached', 'indifferent']], [['differentiate', 'distinguish']], [['diminish', 'decrease']], [['disadvantaged', 'deprived']], [['disagreeable', 'unpleasant']], [['disappear', 'vanish']], [['disaster', 'catastrophe']], [['disclaim', 'deny']], [['disclose', 'reveal']], [['discount', 'reduction']], [['disgrace', 'shame']], [['domesticate', 'cultivate']], [['dossier', 'file']], [['dubious', 'doubtful']], [['eager', 'keen']], [['earth', 'soil']], [['economic', 'profitable']], [['egocentric', 'selfish']], [['elevate', 'promote']], [['elevate', 'raise']], [['emphasise', 'stress']], [['encounter', 'come']], [['enormous', 'immense']], [['enquire', 'investigate']], [['equity', 'fairness']], [['especially', 'particularly']], [['essential', 'fundamental']], [['establish', 'set']], [['evaluate', 'assess']], [['everlasting', 'eternal']], [['exactly', 'precisely']], [['except', 'apart']], [['expire', 'run']], [['explode', 'blow']], [['extra', 'additional']], [['fabricate', 'manufacture']], [['famous', 'renowned']], [['fanatic', 'enthusiast']], [['fantastic', 'great']], [['float', 'drift']], [['fool', 'idiot']], [['foolish', 'silly']], [['forehead', 'brow']], [['foretell', 'predict']], [['formerly', 'previously']], [['fortunate', 'lucky']], [['foxy', 'cunning']], [['foyer', 'lobby']], [['fragrance', 'perfume']], [['French', 'dressing']], [['function', 'operate']], [['garbage', 'rubbish']], [['glitter', 'sparkle']], [['grab', 'seize']], [['grasping', 'greedy']], [['gratis', 'free']], [['gratuity', 'tip']], [['gravestone', 'headstone']], [['gut', 'intestine']], [['hall', 'corridor']], [['scatter', 'distribute']], [['handsome', 'good-looking']], [['frequent', 'haunt']], [['happily', 'fortunately']], [['hard', 'tough']], [['shelter', 'canopy']], [['hawk', 'peddle']], [['hazard', 'endanger']], [['hearsay', 'rumour']], [['hermetic', 'airtight']], [['highbrow', 'intellectual']], [['hint', 'trace,']], [['hole', 'gap']], [['home', 'domestic']], [['homicide', 'murder']], [['housebreaking', 'burglary']], [['hunger', 'starvation']], [['hurry', 'rush']], [['hypothesis', 'speculation']], [['idler', 'loafer']], [['if', 'whether']], [['ignore', 'disregard']], [['illiberal', 'intolerant']], [['illuminate', 'clarify']], [['illuminate', 'light']], [['illustrate', 'demonstrate']], [['imagine', 'assume']], [['imagine', 'suppose']], [['imitate', 'mimic']], [['immediate', 'instant']], [['immobile', 'motionless']], [['immoderate', 'excessive']], [['immodest', 'conceited']], [['impact', 'affect']], [['impartial', 'neutral']], [['impasse', 'deadlock']], [['impassive', 'emotionless']], [['impeach', 'question']], [['impediment', 'obstacle']], [['imperative', 'vital']], [['impolite', 'rude']], [['incidentally', 'by']], [['inconsiderate', 'thoughtless']], [['indisputable', 'undeniable']], [['infamous', 'notorious']], [['infantile', 'childish']], [['infect', 'contaminate']], [['inflexible', 'rigid']], [['inflow', 'influx']], [['informal', 'casual']], [['infrequent', 'rare']], [['inheritor', 'heir']], [['innocent', 'harmless']], [['insolvent', 'bankrupt']], [['inspect', 'examine']], [['instinct', 'intuition']], [['instructions', 'directions']], [['insufferable', 'unbearable']], [['insufficient', 'inadequate']], [['insupportable', 'intolerable']], [['insurgent', 'rebel']], [['intellectual', 'mental']], [['intend', 'mean']], [['intensify', 'heighten']], [['interplay', 'interaction']], [['inventory', 'stock']], [['invoice', 'bill']], [['involve', 'entail']], [['isolated', 'lonely']], [['jealous', 'envious']], [['joy', 'delight']], [['knowingly', 'deliberately']], [['lacking', 'missing']], [['last', 'final']], [['leading', 'main']], [['learn', 'memorize']], [['legitimate', 'valid']], [['lethal', 'deadly']], [['livid', 'furious']], [['lousy', 'awful']], [['lucid', 'clear']], [['madness', 'insanity']], [['magician', 'conjurer']], [['magnify', 'exaggerate']], [['maintain', 'preserve']], [['man-made', 'artificial']], [['mannequin', 'model']], [['material', 'fabric']], [['matters', 'things']], [['maybe', 'perhaps']], [['measure', 'degree']], [['meeting', 'assembly']], [['merciless', 'cruel']], [['middleman', 'intermediary']], [['midway', 'halfway']], [['migrate', 'emigrate']]]
nlist=[['about', 'approximately'], ['abstract', 'summary'], ['accomplish', 'achieve'], ['accumulate', 'build-up'], ['administer', 'manage'], ['admit', 'confess'], ['almost', 'nearly'], ['animated', 'lively'], ['annoy', 'irritate'], ['answer', 'reply'], ['anyway', 'besides'], ['apparent', 'obvious'], ['appear', 'seem'], ['applicable', 'relevant'], ['appreciable', 'considerable'], ['ardour', 'passion'], ['arise', 'occur'], ['aromatic', 'fragrant'], ['arrive', 'reach'], ['artful', 'crafty'], ['association', 'organisation'], ['assure', 'guarantee'], ['attractive', 'appealing'], ['away', 'absent'], ['awful', 'terrible'], ['backbone', 'spine'], ['ballot', 'poll'], ['beat', 'defeat'], ['begin', 'start'], ['believable', 'plausible'], ['belly', 'stomach'], ['beneficial', 'favourable'], ['bid', 'tender'], ['bizarre', 'weird'], ['blameless', 'innocent'], ['branch', 'department'], ['brave', 'courageous'], ['brow', 'forehead'], ['business', 'commerce'], ['busy', 'engaged'], ['categorise', 'classify'], ['charter', 'constitution'], ['chiefly', 'mainly'], ['choosy', 'picky'], ['chop', 'cut'], ['chorus', 'refrain'], ['citation', 'quotation'], ['cite', 'quote'], ['class', 'lesson'], ['clerk', 'receptionist'], ['', ''], ['clever', 'intelligent'], ['close', 'shut'], ['collect', 'gather'], ['comfort', 'consolation'], ['comic', 'comedian'], ['complete', 'total'], ['completely', 'totally'], ['concord', 'harmony'], ['condemn', 'sentence'], ['confine', 'restrict'], ['conflict', 'clash'], ['conform', 'comply'], ['considerate', 'thoughtful'], ['constant', 'fixed'], ['constitution', 'structure'], ['consult', 'refer'], ['contemporary', 'modern'], ['continuous', 'continual'], ['contrary', 'opposite'], ['convention', 'conference'], ['convey', 'communicate'], ['cope', 'manage'], ['correct', 'right'], ['couch', 'sofa'], ['crusade', 'campaign'], ['cube', 'dice'], ['curative', 'healing'], ['dash', 'sprint'], ['daybreak', 'dawn'], ['deceptive', 'misleading'], ['decontrol', 'deregulate'], ['dedicated', 'committed'], ['deduce', 'infer'], ['defective', 'faulty'], ['deliberate', 'planned'], ['deliberately', 'intentionally'], ['delicate', 'fragile'], ['demonstrate', 'protest'], ['denote', 'indicate'], ['deprave', 'corrupt'], ['depraved', 'wicked,'], ['desert', 'abandon'], ['deserted', 'abandoned'], ['destiny', 'fate'], ['detached', 'indifferent'], ['differentiate', 'distinguish'], ['diminish', 'decrease'], ['disadvantaged', 'deprived'], ['disagreeable', 'unpleasant'], ['disappear', 'vanish'], ['disaster', 'catastrophe'], ['disclaim', 'deny'], ['disclose', 'reveal'], ['discount', 'reduction'], ['disgrace', 'shame'], ['domesticate', 'cultivate'], ['dossier', 'file'], ['dubious', 'doubtful'], ['eager', 'keen'], ['earth', 'soil'], ['economic', 'profitable'], ['egocentric', 'selfish'], ['elevate', 'promote'], ['elevate', 'raise'], ['emphasise', 'stress'], ['encounter', 'come'], ['enormous', 'immense'], ['enquire', 'investigate'], ['equity', 'fairness'], ['especially', 'particularly'], ['essential', 'fundamental'], ['establish', 'set'], ['evaluate', 'assess'], ['everlasting', 'eternal'], ['exactly', 'precisely'], ['except', 'apart'], ['expire', 'run'], ['explode', 'blow'], ['extra', 'additional'], ['fabricate', 'manufacture'], ['famous', 'renowned'], ['fanatic', 'enthusiast'], ['fantastic', 'great'], ['float', 'drift'], ['fool', 'idiot'], ['foolish', 'silly'], ['forehead', 'brow'], ['foretell', 'predict'], ['formerly', 'previously'], ['fortunate', 'lucky'], ['foxy', 'cunning'], ['foyer', 'lobby'], ['fragrance', 'perfume'], ['French', 'dressing'], ['function', 'operate'], ['garbage', 'rubbish'], ['glitter', 'sparkle'], ['grab', 'seize'], ['grasping', 'greedy'], ['gratis', 'free'], ['gratuity', 'tip'], ['gravestone', 'headstone'], ['gut', 'intestine'], ['hall', 'corridor'], ['scatter', 'distribute'], ['handsome', 'good-looking'], ['frequent', 'haunt'], ['happily', 'fortunately'], ['hard', 'tough'], ['shelter', 'canopy'], ['hawk', 'peddle'], ['hazard', 'endanger'], ['hearsay', 'rumour'], ['hermetic', 'airtight'], ['highbrow', 'intellectual'], ['hint', 'trace,'], ['hole', 'gap'], ['home', 'domestic'], ['homicide', 'murder'], ['housebreaking', 'burglary'], ['hunger', 'starvation'], ['hurry', 'rush'], ['hypothesis', 'speculation'], ['idler', 'loafer'], ['if', 'whether'], ['ignore', 'disregard'], ['illiberal', 'intolerant'], ['illuminate', 'clarify'], ['illuminate', 'light'], ['illustrate', 'demonstrate'], ['imagine', 'assume'], ['imagine', 'suppose'], ['imitate', 'mimic'], ['immediate', 'instant'], ['immobile', 'motionless'], ['immoderate', 'excessive'], ['immodest', 'conceited'], ['impact', 'affect'], ['impartial', 'neutral'], ['impasse', 'deadlock'], ['impassive', 'emotionless'], ['impeach', 'question'], ['impediment', 'obstacle'], ['imperative', 'vital'], ['impolite', 'rude'], ['incidentally', 'by'], ['inconsiderate', 'thoughtless'], ['indisputable', 'undeniable'], ['infamous', 'notorious'], ['infantile', 'childish'], ['infect', 'contaminate'], ['inflexible', 'rigid'], ['inflow', 'influx'], ['informal', 'casual'], ['infrequent', 'rare'], ['inheritor', 'heir'], ['innocent', 'harmless'], ['insolvent', 'bankrupt'], ['inspect', 'examine'], ['instinct', 'intuition'], ['instructions', 'directions'], ['insufferable', 'unbearable'], ['insufficient', 'inadequate'], ['insupportable', 'intolerable'], ['insurgent', 'rebel'], ['intellectual', 'mental'], ['intend', 'mean'], ['intensify', 'heighten'], ['interplay', 'interaction'], ['inventory', 'stock'], ['invoice', 'bill'], ['involve', 'entail'], ['isolated', 'lonely'], ['jealous', 'envious'], ['joy', 'delight'], ['knowingly', 'deliberately'], ['lacking', 'missing'], ['last', 'final'], ['leading', 'main'], ['learn', 'memorize'], ['legitimate', 'valid'], ['lethal', 'deadly'], ['livid', 'furious'], ['lousy', 'awful'], ['lucid', 'clear'], ['madness', 'insanity'], ['magician', 'conjurer'], ['magnify', 'exaggerate'], ['maintain', 'preserve'], ['man-made', 'artificial'], ['mannequin', 'model'], ['material', 'fabric'], ['matters', 'things'], ['maybe', 'perhaps'], ['measure', 'degree'], ['meeting', 'assembly'], ['merciless', 'cruel'], ['middleman', 'intermediary'], ['midway', 'halfway'], ['migrate', 'emigrate']]


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
