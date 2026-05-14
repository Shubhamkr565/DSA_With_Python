### 1. Right Triangle Star Pattern

**Description**: Prints a right-angled triangle of stars, with each row having one more star than the previous.

```python
def right_triangle(n):
    for i in range(n):
        print('*' * (i + 1))

# Example usage
n = 5
right_triangle(n)
```

**Output**:

```
*
**
***
****
*****
```

---

### 2. Inverted Right Triangle Star Pattern

**Description**: Prints an inverted right-angled triangle, with the first row having the most stars.

```python
def inverted_right_triangle(n):
    for i in range(n, 0, -1):
        print('*' * i)

# Example usage
n = 5
inverted_right_triangle(n)
```

**Output**:

```
*****
****
***
**
*
```

---

### 3. Left Triangle Star Pattern

**Description**: Prints a right-angled triangle aligned to the left, with spaces before stars to create a right-aligned effect.

```python
def left_triangle(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (i + 1))

# Example usage
n = 5
left_triangle(n)
```

**Output**:

```
    *
   **
  ***
 ****
*****
```

---

### 4. Inverted Left Triangle Star Pattern

**Description**: Prints an inverted right-angled triangle aligned to the left.

```python
def inverted_left_triangle(n):
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * i)

# Example usage
n = 5
inverted_left_triangle(n)
```

**Output**:

```
*****
 ****
  ***
   **
    *
```

---

### 5. Pyramid Star Pattern

**Description**: Prints a centered pyramid (triangle) of stars, with spaces used for alignment.

```python
def pyramid(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# Example usage
n = 5
pyramid(n)
```

**Output**:

```
    *
   ***
  *****
 *******
*********
```

---

### 6. Inverted Pyramid Star Pattern

**Description**: Prints an inverted pyramid, with the widest row at the top.

```python
def inverted_pyramid(n):
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

# Example usage
n = 5
inverted_pyramid(n)
```

**Output**:

```
*********
 *******
  *****
   ***
    *
```

---

### 7. Diamond Star Pattern

**Description**: Combines a pyramid and an inverted pyramid to form a diamond shape.

```python
def diamond(n):
    # Upper pyramid
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    # Lower inverted pyramid
    for i in range(n - 1, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# Example usage
n = 5
diamond(n)
```

**Output**:

```
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
```

---

### 8. Hollow Square Star Pattern

**Description**: Prints a square with stars only on the borders.

```python
def hollow_square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')

# Example usage
n = 5
hollow_square(n)
```

**Output**:

```
*****
*   *
*   *
*   *
*****
```

---

### 9. Hollow Pyramid Star Pattern

**Description**: Prints a pyramid with stars only on the edges of the triangle.

```python
def hollow_pyramid(n):
    for i in range(n):
        # Spaces before the stars
        print(' ' * (n - i - 1), end='')
        # Stars and spaces for hollow effect
        if i == 0:
            print('*')
        elif i == n - 1:
            print('*' * (2 * i + 1))
        else:
            print('*' + ' ' * (2 * i - 1) + '*')

# Example usage
n = 5
hollow_pyramid(n)
```

**Output**:

```
    *
   * *
  *   *
 *     *
*********
```

---

### 10. Hourglass Star Pattern

**Description**: Prints an hourglass shape (inverted pyramid followed by a pyramid).

```python
def hourglass(n):
    # Upper inverted pyramid
    for i in range(n, 0, -1):
        print(' ' * (n - i) + '*' * (2 * i - 1))
    # Lower pyramid
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

# Example usage
n = 5
hourglass(n)
```

**Output**:

```
*********
 *******
  *****
   ***
    *
    *
   ***
  *****
 *******
*********
```

---

### 11. Right Pascal’s Triangle

**Description**: Prints a right-angled Pascal’s triangle, combining a right triangle and its inverted form.

```python
def right_pascal(n):
    # Upper right triangle
    for i in range(n):
        print('*' * (i + 1))
    # Lower inverted right triangle
    for i in range(n - 1, 0, -1):
        print('*' * i)

# Example usage
n = 5
right_pascal(n)
```

**Output**:

```
*
**
***
****
*****
****
***
**
*
```

---

### 12. Hollow Diamond Star Pattern

**Description**: Prints a diamond shape with stars only on the borders.

```python
def hollow_diamond(n):
    # Upper hollow pyramid
    for i in range(n):
        print(' ' * (n - i - 1) + '*' + ' ' * (2 * i - 1) + ('*' if i > 0 else ''))
    # Lower hollow inverted pyramid
    for i in range(n - 1, -1, -1):
        print(' ' * (n - i - 1) + '*' + ' ' * (2 * i - 1) + ('*' if i > 0 else ''))

# Example usage
n = 5
hollow_diamond(n)
```

**Output**:

```
    *
   * *
  *   *
 *     *
*       *
*       *
 *     *
  *   *
   * *
    *
```

---

### 13. Numbered Star Pattern

**Description**: Prints a right triangle where each row contains the row number as the count of stars.

```python
def numbered_star(n):
    for i in range(1, n + 1):
        print('*' * i + ' ' + str(i))

# Example usage
n = 5
numbered_star(n)
```

**Output**:

```
* 1
** 2
*** 3
**** 4
***** 5
```

---

### 14. Alternating Star Pattern

**Description**: Prints a pattern where rows alternate between stars and dashes.

```python
def alternating_pattern(n):
    for i in range(n):
        if i % 2 == 0:
            print('*' * (i + 1))
        else:
            print('-' * (i + 1))

# Example usage
n = 5
alternating_pattern(n)
```

**Output**:

```
*
--
***
----
*****
```

---

### 15. Cross Star Pattern

**Description**: Prints a cross shape using stars, with stars forming the diagonals of a square.

```python
def cross_pattern(n):
    for i in range(n):
        for j in range(n):
            if j == i or j == n - 1 - i:
                print('*', end='')
            else:
                print(' ', end='')
        print()

# Example usage
n = 5
cross_pattern(n)
```

**Output**:

```
*   *
 * *
  *
 * *
*   *
```

---

### Notes:

- **Input Handling**: For dynamic input, you can add `n = int(input("Enter the size: "))` at the start of each program.
- **Customization**: Adjust the `n` value to change the size of the pattern.
- **Efficiency**: These programs use basic loops for clarity. For large `n`, string concatenation in loops can be optimized using list joins if needed.
- **Extensibility**: You can modify these patterns (e.g., replace `*` with other characters or add colors using ANSI codes).

If you want more complex patterns, additional examples, or variations (e.g., spiral, heart, or alphanumeric patterns), let me know! I can also help debug or explain any specific pattern in detail.
