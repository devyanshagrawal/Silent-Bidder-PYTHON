import os
print()
print(" "*20 + "!!!! WELCOME TO SILENT BIDDING !!!!")
print()

records = {'name': [], 'bid_amount': []}

def silent_bid(name1, bid_amount1):
    records['name'].append(name1)
    records['bid_amount'].append(bid_amount1)

def select_winner():
    max = records['bid_amount'][0]
    ind = 0
    for i in range(len(records['bid_amount'])):
        if records['bid_amount'][i]>max:
            max = records['bid_amount'][i]
            ind = i

    return ind

if __name__ == "__main__":
    flag = 0
    while flag == 0:
        name = input("Enter name: ")
        amnt = int(input("Enter amount: $"))

        silent_bid(name1=name, bid_amount1=amnt)

        flag = int(input("Enter 0 if more person to bid, else enter 1: "))
        os.system('clear')
    print()
    print(f'Winner is {records["name"][select_winner()]} with ${records["bid_amount"][select_winner()]}!')
    print()