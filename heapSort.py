import datetime
import os
import csv

MYDIR = os.path.dirname(__file__)
class Heap: # Parent class for common functions between minHeap and maxHeap
    def __init__(self,filename):
        self.filename=filename
        self.a=[]    
    def load_insert(self):
        print("file:",self.filename)
        print("mydir",MYDIR)
        if not os.path.isfile(self.filename):
            print("File path {} does not exist. Exiting...".format(filename))   
            
        with open(self.filename, newline='\n') as f:
            txt_line=f.readlines()
            i=0
            for line in txt_line:
                i+=1
                s=line.strip()#.replace(" ","")
                if i<10 or i%10000==0:
                    pass
                    #print(s)
                    ######## Change append to insert function
                self.insert(int(s))
    def deleteByLoad(self):
        with open(self.filename, newline='\n') as f:
            txt_line=f.readlines()
            i=0
            for line in txt_line:
                i+=1
                s=line.strip()#.replace(" ","")
                self.delItem(int(s))
                if i%1000==0:
                    print("removal at index=",i)
                    #if i>49000:
                    #    print(self.a)
                #'''# WARNING: checkHeap() at every iteration increases run time by factor of 30x !!!!!!!!
                if i%5000==0 and not self.checkHeap():
                    print("heap mis-sort at line i=",i)
                    break
                #'''
    def delItem(self,dVal):
        loc=self.a.index(dVal)
        #print("tail,cur item=",self.a[-1]," ",self.a[loc])
        self.a[loc]=self.a[-1] #move last item to loc
        oldSize=len(self.a)
        self.a=self.a[:-1] #remove last item
        size=len(self.a)
        #print("old, new size:",oldSize," ",size," i rem=",loc)
        #Now move the [loc] item back down the heap until sorted
        self.heapify(loc)#int((loc-1)/2))
        #################################
        '''
        cur=loc #Now heapify from loc down the tree (as a large item was moved here)
        child=2*cur+1
        while child<size:
            if self.a[cur] > self.a[child]:
                #swap
                temp=self.a[cur]
                self.a[cur]=self.a[child]
                self.a[child]=temp            
            elif 2*cur+2<size:
                ch2=2*cur+2
                if self.a[cur] > self.a[ch2]:
                    #swap
                    temp=self.a[cur]
                    self.a[cur]=self.a[ch2]
                    self.a[ch2]=temp            
                    #print("Swapping i*2+2, i=",cur)
                pass
            cur=child
            child=2*cur+1
        pass
        '''
        
        
