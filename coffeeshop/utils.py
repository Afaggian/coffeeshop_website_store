SMALL = 'S'
MEDIUM = 'M'
LARGE = 'L'

SIZE_CHOICES = [
    (SMALL, 'Small'),
    (MEDIUM, 'Medium'),
    (LARGE, 'Large'),
]

AMERICANO = 'A'
CAPPUCCINO = 'C'
COLD = 'CB'

COFFEE_CHOICES = [
    (None, 'Please select a drink type'),
    (AMERICANO, 'Americano'),
    (CAPPUCCINO, 'Cappuccino'),
    (COLD, 'Cold Brew Coffee')
]

QUANTITY_CHOICES = [('1', '1'), ('2', '2'), ('3', '3')]
