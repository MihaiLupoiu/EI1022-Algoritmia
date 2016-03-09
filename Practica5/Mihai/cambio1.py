'''
Created on 13/11/2013

@author: al204332
'''

class GreedyCoinChanger2:    
    def __init__(self, v: "IList<int>"):    
        self.n = len(v)
        self.sorting_permutation = list(reversed(sorted(range(len(v)), key = v.__getitem__)))
        self.v = [v[i] for i in self.sorting_permutation]
        
    def change(self, Q: "int") -> "IList<int>":    
        x = []
        for vi in sorted(self.v, reverse=True):
            x.append(Q//vi)
            Q = Q % vi
            if Q == 0: return self.sorted(x + [0] * (self.n-len(x)))
            return None
    
    def sorted(self, x: "IList<int>") -> "IList<int>":    
        d = dict((p, i) for (i,p) in enumerate(self.sorting_permutation))
        return [x[d[i]] for i in range(len(x))]
    