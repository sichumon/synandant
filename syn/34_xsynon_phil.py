#!/usr/bin/python
import string
import random


nlist = [['lone', 'single'],
 ['solitary', 'single'],
 ['region', 'area'],
 ['magnify', 'enlarge'],
 ['malicious', 'mean'],
 ['merit', 'deserve'],
 ['spiteful', 'malicious'],
 ['expand', 'enlarge'],
 ['match', 'contest'],
 ['mimic', 'copy'],
 ['game', 'match'],
 ['miserly', 'mean'],
 ['mislay', 'lose'],
 ['mistake', 'blunder'],
 ['misplace', 'lose'],
 ['contemporary', 'modern'],
 ['morsel', 'taste'],
 ['mound', 'heap'],
 ['humble', 'unassuming'],
 ['mystify', 'perplex'],
 ['puzzle', 'mystify'],
 ['modest', 'humble'],
 ['motion', 'movement'],
 ['pile', 'mound'],
 ['action', 'motion'],
 ['narrate', 'tell'],
 ['necessary', 'vital'],
 ['nervous', 'concerned'],
 ['neutral', 'unbiased'],
 ['essential', 'vital'],
 ['recount', 'narrate'],
 ['anxious', 'nervous'],
 ['nimble', 'quick'],
 ['impartial', 'unbiased'],
 ['notorious', 'infamous'],
 ['agile', 'nimble'],
 ['nominate', 'choose'],
 ['name', 'nominate'],
 ['obstacle', 'barrier'],
 ['obstinate', 'inflexible'],
 ['stubborn', 'obstinate'],
 ['obstruction', 'obstacle'],
 ['origin', 'beginning'],
 ['optimistic', 'hopeful'],
 ['original', 'novel'],
 ['start', 'origin'],
 ['cheerful', 'optimistic'],
 ['outside', 'external'],
 ['interior', 'inside'],
 ['new', 'novel']]

def picksomequestions():
    """ converts questions to a dict()"""
    answers = dict()
    for question in nlist:
        answers[question[0]] = question[1]
        if len(answers.keys()) > 50:
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
    allowed = '12345'
    print("choose a synonym for "+question)
    for option in multichoice.values():
        print(str(counter)+")"+option)
        if option == correct:
            ncorrect = counter
        counter = counter + 1
    res = raw_input(">")
    while (len(res) != 1 or res not in allowed):
       	res = raw_input(">")
        #return res
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
for question in random.sample(answers.keys(),49):
    multichoice = picksomechoices(question, answers[question])
    score = score + choose(multichoice, question, answers[question])

print("You scored "+str(100*score/50.0)+"%")
