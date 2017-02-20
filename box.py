import random
import graphtools
import randomtools
COLUMNS = 8
ROWS = 8
INITPROB = (2,5)
MINSPACE = 30 #must be greater than zero, can be low if mindistance is high
MAXSPACE =  50#must be less than or equal to rows*columns
MINDISTANCE = 15


class binaryDungeon:
    def __init__(self,genfunc=lambda :False):
        self.columns = COLUMNS
        self.rows = ROWS
        self.graph= {}        
        self.box = [[genfunc() for column in range(self.columns)] for row in range(self.rows)]
        self.makeGraph()
        
    def reset(self,genfunc=(lambda :False)):        
        for row in range(self.rows):
                for column in range(self.columns):            
                    self.box[row][column]= genfunc()
        self.makeGraph()
        self.start =(random.randrange(ROWS),random.randrange(COLUMNS))
        self.end = (random.randrange(ROWS),random.randrange(COLUMNS))

    def build(self):
        runc= 0
        while(True):    #break when satisfies conditions
            runc+=1
            self.reset(lambda:randomtools.choose(*INITPROB))            
            if len(self.graph)>MAXSPACE or len(self.graph) < MINSPACE:  #ensures reasonable region
                continue
            while(self.box[self.start[0]][self.start[1]]):#loop to ensure start position is empty
                self.start = (random.randrange(self.rows),random.randrange(self.columns))#random position
                
            distances = graphtools.distancesfrom(self.start,self.graph)
            if -1 in [distances[x] for x in distances.keys()]: #if region is unconnected
                continue
            self.end = max(distances,key=lambda x:distances[x])
            if distances[self.end] < MINDISTANCE: #if distance between start and finish is too short
                continue
            self.path = graphtools.getpath(self.start,self.end,self.graph,distances)
            print("attempts: " + str(runc))
            break
                

    def isBlocked(self,row,column):
              if row>= self.rows or row<0:
                  return True
              if column>= self.columns or column<0:
                  return True
              return self.box[row][column]
            
    def makeGraph(self):
        self.graph = {}
        for row in range(self.rows):
                for column in range(self.columns):
                    if self.box[row][column]: #if a blocked cell                        
                        continue                    
                    self.graph[(row,column)] = []
                    totest = []
                    totest.append((row+1,column)) #down
                    totest.append((row-1,column)) #up
                    totest.append((row,column+1)) #right
                    totest.append((row,column-1)) #left
                    for cell in totest:
                        if not self.isBlocked(*cell):
                            self.graph[(row,column)].append(cell)                
                            
                      
                    
      
  
    def print(self,):
        tiles = {}        
        for row in range(self.rows):
            toprint = ""
            for column in range(self.columns):
                if self.start ==(row,column):
                    toprint+= "⛝"
                    continue
                if self.end ==(row,column):
                    toprint+= "⛝"
                    continue
                if (row,column) in self.path:
                    toprint+= "⛝"
                    continue
                toprint+= "⬛" if self.box[row][column] else "⬜"      #"⬛" if self.box[row][column] else "⬜" "⛝"
            print (toprint)

def choose(x,outof):
    u = random.randint(1,outof)
    return (u<=x)


#Test
if __name__ == '__main__':
    test = binaryDungeon()
    for i in range(8):
        test.build()
        print("path: " +str(len(test.path)) + "\n")
        test.print()
        print("\n")
        
    
    

