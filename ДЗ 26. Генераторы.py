def geometric_progression_generator(start, ratio):
    val = start
    while True:
        yield val
        val *= ratio

print('Геометрическая прогрессия с началом -2 и шагом -5:')
generator1 = geometric_progression_generator(-2, -5)
for _ in range(6):
    print(next(generator1))

print('\nГеометрическая прогрессия с началом 10 и шагом 3:')
generator2 = geometric_progression_generator(10, 3)
for _ in range(6):
    print(next(generator2))