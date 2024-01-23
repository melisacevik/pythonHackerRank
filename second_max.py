# Easy level - Basic Python
# Second Max Value

lst = [10, 20, 4, 45, 99]
m=max(lst)
x=[a for i,a in enumerate(lst) if a<m]
print(max(x))

#Solution

"""
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

if n >= 2 and n <=10:
    m =max(arr)
    x = [ a for i,a in enumerate(arr) if a < m]
    print(max(x))
"""

lst = [4,5,2,4,55,66,77,44,33]
m = max(lst)
x = [s for i,s in enumerate(lst) if s<m]
print(max(x))

# diğer yol new_list adında bir liste oluşturma. ve bu listeden max value'yu cıkarma. yeni listenin max'ını alma

string = "BCDCCDC"
sub_string = "CDC"

substrArray = string.split(sub_string)
substrArray.remove("")
count = len(substrArray)