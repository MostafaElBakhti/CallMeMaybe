from collections.abc import Callable




def mage_counter() -> Callable:
    count = 0 
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

def test():
    count = 0
    count += 1
    return count

res = test()
res = test()
print(res)

c1 = mage_counter()



# print(c1())  # 1
# print(c1())  # 2
# print(c1())  # 3

