# WhiteBoard

## Problem Domain
- Given a 2 linked lists, write a function that returns the count of duplicate values

## Input / Output
- Input: (2) singly linked link-lists
- Output: Int that is the total of duplicates

## Test / Edge Cases
- Valid ll
- Empty Lists, 1 or 2
- All nodes are duplicates
- no duplicates
- multiple of the same. ll1: 2 - 2 ll2: 2
- duplicates in same list
- mismatching sizes
- pytest as testing suite

## Visual
counter
1 -> 3 -> 8 -> 13 -> None
                ^
[1, 3, 8, 13]

2 -> 3 -> 8 -> 23 -> None
^
## Algo
define a function that takes 2 ll as arguments
    create a counter variable
    create an empty list
    assign both heads to current variables
    traverse through ll1 and append to list
    traverse through ll2 and check if values in list
    add to counter for each positive
    return counter

## Big0
Time: o(2n) = o(n)
Space: o(n) # creating a new list

## Code
```python
def check_dupes(ll1, ll2):
    counter = 0
    new_list = []
    if ll1.head:
        current1 = ll1.head
    if ll2.head:
        current2 = ll2.head
    if not ll1.head or not ll2.head:
        return "not valid ll"
    while current1:
        new_list.append(current1.value)
        current1 = current1.next
    while current2:
        if current2.value in new_list:
            counter += 1
        current2 = current2.next
    return counter
```
## Walk though
1 -> 1 -> 1 -> 13 -> None
[1, 3, 8, 13]
2 -> 3 -> 1 -> 23 -> None
1
3

