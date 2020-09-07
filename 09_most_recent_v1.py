conv_his = []

for i in range(5):
    conv_his.append(input("Enter an item: "))

print("="*15)

for conv in range(1, 6):
    print(conv_his[-conv])

print("="*15)