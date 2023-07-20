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
&nbsp; Dictionary는 (key, value)를 가진 자바의 Map과 비슷하다. get() 함수를 이용하면 해당 key를 가지고 있다면 알맞은 value 값을 도출하고 그렇지 않다면 뒤에 작성한 값을 도출해낸다. 그리고 del() 함수를 사용하면 해당 key 값을 가진 dictionary를 삭제한다. 

```python
d = {'cat': 'cute', 'dog': 'furry'}  # Create a new dictionary with some data
print(d['cat'])       # Get an entry from a dictionary; prints "cute"
print('cat' in d)     # Check if a dictionary has a given key; prints "True"
d['fish'] = 'wet'     # Set an entry in a dictionary
print(d['fish'])      # Prints "wet"
# print(d['monkey'])  # KeyError: 'monkey' not a key of d
print(d.get('monkey', 'N/A'))  # Get an element with a default; prints "N/A"
print(d.get('fish', 'N/A'))    # Get an element with a default; prints "wet"
del d['fish']         # Remove an element from a dictionary
print(d.get('fish', 'N/A')) # "fish" is no longer a key; prints "N/A"
```
<b>- Loops </b> 
```python
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print('A %s has %d legs' % (animal, legs))
# Prints "A person has 2 legs", "A cat has 4 legs", "A spider has 8 legs"
```
&nbsp; 위의 코드에서 items 메소드를 사용하면 key와 그에 맞는 value 값에 접근할 수 있다. 
```python
d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, legs in d.items():
    print('A %s has %d legs' % (animal, legs))
# Prints "A person has 2 legs", "A cat has 4 legs", "A spider has 8 legs"
```
<b>- Dictionary comprehension </b> 
```python
nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square)  # Prints "{0: 0, 2: 4, 4: 16}"
```

#### ✔️ Sets

&nbsp; Set은 순서가 없는 요소의 모음이다. set에서 add를 사용하면 set에 해당 요소가 추가 되는데, 만약 set에 이미 존재하는 요소를 추가한다면 아무 일도 발생하지 않는다. 또 len을 사용하면 해당 set에 몇개의 요소가 있는지 알 수 있고, remove 메소드를 사용하면 set에 존재하는 요소를 제거해준다. 
```python
animals = {'cat', 'dog'}
print('cat' in animals)   # Check if an element is in a set; prints "True"
print('fish' in animals)  # prints "False"
animals.add('fish')       # Add an element to a set
print('fish' in animals)  # Prints "True"
print(len(animals))       # Number of elements in a set; prints "3"
animals.add('cat')        # Adding an element that is already in the set does nothing
print(len(animals))       # Prints "3"
animals.remove('cat')     # Remove an element from a set
print(len(animals))       # Prints "2"
```

<b>- Loops </b>
&nbsp; list에서 반복한 것과 똑같이 반복문을 사용하면 된다. 하지만 set과 list의 차이는 set은 순서가 정해져 있지 않기 때문에, 반복 시 set의 순서를 정할 수도 확실히 할 수도 없다. 마찬가지로 리스트와 다르게 인덱스 번호를 사용하여 특정 값에 접근할 수 없다는 특징이 있다. 

* 아래의 코드와 같이 enumerate를 사용하는 이유는 나열해서 번호를 매겨주기 위해서이다. enumerate는 반복문에서 사용하는 함수이며 enumerate를 사용하면 반복문에서 index 번호를 얻을 수 있다. 

```python
animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))
# Prints "#1: fish", "#2: dog", "#3: cat"
```

<b>- Set comprehensions </b>
```python
from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}
print(nums)  # Prints "{0, 1, 2, 3, 4, 5}"
```

#### ✔️ Tuples
&nbsp; 튜플은 값의 순서가 변할 수 있는 list이다. list와 비슷한 부분이 많지만, 둘의 가장 큰 차이는 튜플은 dictionary의 key처럼, set의 요소처럼 사용될 수 있다는 것이다. 

```python
d = {(x, x + 1): x for x in range(10)}  # Create a dictionary with tuple keys
t = (5, 6)        # Create a tuple
print(type(t))    # Prints "<class 'tuple'>"
print(d[t])       # Prints "5"
print(d[(1, 2)])  # Prints "1"
```

