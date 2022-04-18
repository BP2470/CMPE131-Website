## Functional Requirements
1. Login
2. Logout
3. Create new account
4. Delete account
5. Add to cart
6. Buy item (Fake credit card entry)
7. Find items
8. Bid on item
9. Add item to seller store
10. User profiles
11. See all items available from all of the sellers
12. Connect with Google Calendar API*

## Non-functional Requirements
1. System shall be maintainable
2. Website should be easy to access
3. Transactions should be submitted within 10ms
4. Only expected to work on Google Chrome

## Use Cases for 6 functional requirements
1. Add to cart
- **Pre-condition:** 
  1. Customer has previously made an account and logged in
- **Trigger:** 
  1. Customer clicks "Add to cart" on item's page
- **Primary Sequence:**
  1. System prompts customer with an "Add to cart?" confirmation
  2. Customer confirms whether to add to cart
  3. System checks if item is valid
  4. System adds item to cart
- **Primary Postconditions:**
  1. Website displays the item in the cart page
- **Alternate Sequence:** 
  1. Customer adds a nonexistent/invalid item to cart
  - System displays error message to customer
  - System does not add invalid item to cart

2. Buy item (Fake credit card entry)
- **Pre-condition:**
  1. Customer has previously made an account and logged in
  2. Customer has either directly clicks buy item button or has at least an item in cart
- **Trigger:** 
  1. Customer clicks "Buy item" on item's page or from cart's page
- **Primary Sequence:**
  1. System prompts customer with a "Buy item?" confirmation
  2. Customer confirms whether to buy item
  3. System checks if item is valid
  4. System prompts customer with a "Add credit card" entry
  5. Customer adds in credit card credentials
  6. System checks "credit card credentials"
  7. System charges customer
  8. System prompts customer that item is bought
- **Primary Postconditions:** 
  1. Customer "receives" item
    - System removes item in cart
    - System updates item's page to "Sold out!"
- **Alternate Sequence:** 
  1. Customer buys a nonexistent/invalid item
    - System displays error message to customer
    - System does not undergo "Buy item" sequence
    - System removes the nonexistent/invalid item

3. Use Case Name
- **Pre-condition:**
- **Trigger:** 
- **Primary Sequence:**
- **Primary Postconditions:** 
- **Alternate Sequence:** 

4. Use Case Name
- **Pre-condition:**
- **Trigger:** 
- **Primary Sequence:**
- **Primary Postconditions:** 
- **Alternate Sequence:** 

5. Use Case Name
- **Pre-condition:**
- **Trigger:** 
- **Primary Sequence:**
- **Primary Postconditions:** 
- **Alternate Sequence:** 

6. Use Case Name
- **Pre-condition:**
- **Trigger:** 
- **Primary Sequence:**
- **Primary Postconditions:** 
- **Alternate Sequence:** 
