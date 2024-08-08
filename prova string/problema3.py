frase= input("Frase embaralhada:")
a= len(frase)/2
i= 0
a= int(len(frase)/2)

    
p1= frase[0:a]
p2= frase[a:len(frase)]
frase_total= p1[::-1]+p2[::-1]
frase_total= str(frase_total)
print("Frase correta:", frase_total)
    
       
       