def due_amount(total_bill, amount_paid):
    # Calculate how much the shopkeeper should return
    return amount_paid - total_bill

# Example usage
bill = 2.50
paid = 4.00
print("Due amount:", due_amount(bill, paid))
