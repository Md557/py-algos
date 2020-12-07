#####################################
## Two largest elements in array
## Minimize comments and use constructive coding techniques (meaningful variable & method names, etc)
#####################################

class largestTwo:
    def __init__(self):        
        self.first=None
        self.second=None
    
#aList=[4,2,23] -> assert 23,4
#aList=[1] -> assert 1, None
#aList=[-2,10] -> assert 10, -2
#aList=[-20,10,20,11,13,22,12] assert 22, 20
def findLargest2NumbersOfList(aList):
    #lc.first=
    #lc.second=
    lc=largestTwo()
    for ele in aList: #
        if not lc.first:
            lc.first=ele #
        elif ele > lc.first:
            lc.second=lc.first # 
            lc.first=ele #            
        elif not lc.second or ele > lc.second: #Order is important here! second part short-circuited otherwise potential exception if lc.second is None
            lc.second=ele #
    return lc

def verboseSolution(aList):
    #lc.first=20
    #lc.second=10
    lc=largestTwo()
    
    for ele in aList: #
        if not lc.first:
            lc.first=ele #lc.first=
        elif not lc.second : #
            ###################
            if ele>lc.first:
                lc.second=lc.first
                lc.first=ele
            else
                lc.second=ele #
        elif ele > lc.first:
            lc.second=lc.first #
            lc.first=ele #
        elif ele > lc.second:
            lc.second=ele
    return lc
    
