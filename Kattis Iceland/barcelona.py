bags, bennis_bag = map(int, input().split())

all_bags = list(map(int, input().split()))

for count, bag in enumerate(all_bags):
    if bag == bennis_bag:
        if count == 0:
            print ("fyrst")
        elif count == 1:
            print ("naestfyrst")
        else:
            print (count+1, "fyrst")
        