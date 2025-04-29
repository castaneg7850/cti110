# Gabriel Castaneda
# 4/24/2025
# P4HW1_CastanedaGabriel
# Scores

score_num = int(input("How many scored do you wan to enter? "))
print()

scores = []

for num in range(1, score_num + 1):
    score = float(input("Enter score #" + str(num)+ ":"))
    while score < 0 or score > 100:
        print("INVALID SCORE ENTERED!!!")
        print("Score should be between 0 and 100")
        score = float(input("Enter score #" + str(num) +"again: "))
    scores.append(score)
    print()    

lowest = min(scores)
scores.remove(lowest)
avg = sum(scores)/ len(scores)

if avg >= 90:
    Grade= 'A'
elif avg >= 80:
    Grade= 'B' 
elif avg >= 70:
    Grade= 'C'
elif avg >= 60:
    Grade= 'D'
else:
    Grade= 'F'

print("\n------------Results------------")
print(f"Lowest Score     : {lowest:.1f}")
print(f"Modified List    : {scores}")
print(f"Scores Average   : {avg:.2f}")
print(f"Grade            : {Grade}")
print("------------------------------")