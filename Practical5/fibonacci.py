print('I want to make a modifiabe version :-P')
#how many terms you want?
n = int(input('how many terms you want?:'))
#define the first two terms
tm1 = int(input('term1:'))
tm2 = int(input('term2:'))
print(tm1)
print(tm2)
#caculate the sequence and print the result
for i in range(2,n):
    tm = tm1 + tm2
    print(tm)
    tm1 = tm2
    tm2 = tm
