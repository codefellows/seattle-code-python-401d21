def reverse_list1(things):
    return things[::-1]

def reverse_list2(things):
    things.reverse()
    return things

def reverse_list3(things):
    left = 0
    right = len(things) - 1
    while left < right:
      # things[left], things[right] = things[right], things[left]

      temp = things[left]
      things[left] = things[right]
      things[right] = temp
      left += 1
      right -= 1

# [4, 3, 2, 1]
# temp 2

# left 2:2
# right 1:3