class minHeap(Heap):
    def __init__(self,filename):
        super().__init__(filename)        
        
    def insert(self,elem):
        self.a.append(elem)
        s=len(self.a)-1
        # is the index of element just inserted. Now compare to parent (s-1)/2
        p=int((s-1)/2)
                            
        while p>=0 and s>0:

            if self.a[s] < self.a[p]:
                #swap
                temp=self.a[s]
                self.a[s]=self.a[p]
                self.a[p]=temp    
            s=p
            p=int((s-1)/2)
    def traverse(self):
        print("start traverse")
        i=0
        s=len(self.a)
        for l in self.a:
            i+=1
            '''
            if i%1000==0:
                pass
                #print(l)
            '''
            print(l)
            if 2*i+1<s:
                if self.a[i]>self.a[2*i+1]:
                    print("ERROR: traverse, not a min heap")            
            if 2*i+2<s:
                if self.a[i]>self.a[2*i+2]:
                    print("ERROR: traverse, not a min heap")
            #'''
        #print(self.a[:100])        
        pass
    def checkHeap(self): #Verify after insert and delete that actually a heap
        i=0
        s=len(self.a)

        for i in range(int((s-1)/2)):
            i+=1
            if 2*i+1<s:
                if self.a[i]>self.a[2*i+1]:
                    print("not a min heap (left),i=%s, c=%s"%(i,2*i+1))  
                    print("heap condition (20 adjacent values at index, child)")
                    print(self.a[i],self.a[i-10:i+10])
                    print(self.a[2*i+1],self.a[2*i+1-10:2*i+1+10])
                    return False
            if 2*i+2<s:
                if self.a[i]>self.a[2*i+2]:
                    print("not a min heap(right),i=%s"%(i))
                    print("heap condition (20 adjacent values at index, child)")
                    print(self.a[i],self.a[i-10:i+10])
                    print(self.a[2*i+2],self.a[2*i+2-10:2*i+2+10])
                    
                    return False
        return True
    

    def heapify(self,cur,checkPar=False):# checkPar = check parent after swapping current node/left/right child
        #print("heap sort loc=",cur)
        size=len(self.a)
        if cur>=size:
            return
        p=int((cur-1)/2)
        if self.a[p]> self.a[cur]:
            #print("WARNING, parent not sorted, need to move up tree not down, sorting parent=",p)#," ",int((p-1)/2))
            self.heapify(p,checkPar=True)
        else:    
            child=2*cur+1
            if child>=size:
                return
            ch2=2*cur+2
            # go left or right first?
            left=True
            if ch2<size and self.a[child]>self.a[ch2]:
                left=False
            if left:
                if self.a[cur] > self.a[child]:
                    #swap
                    #print("swap L: ",self.a[cur]," ",self.a[child])
                    temp=self.a[cur]
                    self.a[cur]=self.a[child]
                    self.a[child]=temp                    
                    #print("swap L after: ",self.a[cur]," ",self.a[child])
            elif ch2<size: #check right side
                if self.a[cur] > self.a[ch2]:
                    #swap
                    #print("swap R")
                    temp=self.a[cur]
                    self.a[cur]=self.a[ch2]
                    self.a[ch2]=temp             
            '''if not left: #if went right first, now check left second (not left)
                if self.a[cur] > self.a[child]:
                    #swap
                    print("swap L (after R)")
                    temp=self.a[cur]
                    self.a[cur]=self.a[child]
                    self.a[child]=temp                    
            '''
            if checkPar and self.a[p]> self.a[cur]:
                #print("WARNING, parent not sorted (again), need to move up tree not down, sorting parent=",p)#," ",int((p-1)/2))
                self.heapify(p,checkPar=True)
            if left:
                self.heapify(2*cur+1)
            else:
                self.heapify(2*cur+2)

