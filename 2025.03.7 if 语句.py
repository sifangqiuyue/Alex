is_hot= True
is_cold=False
if is_hot:
    print("It's a hot day")
    print("多喝水")
elif is_cold:
    print("天冷多穿衣服")
else:
    print("今天是个好天气")
    
print("Enjoy your day")
A=10000
a=False
b=False
if a:
    c=A*0.1
elif b:
    c=A*0.2
else:
    c=A*0.15
print(f"你应付{c}元，祝各位业主入住愉快")
name="guoshiqi"
if len(name)<3:
    print("name must be at least 3 characters")
elif len(name)>50:
    print("name can be a maximum of 50 characters")
else:
    print("good name")