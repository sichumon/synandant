#!/usr/bin/python
import string  
import random                                    
import urllib
import json
                
llist=[[['clumsy', 'graceful']], [['commemorative', 'neglectful']], [['devoted', 'disloyal']], [['compel', 'deter']], [['deceit', 'truth']], [['definite', 'uncertain']], [['despise', 'admire']], [['destitute', 'prosperous']], [['deter', 'persuade']], [['detract', 'increase']], [['devious', 'frank']], [['disdain', 'admiration']], [['dishonest', 'trustworthy']], [['disingenuous', 'honest']], [['disturb', 'comfort']], [['disparage', 'praise']], [['disperse', 'gather']], [['dispirited', 'encouraged']], [['displeasure', 'delight']], [['dissuade', 'persuade']], [['arrogant', 'modest']], [['cause', 'prevent']], [['diminish', 'increase']], [['energetic', 'lethargic']], [['front', 'rear']], [['harsh', 'gentle']], [['honest', 'deceitful']], [['hostile', 'friendly']], [['insert', 'extract']], [['insolent', 'polite']], [['join', 'separate']], [['leader', 'follower']], [['transparent', 'opaque']], [['vivid', 'dull']], [['minimum', 'maximum']], [['miserly', 'generous']], [['misery', 'joy']], [['near', 'far']], [['neglect', 'maintain']], [['part', 'meet']], [['pale', 'bright']], [['pointless', 'worthwhile']], [['prohibit', 'allow']], [['rare', 'common']], [['regular', 'occasional']], [['sensible', 'absurd']], [['spoil', 'preserve']], [['succeed', 'fail']], [['surplus', 'shortage']], [['tight', 'loose']], [['audible', 'inaudible']], [['immense', 'tiny']], [['just', 'unjust']], [['landlord', 'tenant']], [['lazy', 'industrious']], [['essential', 'inessential']], [['leader', 'follower']], [['lend', 'borrow']], [['melt', 'freeze']], [['obedient', 'disobedient']], [['prudent', 'imprudent']], [['pure', 'contaminated']], [['wisdom', 'folly']], [['abate', 'amplify']], [['abstain', 'use']], [['acute', 'dense']], [['adept', 'clumsy']], [['adequate', 'insufficient']], [['adverse', 'favourable']], [['advice', 'misinformation']], [['advise', 'trick']], [['affable', 'impolite']], [['aghast', 'unsurprised']], [['compromise', 'disagreement']], [['alight', 'board']], [['provoke', 'allay']], [['altercation', 'harmony']], [['altruistic', 'selfish']], [['ambiguous', 'clear']], [['anxiety', 'contentment']], [['apathetic', 'interested']], [['astute', 'ignorant']], [['augment', 'decrease']], [['avarice', 'generosity']], [['aversion', 'fondness']], [['avert', 'aid']], [['avid', 'unenthusiastic']], [['beneficiary', 'giver']], [['boisterous', 'calm']], [['bold', 'fearful']], [['brash', 'reserved']], [['brevity', 'longevity']], [['calamity', 'blessing']], [['cacophony', 'silence']], [['callous', 'compassionate']], [['candour', 'bias']], [['capricious', 'constant']], [['charismatic', 'repulsive']], [['cavity', 'solid']], [['cheap', 'expensive']], [['fresh', 'stale']], [['stationary', 'mobile']], [['steep', 'gradual']], [['straight', 'crooked']], [['superior', 'inferior']], [['tame', 'wild']], [['tiny', 'enormous']], [['unite', 'separate']], [['vacant', 'occupied']], [['clear', 'vague']], [['better', 'worse']], [['wrong', 'right']], [['encourage', 'discourage']], [['import', 'export']], [['careful', 'careless']], [['useful', 'useless']], [['decrease', 'increase']], [['cheerless', 'cheerful']], [['advantage', 'disadvantage']], [['wise', 'unwise']], [['noble', 'ignoble']], [['pleasure', 'displeasure']], [['order', 'disorder']], [['amateur', 'professional']], [['domestic', 'foreign']], [['elementary', 'advanced']], [['emigration', 'immigration']], [['exposure', 'shelter']], [['changeable', 'constant']], [['suspect', 'trust']], [['urgent', 'leisurely']], [['enigmatic', 'clear']], [['illegal', 'legal']], [['action', 'reaction']], [['direct', 'indirect']], [['admit', 'deny']], [['together', 'apart']], [['attractive', 'repulsive']], [['boundless', 'limited']], [['brighten', 'fade']], [['careful', 'careless']], [['clumsy', 'graceful']], [['combine', 'separate']], [['create', 'destroy']], [['approve', 'disapprove']], [['compulsory', 'voluntary']], [['grow', 'shrink']], [['harsh', 'mild']], [['help', 'hinder']], [['important', 'trivial']], [['defend', 'attack']], [['deny', 'admit']], [['depth', 'height']], [['divide', 'multiply']], [['drunk', 'sober']], [['dwarf', 'giant']], [['ebb', 'flow']], [['educated', 'uneducated']], [['entrance', 'exit']], [['everywhere', 'nowhere']], [['expand', 'contract']], [['failure', 'success']], [['faint', 'bold']], [['fair', 'play']], [['few', 'many']], [['foe', 'ally']], [['foolish', 'wise']], [['foreign', 'native']], [['frown', 'smile']], [['gaunt', 'obese']], [['guilty', 'innocent']], [['hell', 'heaven']], [['hero', 'villain']], [['humble', 'proud']], [['ignorant', 'knowledgeable']], [['immense', 'minute']], [['inferior', 'superior']], [['innocent', 'guilty']], [['join', 'separate']], [['juvenile', 'adult']], [['liberty', 'captivity']], [['mad', 'sane']], [['minimum', 'maximum']], [['minority', 'majority']], [['mountain', 'valley']], [['opaque', 'transparent']], [['permanent', 'transitory']], [['plain', 'ornate']], [['plural', 'singular']], [['powerful', 'powerless']], [['private', 'public']], [['prosperity', 'poverty']], [['purchase', 'sell']], [['accept', 'refuse']], [['retreat', 'advance']], [['hide', 'show']], [['slovenly', 'smart']], [['north', 'south']], [['east', 'west']], [['spacious', 'cramped']], [['condemn', 'approve']], [['prohibit', 'allow']], [['feeble', 'robust']], [['obstinate', 'compliant']], [['liberty', 'enslaved']], [['content', 'discontent']], [['sober', 'merry']], [['similar', 'contrast']], [['refuse', 'permit']], [['pasture', 'desert']], [['safe', 'perilous']], [['soft', 'coarse']], [['passive', 'aggressive']], [['optimist', 'pessimist']], [['rigid', 'flexible']], [['cowardice', 'valour']], [['virtuous', 'corrupt']], [['culprit', 'victim']], [['foolish', 'sensible']], [['bogus', 'genuine']], [['absurd', 'sensible']], [['tragedy', 'triumph']], [['seldom', 'often']], [['famine', 'feast']], [['tense', 'relaxed']], [['inferior', 'superior']], [['extrovert', 'introvert']], [['significant', 'insignificant']], [['abroad', 'home']], [['absence', 'presence']], [['accept', 'refuse']], [['ancestor', 'descendant']], [['ancient', 'modern']], [['assemble', 'disperse']], [['barren', 'fertile']], [['bent', 'straight']], [['bitter', 'sweet']], [['bless', 'curse']], [['bold', 'timid']], [['bow', 'stern']], [['bright', 'dull']], [['broad', 'narrow']], [['captive', 'free']], [['captivity', 'freedom']], [['condemn', 'praise']], [['confined', 'free']], [['confirm', 'deny']], [['contract', 'expand']], [['coward', 'hero']], [['defeat', 'victory']], [['lose', 'win']], [['lose', 'find']], [['magnify', 'reduce']], [['minimum', 'maximum']], [['miserly', 'generous']], [['misery', 'joy']], [['near', 'far']], [['neglect', 'maintain']], [['object', 'approve']], [['pale', 'bright']], [['part', 'meet']], [['peculiar', 'usual']], [['pointless', 'worthwhile']], [['prohibit', 'allow']], [['progress', 'retreat']], [['raised', 'lower']], [['rare', 'common']], [['regular', 'occasional']], [['resist', 'yield']], [['retreat', 'advance']], [['rough', 'smooth']], [['sensible', 'absurd']], [['separate', 'unite']], [['spoil', 'preserve']], [['succeed', 'fail']], [['suck', 'blow']], [['surplus', 'shortage']], [['tight', 'loose']], [['transparent', 'opaque']], [['unusual', 'common']], [['vacant', 'occupied']], [['vivid', 'dull']], [['warm', 'cool']], [['weaken', 'strengthen']], [['well', 'ill']], [['liberal', 'strict']], [['arouse', 'allay']], [['wither', 'thrive']], [['liberal', 'strict']], [['grieve', 'rejoice']], [['din', 'silence']], [['insolent', 'polite']], [['celebrate', 'lament']], [['sane', 'mad']], [['scarce', 'abundant']], [['coax', 'dissuade']], [['sensible', 'absurd']], [['disperse', 'gather']], [['destitute', 'rich']], [['cherish', 'despise']], [['abandon', 'keep']], [['able', 'incompetent']], [['accept', 'reject']], [['acquire', 'lose']], [['admit', 'deny']], [['agile', 'awkward']], [['aid', 'hinder']], [['alert', 'asleep']], [['amiable', 'unfriendly']], [['arrogant', 'modest']], [['counterfeit', 'genuine']], [['ascend', 'descend']], [['attack', 'defend']], [['banish', 'welcome']], [['begin', 'cease']], [['believe', 'doubt']], [['benefit', 'disadvantage']], [['brief', 'long']], [['broad', 'narrow']], [['cause', 'prevent']], [['comic', 'serious']], [['competent', 'incapable']], [['complex', 'simple']], [['conceal', 'reveal']], [['damp', 'dry']], [['deep', 'shallow']], [['despondent', 'elated']], [['diligent', 'lazy']], [['dilute', 'concentrate']], [['diminish', 'increase']], [['doubtful', 'definite']], [['economical', 'wasteful']], [['fake', 'genuine']], [['fizzy', 'still']], [['flexible', 'rigid']], [['fluid', 'solid']], [['foe', 'friend']], [['frequently', 'seldom']], [['front', 'rear']], [['garbled', 'clear']], [['gather', 'disperse']], [['harsh', 'gentle']], [['honest', 'deceitful']], [['hostile', 'friendly']], [['imperfect', 'flawless']], [['important', 'trivial']], [['insert', 'extract']], [['insolent', 'polite']], [['join', 'separate']], [['lead', 'follow']], [['turbulent', 'calm']], [['magnify', 'reduce']], [['challenging', 'simple']], [['intrepid', 'timid']], [['ignorant', 'educated']], [['unknown', 'famous']], [['vacant', 'occupied']], [['reality', 'fantasy']], [['plural', 'singular']], [['inaudible', 'loud']], [['vile', 'pleasant']], [['scarce', 'plentiful']], [['omit', 'include']], [['precise', 'vague']], [['traitor', 'supporter']], [['generous', 'miserly']], [['perilous', 'safe']], [['postpone', 'continue']], [['accept', 'deny']], [['jubilation', 'sadness']], [['courageous', 'cowardly']], [['major', 'insignificant']], [['commence', 'cease']], [['allow', 'prohibit']], [['sour', 'sweet']], [['conceal', 'reveal']], [['obscure', 'famous']], [['ancient', 'modern']], [['dusk', 'dawn']], [['typical', 'unusual']], [['fruitful', 'futile']], [['honest', 'deceitful']], [['springy', 'inflexible']], [['delighted', 'disappointed']], [['ordered', 'chaostic']], [['precise', 'inaccurate']]]
nlist=[['clumsy', 'graceful'], ['commemorative', 'neglectful'], ['devoted', 'disloyal'], ['compel', 'deter'], ['deceit', 'truth'], ['definite', 'uncertain'], ['despise', 'admire'], ['destitute', 'prosperous'], ['deter', 'persuade'], ['detract', 'increase'], ['devious', 'frank'], ['disdain', 'admiration'], ['dishonest', 'trustworthy'], ['disingenuous', 'honest'], ['disturb', 'comfort'], ['disparage', 'praise'], ['disperse', 'gather'], ['dispirited', 'encouraged'], ['displeasure', 'delight'], ['dissuade', 'persuade'], ['arrogant', 'modest'], ['cause', 'prevent'], ['diminish', 'increase'], ['energetic', 'lethargic'], ['front', 'rear'], ['harsh', 'gentle'], ['honest', 'deceitful'], ['hostile', 'friendly'], ['insert', 'extract'], ['insolent', 'polite'], ['join', 'separate'], ['leader', 'follower'], ['transparent', 'opaque'], ['vivid', 'dull'], ['minimum', 'maximum'], ['miserly', 'generous'], ['misery', 'joy'], ['near', 'far'], ['neglect', 'maintain'], ['part', 'meet'], ['pale', 'bright'], ['pointless', 'worthwhile'], ['prohibit', 'allow'], ['rare', 'common'], ['regular', 'occasional'], ['sensible', 'absurd'], ['spoil', 'preserve'], ['succeed', 'fail'], ['surplus', 'shortage'], ['tight', 'loose'], ['audible', 'inaudible'], ['immense', 'tiny'], ['just', 'unjust'], ['landlord', 'tenant'], ['lazy', 'industrious'], ['essential', 'inessential'], ['leader', 'follower'], ['lend', 'borrow'], ['melt', 'freeze'], ['obedient', 'disobedient'], ['prudent', 'imprudent'], ['pure', 'contaminated'], ['wisdom', 'folly'], ['abate', 'amplify'], ['abstain', 'use'], ['acute', 'dense'], ['adept', 'clumsy'], ['adequate', 'insufficient'], ['adverse', 'favourable'], ['advice', 'misinformation'], ['advise', 'trick'], ['affable', 'impolite'], ['aghast', 'unsurprised'], ['compromise', 'disagreement'], ['alight', 'board'], ['provoke', 'allay'], ['altercation', 'harmony'], ['altruistic', 'selfish'], ['ambiguous', 'clear'], ['anxiety', 'contentment'], ['apathetic', 'interested'], ['astute', 'ignorant'], ['augment', 'decrease'], ['avarice', 'generosity'], ['aversion', 'fondness'], ['avert', 'aid'], ['avid', 'unenthusiastic'], ['beneficiary', 'giver'], ['boisterous', 'calm'], ['bold', 'fearful'], ['brash', 'reserved'], ['brevity', 'longevity'], ['calamity', 'blessing'], ['cacophony', 'silence'], ['callous', 'compassionate'], ['candour', 'bias'], ['capricious', 'constant'], ['charismatic', 'repulsive'], ['cavity', 'solid'], ['cheap', 'expensive'], ['fresh', 'stale'], ['stationary', 'mobile'], ['steep', 'gradual'], ['straight', 'crooked'], ['superior', 'inferior'], ['tame', 'wild'], ['tiny', 'enormous'], ['unite', 'separate'], ['vacant', 'occupied'], ['clear', 'vague'], ['better', 'worse'], ['wrong', 'right'], ['encourage', 'discourage'], ['import', 'export'], ['careful', 'careless'], ['useful', 'useless'], ['decrease', 'increase'], ['cheerless', 'cheerful'], ['advantage', 'disadvantage'], ['wise', 'unwise'], ['noble', 'ignoble'], ['pleasure', 'displeasure'], ['order', 'disorder'], ['amateur', 'professional'], ['domestic', 'foreign'], ['elementary', 'advanced'], ['emigration', 'immigration'], ['exposure', 'shelter'], ['changeable', 'constant'], ['suspect', 'trust'], ['urgent', 'leisurely'], ['enigmatic', 'clear'], ['illegal', 'legal'], ['action', 'reaction'], ['direct', 'indirect'], ['admit', 'deny'], ['together', 'apart'], ['attractive', 'repulsive'], ['boundless', 'limited'], ['brighten', 'fade'], ['careful', 'careless'], ['clumsy', 'graceful'], ['combine', 'separate'], ['create', 'destroy'], ['approve', 'disapprove'], ['compulsory', 'voluntary'], ['grow', 'shrink'], ['harsh', 'mild'], ['help', 'hinder'], ['important', 'trivial'], ['defend', 'attack'], ['deny', 'admit'], ['depth', 'height'], ['divide', 'multiply'], ['drunk', 'sober'], ['dwarf', 'giant'], ['ebb', 'flow'], ['educated', 'uneducated'], ['entrance', 'exit'], ['everywhere', 'nowhere'], ['expand', 'contract'], ['failure', 'success'], ['faint', 'bold'], ['fair', 'play'], ['few', 'many'], ['foe', 'ally'], ['foolish', 'wise'], ['foreign', 'native'], ['frown', 'smile'], ['gaunt', 'obese'], ['guilty', 'innocent'], ['hell', 'heaven'], ['hero', 'villain'], ['humble', 'proud'], ['ignorant', 'knowledgeable'], ['immense', 'minute'], ['inferior', 'superior'], ['innocent', 'guilty'], ['join', 'separate'], ['juvenile', 'adult'], ['liberty', 'captivity'], ['mad', 'sane'], ['minimum', 'maximum'], ['minority', 'majority'], ['mountain', 'valley'], ['opaque', 'transparent'], ['permanent', 'transitory'], ['plain', 'ornate'], ['plural', 'singular'], ['powerful', 'powerless'], ['private', 'public'], ['prosperity', 'poverty'], ['purchase', 'sell'], ['accept', 'refuse'], ['retreat', 'advance'], ['hide', 'show'], ['slovenly', 'smart'], ['north', 'south'], ['east', 'west'], ['spacious', 'cramped'], ['condemn', 'approve'], ['prohibit', 'allow'], ['feeble', 'robust'], ['obstinate', 'compliant'], ['liberty', 'enslaved'], ['content', 'discontent'], ['sober', 'merry'], ['similar', 'contrast'], ['refuse', 'permit'], ['pasture', 'desert'], ['safe', 'perilous'], ['soft', 'coarse'], ['passive', 'aggressive'], ['optimist', 'pessimist'], ['rigid', 'flexible'], ['cowardice', 'valour'], ['virtuous', 'corrupt'], ['culprit', 'victim'], ['foolish', 'sensible'], ['bogus', 'genuine'], ['absurd', 'sensible'], ['tragedy', 'triumph'], ['seldom', 'often'], ['famine', 'feast'], ['tense', 'relaxed'], ['inferior', 'superior'], ['extrovert', 'introvert'], ['significant', 'insignificant'], ['abroad', 'home'], ['absence', 'presence'], ['accept', 'refuse'], ['ancestor', 'descendant'], ['ancient', 'modern'], ['assemble', 'disperse'], ['barren', 'fertile'], ['bent', 'straight'], ['bitter', 'sweet'], ['bless', 'curse'], ['bold', 'timid'], ['bow', 'stern'], ['bright', 'dull'], ['broad', 'narrow'], ['captive', 'free'], ['captivity', 'freedom'], ['condemn', 'praise'], ['confined', 'free'], ['confirm', 'deny'], ['contract', 'expand'], ['coward', 'hero'], ['defeat', 'victory'], ['lose', 'win'], ['lose', 'find'], ['magnify', 'reduce'], ['minimum', 'maximum'], ['miserly', 'generous'], ['misery', 'joy'], ['near', 'far'], ['neglect', 'maintain'], ['object', 'approve'], ['pale', 'bright'], ['part', 'meet'], ['peculiar', 'usual'], ['pointless', 'worthwhile'], ['prohibit', 'allow'], ['progress', 'retreat'], ['raised', 'lower'], ['rare', 'common'], ['regular', 'occasional'], ['resist', 'yield'], ['retreat', 'advance'], ['rough', 'smooth'], ['sensible', 'absurd'], ['separate', 'unite'], ['spoil', 'preserve'], ['succeed', 'fail'], ['suck', 'blow'], ['surplus', 'shortage'], ['tight', 'loose'], ['transparent', 'opaque'], ['unusual', 'common'], ['vacant', 'occupied'], ['vivid', 'dull'], ['warm', 'cool'], ['weaken', 'strengthen'], ['well', 'ill'], ['liberal', 'strict'], ['arouse', 'allay'], ['wither', 'thrive'], ['liberal', 'strict'], ['grieve', 'rejoice'], ['din', 'silence'], ['insolent', 'polite'], ['celebrate', 'lament'], ['sane', 'mad'], ['scarce', 'abundant'], ['coax', 'dissuade'], ['sensible', 'absurd'], ['disperse', 'gather'], ['destitute', 'rich'], ['cherish', 'despise'], ['abandon', 'keep'], ['able', 'incompetent'], ['accept', 'reject'], ['acquire', 'lose'], ['admit', 'deny'], ['agile', 'awkward'], ['aid', 'hinder'], ['alert', 'asleep'], ['amiable', 'unfriendly'], ['arrogant', 'modest'], ['counterfeit', 'genuine'], ['ascend', 'descend'], ['attack', 'defend'], ['banish', 'welcome'], ['begin', 'cease'], ['believe', 'doubt'], ['benefit', 'disadvantage'], ['brief', 'long'], ['broad', 'narrow'], ['cause', 'prevent'], ['comic', 'serious'], ['competent', 'incapable'], ['complex', 'simple'], ['conceal', 'reveal'], ['damp', 'dry'], ['deep', 'shallow'], ['despondent', 'elated'], ['diligent', 'lazy'], ['dilute', 'concentrate'], ['diminish', 'increase'], ['doubtful', 'definite'], ['economical', 'wasteful'], ['fake', 'genuine'], ['fizzy', 'still'], ['flexible', 'rigid'], ['fluid', 'solid'], ['foe', 'friend'], ['frequently', 'seldom'], ['front', 'rear'], ['garbled', 'clear'], ['gather', 'disperse'], ['harsh', 'gentle'], ['honest', 'deceitful'], ['hostile', 'friendly'], ['imperfect', 'flawless'], ['important', 'trivial'], ['insert', 'extract'], ['insolent', 'polite'], ['join', 'separate'], ['lead', 'follow'], ['turbulent', 'calm'], ['magnify', 'reduce'], ['challenging', 'simple'], ['intrepid', 'timid'], ['ignorant', 'educated'], ['unknown', 'famous'], ['vacant', 'occupied'], ['reality', 'fantasy'], ['plural', 'singular'], ['inaudible', 'loud'], ['vile', 'pleasant'], ['scarce', 'plentiful'], ['omit', 'include'], ['precise', 'vague'], ['traitor', 'supporter'], ['generous', 'miserly'], ['perilous', 'safe'], ['postpone', 'continue'], ['accept', 'deny'], ['jubilation', 'sadness'], ['courageous', 'cowardly'], ['major', 'insignificant'], ['commence', 'cease'], ['allow', 'prohibit'], ['sour', 'sweet'], ['conceal', 'reveal'], ['obscure', 'famous'], ['ancient', 'modern'], ['dusk', 'dawn'], ['typical', 'unusual'], ['fruitful', 'futile'], ['honest', 'deceitful'], ['springy', 'inflexible'], ['delighted', 'disappointed'], ['ordered', 'chaostic'], ['precise', 'inaccurate']]

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
#   title = x[0]
#   url = 'http://glosbe.com/gapi/translate?from=eng&dest=eng&format=json&phrase='+title+'&pretty=true'
#   resultx = json.load(urllib.urlopen(url))
#   hyphen = " ----- "
#   resul = resultx["tuc"][0]["meanings"][0]["text"]
#   result = hyphen+resul
   #-------------------------------


   ll=[y[0],z[0],w[0],h[0]]
   ll.insert(i,x[1])
   print "choose a antonym for "+x[0]
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