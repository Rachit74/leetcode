

def productExceptSelf(nums: list) -> list :

    n = len(nums)
    output = [1]*n
    
    # We first put the product into the output,
    # then we update the product using the current index. 

    # left product
    left = 1
    for i in range(n):
        output[i] = left
        left = left * nums[i]

    # right product
    right = 1
    # pythons range function can have (start, stop, step_size)
    for i in range(n-1, -1, -1):
        output[i] = output[i] * right
        right = right * nums[i]

    print(nums)
    print(output)


nums = [1,2,4,6]

productExceptSelf(nums)