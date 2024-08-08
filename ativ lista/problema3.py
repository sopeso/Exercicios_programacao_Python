todos=[]
pares[]
impares=[]
for i in range(5):
    todo = int(input())
    todos.append(todo)
        if todo % 2==0:
            pares.append(todo)
        else:
            impares.append(todo)
            
print(todos)
print(pares)
print(impares)
    
