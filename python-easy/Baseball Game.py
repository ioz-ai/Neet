# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

# Given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

# An integer x: Record a new score of x.
# '+': Record a new score that is the sum of the previous two scores.
# 'D': Record a new score that is the double of the previous score.
# 'C': Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for i in range(len(operations)):
            if operations[i] == "+":
                # add prev 2 numbers
                res.append(res[-1] + res[len(res)-2])
            elif operations[i] == "C":
                del res[-1]
            elif operations[i] == "D":
                res.append(2*res[-1])
            else:
                res.append(int(operations[i]))
            print("res", res)
        return sum(res)