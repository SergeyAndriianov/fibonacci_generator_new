
def fibonacci_generator():
    a, b = 0, 3
    while True:
        yield a
        a, b = b, a + b


num = fibonacci_generator()
for i in range(10):
    print(next(num))