class maxHeap(Heap):
    def __init__(self,filename):
        super().__init__(filename)        
        
    def insert(self,elem):
        self.a.append(elem)
        s=len(self.a)-1
        # is the index of element just inserted. Now compare to parent (s-1)/2
        p=int((s-1)/2)
                            
        while p>=0 and s>0:

            if self.a[s] > self.a[p]:
                #swap
                temp=self.a[s]
                self.a[s]=self.a[p]
                self.a[p]=temp    
            s=p
            p=int((s-1)/2)
    def traverse(self):
        print("start traverse")
        i=0
        s=len(self.a)
        for l in self.a:
            i+=1
            '''if i%1000==0:
                pass
                print(l)
            '''
            print(l)
            if 2*i+1<s:
                if self.a[i]<self.a[2*i+1]:
                    print("ERROR: traverse, not a max heap")            
            if 2*i+2<s:
                if self.a[i]<self.a[2*i+2]:
                    print("ERROR: traverse, not a max heap")
            #'''
        #print(self.a[:100])        
        pass
    def checkHeap(self): #Verify after insert and delete that actually a heap
        i=0
        s=len(self.a)

        for i in range(int((s-1)/2)):
            i+=1
            if 2*i+1<s:
                if self.a[i]<self.a[2*i+1]:
                    print("not a max heap (left),i=%s, c=%s"%(i,2*i+1))  
                    print("heap condition (20 adjacent values at index, child)")
                    print(self.a[i],self.a[i-10:i+10])
                    print(self.a[2*i+1],self.a[2*i+1-10:2*i+1+10])
                    return False
            if 2*i+2<s:
                if self.a[i]<self.a[2*i+2]:
                    print("not a max heap(right),i=%s"%(i))
                    print("heap condition (20 adjacent values at index, child)")
                    print(self.a[i],self.a[i-10:i+10])
                    print(self.a[2*i+2],self.a[2*i+2-10:2*i+2+10])
                    
                    return False
        return True
    

    def heapify(self,cur,checkPar=False):# checkPar = check parent after swapping current node/left/right child
        #print("heap sort loc=",cur)
        size=len(self.a)
        if cur>=size:
            return
        p=int((cur-1)/2)
        if self.a[p]< self.a[cur]:
            #print("WARNING, parent not sorted, need to move up tree not down, sorting parent=",p)#," ",int((p-1)/2))
            self.heapify(p,checkPar=True)
        else:    
            child=2*cur+1
            if child>=size:
                return
            ch2=2*cur+2
            # go left or right first?
            left=True
            if ch2<size and self.a[child]<self.a[ch2]:
                left=False
            if left:
                if self.a[cur] < self.a[child]:
                    #swap
                    #print("swap L: ",self.a[cur]," ",self.a[child])
                    temp=self.a[cur]
                    self.a[cur]=self.a[child]
                    self.a[child]=temp                    
                    #print("swap L after: ",self.a[cur]," ",self.a[child])
            elif ch2<size: #check right side
                if self.a[cur] < self.a[ch2]:
                    #swap
                    #print("swap R")
                    temp=self.a[cur]
                    self.a[cur]=self.a[ch2]
                    self.a[ch2]=temp             
            '''if not left: #if went right first, now check left second (not left)
                if self.a[cur] > self.a[child]:
                    #swap
                    print("swap L (after R)")
                    temp=self.a[cur]
                    self.a[cur]=self.a[child]
                    self.a[child]=temp                    
            '''
            if checkPar and self.a[p] < self.a[cur]:
                #print("WARNING, parent not sorted (again), need to move up tree not down, sorting parent=",p)#," ",int((p-1)/2))
                self.heapify(p,checkPar=True)
            if left:
                self.heapify(2*cur+1)
            else:
                self.heapify(2*cur+2)
                
                
def runInput(size,sort):
    modelType="min" #*** Change this variable to switch from min/max heap
    #modelType="max" #*** Change this variable to switch from min/max heap
    
    filename=None
    time_a=datetime.datetime.now()
    if size ==50000:
        file_part_A="50k"
    elif size ==5000:
        file_part_A="5k"
    else:
        file_part_A="500"
    if sort=="unsorted":
        file_part_B="unsort"
    elif sort=="asc":
        file_part_B="asc"
    else:
        file_part_B="desc"
    
    filename=file_part_A+"_"+file_part_B+".txt"
    
    if modelType=="min":
        print("min heap selected")
        obj=minHeap(filename)
    else:
        print("max heap selected")
        obj=maxHeap(filename)       
    
    
    obj.load_insert()
    time_b=datetime.datetime.now()
    insert=time_b-time_a
    obj.traverse()
    time_c=datetime.datetime.now()    
    traverse=time_c-time_b
    #'''
    obj.deleteByLoad()
    time_d=datetime.datetime.now()
    
    delete_time=time_d-time_c
    print("Insert total seconds elapsed: ",insert.total_seconds())
    print("Traverse total seconds elapsed: ",traverse.total_seconds())
    print("Delete net seconds elapsed: ",delete_time.total_seconds(),"\n\n")
    #'''
    
if __name__ == "__main__": 
    #Tested on Python 3.7
    #Commandline usage: > python proj.py
    #Switch from Min Heap to Max Heap in runInput function, modelType="min" / "max"
    # Change first parameter in runInput() from 500, 5000, 50000
    # Change second param in runInput() from "unsorted" (Random), "asc" (Ascending), "desc" (Descending)
    
    runInput(50000,"unsorted")
    #runInput(50000,"asc")
    #runInput(50000,"desc")
    
    
    #runInput(5000,"unsorted")
    #runInput(5000,"asc")
    #runInput(5000,"desc")
    
    
    #runInput(500,"unsorted")
    #runInput(500,"asc")
    #runInput(500,"desc")
    
    