"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.


def foo(x):
  
  if x <= 1:
    return x
    
  else:
    return foo(x-1) + foo(x-2)


  

def longest_run(mylist, key):

    counter1 = 0
    counter2 = 0

    for num in mylist:
      if num == key:
        counter1 += 1
      else:
        counter1 = 0
      if counter1 > counter2:
        counter2 = counter1

    return counter2

      


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):

  #base cases
  if len(mylist) == 1 and mylist[0] == key:
    return Result(1, 1, 1, True)
  if len(mylist) == 1 and mylist[0] != key:
    return Result(0, 0, 0, False)

  #dividing list and recursive call
  left = longest_run_recursive(mylist[:len(mylist)//2], key)
  right = longest_run_recursive(mylist[len(mylist)//2:], key)
  
  #both entire
  if left.is_entire_range and right.is_entire_range:
    run = left.longest_size + right.longest_size
    return Result(left.left_size + left.right_size, right.left_size + right.right_size, run, True)

  #left is entire; right is not
  elif left.is_entire_range:
    if (right.left_size + left.longest_size) <= left.longest_size:
      # condition checks: key does NOT appear in left side of right
      run = left.longest_size
    else:
      # key DOES appear in left side of right
      run = right.left_size + left.longest_size
    return Result(left.left_size + right.left_size, right.right_size, run, False)

  #right is entire; left is not
  elif right.is_entire_range:
    if (left.right_size + right.longest_size) <= right.longest_size:
      # condition checks: key does NOT appear in right side of left
      run = right.longest_size
    else:
      # key DOES appear in right side of left
      run = left.right_size + right.longest_size
    return Result(left.left_size, right.right_size + left.right_size, run, False)

  else:
    
    if (left.right_size + right.left_size) < right.longest_size:
      run = right.longest_size

    elif (left.right_size + right.left_size) < left.longest_size:
      run = left.longest_size

    else:
      run = left.right_size + right.left_size

    return Result(left.left_size, right.right_size, run, False)
    
    
  

## Feel free to add your own tests here.
def test_longest_run():
  assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
  assert longest_run([1,2,4,4,4,4,4], 4) == 5