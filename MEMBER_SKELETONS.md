# CODE SKELETONS FOR MEMBERS 3-6

## 📁 MEMBER 3: MEME NFT MARKETPLACE

Create file: `member3_memes.py`

```python
"""
MEMBER 3: MEME NFT MARKETPLACE
Handles: Creating memes, trading, collecting, liking
"""

import os
import member1_profiles as profiles

# Data file: data/memes.txt
# Format: nft_id|name|description|creator_id|rarity|price|owner_id|likes

def get_all_memes():
    """Read all memes from file"""
    # TODO: Implement
    pass

def save_all_memes(memes):
    """Save memes back to file"""
    # TODO: Implement
    pass

def create_meme(creator_id):
    """Create a new meme NFT"""
    # TODO: Get meme name, description
    # TODO: Assign rarity (Common/Rare/Epic/Legendary)
    # TODO: Generate NFT ID
    # TODO: Save to file
    # TODO: Add to creator's NFT collection (call profiles.add_nft)
    print("✅ Meme created!")

def browse_marketplace():
    """Show all memes for sale"""
    # TODO: Read all memes
    # TODO: Display each meme with details
    print("🎨 Meme Marketplace")

def buy_meme(buyer_id, nft_id):
    """Purchase a meme"""
    # TODO: Find meme
    # TODO: Check buyer has enough coins
    # TODO: Deduct coins from buyer (call profiles.update_student_coins)
    # TODO: Add coins to seller
    # TODO: Change meme owner
    # TODO: Update NFT collections
    print("✅ Meme purchased!")

def view_collection(student_id):
    """Show owned memes"""
    # TODO: Get student's NFT collection
    # TODO: Display each meme
    print("🎨 Your Collection")

def like_meme(student_id, nft_id):
    """Like a meme"""
    # TODO: Find meme
    # TODO: Increase likes count
    print("👍 Meme liked!")

def meme_menu(student_id):
    """Meme marketplace menu"""
    while True:
        print("\n=== 🎨 MEME NFT MARKETPLACE ===")
        print("1. Browse Marketplace")
        print("2. Create Meme")
        print("3. Buy Meme")
        print("4. My Collection")
        print("5. Like Meme")
        print("0. Back")
        
        choice = input("Choose: ")
        
        if choice == "1":
            browse_marketplace()
        elif choice == "2":
            create_meme(student_id)
        elif choice == "3":
            nft_id = input("Enter NFT ID: ")
            buy_meme(student_id, nft_id)
        elif choice == "4":
            view_collection(student_id)
        elif choice == "5":
            nft_id = input("Enter NFT ID: ")
            like_meme(student_id, nft_id)
        elif choice == "0":
            break
        
        input("Press Enter to continue...")
```

---

## 📁 MEMBER 4: PERK SHOP

Create file: `member4_perks.py`

```python
"""
MEMBER 4: PERK SHOP
Handles: Browsing perks, purchasing, inventory, redemption
"""

import os
import member1_profiles as profiles

# Data files:
# data/perks.txt - Available perks
# data/inventory.txt - Student purchases

# perks.txt format: perk_id|name|cost|quantity|type|seller_id|validity
# inventory.txt format: student_id|perk_id|purchase_date|status

def get_all_perks():
    """Read all perks from file"""
    # TODO: Implement
    pass

def save_all_perks(perks):
    """Save perks back to file"""
    # TODO: Implement
    pass

def get_student_inventory(student_id):
    """Get student's purchased perks"""
    # TODO: Read inventory.txt
    # TODO: Return list of student's perks
    pass

def view_perks():
    """Display all available perks"""
    # TODO: Read perks
    # TODO: Display each perk
    print("🛒 Available Perks")

def purchase_perk(student_id, perk_id):
    """Buy a perk"""
    # TODO: Find perk
    # TODO: Check student has enough coins
    # TODO: Deduct coins (call profiles.update_student_coins)
    # TODO: Add to inventory
    # TODO: Decrease perk quantity
    print("✅ Perk purchased!")

def view_inventory(student_id):
    """Show owned perks"""
    # TODO: Get inventory
    # TODO: Display each perk
    print("📦 Your Inventory")

def redeem_perk(student_id, perk_id):
    """Use a perk"""
    # TODO: Find in inventory
    # TODO: Mark as used
    print("✅ Perk redeemed!")

def perk_menu(student_id):
    """Perk shop menu"""
    while True:
        print("\n=== 🛒 PERK SHOP ===")
        print("1. Browse Perks")
        print("2. Purchase Perk")
        print("3. My Inventory")
        print("4. Redeem Perk")
        print("0. Back")
        
        choice = input("Choose: ")
        
        if choice == "1":
            view_perks()
        elif choice == "2":
            perk_id = input("Enter Perk ID: ")
            purchase_perk(student_id, perk_id)
        elif choice == "3":
            view_inventory(student_id)
        elif choice == "4":
            perk_id = input("Enter Perk ID: ")
            redeem_perk(student_id, perk_id)
        elif choice == "0":
            break
        
        input("Press Enter to continue...")
```

---

## 📁 MEMBER 5: SOCIAL CREDIT ENGINE

Create file: `member5_social.py`

