#The Tribonacci sequence Tn is defined as follows:

#T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

#Given n, return the value of Tn.

class Solution:
    memory = {0:0, 1:1, 2:1}
    def tribonacci(self, n: int) -> int:
        
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1
        n1 = 0
        n2 = 0
        n3 = 0
        if n-1 not in self.memory:
            n1=self.tribonacci(n-1)
            self.memory[n-1] = n1
        else:
            n1 = self.memory[n-1]
        
        if n-2 not in self.memory:
            n2=self.tribonacci(n-2)
            self.memory[n-2]=n2
        else:
            n2 = self.memory[n-2]
        if n-3 not in self.memory:
            n3=self.tribonacci(n-3)
            self.memory[n-3]=n3
        else:
            n3 = self.memory[n-3]
        return n3+n2+n1