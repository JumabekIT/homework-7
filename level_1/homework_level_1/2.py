# ex 1
                    #   password = clash
password = input("Введите пароль")
if password == "clash":
    print("Password is correct. You are welcome")
else:
    print("Password is uncorrect. Please try again")

# ex 2
temperature = float(input("Введите температуру за окном"))    
if temperature < -30:
    print("Там так холодно, лучше дома сиди!")
elif temperature > -30 and temperature < 0:
    print("Холодновато. Оденься потеплее!")
elif temperature > 0 and temperature < 15:
    print("Прохладно. Куртку накинь!")
elif temperature > 15 and temperature < 30:
    print("Тепло. Иди погуляй в парке!")
elif temperature > 30 and temperature < 50:
    print("Ого, как жарко!")
elif temperature > 50:
    print("Там такая жара, лучше сиди дома!")
else:
    print("Ошибка!")

# ex 3
text = '''Advertig companies say advertising is necessary and important. It informs people about
new products. Advertising hoardings in the street make our environment colourful. And
adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next
programme in the mini-drama. Advertising can educate, too. Adverts tell us about new,
healthy products. And adverts in magazines give us ideas for how to look prettier, be
fashionable and be successful. Without advertising, life is boring and colourless.
But some consumers argue that advertising is a bad thing. They say that advertising is bad
for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers
know we love our children and want to give them everything. So they use children’s ‘pester
power’ to sell their products. Finally, consumers say, if there is advertising there must be
rules. Some adverts advertise unhealthy things like cigarettes and make people waste their
money.'''
print("количство t", text.count("t"))
print("количство s", text.count("s"))

# ex add
str_1 = str("Aidana")
str_2 = str("Adilet")
len = len(str_1)
a = 0
str_3 =""
while a < len:
    str_3 += str_1[a] + str_2[a] 
    a += 1
print(str_3)


