#!/usr/bin/python
import string  
import random                                    
                
llist=[[['chorus', 'song']], [['spire', 'church']], [['pillow', 'head']], [['pen', 'ink']], [['key', 'lock']], [['pane', 'window']], [['fortune', 'spend']], [['gold', 'wealth']], [['grief', 'death']], [['gift', 'wrap']], [['fire', 'flame']], [['judge', 'court']], [['melody', 'note']], [['mountain', 'climb']], [['snake', 'venom']], [['shower', 'water']], [['planet', 'space']], [['listen', 'ear']], [['drink', 'thirst']], [['battle', 'victory']], [['reflection', 'mirror']], [['shore', 'sea']], [['frost', 'winter']], [['act', 'stage']], [['foot', 'heel']], [['house', 'resident']], [['feather', 'bird']], [['food', 'taste']], [['weep', 'tear']], [['sew', 'needle']], [['monarch', 'throne']], [['stationery', 'paper']], [['knight', 'armour']], [['harbour', 'ship']], [['medal', 'win']], [['earn', 'money']], [['vehicle', 'road']], [['boat', 'sail']], [['apple', 'pip']], [['saddle', 'horse']], [['letter', 'envelope']], [['teacher', 'school']], [['stick', 'glue']], [['book', 'page']], [['transport', 'ticket']], [['fish', 'scale']], [['bicycle', 'pedal']], [['will', 'heir']], [['route', 'travel']], [['violin', 'string']], [['library', 'book']], [['crime', 'culprit']], [['rabbit', 'burrow']], [['chauffeur', 'car']], [['surgeon', 'operation']], [['butcher', 'meat']], [['party', 'host']], [['retreat', 'coward']], [['fight', 'enemy']], [['blunt', 'blade']], [['mine', 'coal']], [['elephant', 'trunk']], [['time', 'clock']], [['umbrella', 'rain']], [['chief', 'tribe']], [['cereal', 'breakfast']], [['disease', 'symptom']], [['contest', 'prize']], [['volcano', 'eruption']], [['weight', 'scales']], [['aeroplane', 'pilot']], [['astronomy', 'star']], [['museum', 'artefact']], [['agenda', 'meeting']], [['prescription', 'medicine']], [['castle', 'drawbridge']], [['dinosaur', 'extinct']], [['excavate', 'soil']], [['cloud', 'rain']], [['plug', 'electricity']], [['bouquet', 'vase']], [['view', 'window']], [['song', 'voice']], [['bee', 'honey']], [['camera', 'photograph']], [['coin', 'purse']], [['needle', 'thread']], [['trunk', 'tree']], [['mast', 'ship']], [['joke', 'giggle']], [['story', 'chapter']], [['invade', 'army']], [['handkerchief', 'cry']], [['kettle', 'steam']], [['blanket', 'bed']], [['tear', 'paper']], [['hood', 'coat']], [['mane', 'lion']], [['author', 'book']], [['waiter', 'restaurant']], [['tooth', 'gum']], [['soap', 'wash']], [['heart', 'love']], [['cliff', 'coast']], [['hammock', 'sleep']], [['mechanic', 'car']], [['laboratory', 'experiment']], [['storm', 'debris']], [['sledge', 'snow']], [['hunt', 'prey']], [['bomb', 'explosion']], [['sponge', 'absorb']], [['temple', 'worship']], [['blood', 'circulate']], [['candle', 'flame']], [['horse', 'stable']], [['teacher', 'pupil']]]
nlist=[['chorus', 'song'], ['spire', 'church'], ['pillow', 'head'], ['pen', 'ink'], ['key', 'lock'], ['pane', 'window'], ['fortune', 'spend'], ['gold', 'wealth'], ['grief', 'death'], ['gift', 'wrap'], ['fire', 'flame'], ['judge', 'court'], ['melody', 'note'], ['mountain', 'climb'], ['snake', 'venom'], ['shower', 'water'], ['planet', 'space'], ['listen', 'ear'], ['drink', 'thirst'], ['battle', 'victory'], ['reflection', 'mirror'], ['shore', 'sea'], ['frost', 'winter'], ['act', 'stage'], ['foot', 'heel'], ['house', 'resident'], ['feather', 'bird'], ['food', 'taste'], ['weep', 'tear'], ['sew', 'needle'], ['monarch', 'throne'], ['stationery', 'paper'], ['knight', 'armour'], ['harbour', 'ship'], ['medal', 'win'], ['earn', 'money'], ['vehicle', 'road'], ['boat', 'sail'], ['apple', 'pip'], ['saddle', 'horse'], ['letter', 'envelope'], ['teacher', 'school'], ['stick', 'glue'], ['book', 'page'], ['transport', 'ticket'], ['fish', 'scale'], ['bicycle', 'pedal'], ['will', 'heir'], ['route', 'travel'], ['violin', 'string'], ['library', 'book'], ['crime', 'culprit'], ['rabbit', 'burrow'], ['chauffeur', 'car'], ['surgeon', 'operation'], ['butcher', 'meat'], ['party', 'host'], ['retreat', 'coward'], ['fight', 'enemy'], ['blunt', 'blade'], ['mine', 'coal'], ['elephant', 'trunk'], ['time', 'clock'], ['umbrella', 'rain'], ['chief', 'tribe'], ['cereal', 'breakfast'], ['disease', 'symptom'], ['contest', 'prize'], ['volcano', 'eruption'], ['weight', 'scales'], ['aeroplane', 'pilot'], ['astronomy', 'star'], ['museum', 'artefact'], ['agenda', 'meeting'], ['prescription', 'medicine'], ['castle', 'drawbridge'], ['dinosaur', 'extinct'], ['excavate', 'soil'], ['cloud', 'rain'], ['plug', 'electricity'], ['bouquet', 'vase'], ['view', 'window'], ['song', 'voice'], ['bee', 'honey'], ['camera', 'photograph'], ['coin', 'purse'], ['needle', 'thread'], ['trunk', 'tree'], ['mast', 'ship'], ['joke', 'giggle'], ['story', 'chapter'], ['invade', 'army'], ['handkerchief', 'cry'], ['kettle', 'steam'], ['blanket', 'bed'], ['tear', 'paper'], ['hood', 'coat'], ['mane', 'lion'], ['author', 'book'], ['waiter', 'restaurant'], ['tooth', 'gum'], ['soap', 'wash'], ['heart', 'love'], ['cliff', 'coast'], ['hammock', 'sleep'], ['mechanic', 'car'], ['laboratory', 'experiment'], ['storm', 'debris'], ['sledge', 'snow'], ['hunt', 'prey'], ['bomb', 'explosion'], ['sponge', 'absorb'], ['temple', 'worship'], ['blood', 'circulate'], ['candle', 'flame'], ['horse', 'stable'], ['teacher', 'pupil']]
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
   
   ll=[y[0],z[0],w[0],h[0]]
   ll.insert(i,x[1])
   print "choose a antonym  for "+x[0]
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
