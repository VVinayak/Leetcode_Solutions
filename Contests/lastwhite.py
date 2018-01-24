# // You are given a jar of W white beans and R red beans.
# // You are hungry, but you prefer the white beans, so you choose the next bean to eat using the following process:
# // Randomly select a bean from the jar and if it is white, eat it.  Otherwise return the bean to the jar and select randomly again and eat the bean regardless of color.
# // w -> eat white
# // rw -> eat white
# // rr -> eat red
# // What is the probability that the final/last bean consumed is white?

def Lastwhite(num_white, num_red):
    buckets = [[0 for col in range(num_red+1)] for row in range(num_white+1)]
    #storing the probabilities of having the last bean white with i white beans and j red beans before
    
    if num_white == 0 and num_red == 0:
        return 0
    elif num_white == 0:
        return 0
    elif num_red == 0:
        return 1
        
    for i in range(1,num_white+1):
        for j in range(num_red+1):
            if j==0:
                buckets[i][j] = 1.0
            else:
                buckets[i][j] = 1.0*(float(i)/(i+j))*buckets[i-1][j] + 1.0*(float(j)/(j+i))*((i/(i+j))*buckets[i-1][j]+(float(j)/(i+j)*buckets[i][j-1]))
                
    print buckets
    return buckets[num_white][num_red]
     
def main():
    white = input("Number of white beans = ")
    red = input("Number of red beans = ")
    print Lastwhite(white, red)
    
if __name__ == '__main__':
    main()