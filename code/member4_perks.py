"""
MEMBER 4: PERK SHOP SYSTEM
Author: [Your Name Here]
Description: Handles perk browsing, purchasing, inventory, and redemption
"""

import os
import sys
from datetime import datetime, timedelta

# Import Member 1's module
sys.path.insert(0, os.path.dirname(__file__))
import member1_profiles as profiles

# ============= DATA FILE PATHS =============

DATA_DIR = "data"
PERKS_FILE = os.path.join(DATA_DIR, "perks.txt")
INVENTORY_FILE = os.path.join(DATA_DIR, "inventory.txt")

# Ensure data directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Initialize perks file with default perks if it doesn't exist
if not os.path.exists(PERKS_FILE):
    with open(PERKS_FILE, "w") as f:
        f.write("PERK01|Canteen Queue Skip|30|10|Instant|CSE Club|1 day\n")
        f.write("PERK02|Premium Notes Access|50|5|Academic|EEE Club|1 week\n")
        f.write("PERK03|Front Row Seat|40|8|Instant|Admin|1 day\n")
        f.write("PERK04|Library Late Return|60|3|Academic|Library|3 days\n")
        f.write("PERK05|Gaming Zone Priority|25|15|Instant|CSE Club|2 hours\n")

# ============= HELPER FUNCTIONS =============

def get_all_perks():
    """Read all perks from file and return as list of dictionaries"""
    perks = []
    if os.path.exists(PERKS_FILE):
        with open(PERKS_FILE, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) >= 7:
                    perk = {
                        "id": parts[0],
                        "name": parts[1],
                        "cost": int(parts[2]),
                        "quantity": int(parts[3]),
                        "type": parts[4],
                        "seller": parts[5],
                        "validity": parts[6]
                    }
                    perks.append(perk)
    return perks


def save_all_perks(perks):
    """Save all perks back to file"""
    with open(PERKS_FILE, "w") as f:
        for perk in perks:
            line = f"{perk['id']}|{perk['name']}|{perk['cost']}|{perk['quantity']}|{perk['type']}|{perk['seller']}|{perk['validity']}\n"
            f.write(line)


def get_student_inventory(student_id):
    """Get all perks owned by a student"""
    inventory = []
    if os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) >= 4 and parts[0] == student_id:
                    item = {
                        "student_id": parts[0],
                        "perk_id": parts[1],
                        "purchase_date": parts[2],
                        "status": parts[3]
                    }
                    inventory.append(item)
    return inventory


def add_to_inventory(student_id, perk_id):
    """Add a purchased perk to student's inventory"""
    purchase_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(INVENTORY_FILE, "a") as f:
        # Format: student_id|perk_id|purchase_date|status
        line = f"{student_id}|{perk_id}|{purchase_date}|Active\n"
        f.write(line)


def update_inventory_status(student_id, perk_id, new_status):
    """Update the status of a perk in inventory"""
    if not os.path.exists(INVENTORY_FILE):
        return False
    
    lines = []
    updated = False
    
    with open(INVENTORY_FILE, "r") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) >= 4 and parts[0] == student_id and parts[1] == perk_id and parts[3] == "Active":
                parts[3] = new_status
                updated = True
            lines.append("|".join(parts) + "\n")
    
    if updated:
        with open(INVENTORY_FILE, "w") as f:
            f.writelines(lines)
    
    return updated


# ============= MAIN FUNCTIONS =============

def view_perks():
    """Display all available perks"""
    perks = get_all_perks()
    available_perks = [p for p in perks if p['quantity'] > 0]
    
    if not available_perks:
        print("\n❌ No perks available right now!")
        input("Press Enter to continue...")
        return
    
    print("\n" + "="*70)
    print("🛒 PERK SHOP - AVAILABLE PERKS".center(70))
    print("="*70)
    
    for i, perk in enumerate(available_perks, 1):
        print(f"\n{i}. {perk['name']} [{perk['type']}]")
        print(f"   💰 Cost: {perk['cost']} MemeCoins")
        print(f"   📦 Available: {perk['quantity']} left")
        print(f"   👤 Seller: {perk['seller']}")
        print(f"   ⏱️  Valid for: {perk['validity']}")
        print(f"   🆔 Perk ID: {perk['id']}")
    
    print("="*70)
    input("\nPress Enter to continue...")


def purchase_perk(student_id, perk_id):
    """Purchase a perk"""
    perks = get_all_perks()
    
    for perk in perks:
        if perk['id'] == perk_id:
            # Check quantity
            if perk['quantity'] <= 0:
                print("❌ This perk is out of stock!")
                input("Press Enter to continue...")
                return False
            
            # Check if student has enough coins
            student = profiles.get_student_by_id(student_id)
            if not student or student['coins'] < perk['cost']:
                print(f"❌ Not enough coins! Need {perk['cost']}, you have {student['coins'] if student else 0}")
                input("Press Enter to continue...")
                return False
            
            # Process purchase
            # Deduct coins from buyer
            profiles.update_student_coins(student_id, -perk['cost'])
            
            # Reduce quantity
            perk['quantity'] -= 1
            save_all_perks(perks)
            
            # Add to inventory
            add_to_inventory(student_id, perk_id)
            
            print(f"\n✅ Perk purchased successfully!")
            print(f"🎁 You bought: {perk['name']}")
            print(f"💰 Cost: {perk['cost']} MemeCoins")
            print(f"⏱️  Valid for: {perk['validity']}")
            
            # Show remaining balance
            student = profiles.get_student_by_id(student_id)
            print(f"🪙 Remaining balance: {student['coins']} MemeCoins")
            
            input("\nPress Enter to continue...")
            return True
    
    print("❌ Perk not found!")
    input("Press Enter to continue...")
    return False


