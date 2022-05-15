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
12. Add picture to items*
13. User ratings
14. Splash Page

## Non-functional Requirements
1. System shall be maintainable
2. Website should be easy to deploy and access
3. Transactions should be submitted within 10ms
4. Only expected to work on Google Chrome

## Use Cases for 8 functional requirements
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
        1. System displays error message to customer
        2. System does not add invalid item to cart

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
        1. System removes item in cart
        2. System updates item's page to "Sold out!"
- **Alternate Sequence:** 
    1. Customer buys a nonexistent/invalid item
        1. System displays error message to customer
        2. System does not undergo "Buy item" sequence
        3. System removes the nonexistent/invalid item

3. Find items
- **Pre-condition:**
  1. Customer has previously made an account and logged in
- **Trigger:** 
  1. Customer clicks the "Find items" page
- **Primary Sequence:**
  1. System prompts the customer to enter an item in a searchbar
  2. System also has sorting options available for the customer to list
  3. Customer enters an item
  4. System checks if there is a matching item to what the customer enters
  5. System displays the item
- **Primary Postconditions:** 
  1. Customer is able to find a matching item
  2. Customer is not able to find a matching item
- **Alternate Sequence:** 
  1. Customer does not enter any input in searchbar and searches for item
        1. System prompts customer to enter an item

4. Bid on items
- **Pre-condition:**
  1. The customer has previously made an account and logged in
- **Trigger:** 
  1. Customer clicks "Bid" on item's page
- **Primary Sequence:**
  1. System prompts the customer with a "Bid?" confirmation.
  2. Customer confirms if they want to make a bid
  3. System checks if the item is open to bidding
  4. System prompts customer how much they want to bid on the item
  5. Customer enters amount they would like to bid
  6. System checks if credit card information is already set
  7. System prompts customer to enter credit card information if not set
  8. Customer enters credit card information
  9. System prompts that item has been bid on 
- **Primary Postconditions:** 
  1. Customer makes a bid on item
  2. Customer chooses to not make a bid after clicking "Bid?"
- **Alternate Sequence:** 
  1. Customer enters no amount to bid on item
	1. System prompts the customer to enter an amount to bid 

5. User Profiles
- **Pre-condition:**
	1. User has previously made an account
- **Trigger:**
	1. User clicks profile button on seller
- **Primary Sequence:**
	1. System loads seller page from file
	2. System displays page
- **Primary Postconditions:**
	1. has previously made an account
- **Alternate Sequence:**
	1. User does not click on profile of seller
	2. No action is performed by system

6. Add picture to items*
- **Pre-condition:**
	1. User has previously made an account
- **Trigger:** 
	1. Seller posts item
- **Primary Sequence:**
	1. Seller clicks button to upload image to item post
	2. System retrieves image and saves to database
- **Primary Postconditions:**
	1. System displays image and item post
- **Alternate Sequence:** 
	1. User does not upload image
	2. System will not place item in system

7. User ratings
- **Pre-condition:**
    1. User has previously made an account
- **Trigger:**
    1. Customer click rating buttom after buy item
- **Primary Sequence:**
    1. System prompts customer with an "rate 1-5, 5 is the most satisfied" confirmation
    2. Customer confirms the rating
    3. System saves the rating
- **Primary Postconditions:**
    1. Website display the rating on the page
- **Alternate Sequence:**
    1. Customer does not confirm the rating
    2. System does not save the rating

8. Splash Page
- **Pre-condition:**
    1. User type the webiste address
- **Trigger:**
    1. User press enter in the website address bar
    2. User press "Enter" button in the middle of the page
- **Primary Sequence:**
    1. User type the website address in the address bar
    2. System display the splash page to the user
    3. User click "Enter" button
- **Primary Postconditions:**
    1. User are redirected to the website's main page
- **Alternate Sequence:**
    1. User does not click "Enter" button
    2. Website stays on the splash page
