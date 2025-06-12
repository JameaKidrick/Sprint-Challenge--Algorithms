#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The snippet's line-by-line big-o looks like:
```python
    a = 0                             O(1)
    while (a < n * n * n):          O(n)
      a = a + n * n                   O(1)
```
Lines 7 and 9 are all individual statements which are O(1) while loops are O(however many elements there are).

Multiply the body of the loops times the loops themselves:
O(1)
O(n * 1)

Add sequences:
O(1 + n * 1)

Final Answer:
O(1 + n)



b)The snippet's line-by-line big-o looks like:
```
    sum = 0                           O(1)
    for i in range(n):              O(n)
      j = 1                           O(1)
      while j < n:                  O(n)
        j *= 2                        O(1)
        sum += 1                      O(1)
```
Lines 15, 17, 19, and 20 are all individual statements which are O(1) while loops are O(however many elements there are). Adding up the Os of lines 19 and 20 we get O(2):

O(1)
O(n)
  O(1)
  O(n)
    O(2)

Multiply the body of the loops times the loops themselves except for those that have more than one item in their body:
O(1)
O(n * 1)
  O(1)
  O(n * 2)

Add sequences
O(1)
O(n * 1)


Multiply body of loops: 
O(1)
O(n * 1 * (1 + n * 2))

Add sequences:
O(1 + n * 1 * (1 + n * 2))

Math: 
1 + n * (1 + 2n)
1 + 1n + 3n

Final Answer:
O(1 + 4n)



c)The snippet's line-by-line big-o looks like:
```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0                        O(1)

      return 2 + bunnyEars(bunnies-1)   O(n ^ n)
```

Final Answer:
Run time may be halved, doubled, tripled, etc each step based on the the number of bunnies - 1, so the answer is O(n ^ n).


## Exercise II
Most efficient method: Binary search - O(n)

Cut the floor range in half
Drop an egg
If the egg breaks, cut the left side in half, drop an egg
If the egg does not break, cut the right side in half, drop an egg
Repeat until you find the floor


Less efficient method: Linear search - O(n)

Loop through range of 0 to the number of floors
Drop an egg for each floor
If broken, return position
Stop loop

Final Answer:
Binary search is the most efficient because, although both binary and linear are O(n), the binary search takes less developer and computer time. Also, in terms of the problem, you are using less eggs.
