**Mild**

```py
def example1(n):
    for i in range(n):
        print(i)
```
1. O(n) - single for loop

```py
def example2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
```
2. O(n^2) - nested for loop

```py
def example3(n):
    i = 0
    while i < n:
        print(i)
        i += 2
```
3. O(n) - 'i' increases linearly; the iterations depend on n

```py
def example4(n):
    if n > 9:
        n = 9
    print(n)
```
4. O(1) - There are no loops!

```py
def example5(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
```
5. O(n) - There are 2 loops, but they are not nested; 2n = n for these purposes.

**Medium**

```py
def example6(n):
    i = 0
    while False:
        print(i)
        i += 2
```
6. O(1) - "while False" will never loop

```py
def example7(n):
    i = 1
    while i < n:
        print(i)
        i = i * 2
```
7. O(log n) - because i is incremented exponentially, the end of the looping comes much quicker than if it were increasing linearly. Try plugging in 100! This is similar to binary search.

```py
def example8(n):
    for i in range(n):
        for j in range(i, n):
            print(i, j)
```
8. O(n^2)

```py
def example9(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
            break
```
9. O(n) - Tricky! the `break` doesn't allow for any more looping from that inner loop. It will only happen once.

**Spicy**

```py
def example10(n):
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                print(i, j, k)
```
10. O(n^3) - 3 for loops all nested

```py
def example11(n):
    if n > 100:
        print("too big")
    elif n > 0:
        for i in range(n):
            print(i)
    else:
        print("too small")
```
11. O(n) - if else doesn't add to time complexity (still only 3 statements no matter the size of n). But, there is 1 for loop in there. 

```py
def example12(n):
    print(n)
    if n <= 1:
        print("Hurray!")
    else:
        example12(n-1)
```
12. O(n) - Recursion replaces a loop! (...and takes up more memory)