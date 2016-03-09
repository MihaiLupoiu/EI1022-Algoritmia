'''
Created on 06/11/2013

@author: al204332
'''
from algoritmia.statespace import IReversibleForwardStateSpace

class NQueensStateSpace(IReversibleForwardStateSpace):    
    def __init__(self, N: "int"):    
        self.n = N
        
    def initial_states(self) -> "Iterable<IList<int>>":     
        yield []
    
    def is_final(self, s: "IList<int>") -> "bool":    
        return len(s) == self.n
    
    def decisions(self, s: "IList<int>") -> "Iterable<IList<int>>":    
        for row in range(self.n):
            #comprobar la diagonal principal len(s) es la columna
            #if row != len(s) or row+len(s) != (self.n - 1):
            if ( row != len(s) or row+len(s) != (self.n - 1) ) and row not in s and all(len(s)-j != abs(row-s[j]) for j in range(len(s))):
                yield row
      
    #===========================================================================
    # def decisions(self, s: "IList<int>") -> "Iterable<IList<int>>":    
    #     for row in range(self.n):
    #       
    #         if row not in s and all(len(s)-j != abs(row-s[j]) for j in range(len(s))):
    #             yield row
    #===========================================================================
    
    def decide(self, s: "IList<int>", d: "int") -> "IList<int>":    
        s.append(d)
        return s
    
    def undo(self, s: "IList<int>", d: "int") -> "IList<int>":    
        s.pop()
        return s
    
    
def n_queens(space:    "NQueensStateSpace1")    ->    "Iterable<IList<int>>":    
    def backtracking(state:    "IList<int>")    ->    "Iterable<IList<int>>":    
        if space.is_final(state):        
            yield state
        for decision in space.decisions(state):    
            successor = space.decide(state, decision)
            for result in backtracking(successor):        
                    yield result
            state = space.undo(successor, decision)
    initial = next(space.initial_states())    
    for result in backtracking(initial):    
        yield result
        
space = NQueensStateSpace(5)            
for result in n_queens(space):    
    print(result)