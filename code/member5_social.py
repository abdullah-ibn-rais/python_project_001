"""
MEMBER 5: SOCIAL CREDIT ENGINE
Author: [Your Name Here]
Description: Handles direct coin transfers, transactions, verification, and reputation
"""

import os
import sys
from datetime import datetime

# Import Member 1's module
sys.path.insert(0, os.path.dirname(__file__))
import member1_profiles as profiles

# ============= DATA FILE PATHS =============

DATA_DIR = "data"
TRANSACTIONS_FILE = os.path.join(DATA_DIR, "transactions.txt")

# Ensure data directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# ============= HELPER FUNCTIONS =============

def get_all_transactions():
    """Read all transactions from file and return as list of dictionaries"""
    transactions = []
    if os.path.exists(TRANSACTIONS_FILE):
        with open(TRANSACTIONS_FILE, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) >= 7:
                    txn = {
                        "id": parts[0],
                        "from_id": parts[1],
                        "to_id": parts[2],
                        "amount": int(parts[3]),
                        "reason": parts[4],
                        "verified": parts[5] == "True",
                        "timestamp": parts[6]
                    }
                    transactions.append(txn)
    return transactions


def save_all_transactions(transactions):
    """Save all transactions back to file"""
    with open(TRANSACTIONS_FILE, "w") as f:
        for txn in transactions:
            verified_str = "True" if txn['verified'] else "False"
            line = f"{txn['id']}|{txn['from_id']}|{txn['to_id']}|{txn['amount']}|{txn['reason']}|{verified_str}|{txn['timestamp']}\n"
            f.write(line)


def get_transaction_count():
    """Get total number of transactions"""
    transactions = get_all_transactions()
    return len(transactions)


# ============= MAIN FUNCTIONS =============

def send_coins(from_id, to_id, amount, reason):
    """Send coins from one student to another"""
    # Validate inputs
    if from_id == to_id:
        print("❌ You cannot send coins to yourself!")
        input("Press Enter to continue...")
        return False
    
    if amount <= 0:
        print("❌ Amount must be positive!")
        input("Press Enter to continue...")
        return False
    
    # Check if sender exists and has enough coins
    sender = profiles.get_student_by_id(from_id)
    if not sender:
        print("❌ Sender not found!")
        input("Press Enter to continue...")
        return False
    
    if sender['coins'] < amount:
        print(f"❌ Not enough coins! You have {sender['coins']}, need {amount}")
        input("Press Enter to continue...")
        return False
    
    # Check if receiver exists
    receiver = profiles.get_student_by_id(to_id)
    if not receiver:
        print("❌ Receiver not found!")
        input("Press Enter to continue...")
        return False
    
    # Process transaction
    # Deduct from sender
    profiles.update_student_coins(from_id, -amount)
    # Add to receiver
    profiles.update_student_coins(to_id, amount)
    
    # Log transaction
    txn_id = f"T{get_transaction_count() + 1:03d}"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    with open(TRANSACTIONS_FILE, "a") as f:
        # Format: id|from|to|amount|reason|verified|timestamp
        line = f"{txn_id}|{from_id}|{to_id}|{amount}|{reason}|False|{timestamp}\n"
        f.write(line)
    
    print(f"\n✅ Transaction successful!")
    print(f"💸 Sent {amount} MemeCoins to {to_id}")
    print(f"📝 Reason: {reason}")
    print(f"🆔 Transaction ID: {txn_id}")
    print(f"\n⚠️  Transaction is UNVERIFIED until receiver confirms")
    
    # Show remaining balance
    sender = profiles.get_student_by_id(from_id)
    print(f"🪙 Your new balance: {sender['coins']} MemeCoins")
    
    input("\nPress Enter to continue...")
    return True


def view_transactions(student_id):
    """Show transaction history for a student"""
    transactions = get_all_transactions()
    
    sent = [t for t in transactions if t['from_id'] == student_id]
    received = [t for t in transactions if t['to_id'] == student_id]
    
    if not sent and not received:
        print("\n❌ No transactions yet!")
        input("Press Enter to continue...")
        return
    
    print("\n" + "="*70)
    print("💸 TRANSACTION HISTORY".center(70))
    print("="*70)
    
    if sent:
        print("\n📤 SENT TRANSACTIONS:")
        for txn in sent:
            verified_icon = "✓" if txn['verified'] else "⏳"
            print(f"\n{verified_icon} {txn['id']}: Sent {txn['amount']} coins to {txn['to_id']}")
            print(f"   📝 Reason: {txn['reason']}")
            print(f"   📅 Date: {txn['timestamp']}")
            print(f"   ✅ Status: {'Verified' if txn['verified'] else 'Pending Verification'}")
    
    if received:
        print("\n📥 RECEIVED TRANSACTIONS:")
        for txn in received:
            verified_icon = "✓" if txn['verified'] else "⏳"
            print(f"\n{verified_icon} {txn['id']}: Received {txn['amount']} coins from {txn['from_id']}")
            print(f"   📝 Reason: {txn['reason']}")
            print(f"   📅 Date: {txn['timestamp']}")
            print(f"   ✅ Status: {'Verified' if txn['verified'] else 'Pending Verification'}")
    
    print("="*70)
    input("\nPress Enter to continue...")


