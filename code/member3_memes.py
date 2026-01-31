"""
MEMBER 3: MEME NFT MARKETPLACE
Author: [Your Name Here]
Description: Handles meme creation, trading, collecting, and liking
"""

import os
import sys
import random

# Import Member 1's module
sys.path.insert(0, os.path.dirname(__file__))
import member1_profiles as profiles

# ============= DATA FILE PATHS =============

DATA_DIR = "data"
MEMES_FILE = os.path.join(DATA_DIR, "memes.txt")

# Ensure data directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# ============= HELPER FUNCTIONS =============

def get_all_memes():
    """Read all memes from file and return as list of dictionaries"""
    memes = []
    if os.path.exists(MEMES_FILE):
        with open(MEMES_FILE, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) >= 8:
                    meme = {
                        "id": parts[0],
                        "name": parts[1],
                        "description": parts[2],
                        "creator_id": parts[3],
                        "rarity": parts[4],
                        "price": int(parts[5]),
                        "owner_id": parts[6],
                        "likes": int(parts[7])
                    }
                    memes.append(meme)
    return memes


def save_all_memes(memes):
    """Save all memes back to file"""
    with open(MEMES_FILE, "w") as f:
        for meme in memes:
            line = f"{meme['id']}|{meme['name']}|{meme['description']}|{meme['creator_id']}|{meme['rarity']}|{meme['price']}|{meme['owner_id']}|{meme['likes']}\n"
            f.write(line)


def determine_rarity():
    """Determine rarity based on random chance"""
    roll = random.randint(1, 100)
    if roll >= 95:
        return "Legendary", 100
    elif roll >= 80:
        return "Epic", 70
    elif roll >= 50:
        return "Rare", 40
    else:
        return "Common", 15


# ============= MAIN FUNCTIONS =============

def create_meme(creator_id):
    """Create a new meme NFT - INTERACTIVE"""
    print("\n" + "="*50)
    print("🎨 CREATE NEW MEME NFT".center(50))
    print("="*50)
    
    name = input("Meme Name: ").strip()
    if not name:
        print("❌ Name cannot be empty!")
        input("Press Enter to continue...")
        return
    
    description = input("Description (the moment/joke): ").strip()
    if not description:
        print("❌ Description cannot be empty!")
        input("Press Enter to continue...")
        return
    
    # Determine rarity and price
    rarity, base_price = determine_rarity()
    
    # Generate meme ID
    memes = get_all_memes()
    meme_id = f"NFT{len(memes) + 1:03d}"
    
    # Save meme (creator is also the owner initially)
    with open(MEMES_FILE, "a") as f:
        # Format: id|name|description|creator|rarity|price|owner|likes
        line = f"{meme_id}|{name}|{description}|{creator_id}|{rarity}|{base_price}|{creator_id}|0\n"
        f.write(line)
    
    # Add to creator's NFT collection
    profiles.add_nft_to_collection(creator_id, name)
    
    print(f"\n✅ Meme NFT created successfully!")
    print(f"🎨 NFT ID: {meme_id}")
    print(f"✨ Rarity: {rarity}")
    print(f"💰 Base Price: {base_price} MemeCoins")
    
    # Check for achievements
    memes = get_all_memes()
    creator_memes = [m for m in memes if m['creator_id'] == creator_id]
    if len(creator_memes) == 1:
        profiles.unlock_achievement(creator_id, "Meme Dealer")
    elif len(creator_memes) == 5:
        profiles.unlock_achievement(creator_id, "Meme Master")
    
    input("\nPress Enter to continue...")


def browse_marketplace():
    """Display all available memes"""
    memes = get_all_memes()
    
    if not memes:
        print("\n❌ No memes in the marketplace yet!")
        input("Press Enter to continue...")
        return
    
    print("\n" + "="*70)
    print("🎨 MEME NFT MARKETPLACE".center(70))
    print("="*70)
    
    for i, meme in enumerate(memes, 1):
        print(f"\n{i}. {meme['name']} [{meme['rarity']}]")
        print(f"   📝 Description: {meme['description']}")
        print(f"   👤 Creator: {meme['creator_id']}")
        print(f"   💰 Price: {meme['price']} MemeCoins")
        print(f"   👑 Owner: {meme['owner_id']}")
        print(f"   👍 Likes: {meme['likes']}")
        print(f"   🆔 NFT ID: {meme['id']}")
    
    print("="*70)
    input("\nPress Enter to continue...")


def buy_meme(buyer_id, nft_id):
    """Purchase a meme NFT"""
    memes = get_all_memes()
    
    for meme in memes:
        if meme['id'] == nft_id:
            # Check if trying to buy own meme
            if meme['owner_id'] == buyer_id:
                print("❌ You already own this meme!")
                input("Press Enter to continue...")
                return False
            
            # Check if buyer has enough coins
            buyer = profiles.get_student_by_id(buyer_id)
            if not buyer or buyer['coins'] < meme['price']:
                print(f"❌ Not enough coins! Need {meme['price']}, you have {buyer['coins'] if buyer else 0}")
                input("Press Enter to continue...")
                return False
            
            seller_id = meme['owner_id']
            price = meme['price']
            meme_name = meme['name']
            
            # Process transaction
            # Deduct from buyer
            profiles.update_student_coins(buyer_id, -price)
            # Credit seller
            profiles.update_student_coins(seller_id, price)
            
            # Update NFT ownership
            profiles.remove_nft_from_collection(seller_id, meme_name)
            profiles.add_nft_to_collection(buyer_id, meme_name)
            
            # Update meme owner
            meme['owner_id'] = buyer_id
            save_all_memes(memes)
            
            print(f"\n✅ Meme NFT purchased successfully!")
            print(f"🎨 You now own: {meme_name}")
            print(f"💰 Paid: {price} MemeCoins")
            
            # Check for collector achievement
            buyer_nfts = buyer['nft_collection'].split(",") if buyer['nft_collection'] else []
            if len(buyer_nfts) >= 10:
                profiles.unlock_achievement(buyer_id, "Collector")
            
            input("\nPress Enter to continue...")
            return True
    
    print("❌ Meme NFT not found!")
    input("Press Enter to continue...")
    return False


