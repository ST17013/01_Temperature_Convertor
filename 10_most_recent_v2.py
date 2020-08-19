conv_his = []

get_item = " "

while get_item:
    get_item = input("Enter an item: ")
    if get_item:
        conv_his.append(get_item)

print("="*15)

if len(conv_his) == 0:
    print("List Empty!")
elif len(conv_his) >= 3:
    for conv in range(1, 4):
        print(conv_his[-conv])
else:
    for conv in range(1, len(conv_his)+1):
        print(conv_his[-conv])

print("="*15)