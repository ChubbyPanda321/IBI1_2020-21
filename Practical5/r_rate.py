print('I want to make a modifiable version that you can change the r_rate easier :-P')
#define the variables
r = float(input('r_rate='))
n = 84
#caculate the number of infected individuals and remove the decimal
for i in range(1,6):
    n = n*(r+1)
n = int(n)
#print the result
print(str(n)+' individuals are infected after 5 generations with r='+str(r))
