# Cash register rules:
# * The number of articles is unknown at the begining
# * If an item cots more than $100, it will have a 5% discount
# * For every 3 products, you must charge $1 extra for a plastic bag to pack them
# * when there is no more articles, enter 0 or a negative number to end the program

count = 0
total = 0

while True:
    try:
        cost = float(input("Enter the article cost or enter 0 ( or negative) to get the total: "))

        if cost > 0 and cost > 100:
            count +=1
            total += cost*0.95
        
        elif cost > 0 and cost <= 100:
            count += 1
            total += cost

        else: 
            total += count//3
            break

        print("Sub total: $", round(total, 2))

    except:
        print("Invalid input")

print("There is a total of ", count, " articles.")
print("The total is: $", round(total, 2), "with a $", count//3, " charge for the plastic bags.")
