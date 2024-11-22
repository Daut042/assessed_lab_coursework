import random

def daily_sales(available_items, inventory_records, current_day):
    
    sold_units = 0 # Initialize the number of sold units to 0

    if current_day % 7 != 0: # Check if the current day is not a restocking day
        
        sold_units = random.randint(0 , 200)  # Generate a random number of units sold between 0 and 200
        
        available_items -= sold_units  # Subtract the sold units from available items
        
        inventory_records.append((current_day, sold_units, 0, available_items))  # Append today's activity to inventory_records


    
    return available_items