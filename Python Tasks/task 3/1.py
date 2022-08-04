# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath;

num = complex(input())
z = complex(num)

print(cmath.polar(z)[0])
print(cmath.polar(z)[1])