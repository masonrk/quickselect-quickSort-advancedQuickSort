import random
import time
import sys
sys.setrecursionlimit(10**8) #change recursion limit

def partition(array, low, high):
    pivot = array[high] #set pivot to value in highest position in array
    i = low - 1 #decrement i
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1 #increment i
            array[i],array[j] = array[j],array[i] #swap
    array[i+1],array[high] = array[high],array[i+1] #swap
    return i+1 #return value plus 1

def quick_partition(array, low, high):
    #use quickselect to return the value that is in high position for the pivot
    pivot = quickselect(array,low,high,len(array)-1)
    i = low - 1 #decrement i
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1 #increment i
            array[i],array[j] = array[j],array[i] #swap
    array[i+1],array[high] = array[high],array[i+1] #swap
    return i+1 #return value plus 1


def quickselect(array, low, high, pos):
   pos = int(pos)
   while low <= high:
       # call the partition and set the pivot to it in this
       # case it is the high positition value
       pivot = partition(array,low,high)
       if pos - 1 == pivot:
           return array[pos] #return the value
       elif pos - 1 < pivot:
           high = pivot - 1 #decrease the rightmost position
       else:
           low = pivot + 1 #increase the left most position
   return 0

def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high) #call partition function
        #recursive quicksort calls
        quicksort(array, low, pi-1)
        quicksort(array, pi+1, high)
def adv_quicksort(array, low, high):
    if low < high:
        pi = quick_partition(array, low, high) #call partition method that uses quicksort
        #recursive quicksort calls
        quicksort(array, low, pi-1)
        quicksort(array, pi+1, high)
#loop to execute 10 times
for i in range(10):
    #define all the arrays
    oneArray = []
    twoArray = []
    thrArray = []
    forArray = []
    fivArray = []
    tmpArray1 = []
    tmpArray2 = []
    tmpArray3 = []
    tmpArray4 = []
    tmpArray5 = []
    #create all the arrays
    for i in range(500000):
        if i < 100000:
            oneArray.insert(i, random.randint(1,1000000))
        if i < 200000:
            twoArray.insert(i, random.randint(1, 1000000))
        if i < 300000:
            thrArray.insert(i, random.randint(1, 1000000))
        if i < 400000:
            forArray.insert(i, random.randint(1, 1000000))
        if i < 500000:
            fivArray.insert(i, random.randint(1, 1000000))
    #this copys the arrays that were created
    tmpArray1 = oneArray.copy()
    tmpArray2 = twoArray.copy()
    tmpArray3 = thrArray.copy()
    tmpArray4 = forArray.copy()
    tmpArray5 = fivArray.copy()
##################################quickselect#########################################
    print("quickselect")
    startime = time.time() #start timer
    quick_median = (quickselect(oneArray, 0, len(oneArray) - 1, (len(oneArray) / 2)))
    print(time.time() - startime)    #end timer
    print(quick_median)
    startime = time.time()  #start timer
    quick_median = (quickselect(twoArray, 0, len(twoArray) - 1, (len(twoArray) / 2)))
    print(time.time() - startime)    #end timer
    print(quick_median)
    startime = time.time()  #start timer
    quick_median = (quickselect(thrArray, 0, len(thrArray) - 1, (len(thrArray) / 2)))
    print(time.time() - startime)    #end timer
    print(quick_median)
    startime = time.time()  #start timer
    quick_median = (quickselect(forArray, 0, len(forArray) - 1, (len(forArray) / 2)))
    print(time.time() - startime)    #end timer
    print(quick_median)
    startime = time.time()  #start timer
    quick_median = (quickselect(fivArray, 0, len(fivArray) - 1, (len(fivArray) / 2)))
    print(time.time() - startime)    #end timer
    print(quick_median)
####################quicksort method##########################
    print("quicksort")
    startime = time.time()  #start timer
    quicksort(oneArray,0,len(oneArray)-1)
    print(time.time() - startime)    #end timer
    print(oneArray[50000])
    startime = time.time()  #start timer
    quicksort(twoArray,0,len(twoArray)-1)
    print(time.time() - startime)    #end timer
    print(twoArray[100000])
    startime = time.time()  #start timer
    quicksort(thrArray,0,len(thrArray)-1)
    print(time.time() - startime)    #end timer
    print(thrArray[150000])
    startime = time.time()  #start timer
    quicksort(forArray,0,len(forArray)-1)
    print(time.time() - startime)    #end timer
    print(forArray[200000])
    startime = time.time()  #start timer
    quicksort(fivArray,0,len(fivArray)-1)
    print(time.time() - startime)    #end timer
    print(fivArray[250000])
    ######################### advanced quicksort ###############################
    print("advanced quicksort")
    startime = time.time()  #start timer
    adv_quicksort(tmpArray1,0,len(tmpArray1)-1)
    print(time.time() - startime)    #end timer
    print(tmpArray1[50000])
    startime = time.time()  #start timer
    adv_quicksort(tmpArray2,0,len(tmpArray2)-1)
    print(time.time() - startime)    #end timer
    print(tmpArray2[100000])
    startime = time.time()  #start timer
    adv_quicksort(tmpArray3,0,len(tmpArray3)-1)
    print(time.time() - startime)    #end timer
    print(tmpArray3[150000])
    startime = time.time()  #start timer
    adv_quicksort(tmpArray4,0,len(tmpArray4)-1)
    print(time.time() - startime)    #end timer
    print(tmpArray4[200000])
    startime = time.time()  #start timer
    adv_quicksort(tmpArray5,0,len(tmpArray5)-1)
    print(time.time() - startime)
    print(tmpArray5[250000])    #end timer
