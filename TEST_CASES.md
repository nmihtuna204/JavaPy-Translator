# Test Cases for JavaPy-Translator

Use these test cases to verify the translator works correctly.

---

## Python → Java Test Cases

### Test Case 1: Simple Function with Print
**Input (Python):**
```python
def greet(name):
    print(name)

if __name__ == "__main__":
    greet("World")
```

**Expected Output (Java):**
```java
public static int greet(int name) {
        System.out.println(name);
}
public static void main(String[] args) {
        greet("World");
}
```

---

### Test Case 2: If-Else Statement
**Input (Python):**
```python
def checkNumber(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

if __name__ == "__main__":
    checkNumber(5)
```

**Expected Output (Java):**
```java
public static int checkNumber(int num) {
        if (num > 0) {
            System.out.println("Positive");
    }
    else if (num < 0) {
            System.out.println("Negative");
    }
    else {
            System.out.println("Zero");
    }
}
public static void main(String[] args) {
        checkNumber(5);
}
```

---

### Test Case 3: While Loop
**Input (Python):**
```python
def countdown(n):
    while n > 0:
        print(n)
        n-=1

if __name__ == "__main__":
    countdown(3)
```

**Expected Output (Java):**
```java
public static int countdown(int n) {
        while (n > 0) {
        System.out.println(n);
        n -= 1;
    }
}
public static void main(String[] args) {
        countdown(3);
}
```

---

### Test Case 4: For Loop with Range
**Input (Python):**
```python
def printNumbers():
    for i in range(1, 4):
        print(i)

if __name__ == "__main__":
    printNumbers()
```

**Expected Output (Java):**
```java
public static int printNumbers() {
        for (int i = 1; 1 < 4; 1++) {
        System.out.println(i);
    }
}
public static void main(String[] args) {
        printNumbers();
}
```

---

### Test Case 5: Arithmetic Operations
**Input (Python):**
```python
def calculate(a, b):
    sum_val = a + b
    diff = a - b
    prod = a * b
    return prod

if __name__ == "__main__":
    result = calculate(10, 5)
    print(result)
```

**Expected Output (Java):**
```java
public static int calculate(int a, int b) {
        int sum_val = (a + b);
        int diff = (a - b);
        int prod = (a * b);
        return prod;
}
public static void main(String[] args) {
        int result = calculate(10, 5);
        System.out.println(result);
}
```

---

## Java → Python Test Cases

### Test Case 1: Simple Main Method with Print
**Input (Java):**
```java
public class HelloWorld {
    public static void main(String[] args) {
        int x = 42;
        System.out.println(x);
    }
}
```

**Expected Output (Python):**
```python
if __name__ == '__main__':
    x = 42
    print(x)
```

---

### Test Case 2: If-Else Logic
**Input (Java):**
```java
public class Check {
    public static void main(String[] args) {
        int x = 10;
        if (x > 5) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}
```

**Expected Output (Python):**
```python
if __name__ == '__main__':
    x = 10
    if x > 5:
        print(1)
    else:
        print(0)
```

---

### Test Case 3: While Loop
**Input (Java):**
```java
public class Loop {
    public static void main(String[] args) {
        int i = 0;
        while (i < 3) {
            System.out.println(i);
            i++;
        }
    }
}
```

**Expected Output (Python):**
```python
if __name__ == '__main__':
    i = 0
    while i < 3:
        print(i)
        i += 1
```

---

### Test Case 4: Method Call and Return
**Input (Java):**
```java
public class MyClass {
    public static int add(int a, int b) {
        return a + b;
    }
    public static void main(String[] args) {
        int result = add(5, 3);
        System.out.println(result);
    }
}
```

**Expected Output (Python):**
```python
def add(a, b):
    return (a + b)
if __name__ == '__main__':
    result = add(5, 3)
    print(result)
```

---

### Test Case 5: Comparisons and Logic
**Input (Java):**
```java
public class Logic {
    public static void main(String[] args) {
        int age = 25;
        if (age >= 18 && age < 65) {
            System.out.println(age);
        }
    }
}
```

**Expected Output (Python):**
```python
if __name__ == '__main__':
    age = 25
    if age >= 18 and age < 65:
        print(age)
```

---

## How to Test

### Method 1: Using Frontend UI
1. Start backend: `python -m uvicorn server:app --reload`
2. Start frontend: `npm run dev`
3. Copy any test case code
4. Paste into chat input
5. Check output matches expected result

### Method 2: Using Backend API Directly
```bash
curl -X POST http://localhost:8000/convert \
  -H "Content-Type: application/json" \
  -d '{"code":"def hello():\n    print(\"Hi\")\n\nif __name__ == \"__main__\":\n    hello()", "conversation_id":"test1"}'
```

### Method 3: Using Python Script
```python
import requests

code = '''def hello():
    print("Hi")

if __name__ == "__main__":
    hello()'''

response = requests.post(
    'http://localhost:8000/convert',
    json={'code': code, 'conversation_id': 'test1'}
)
print(response.json())
```

---

## Notes

- ⚠️ Grammar currently doesn't support imports, decorators, or classes
- Only basic control flow and functions are supported
- Output needs manual review for production code
- For complex code, consider expanding the grammar files
