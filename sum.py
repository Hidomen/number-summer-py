# LINEER TOTAL : SUMS ALL NUMBER BETWEEN 1-LAST_NUM
# CHALLENGES
    # MAKE IT WITH N(N+1)/2 FORMULA

while True :
    try :
        last_num = int(input("How far? : "))
        break
    except ValueError :
        print("GIMME NUMBER!")

total = 0

for i in range(last_num + 1) :
    total += i

print(f"Total of all numbers between 1-{last_num} = {total}")
