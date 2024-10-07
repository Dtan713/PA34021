int1 = 5
int2 = 10
int_sum = int1 + int2
print("Sum of integers:", int_sum)

float1 = 5.5
float2 = 10.2
float_sum = float1 + float2
print("Sum of floats:", float_sum)

int_var = 5
float_var = 10.5
mixed_sum = int_var + float_var
print("Sum of integer and float:", mixed_sum)
print("Type of mixed sum:", type(mixed_sum))  # Should be a float

larger_int = 20
smaller_int = 5
int_division = larger_int / smaller_int
print("Division of integers:", int_division)


larger_float = 20.5
smaller_float = 5.1
float_division = larger_float / smaller_float
print("Division of floats:", float_division)


coffee_price = 3.50
cappuccino_price = 4.00
espresso_price = 2.75

subtotal = (3 * coffee_price) + (4 * cappuccino_price) + (2 * espresso_price)
SALES_TAX = 0.07  # 7% sales tax
totalSale = subtotal + (subtotal * SALES_TAX)
print("Subtotal:", subtotal)
print("Total Sale (including tax):", totalSale)


radius = 63
pi = 3.14
area = pi * (radius ** 2)
print("Area of the circle:", area)
