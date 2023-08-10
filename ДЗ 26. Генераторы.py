def simple_generator(start, step):
    val = start
    while True:
        yield val
        val *= step


for item in simple_generator(-2, -5):
    print(item)
    if -1000 <= item <= 1000:
        break

for item in simple_generator(10, 3):
    print(item)
    if -1000 <= item <= 1000:
        break