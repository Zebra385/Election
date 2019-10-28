#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import random

# Initialize seed so we always get the same result between two runs.
# Comment this out if you want to change results between two runs.
# More on this here: http://stackoverflow.com/questions/22639587/random-seed-what-does-it-do
random.seed(0)

##################################################
#################### VOTES SETUP #################
##################################################
# initialisation variabable
VOTES = 100000 # number of votes
MEDIAN = VOTES/2# value of median
#definition dictionnary CANDITATES
CANDIDATES = {
    "hermione": "Hermione Granger",
    "balou": "Balou",
    "chuck-norris": "Chuck Norris",
    "elsa": "Elsa",
    "gandalf": "Gandalf",
    "beyonce": "Beyoncé"
}
#definition dictionnary MENTION
MENTIONS = [
    "A rejeter",
    "Insuffisant",
    "Passable",
    "Assez Bien",
    "Bien",
    "Très bien",
    "Excellent"
]
# Fonction to créate  100000 votes
def create_votes():
    return [
        {
            "hermione": random.randint(3, 6),
            "balou": random.randint(0, 6),
            "chuck-norris": random.randint(0, 2),
            "elsa": random.randint(1, 2),
            "gandalf": random.randint(3, 6),
            "beyonce": random.randint(2, 6)
        } for _ in range(0, VOTES)
    ]

##################################################
#################### FUNCTIONS ###################
##################################################
# Fonction to stock the résult of total votes
def results_hash(votes):
    #Variable canditates-results
    candidates_results = \
        {
        candidate: [0]*len(MENTIONS)#initizializing
        for candidate in CANDIDATES.keys()
        }
    for vote in votes:
        for candidate, mention in vote.items():
            candidates_results[candidate][mention] += 1
    return (candidates_results)

#fonction to determine the medium

def majoritary_mentions_hash(candidates_results):
    r = {}
    for candidate, candidate_result in candidates_results.items():
        cumulated_votes = 0#initilize
        for mention, vote_count in enumerate(candidate_result):
            cumulated_votes += vote_count
            if MEDIAN < cumulated_votes:
                # add a key in a dictionary
                r[candidate] = {
                    "mention": mention,
                    "score": cumulated_votes
                }
                break
    return r
def sort_candidates_by(mentions):
    ## bubble sort here we go!
    unsorted = [(key, (mention["mention"], mention["score"])) for key, mention in mentions.items()]
    swapped = True
    while swapped:
        swapped = False
        for j in range(0, len(unsorted) - 1):
            ## but we need REVERSE bubble sort ;-)
            # (note that here we compare tuples, which is pretty neat)
            if unsorted[j + 1][1] > unsorted[j][1]:
                unsorted[j+1], unsorted[j] = unsorted[j], unsorted[j+1]
                swapped = True
    print(unsorted)

    return [
        {
            "name": candidate[0],
            "mention": candidate[1][0],
            "score": candidate[1][1],
        }
        for candidate in unsorted
    ]
def print_results(results):
    for i, result in enumerate(results):
        name = CANDIDATES[result["name"]]
        mention = MENTIONS[result["mention"]]
        score = result["score"] * 100. / VOTES
        if i == 0:
            print("Gagnant: {} avec {:.2f}% de mentions {}".format(
                name, score, mention
            ))
            continue
        else:
            print("- {} avec {:.2f}% de mentions {}".format(
                name, score, mention
            ))

##################################################
#################### MAIN FUNCTION ###############
##################################################

def main():
    votes = create_votes()# creation of 100000 votes
    results = results_hash(votes)# take result votes in results
    majoritary_mentions = majoritary_mentions_hash(results)
    sorted_candidates = sort_candidates_by(majoritary_mentions)
    print_results(sorted_candidates)
if __name__ == '__main__':
    main()