def view_collection(student_id):
    """Show owned memes"""
    memes = get_all_memes()
    my_memes = [m for m in memes if m['owner_id'] == student_id]
    
    if not my_memes:
        print("\n❌ You don't own any memes yet!")
        input("Press Enter to continue...")
        return
    
    print("\n" + "="*60)
    print("🎨 YOUR NFT COLLECTION".center(60))
    print("="*60)
    
    total_value = 0
    for i, meme in enumerate(my_memes, 1):
        print(f"\n{i}. {meme['name']} [{meme['rarity']}]")
        print(f"   📝 Description: {meme['description']}")
        print(f"   💰 Current Value: {meme['price']} MemeCoins")
        print(f"   👍 Likes: {meme['likes']}")
        print(f"   🆔 NFT ID: {meme['id']}")
        total_value += meme['price']
    
    print(f"\n📊 Collection Stats:")
    print(f"   Total NFTs: {len(my_memes)}")
    print(f"   Total Value: {total_value} MemeCoins")
    print("="*60)
    input("\nPress Enter to continue...")


def like_meme(student_id, nft_id):
    """Like a meme"""
    memes = get_all_memes()
    
    for meme in memes:
        if meme['id'] == nft_id:
            meme['likes'] += 1
            save_all_memes(memes)
            
            print(f"\n👍 Liked: {meme['name']}")
            print(f"Total likes: {meme['likes']}")
            
            # Increase price based on popularity (every 10 likes = +5 coins)
            if meme['likes'] % 10 == 0:
                meme['price'] += 5
                save_all_memes(memes)
                print(f"🔥 Popular! Price increased to {meme['price']} coins")
            
            input("\nPress Enter to continue...")
            return True
    
    print("❌ Meme NFT not found!")
    input("Press Enter to continue...")
    return False


def set_price(student_id, nft_id, new_price):
    """Set new price for owned meme"""
    memes = get_all_memes()
    
    for meme in memes:
        if meme['id'] == nft_id:
            if meme['owner_id'] != student_id:
                print("❌ You don't own this meme!")
                input("Press Enter to continue...")
                return False
            
            meme['price'] = new_price
            save_all_memes(memes)
            
            print(f"✅ Price updated to {new_price} MemeCoins")
            input("\nPress Enter to continue...")
            return True
    
    print("❌ Meme NFT not found!")
    input("Press Enter to continue...")
    return False


# ============= MENU FUNCTION =============

def meme_menu(student_id):
    """Main meme marketplace menu - INTERACTIVE"""
    while True:
        print("\n" + "="*50)
        print("🎨 MEME NFT MARKETPLACE".center(50))
        print("="*50)
        print("1. Browse Marketplace")
        print("2. Create Meme NFT")
        print("3. Buy Meme")
        print("4. My Collection")
        print("5. Like Meme")
        print("6. Set Price (for my memes)")
        print("0. Back to Main Menu")
        print("="*50)
        
        choice = input("\nChoose an option: ").strip()
        
        if choice == "1":
            browse_marketplace()
        
        elif choice == "2":
            create_meme(student_id)
        
        elif choice == "3":
            browse_marketplace()
            nft_id = input("\nEnter NFT ID to buy (or press Enter to cancel): ").strip().upper()
            if nft_id:
                buy_meme(student_id, nft_id)
        
        elif choice == "4":
            view_collection(student_id)
        
        elif choice == "5":
            browse_marketplace()
            nft_id = input("\nEnter NFT ID to like (or press Enter to cancel): ").strip().upper()
            if nft_id:
                like_meme(student_id, nft_id)
        
        elif choice == "6":
            view_collection(student_id)
            nft_id = input("\nEnter NFT ID to update price (or press Enter to cancel): ").strip().upper()
            if nft_id:
                try:
                    new_price = int(input("Enter new price: "))
                    if new_price > 0:
                        set_price(student_id, nft_id, new_price)
                    else:
                        print("❌ Price must be positive!")
                        input("Press Enter to continue...")
                except ValueError:
                    print("❌ Invalid price!")
                    input("Press Enter to continue...")
        
        elif choice == "0":
            break
        
        else:
            print("❌ Invalid choice! Please try again.")
            input("Press Enter to continue...")


# ============= TESTING (Only runs when this file is run directly) =============

if __name__ == "__main__":
    print("="*60)
    print("TESTING MEMBER 3: MEME NFT MARKETPLACE".center(60))
    print("="*60)
    
    test_student_id = input("\nEnter your Student ID for testing: ").strip()
    
    if not test_student_id:
        test_student_id = "TEST001"
        print(f"Using test ID: {test_student_id}")
    
    meme_menu(test_student_id)