```python
"""
MEMBER 5: SOCIAL CREDIT ENGINE
Handles: Sending coins, transactions, verification, reputation
"""

import os
from datetime import datetime
import member1_profiles as profiles

# Data file: data/transactions.txt
# Format: txn_id|from_id|to_id|amount|reason|verified|timestamp

def get_all_transactions():
    """Read all transactions from file"""
    # TODO: Implement
    pass

def send_coins(from_id, to_id, amount, reason):
    """Send coins to another student"""
    # TODO: Check sender has enough coins
    # TODO: Deduct from sender (call profiles.update_student_coins)
    # TODO: Add to receiver
    # TODO: Log transaction with timestamp
    print("✅ Coins sent!")

def view_transactions(student_id):
    """Show transaction history"""
    # TODO: Read all transactions
    # TODO: Filter for this student (sent or received)
    # TODO: Display each transaction
    print("💸 Transaction History")

def verify_transaction(txn_id, verifier_id):
    """Verify a good deed"""
    # TODO: Find transaction
    # TODO: Mark as verified
    # TODO: Update reputation for both parties
    print("✅ Transaction verified!")

def calculate_reputation(student_id):
    """Calculate reputation score"""
    # TODO: Count verified transactions
    # TODO: Count coins sent vs received
    # TODO: Calculate score
    return 0

def social_menu(student_id):
    """Social credit menu"""
    while True:
        print("\n=== 💸 SOCIAL CREDIT ===")
        print("1. Send Coins")
        print("2. View Transactions")
        print("3. Verify Good Deed")
        print("4. My Reputation")
        print("0. Back")
        
        choice = input("Choose: ")
        
        if choice == "1":
            to_id = input("Send to (Student ID): ")
            amount = int(input("Amount: "))
            reason = input("Reason: ")
            send_coins(student_id, to_id, amount, reason)
        elif choice == "2":
            view_transactions(student_id)
        elif choice == "3":
            txn_id = input("Transaction ID: ")
            verify_transaction(txn_id, student_id)
        elif choice == "4":
            rep = calculate_reputation(student_id)
            print(f"Your reputation: {rep}")
        elif choice == "0":
            break
        
        input("Press Enter to continue...")
```

---

## 📁 MEMBER 6: LEADERBOARDS & ANALYTICS

Create file: `member6_leaderboards.py`

```python
"""
MEMBER 6: LEADERBOARDS & ANALYTICS
Handles: Rankings, statistics, analytics
"""

import os
import member1_profiles as profiles
import member2_quests as quests

def show_richest():
    """Top students by coins"""
    # TODO: Get all students
    # TODO: Sort by coins (highest first)
    # TODO: Display top 10
    print("🏆 Richest Students")

def show_quest_leaders():
    """Most quests completed"""
    # TODO: Get all students
    # TODO: Count completed quests for each
    # TODO: Sort and display
    print("🎯 Quest Leaders")

def show_most_helpful():
    """Most coins sent to others"""
    # TODO: Read transactions
    # TODO: Count total sent for each student
    # TODO: Sort and display
    print("💝 Most Helpful")

def show_meme_kings():
    """Most memes created"""
    # TODO: Read memes
    # TODO: Count by creator
    # TODO: Sort and display
    print("🎨 Meme Kings/Queens")

def show_analytics(student_id):
    """Individual student stats"""
    # TODO: Calculate various stats
    # - Total coins earned
    # - Total spent
    # - Quests completed
    # - Memes created
    # - Ranking position
    print("📊 Your Analytics")

def leaderboard_menu():
    """Leaderboards menu"""
    while True:
        print("\n=== 🏆 LEADERBOARDS ===")
        print("1. Richest Students")
        print("2. Quest Leaders")
        print("3. Most Helpful")
        print("4. Meme Kings/Queens")
        print("5. My Analytics")
        print("0. Back")
        
        choice = input("Choose: ")
        
        if choice == "1":
            show_richest()
        elif choice == "2":
            show_quest_leaders()
        elif choice == "3":
            show_most_helpful()
        elif choice == "4":
            show_meme_kings()
        elif choice == "5":
            student_id = input("Enter your Student ID: ")
            show_analytics(student_id)
        elif choice == "0":
            break
        
        input("Press Enter to continue...")
```

---

## 🎯 INSTRUCTIONS FOR EACH MEMBER

1. **Copy the skeleton code above for your module**
2. **Fill in the TODO sections** - this is your work!
3. **Test your module independently** - run it alone first
4. **Ask for help** when stuck - that's what team is for!
5. **Practice your 2-minute presentation**

## 📝 WHAT EACH TODO MEANS

**"TODO: Implement"** = Write the code to do this
**"TODO: Get..."** = Ask user for input
**"TODO: Check..."** = Use if statement to verify
**"TODO: Display..."** = Use print to show info
**"TODO: Calculate..."** = Do some math or counting

## ✅ TESTING YOUR CODE

Before integration, test like this:

```python
if __name__ == "__main__":
    # Create data directory
    import os
    if not os.path.exists("data"):
        os.makedirs("data")
    
    # Test your functions
    print("Testing Member X Module")
    your_menu_function("NSU210101")  # Use a test ID
```

## 🤝 GETTING HELP

If stuck:
1. Read the Python basics guide
2. Look at Members 1 & 2 code (complete examples)
3. Ask your coordinator
4. Check online Python tutorials
5. Ask team members

**You got this! 🚀**
