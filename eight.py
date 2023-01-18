#Check the parentheses. You have 3 types of parentheses () [] {}, for example! ({{}} {] []}})! Check that each open
#parenthesis has a closing parenthesis.

paratn = "{{}} {] []}}"

count = 0

for i in paratn:
    if i == "{" or i == "(" or i == "[":
        count += 1
    if i == "}"  or i == ")" or i == "]":
        count -= 1

if count == 0:
    print("each open parenthesis has a closing parenthesis")
else:
    print("There are mistake")
