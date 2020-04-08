from concurrent.futures import ProcessPoolExecutor


def fib(n):
  if n > 30:
    return n
  if n <= 2:
    return 1


nums = [13, 17, 0, 22, 19, 33, 7, 12, 8, 16]
'''

'''
with ProcessPoolExecutor() as executor:
    try:
      results = executor.map(fib, nums)
      for num, result in zip(nums, results):
        print('fib(%s) result is %s.' % (num, result))
    except Exception as e:
      print(e)