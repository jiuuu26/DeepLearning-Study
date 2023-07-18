## 💡Python
### [Basic data types]
<b>- Numbers</b>  

&nbsp; 파이썬에서는 x++ 이나 x--와 같은 단항 계산을 하지 않는다.    
```python
x = 3
print(type(x)) # Prints "<class 'int'>"
print(x)       # Prints "3"
print(x + 1)   # Addition; prints "4"
print(x - 1)   # Subtraction; prints "2"
print(x * 2)   # Multiplication; prints "6"
print(x ** 2)  # Exponentiation; prints "9"
x += 1
print(x)  # Prints "4"
x *= 2
print(x)  # Prints "8"
y = 2.5
print(type(y)) # Prints "<class 'float'>"
print(y, y + 1, y * 2, y ** 2) # Prints "2.5 3.5 5.0 6.25"
```

<b>- Booleans </b>  

&nbsp; &&, ||을 쓰는 다른 언어들과 달리 and, or과 같은 영어 단어를 사용한다. 
```python
t = True
f = False
print(type(t)) # Prints "<class 'bool'>"
print(t and f) # Logical AND; prints "False"
print(t or f)  # Logical OR; prints "True"
print(not t)   # Logical NOT; prints "False"
print(t != f)  # Logical XOR; prints "True"
```
<b>- Strings </b>  

&nbsp; capitalize()는 앞의 문자를 대문자로 변경해주는 함수이고 upper()은 전체 문자를 대문자로 변경해주는 함수이다. rjust()는 괄호 안에 넣은 숫자만큼 단어의 길이를 조절해주기 위해 공백을 추가하는 함수이다. 비슷하게 center()은 괄호 안의 숫자만큼 단어의 길이를 조절해주기 위해 양쪽에 공백을 추가하는 함수이다. replace()는 좌측의 문자를 우측의 문자로 변경해주는 함수이며, strip()은 해당 문자의 공백을 없애주는 함수이다.

```python
hello = 'hello'    # String literals can use single quotes
world = "world"    # or double quotes; it does not matter.
print(hello)       # Prints "hello"
print(len(hello))  # String length; prints "5"
hw = hello + ' ' + world  # String concatenation
print(hw)  # prints "hello world"
hw12 = '%s %s %d' % (hello, world, 12)  # sprintf style string formatting
print(hw12)  # prints "hello world 12"

s = "hello"
print(s.capitalize())  # Capitalize a string; prints "Hello"
print(s.upper())       # Convert a string to uppercase; prints "HELLO"
print(s.rjust(7))      # Right-justify a string, padding with spaces; prints "  hello"
print(s.center(7))     # Center a string, padding with spaces; prints " hello "
print(s.replace('l', '(ell)'))  # Replace all instances of one substring with another;
                                # prints "he(ell)(ell)o"
print('  world '.strip())  # Strip leading and trailing whitespace; prints "world"
```

### [Containers]
#### ✔️ Lists
&nbsp; 파이썬에서의 배열이면서, 사이즈를 재조정하고 다른 type의 요소를 포함할 수 있다는 것이 특징이다. 여기서 pop()은 list의 마지막 요소를 제거하고 반환하는 함수이다. 
```python
xs = [3, 1, 2]    # Create a list
print(xs, xs[2])  # Prints "[3, 1, 2] 2"
print(xs[-1])     # Negative indices count from the end of the list; prints "2"
xs[2] = 'foo'     # Lists can contain elements of different types
print(xs)         # Prints "[3, 1, 'foo']"
xs.append('bar')  # Add a new element to the end of the list
print(xs)         # Prints "[3, 1, 'foo', 'bar']"
x = xs.pop()      # Remove and return the last element of the list
print(x, xs)      # Prints "bar [3, 1, 'foo']"
```
<b>- Slicing </b> 
&nbsp; slicing인 [ : ]에서 오른쪽에 오는 요소는 뺀다고 생각하면 된다. 
```python
nums = list(range(5))     # range is a built-in function that creates a list of integers
print(nums)               # Prints "[0, 1, 2, 3, 4]"
print(nums[2:4])          # Get a slice from index 2 to 4 (exclusive); prints "[2, 3]"
print(nums[2:])           # Get a slice from index 2 to the end; prints "[2, 3, 4]"
print(nums[:2])           # Get a slice from the start to index 2 (exclusive); prints "[0, 1]"
print(nums[:])            # Get a slice of the whole list; prints "[0, 1, 2, 3, 4]"
print(nums[:-1])          # Slice indices can be negative; prints "[0, 1, 2, 3]"
nums[2:4] = [8, 9]        # Assign a new sublist to a slice
print(nums)               # Prints "[0, 1, 8, 9, 4]"
```

<b>- Loops </b> 
```python
animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print(animal)
# Prints "cat", "dog", "monkey", each on its own line.
```

<b>- Lish comprehensions </b>

```python
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)   # Prints [0, 1, 4, 9, 16]
``` 
 &nbsp;위의 코드를 list comprehension을 사용하여 더 간단하게 표현할 수 있다.
```python
nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print(squares)   # Prints [0, 1, 4, 9, 16]
```
&nbsp; 위와 같은 list comprehension은 조건을 포함할 수도 있다. 
```python
nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)  # Prints "[0, 4, 16]"
```


#### ✔️ Dictionaries

#### ✔️ Sets

#### ✔️ Tuples


### [Functions]

### [Classes]


## 💡Numpy

### [Arrays]

### [Array indexing]

### [Datatypes]

### [Array math]

### [Broadcasting]

### [Numpy Documentation]


## 💡SciPy

### [Image operations]

### [MATLAB files]

### [Distance between points]



## 💡Matplotlib

### [Plotting]

### [Subplots]

### [Images]



