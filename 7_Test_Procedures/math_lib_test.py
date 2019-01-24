from math_lib import pow_native
def test_res(res):
    return "Pass" if res else "Fail"

print("Math_TC_1 result: " + test_res(pow_native(0, 0) == 1))
print("Math_TC_2 result: " + test_res(pow_native(10, 0) == 1))

print("Math_TC_3 result: " + test_res(pow_native(2, 2) == 4))
print("Math_TC_4 result: " + test_res(pow_native(3, 5) == 243))

print("Math_TC_5 result: " + test_res(pow_native(4, -4) == 0.00390625))
print("Math_TC_6 result: " + test_res(pow_native(2, -7) == 0.00781251))

print("Math_TC_7 result: " + test_res(pow_native(0, -1) == 1))
