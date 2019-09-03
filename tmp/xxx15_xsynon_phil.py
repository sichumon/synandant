#!/usr/bin/python
import string
import random


nlist = [['origin', 'beginning'],
['commercial', 'trade'],
['advent', 'arrival'],
['initiate', 'begin'],
['amalgamate', 'combine'],
['exuberant', 'enthusiastic'],
['derivative', 'byproduct'],
['superfluous', 'excess'],
['serene', 'peaceful'],
['superficial', 'shallow'],
['partial', 'incomplete'],
['tenacious', 'resolute'],
['pessimistic', 'negative'],
['volatile', 'changeable'],
['erratic', 'unpredictable'],
['affable', 'friendly'],
['irony', 'absurdity'],
['allusion', 'implication'],
['analogy', 'comparison'],
['succinct', 'concise'],
['personification', 'embodiment'],
['affable', 'friendly'],
['devoured', 'gobbled'],
['beckoned', 'summoned'],
['glared', 'glowered'],
['lackadaisical', 'lazy'],
['distinctive', 'characteristic'],
['contrary', 'opposite'],
['inactive', 'stationary'],
['languid', 'inactive'],
['controversial', 'disputed'],
['ethical', 'moral'],
['roam', 'wander'],
['aspiration', 'aim'],
['incident', 'event'],
['parched', 'dehydrated'],
['loathe', 'despise'],
['intensity', 'force'],
['wretched', 'unfortunate'],
['awed', 'impressed'],
['coaxed', 'persuaded'],
['severity', 'strictness'],
['dignified', 'honourable'],
['eerie', 'strange'],
['festooned', 'decorated'],
['hoist', 'raise'],
['precarious', 'insecure'],
['seething', 'furious'],
['livid', 'enraged'],
['bustling', 'crowded']]


def picksomequestions():
    """ converts questions to a dict()"""
    answers = dict()
    for question in nlist:
        answers[question[0]] = question[1]
        if len(answers.keys()) > 49:
            break

    return answers


def picksomechoices(question, answer):
    """ returns the correct q/a plus 3 other random choices as a dict()"""
    """ because of the way dict() works all 4 choices will be unique """
    choices = dict()
    choices[question] = answer
    for choice in random.sample(nlist, 10):
        choices[choice[0]] = choice[1]
        if len(choices.keys()) > 3:
            break

    return choices


def choose(multichoice, question, correct):
    """ takes the list of choices, the correct q and the correct a.  Returns 1 for correct and 0 for incorrect """
    counter = 1
    ncorrect = 0
    print("choose a synonym for "+question)
    for option in multichoice.values():
        print(str(counter)+")"+option)
        if option == correct:
            ncorrect = counter
        counter = counter + 1
    res = raw_input(">")
    if int(res) == ncorrect:
        print("CORRECT!")
        return 1
    else:
        print("\n >>>>>> The answer is actually -- " + correct)
	print 
        return 0


# main program starts here
score = 0
answers = picksomequestions()
for question in random.sample(answers.keys(),50):
    multichoice = picksomechoices(question, answers[question])
    score = score + choose(multichoice, question, answers[question])

print("You scored "+str(100*score/50.0)+"%")