def verify_transaction(txn_id, verifier_id):
    """Verify a transaction (called by receiver)"""
    transactions = get_all_transactions()
    
    for txn in transactions:
        if txn['id'] == txn_id:
            # Check if verifier is the receiver
            if txn['to_id'] != verifier_id:
                print("❌ You can only verify transactions sent TO you!")
                input("Press Enter to continue...")
                return False
            
            # Check if already verified
            if txn['verified']:
                print("❌ This transaction is already verified!")
                input("Press Enter to continue...")
                return False
            
            # Mark as verified
            txn['verified'] = True
            save_all_transactions(transactions)
            
            # Update reputation for both parties
            # Sender gets +10 points
            profiles.update_reputation(txn['from_id'], 10)
            # Receiver gets +5 points
            profiles.update_reputation(txn['to_id'], 5)
            
            print(f"\n✅ Transaction verified successfully!")
            print(f"💸 {txn['from_id']} → {txn['to_id']}: {txn['amount']} coins")
            print(f"📝 Reason: {txn['reason']}")
            print(f"\n🎉 Reputation updated:")
            print(f"   {txn['from_id']}: +10 reputation")
            print(f"   {txn['to_id']}: +5 reputation")
            
            # Check for achievements
            verified_sent = sum(1 for t in transactions if t['from_id'] == txn['from_id'] and t['verified'])
            if verified_sent == 5:
                profiles.unlock_achievement(txn['from_id'], "Helper")
            elif verified_sent == 10:
                profiles.unlock_achievement(txn['from_id'], "Social Butterfly")
            
            input("\nPress Enter to continue...")
            return True
    
    print("❌ Transaction not found!")
    input("Press Enter to continue...")
    return False


def calculate_reputation(student_id):
    """Calculate total reputation score for a student"""
    transactions = get_all_transactions()
    
    # Count verified transactions sent (+10 each)
    verified_sent = sum(10 for t in transactions if t['from_id'] == student_id and t['verified'])
    
    # Count verified transactions received (+5 each)
    verified_received = sum(5 for t in transactions if t['to_id'] == student_id and t['verified'])
    
    total_reputation = verified_sent + verified_received
    
    return total_reputation


def get_unverified_transactions(student_id):
    """Get transactions that need verification by this student"""
    transactions = get_all_transactions()
    
    # Find unverified transactions where student is the receiver
    unverified = [t for t in transactions if t['to_id'] == student_id and not t['verified']]
    
    return unverified


def view_pending_verifications(student_id):
    """Show transactions waiting for verification"""
    unverified = get_unverified_transactions(student_id)
    
    if not unverified:
        print("\n✅ No pending verifications!")
        input("Press Enter to continue...")
        return
    
    print("\n" + "="*70)
    print("⏳ PENDING VERIFICATIONS".center(70))
    print("="*70)
    print("\nThese people sent you coins. Please verify if they actually helped you:\n")
    
    for txn in unverified:
        print(f"🆔 {txn['id']}: {txn['from_id']} sent you {txn['amount']} coins")
        print(f"   📝 Reason: {txn['reason']}")
        print(f"   📅 Date: {txn['timestamp']}")
        print()
    
    print("="*70)
    input("\nPress Enter to continue...")


# ============= MENU FUNCTION =============

def social_menu(student_id):
    """Main social credit menu - INTERACTIVE"""
    while True:
        # Calculate and show current reputation
        rep = calculate_reputation(student_id)
        
        print("\n" + "="*50)
        print("💸 SOCIAL CREDIT ENGINE".center(50))
        print("="*50)
        print(f"💯 Your Reputation: {rep} points")
        print("="*50)
        print("1. Send Coins to Someone")
        print("2. View My Transactions")
        print("3. Verify Transaction")
        print("4. Pending Verifications")
        print("5. View My Reputation")
        print("0. Back to Main Menu")
        print("="*50)
        
        choice = input("\nChoose an option: ").strip()
        
        if choice == "1":
            print("\n" + "="*50)
            print("💸 SEND COINS".center(50))
            print("="*50)
            
            to_id = input("Recipient Student ID: ").strip()
            if not to_id:
                continue
            
            try:
                amount = int(input("Amount (MemeCoins): "))
            except ValueError:
                print("❌ Invalid amount!")
                input("Press Enter to continue...")
                continue
            
            reason = input("Reason for sending: ").strip()
            if not reason:
                reason = "No reason specified"
            
            send_coins(student_id, to_id, amount, reason)
        
        elif choice == "2":
            view_transactions(student_id)
        
        elif choice == "3":
            view_pending_verifications(student_id)
            txn_id = input("\nEnter Transaction ID to verify (or press Enter to cancel): ").strip().upper()
            if txn_id:
                verify_transaction(txn_id, student_id)
        
        elif choice == "4":
            view_pending_verifications(student_id)
        
        elif choice == "5":
            transactions = get_all_transactions()
            sent_verified = sum(1 for t in transactions if t['from_id'] == student_id and t['verified'])
            received_verified = sum(1 for t in transactions if t['to_id'] == student_id and t['verified'])
            
            print("\n" + "="*50)
            print("💯 YOUR REPUTATION BREAKDOWN".center(50))
            print("="*50)
            print(f"📤 Verified Coins Sent: {sent_verified} transactions × 10 = {sent_verified * 10} points")
            print(f"📥 Verified Coins Received: {received_verified} transactions × 5 = {received_verified * 5} points")
            print(f"{'─'*50}")
            print(f"💯 TOTAL REPUTATION: {rep} points")
            print("="*50)
            input("\nPress Enter to continue...")
        
        elif choice == "0":
            break
        
        else:
            print("❌ Invalid choice! Please try again.")
            input("Press Enter to continue...")


# ============= TESTING (Only runs when this file is run directly) =============

if __name__ == "__main__":
    print("="*60)
    print("TESTING MEMBER 5: SOCIAL CREDIT ENGINE".center(60))
    print("="*60)
    
    test_student_id = input("\nEnter your Student ID for testing: ").strip()
    
    if not test_student_id:
        test_student_id = "TEST001"
        print(f"Using test ID: {test_student_id}")
    
    social_menu(test_student_id)
