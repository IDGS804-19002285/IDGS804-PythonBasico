def tabla():

x= int(input("Dame un numero: "))

for y in range(1,11):
    res=x*y
    print('{} x {} = {}'.format(x,y,res))

tabla()