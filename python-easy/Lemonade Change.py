# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

# Note that you do not have any change in hand at first.

# You are given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

from typing import List, Dict
class Solution:
    def fullfill(self, bill: int, box: Dict[int, int]) -> bool: 
        print(bill)
        # Case 1: Customer pays $5 (No change needed)
        if bill == 5:
            box[5] += 1
            return True
        
        # Case 2: Customer pays $10 (Need $5 change)
        elif bill == 10:
            if box[5] >= 1:
                box[5] -= 1  # Give $5 change
                box[10] += 1 # Take $10 bill
                return True
            else:
                return False # Cannot make $5 change
        else: # 20
            if box[10] >=1 and box[5] >= 1:
                box[10] = box[10]-1
                box[5] = box[5] -1
                box[20] = box[20] + 1
                return True
            if box[5] >= 3:
                box[5] = box[5]-3
                box[20] = box[20] + 1
                return True
        return False
    
    def lemonadeChange(self, bills: List[int]) -> bool:
        box={5:0, 10:0, 20:0}

        for i in range(len(bills)):
            if self.fullfill(bills[i], box) == False:
                return False

        return True