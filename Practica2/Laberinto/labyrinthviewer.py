'''
Created on 03/10/2012

@author: David

Dibuja un laberinto a partir de un grafo no dirigido con las siguientes características:
- Los vértices son tuplas de enteros (fila, columna) que se corresponden con las celdas 
  del laberinto. El vértice (0,0) se corresponde en el dibujo con la celda superior 
  izquierda del laberinto.
- Sólo puede haber una arista entre dos vértices si se corresponden a celdas vecinas en 
  el laberinto: La existencia de una arista significa que entre dichas celdas del laberinto 
  NO hay muro.
'''

from easycanvas import EasyCanvas
from algoritmia.datastructures.digraphs import UndirectedGraph

class LabyrinthViewer(EasyCanvas):
    def __init__(self, lab, cell_size=10, margin=10, show_io = False):
        EasyCanvas.__init__(self)
        
        # check 'lab' type
        if not isinstance(lab, UndirectedGraph) or \
           any([type(p)!=type((1,1)) or len(p)!=2 or type(p[0])!=type(1) or type(p[1])!=type(1) for p in lab.V]):
            raise TypeError("The labyrinth must be an UnirectedGraph of two integer tuples")
        
        self.lab = lab
        self.cell_size = cell_size
        self.margin = margin
        self.max_col = max(p[1] for p in self.lab.V)
        self.max_row = max(p[0] for p in self.lab.V)
        self.paths=[]
        self.treasure = None
        self.show_io = show_io
      
    def set_treasure_pos(self, pos): 
        self.treasure = pos
        
    def add_path(self, path, color='red', offset=0): 
        self.paths.append((path, color, offset))
        
    def _draw_path(self,path,color,offset):
        u = path[0]
        m = self.cell_size/2+offset
        for v in path[1:]:
            self.create_line(u[1]*self.cell_size+m, u[0]*self.cell_size+m, v[1]*self.cell_size+m, v[0]*self.cell_size+m, color)
            u = v
                
    def main(self):
        m = self.margin
        
        self.easycanvas_configure(title = 'Labyrinth',
                                  background = 'white',
                                  size = (self.max_col*self.cell_size+m*2+1, self.max_row*self.cell_size+m*2+1), 
                                  coordinates = (-m, (self.max_row+1)*self.cell_size+m, (self.max_col+1)*self.cell_size+m, -m))

        # Draw borders
        self.create_rectangle(0, 0, (self.max_col+1)*self.cell_size, (self.max_row+1)*self.cell_size)
        """
        self.create_line(0,0, (self.max_col+1)*self.cell_size, 0)
        self.create_line(0,(self.max_row+1)*self.cell_size, (self.max_col+1)*self.cell_size, (self.max_row+1)*self.cell_size)
        self.create_line(0,self.cell_size, 0, (self.max_row+1)*self.cell_size)
        self.create_line((self.max_col+1)*self.cell_size, 0, (self.max_col+1)*self.cell_size, (self.max_row+1)*self.cell_size-self.cell_size)
        """
        # Draw internal walls
        for r in range(self.max_row+1):
            for c in range(self.max_col+1):
                u = r, c
                x = c*self.cell_size
                y = r*self.cell_size
                
                if u not in self.lab.V or (r+1,c) not in self.lab.succs(u):
                    self.create_line(x, y+self.cell_size, x+self.cell_size, y+self.cell_size)
        
                if u not in self.lab.V or (r,c+1) not in self.lab.succs(u):
                    self.create_line(x+self.cell_size, y, x+self.cell_size, y+self.cell_size)
         
        for path, color, offset in self.paths:
            self._draw_path(path, color, offset)
        
        if self.treasure != None:
            self.create_filled_circle(self.treasure[1]*self.cell_size+self.cell_size/2, self.treasure[0]*self.cell_size+self.cell_size/2, self.cell_size/3, 'black', 'yellow')
            
        if self.show_io:
            self.create_text(self.cell_size/2, self.cell_size/2, "I", self.cell_size/2)
            self.create_text((self.max_col+0.5)*self.cell_size, (self.max_row+0.5)*self.cell_size, "O", self.cell_size/2)
        # Wait for a key   
        self.readkey(True)
        