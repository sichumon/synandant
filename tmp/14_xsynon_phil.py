#!/usr/bin/python
import string
import random


nlist = [['evaluate', 'assess'],
 ['authentic', 'genuine'],
 ['distinctive', 'characteristic'],
 ['conclusive', 'convincing'],
 ['imminent', 'impending'],
 ['incriminate', 'implicate'],
 ['respectable', 'worthy'],
 ['brief', 'concise'],
 ['accustomed', 'adapted'],
 ['unsuitable', 'inappropriate'],
 ['persuaded', 'urged'],
 ['absence', 'lack'],
 ['profile', 'outline'],
 ['hovering', 'float'],
 ['ecstatic', 'elated'],
 ['resolution', 'settlement'],
 ['anonymity', 'nameless'],
 ['coy', 'shy'],
 ['humble', 'modest'],
 ['antiquity', 'relic'],
 ['abundance', 'plenty'],
 ['flamboyant', 'showy'],
 ['din', 'noise'],
 ['unorthodox', 'unconventional'],
 ['inaugurate', 'commence'],
 ['pigment', 'colour'],
 ['rigid', 'stiff'],
 ['gregarious', 'outgoing'],
 ['evaluation', 'assessment'],
 ['inferior', 'lesser'],
 ['dismal', 'dreary'],
 ['trivial', 'insignificant'],
 ['covet', 'envy'],
 ['mandatory', 'compulsory'],
 ['melancholy', 'glum'],
 ['thrive', 'flourish'],
 ['opposed', 'against'],
 ['unveil', 'reveal'],
 ['automatic', 'mechanical'],
 ['paradox', 'contradiction'],
 ['psychiatrist', 'therapist'],
 ['pseudonym', 'alias'],
 ['psychological', 'mental'],
 ['psychic', 'spiritual'],
 ['fictitious', 'false'],
 ['subconscious', 'subliminal'],
 ['dormant', 'inactive'],
 ['robust', 'sturdy'],
 ['income', 'revenue'],
 ['outlay', 'expenditure']]


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
