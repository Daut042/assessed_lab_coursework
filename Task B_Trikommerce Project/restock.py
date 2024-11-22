def restock_inventory(available_items, inventory_records, current_day):
   
    if current_day % 7 == 0: # Check if the current day is a restocking day 
        
        if current_day == 0:  # Special case: Day 0
            
            inventory_records.append((0, 0, 2000, 2000))  # On day 0, initialize the inventory to 2000 without calculating restock
            available_items = 2000
        
        else:  # For any other 7th day
            
            restocked_units = 2000 - available_items  # Calculate how many units need to be restocked to reach 2000
            inventory_records.append((current_day, 0, restocked_units, 2000))  # Append a record of the restocking
            
            available_items = 2000  # Update available items to the maximum of 2000

    return available_items
