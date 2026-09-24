# ---- problem 1 ----

n = 23

prime_num = True 

if n <= 1:
    prime_num = False
else:
    # check for factors from 2 up to n - 1
    for i in range(2, n):
        if n % i == 0:
            prime_num = False
            break

if prime_num:
    print(n, "is a prime number.")
else: 
    print(n, "is not a prime number.")

#  ---- problem 2 ----

n = 49

square_num = False

if n >= 0:
    # test int root from 0 to n
    for i in range(n + 1):
        if i * i == n:
            square_num = True
            break

if square_num:
    print(n, "is a square number.")
else: 
    print(n, "is not a square number.")
    
# --- problem 3 ---

a = 2 # coeff for x^2
b = 3 # coeff for x
c = 1 # const term
n = 1000 # num of rect

start_x = 0
end_x = 5

total_area = 0
            
for i in range(n):
    x = start_x + (i * (end_x - start_x)) / n
    height = a * (x ** 2) + b * x + c
    area = height * ((end_x - start_x) / n)
    total_area += area
    
print("Estimated definite integral from 0 to 5:", total_area)

# --- problem 3b ---

n = 7 # set the target item index n

if n == 0:
    fib_num = 0
elif n == 1:
    fib_num = 1
else:
    prev = 0
    curr = 1
    for i in range(2, n + 1):
        next_num = prev + curr
        prev = curr
        curr = next_num 
    fib_num = curr

print("The", n, "th Fibonacci number is:", fib_num)




                
