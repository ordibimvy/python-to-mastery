# I liked this solution to a problem I was given.

#Given a string. Cut it into two "equal" parts (If the length of the string is odd, 
#place the center character in the first string, so that the first string contains 
#one more characther than the second). Now print a new string on a single row with 
#the first and second halfs interchanged (second half first and the first half second)

s = input()

mid_pt = (len(s) // 2) + (len(s) % 2) # handles the odd numbers

first_half  = s[:mid_pt]
second_half = s[mid_pt:]

print(second_half + first_half)
