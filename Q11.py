def run_election():
    num_votes = int(input("Number of votes: "))

    tally = {}

    for i in range(num_votes):
        candidate = input("Vote for: ")

        if candidate in tally:
            tally[candidate] += 1
        else:
            tally[candidate] = 1

    winner = max(tally, key=tally.get)
    candidates = set(tally.keys())

    print("Tally:", tally)
    print("Winner:", winner)
    print("Candidates:", candidates)

    return candidates

run_election()
