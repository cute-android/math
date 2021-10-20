import matplotlib.pyplot as plt

num = int(input("Enter your favourite number: "))
plt.title('Collatz for number: ' + str(num))

y=[]

i = 0
while num != 1: 
    if num%2 == 0: 
        y.append(int(num/2))
    else:
        y.append(3*num+1)
    num = y[i]
    i = i + 1

x=[]
for n in range(i):
    x.append(n+1)
    #Uncomment if you want to see labels
    #plt.text(x[n],y[n]+1, "[ " + str(x[n]) + ", " + str(y[n]) + " ]") 


#Uncomment if you want to see the generated sets
#print(x)
#print(y)
plt.scatter(x,y)
plt.plot(x,y)
plt.show()