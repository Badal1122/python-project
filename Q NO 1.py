# How do you design a function that calculates the total price of items, where the base price is 
# a required parameter and tax rate and discount are optional keyword parameters with default values?

def total_price(base_price,tax_rate=0.05,discount=0):
    price_tax=base_price*(1+tax_rate)
    total_price=price_tax-discount
    return total_price
print(total_price(500,0.05,0))