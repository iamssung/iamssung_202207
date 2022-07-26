# Demo3.py
# 복사

# 얕은 복사
a = [1,2,3]
b = a
a[0] = 38
print(a)
print(b)
print(id(a), id(b))

# 깊은 복사
a = [1,2,3]
b = a[:]
a[0] = 38
print(a)
print(b)
print(id(a), id(b))

# 다른 형태 복사
import copy
a = [1,2,3]
b = copy.deepcopy(a)
a[0] = 38
print(a)
print(b)
print(id(a), id(b))
