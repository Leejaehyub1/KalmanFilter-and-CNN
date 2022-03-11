num = int(input("몇 명? "))
grade_high = []
grade_low = []
sum_high = 0
sum_low = 0

for i in range(num):
    grade = int(input("성적> "))
    if grade >= 80:
        grade_high.append(grade)
        sum_high += grade
    else:
        grade_low.append(grade)
        sum_low += grade

print()
print("<상위 집단>")
print("평균 = %f"%(sum_high/len(grade_high)))
print("인원 = %d 명"%len(grade_high))
print()
print("<하위 집단>")
print("평균 = %f"%(sum_low/len(grade_low)))
print("인원 = %d 명"%len(grade_low))

