#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = []

  def add_item(self, title, price, quantity=1):
    self.items.append(title)  
    self.total += price * quantity
    self.last_transaction.append({
          "title": title, "quantity" : quantity, "price" : price
      })       
  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      self.total -= self.total * (self.discount / 100)
      print(f"After the discount, the total comes to ${int(self.total)}.")
  def void_last_transaction(self):
    if not self.last_transaction:
      print("No transactions to void.")
      return []
    else:
      last_transaction_value = self.last_transaction[-1]["price"] * self.last_transaction[-1]["quantity"]
      self.total -= last_transaction_value

        # Create a list representing the state of items after voiding the last transaction
      items_after_void = self.items[:-self.last_transaction[-1]["quantity"]]
        
        # Remove the last transaction from the last_transaction list
      voided_transaction = self.last_transaction.pop()

      print(f"Voided transaction: {voided_transaction}")

      return items_after_void
 