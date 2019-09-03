#!/usr/bin/python
import string
import random


nlist = [ ['frail', 'brittle'],
 ['nimble', 'agile'],
 ['feeble', 'weak'],
 ['sprightly', 'brisk'],
 ['sparse', 'paltry'],
 ['meagre', 'scanty'],
 ['vulnerable', 'frail'],
 ['venison', 'meat (deer)'],
 ['penal', 'corrective'],
 ['turmoil', 'chaos'],
 ['tyrant', 'bully'],
 ['despondent', 'dejected'],
 ['disorder', 'confusion'],
 ['panorama', 'view'],
 ['vista', 'scene'],
 ['tepid', 'lukewarm'],
 ['seldom', 'rarely'],
 ['infrequently', 'not often'],
 ['convene', 'congregate'],
 ['congregate', 'gather'],
 ['rally', 'assemble'],
 ['assailant', 'attacker'],
 ['synthetic', 'artificial'],
 ['compute', 'calculate'],
 ['pliable', 'flexible'],
 ['lunacy', 'madness'],
 ['concoct', 'devise'],
 ['cease', 'stop'],
 ['fringe', 'border'],
 ['empathy', 'compassion'],
 ['liable', 'responsible'],
 ['irate', 'angry'],
 ['peddle', 'sell'],
 ['indicted', 'accused'],
 ['handbook', 'manual'],
 ['phoney', 'fake'],
 ['clunk', 'thump'],
 ['unique', 'single'],
 ['rubbish', 'litter'],
 ['litter', 'refuse'],
 ['idle', 'lazy'],
 ['insolent', 'rude'],
 ['isle', 'small island'],
 ['islet', 'tiny island'],
 ['initial', 'first'],
 ['dismantle', 'disassemble'],
 ['campanology', 'bell-ringing'],
 ['cartographer', 'mapmaker'],
 ['credible', 'believable'],
 ['convalescence', 'recovery']]

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
for question in random.sample(answers.keys(),50):
    multichoice = picksomechoices(question, answers[question])
    score = score + choose(multichoice, question, answers[question])

print("You scored "+str(100*score/49.0)+"%")