def view_inventory(student_id):
    """Show student's purchased perks"""
    inventory = get_student_inventory(student_id)
    
    if not inventory:
        print("\n❌ Your inventory is empty!")
        input("Press Enter to continue...")
        return
    
    print("\n" + "="*60)
    print("📦 YOUR PERK INVENTORY".center(60))
    print("="*60)
    
    perks = get_all_perks()
    perk_dict = {p['id']: p for p in perks}
    
    active_count = 0
    used_count = 0
    
    for item in inventory:
        perk = perk_dict.get(item['perk_id'])
        if perk:
            status_emoji = "✅" if item['status'] == "Active" else "✓"
            print(f"\n{status_emoji} {perk['name']}")
            print(f"   📅 Purchased: {item['purchase_date']}")
            print(f"   ⏱️  Valid for: {perk['validity']}")
            print(f"   📊 Status: {item['status']}")
            print(f"   🆔 Perk ID: {item['perk_id']}")
            
            if item['status'] == "Active":
                active_count += 1
            else:
                used_count += 1
    
    print(f"\n📊 Inventory Stats:")
    print(f"   Active Perks: {active_count}")
    print(f"   Used Perks: {used_count}")
    print(f"   Total Perks: {len(inventory)}")
    print("="*60)
    input("\nPress Enter to continue...")


def redeem_perk(student_id, perk_id):
    """Redeem/use a perk"""
    inventory = get_student_inventory(student_id)
    
    # Find active perk in inventory
    found = False
    for item in inventory:
        if item['perk_id'] == perk_id and item['status'] == "Active":
            found = True
            break
    
    if not found:
        print("❌ You don't have an active perk with this ID!")
        input("Press Enter to continue...")
        return False
    
    # Get perk details
    perks = get_all_perks()
    perk = None
    for p in perks:
        if p['id'] == perk_id:
            perk = p
            break
    
    if not perk:
        print("❌ Perk not found!")
        input("Press Enter to continue...")
        return False
    
    # Update status to Used
    if update_inventory_status(student_id, perk_id, "Used"):
        print(f"\n✅ Perk redeemed successfully!")
        print(f"🎁 {perk['name']}")
        print(f"📝 Show this confirmation to claim your benefit!")
        print(f"🔢 Redemption Code: {perk_id}-{student_id[-4:]}")
        input("\nPress Enter to continue...")
        return True
    else:
        print("❌ Failed to redeem perk!")
        input("Press Enter to continue...")
        return False


def add_perk_to_shop():
    """Add a new perk to the shop (admin function)"""
    print("\n" + "="*50)
    print("➕ ADD NEW PERK TO SHOP".center(50))
    print("="*50)
    
    name = input("Perk Name: ").strip()
    if not name:
        print("❌ Name cannot be empty!")
        input("Press Enter to continue...")
        return
    
    try:
        cost = int(input("Cost (MemeCoins): "))
        if cost <= 0:
            print("❌ Cost must be positive!")
            input("Press Enter to continue...")
            return
    except ValueError:
        print("❌ Invalid cost!")
        input("Press Enter to continue...")
        return
    
    try:
        quantity = int(input("Quantity: "))
        if quantity <= 0:
            print("❌ Quantity must be positive!")
            input("Press Enter to continue...")
            return
    except ValueError:
        print("❌ Invalid quantity!")
        input("Press Enter to continue...")
        return
    
    perk_type = input("Type (Instant/Academic/Campus): ").strip()
    seller = input("Seller (e.g., CSE Club, Admin): ").strip()
    validity = input("Validity (e.g., 1 day, 1 week): ").strip()
    
    # Generate perk ID
    perks = get_all_perks()
    perk_id = f"PERK{len(perks) + 1:02d}"
    
    # Save perk
    with open(PERKS_FILE, "a") as f:
        line = f"{perk_id}|{name}|{cost}|{quantity}|{perk_type}|{seller}|{validity}\n"
        f.write(line)
    
    print(f"\n✅ Perk added to shop!")
    print(f"🆔 Perk ID: {perk_id}")
    input("\nPress Enter to continue...")


# ============= MENU FUNCTION =============

def perk_menu(student_id):
    """Main perk shop menu - INTERACTIVE"""
    while True:
        print("\n" + "="*50)
        print("🛒 PERK SHOP".center(50))
        print("="*50)
        print("1. Browse Available Perks")
        print("2. Purchase Perk")
        print("3. My Inventory")
        print("4. Redeem Perk")
        print("5. Add Perk to Shop (Admin)")
        print("0. Back to Main Menu")
        print("="*50)
        
        choice = input("\nChoose an option: ").strip()
        
        if choice == "1":
            view_perks()
        
        elif choice == "2":
            view_perks()
            perk_id = input("\nEnter Perk ID to buy (or press Enter to cancel): ").strip().upper()
            if perk_id:
                purchase_perk(student_id, perk_id)
        
        elif choice == "3":
            view_inventory(student_id)
        
        elif choice == "4":
            view_inventory(student_id)
            perk_id = input("\nEnter Perk ID to redeem (or press Enter to cancel): ").strip().upper()
            if perk_id:
                redeem_perk(student_id, perk_id)
        
        elif choice == "5":
            add_perk_to_shop()
        
        elif choice == "0":
            break
        
        else:
            print("❌ Invalid choice! Please try again.")
            input("Press Enter to continue...")


# ============= TESTING (Only runs when this file is run directly) =============

if __name__ == "__main__":
    print("="*60)
    print("TESTING MEMBER 4: PERK SHOP SYSTEM".center(60))
    print("="*60)
    
    test_student_id = input("\nEnter your Student ID for testing: ").strip()
    
    if not test_student_id:
        test_student_id = "TEST001"
        print(f"Using test ID: {test_student_id}")
    
    perk_menu(test_student_id)
