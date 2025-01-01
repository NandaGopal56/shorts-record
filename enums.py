from enum import Enum

# Enum for Ice Cream Sizes
class IceCreamSize(Enum):
    SMALL = 3.00
    MEDIUM = 4.50
    LARGE = 6.00

# Function to get the price
def get_price(size: IceCreamSize):
    return size.value  # Use the value from the enum

# Example usage
order_size = IceCreamSize.MEDIUM
print(f"You ordered a {order_size.name.lower()} ice cream. The price is ${get_price(order_size):.2f}.")
