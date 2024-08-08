def has_duplicates(l):
    cont=1

    for i in range(len(l)-1):
        for t in range(cont,len(l)):
            if l[i]==l[t]:
                return True
        cont= cont+1
    return False


        
        
        

#usar .count, if ==0 True, if !=0 False
    
    
    
    