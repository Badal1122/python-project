def calculate_cost(item, quantity):
    if item.lower() == 'apple':
        price_per_unit = 1.0
    elif item.lower() == 'bananas':
        price_per_unit = 0.5
    elif item.lower() == 'oranges':
        price_per_unit = 0.75
    else:
        print("Sorry, we don't have information about", item)
        return 0
    
    total_cost = price_per_unit * quantity
    return total_cost

def main():
    total_cost = 0
    item_list = ['apple', 'bananas', 'oranges']
    
    for item in item_list:
        quantity = float(input("Enter the quantity of " + item + " purchased: "))
        total_cost += calculate_cost(item, quantity)
    
    if total_cost > 50:
        total_cost *= 0.95  # Apply 5% discount if total cost exceeds $50
    
    print("Total cost: $", format(total_cost, ".2f"))

if __name__ == "__main__":
    main()