### [Functions]
&nbsp; "def" 키워드를 사용해서 함수를 생성할 수 있다. 

```python
def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'

for x in [-1, 0, 1]:
    print(sign(x))
# Prints "negative", "zero", "positive"
```

```pyhton
def hello(name, loud=False):
    if loud:
        print('HELLO, %s!' % name.upper())
    else:
        print('Hello, %s' % name)

hello('Bob') # Prints "Hello, Bob"
hello('Fred', loud=True)  # Prints "HELLO, FRED!"
```

### [Classes]

```python
class Greeter(object):

    # Constructor
    def __init__(self, name):
        self.name = name  # Create an instance variable

    # Instance method
    def greet(self, loud=False):
        if loud:
            print('HELLO, %s!' % self.name.upper())
        else:
            print('Hello, %s' % self.name)

g = Greeter('Fred')  # Construct an instance of the Greeter class
g.greet()            # Call an instance method; prints "Hello, Fred"
g.greet(loud=True)   # Call an instance method; prints "HELLO, FRED!"
```

## 💡Numpy
&nbsp; Numpy는 파이썬에서 scientific computing에 핵심적인 라이브러리다. multidimensional array object와 이 array들을 다룰 수 있는 도구를 제공한다. 

### [Arrays]
&nbsp; numpy의 array는 같은 type을 가진 값들이 격자로 존재하는 것이고, 이 값들은 음이 아닌 정수의 튜플로 index된다. 차원의 수는 이 array의 열(rank)이다. 그리고 array의 shape는 각 차원에 따라 array에 size를 주는 것이다. 머신러닝에서는 행렬의 차원을 shape라는 개념으로 표현한다. 

```python
import numpy as np

a = np.array([1, 2, 3])   # Create a rank 1 array
print(type(a))            # Prints "<class 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                  # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"
```
&nbsp; Numpy는 array를 생성할 수 있는 많은 함수를 제공한다.
```python
import numpy as np

a = np.zeros((2,2))   # Create an array of all zeros
print(a)              # Prints "[[ 0.  0.]
                      #          [ 0.  0.]]"

b = np.ones((1,2))    # Create an array of all ones
print(b)              # Prints "[[ 1.  1.]]"

c = np.full((2,2), 7)  # Create a constant array
print(c)               # Prints "[[ 7.  7.]
                       #          [ 7.  7.]]"

d = np.eye(2)         # Create a 2x2 identity matrix
print(d)              # Prints "[[ 1.  0.]
                      #          [ 0.  1.]]"

e = np.random.random((2,2))  # Create an array filled with random values
print(e)                     # Might print "[[ 0.91940167  0.08143941]
                             #               [ 0.68744134  0.87236687]]"
```

### [Array indexing]

<b>- Slicing </b>

&nbsp; multidimensional array을 각 차원의 array로 slice할 수 있다. 아래의 코드의 b에서 보이는 것과 같이 a[:2, 1:3]은 array a의 행을 0 ~ 1(2전), 열을 1 ~ 2(3전)로 slice한 배열을 b로 정하겠다는 의미이다. 이렇게 slice된 array는 원래의 data와 같은 것인데, 그렇기 때문에 만약 b의 어떠한 값을 수정한다면 a에서도 해당 값이 변하게 된다는 특징이 있다. 

```python
import numpy as np

# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]

# A slice of an array is a view into the same data, so modifying it
# will modify the original array.
print(a[0, 1])   # Prints "2"
b[0, 0] = 77     # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1])   # Prints "77"
```

```python
import numpy as np

# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# Two ways of accessing the data in the middle row of the array.
# Mixing integer indexing with slices yields an array of lower rank,
# while using only slices yields an array of the same rank as the
# original array:
row_r1 = a[1, :]    # Rank 1 view of the second row of a
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
print(row_r1, row_r1.shape)  # Prints "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape)  # Prints "[[5 6 7 8]] (1, 4)"

# We can make the same distinction when accessing columns of an array:
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)  # Prints "[ 2  6 10] (3,)"
print(col_r2, col_r2.shape)  # Prints "[[ 2]
                             #          [ 6]
                             #          [10]] (3, 1)"
```

<b>- Integer array indexing </b>



<b>- Boolean array indexing </b>



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



