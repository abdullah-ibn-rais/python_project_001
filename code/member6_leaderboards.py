"""
MEMBER 6: LEADERBOARDS & ANALYTICS
Author: [Your Name Here]
Description: Handles rankings, statistics, and analytics across all modules
"""

import os
import sys

# Import all other modules to read their data
sys.path.insert(0, os.path.dirname(__file__))
import member1_profiles as profiles
import member2_quests as quests
import member5_social as social

# ============= DATA FILE PATHS =============

DATA_DIR = "data"
MEMES_FILE = os.path.join(DATA_DIR, "memes.txt")
INVENTORY_FILE = os.path.join(DATA_DIR, "inventory.txt")

# ============= HELPER FUNCTIONS =============

def get_all_memes():
    """Read memes for statistics"""
    memes = []
    if os.path.exists(MEMES_FILE):
        with open(MEMES_FILE, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) >= 8:
                    meme = {
                        "id": parts[0],
                        "name": parts[1],
                        "creator_id": parts[3],
                        "likes": int(parts[7])
                    }
                    memes.append(meme)
    return memes


# ============= MAIN LEADERBOARD FUNCTIONS =============

def show_richest():
    """Display top students by coin balance"""
    students = profiles.get_all_students()
    
    if not students:
        print("\n❌ No students registered yet!")
        input("Press Enter to continue...")
        return
    
    # Sort by coins descending
    sorted_students = sorted(students, key=lambda x: x['coins'], reverse=True)
    top_10 = sorted_students[:10]
    
    print("\n" + "="*60)
    print("💰 TOP 10 RICHEST STUDENTS".center(60))
    print("="*60)
    
    medals = ["🥇", "🥈", "🥉"]
    
    for i, student in enumerate(top_10, 1):
        medal = medals[i-1] if i <= 3 else f"{i}."
        print(f"\n{medal} {student['name']} ({student['id']})")
        print(f"   💰 Coins: {student['coins']}")
        print(f"   ⭐ Level: {student['level']} ({student['title']})")
    
    print("="*60)
    input("\nPress Enter to continue...")


def show_quest_leaders():
    """Display students with most quests completed"""
    students = profiles.get_all_students()
    all_quests = quests.get_all_quests()
    
    if not students:
        print("\n❌ No students registered yet!")
        input("Press Enter to continue...")
        return
    
    # Count completed quests for each student
    student_quest_counts = []
    for student in students:
        count = sum(1 for q in all_quests 
                   if q['status'] == 'Completed' 
                   and q['participants'] 
                   and student['id'] in q['participants'])
        student_quest_counts.append({
            'id': student['id'],
            'name': student['name'],
            'count': count
        })
    
    # Sort by count descending
    sorted_students = sorted(student_quest_counts, key=lambda x: x['count'], reverse=True)
    top_10 = sorted_students[:10]
    
    print("\n" + "="*60)
    print("🎯 TOP 10 QUEST LEADERS".center(60))
    print("="*60)
    
    medals = ["🥇", "🥈", "🥉"]
    
    for i, student in enumerate(top_10, 1):
        if student['count'] == 0:
            continue
        medal = medals[i-1] if i <= 3 else f"{i}."
        print(f"\n{medal} {student['name']} ({student['id']})")
        print(f"   🎯 Quests Completed: {student['count']}")
    
    print("="*60)
    input("\nPress Enter to continue...")


def show_most_helpful():
    """Display students who sent the most coins to others"""
    students = profiles.get_all_students()
    transactions = social.get_all_transactions()
    
    if not students:
        print("\n❌ No students registered yet!")
        input("Press Enter to continue...")
        return
    
    # Calculate total coins sent for each student (verified only)
    student_sent = []
    for student in students:
        total_sent = sum(t['amount'] for t in transactions 
                        if t['from_id'] == student['id'] and t['verified'])
        student_sent.append({
            'id': student['id'],
            'name': student['name'],
            'sent': total_sent
        })
    
    # Sort by total sent descending
    sorted_students = sorted(student_sent, key=lambda x: x['sent'], reverse=True)
    top_10 = sorted_students[:10]
    
    print("\n" + "="*60)
    print("💝 TOP 10 MOST HELPFUL STUDENTS".center(60))
    print("="*60)
    
    medals = ["🥇", "🥈", "🥉"]
    
    for i, student in enumerate(top_10, 1):
        if student['sent'] == 0:
            continue
        medal = medals[i-1] if i <= 3 else f"{i}."
        print(f"\n{medal} {student['name']} ({student['id']})")
        print(f"   💝 Total Coins Given: {student['sent']}")
    
    print("="*60)
    input("\nPress Enter to continue...")


def show_meme_kings():
    """Display top meme creators"""
    students = profiles.get_all_students()
    memes = get_all_memes()
    
    if not students:
        print("\n❌ No students registered yet!")
        input("Press Enter to continue...")
        return
    
    if not memes:
        print("\n❌ No memes created yet!")
        input("Press Enter to continue...")
        return
    
    # Count memes and total likes for each creator
    creator_stats = []
    for student in students:
        meme_count = sum(1 for m in memes if m['creator_id'] == student['id'])
        total_likes = sum(m['likes'] for m in memes if m['creator_id'] == student['id'])
        
        if meme_count > 0:
            creator_stats.append({
                'id': student['id'],
                'name': student['name'],
                'meme_count': meme_count,
                'total_likes': total_likes,
                'score': meme_count * 10 + total_likes  # Weighted score
            })
    
    # Sort by score descending
    sorted_creators = sorted(creator_stats, key=lambda x: x['score'], reverse=True)
    top_10 = sorted_creators[:10]
    
    print("\n" + "="*60)
    print("🎨 TOP 10 MEME KINGS/QUEENS".center(60))
    print("="*60)
    
    medals = ["🥇", "🥈", "🥉"]
    
    for i, creator in enumerate(top_10, 1):
        medal = medals[i-1] if i <= 3 else f"{i}."
        print(f"\n{medal} {creator['name']} ({creator['id']})")
        print(f"   🎨 Memes Created: {creator['meme_count']}")
        print(f"   👍 Total Likes: {creator['total_likes']}")
        print(f"   ⭐ Score: {creator['score']}")
    
    print("="*60)
    input("\nPress Enter to continue...")


def show_top_reputation():
    """Display students with highest reputation"""
    students = profiles.get_all_students()
    
    if not students:
        print("\n❌ No students registered yet!")
        input("Press Enter to continue...")
        return
    
    # Sort by reputation descending
    sorted_students = sorted(students, key=lambda x: x['reputation'], reverse=True)
    top_10 = sorted_students[:10]
    
    print("\n" + "="*60)
    print("💯 TOP 10 REPUTATION LEADERS".center(60))
    print("="*60)
    
    medals = ["🥇", "🥈", "🥉"]
    
    for i, student in enumerate(top_10, 1):
        if student['reputation'] == 0:
            continue
        medal = medals[i-1] if i <= 3 else f"{i}."
        print(f"\n{medal} {student['name']} ({student['id']})")
        print(f"   💯 Reputation: {student['reputation']} points")
        print(f"   ⭐ Level: {student['level']} ({student['title']})")
    
    print("="*60)
    input("\nPress Enter to continue...")


def show_analytics(student_id):
    """Display comprehensive analytics for a specific student"""
    student = profiles.get_student_by_id(student_id)
    
    if not student:
        print("❌ Student not found!")
        input("Press Enter to continue...")
        return
    
    # Gather all statistics
    all_quests = quests.get_all_quests()
    all_transactions = social.get_all_transactions()
    all_memes = get_all_memes()
    
    # Quest stats
    quests_completed = sum(1 for q in all_quests 
                          if q['status'] == 'Completed' 
                          and q['participants'] 
                          and student_id in q['participants'])
    quests_created = sum(1 for q in all_quests if q['creator_id'] == student_id)
    
    # Transaction stats
    coins_sent = sum(t['amount'] for t in all_transactions if t['from_id'] == student_id)
    coins_received = sum(t['amount'] for t in all_transactions if t['to_id'] == student_id)
    
    # Meme stats
    memes_created = sum(1 for m in all_memes if m['creator_id'] == student_id)
    total_likes = sum(m['likes'] for m in all_memes if m['creator_id'] == student_id)
    
    # Calculate total earned (quests + received)
    quest_rewards = sum(q['reward'] for q in all_quests 
                       if q['status'] == 'Completed' 
                       and q['participants'] 
                       and student_id in q['participants'])
    total_earned = quest_rewards + coins_received + 100  # +100 for starting balance
    
    # Total spent
    total_spent = coins_sent + (total_earned - student['coins'])
    
    print("\n" + "="*70)
    print(f"📊 COMPLETE ANALYTICS: {student['name']}".center(70))
    print("="*70)
    
    print("\n💰 FINANCIAL OVERVIEW:")
    print(f"   Current Balance: {student['coins']} MemeCoins")
    print(f"   Total Earned: {total_earned} MemeCoins")
    print(f"   Total Spent: {total_spent} MemeCoins")
    
    print("\n🎯 QUEST STATISTICS:")
    print(f"   Quests Completed: {quests_completed}")
    print(f"   Quests Created: {quests_created}")
    print(f"   Coins from Quests: {quest_rewards}")
    
    print("\n💸 SOCIAL CREDIT:")
    print(f"   Coins Sent to Others: {coins_sent}")
    print(f"   Coins Received: {coins_received}")
    print(f"   Reputation Score: {student['reputation']} points")
    
    print("\n🎨 MEME ACTIVITY:")
    print(f"   Memes Created: {memes_created}")
    print(f"   Total Likes Received: {total_likes}")
    nft_count = len(student['nft_collection'].split(",")) if student['nft_collection'] else 0
    print(f"   NFTs Owned: {nft_count}")
    
    print("\n🏆 PROFILE:")
    print(f"   Level: {student['level']} ({student['title']})")
    achievement_count = len(student['achievements'].split(",")) if student['achievements'] else 0
    print(f"   Achievements: {achievement_count} unlocked")
    
    # Calculate rankings
    all_students = profiles.get_all_students()
    coin_rank = sorted(all_students, key=lambda x: x['coins'], reverse=True).index(student) + 1
    rep_rank = sorted(all_students, key=lambda x: x['reputation'], reverse=True).index(student) + 1
    
    print("\n📊 YOUR RANKINGS:")
    print(f"   Richest: #{coin_rank} out of {len(all_students)}")
    print(f"   Reputation: #{rep_rank} out of {len(all_students)}")
    
    print("="*70)
    input("\nPress Enter to continue...")


# ============= MENU FUNCTION =============

def leaderboard_menu():
    """Main leaderboard menu - INTERACTIVE"""
    while True:
        print("\n" + "="*50)
        print("🏆 LEADERBOARDS & ANALYTICS".center(50))
        print("="*50)
        print("1. 💰 Richest Students")
        print("2. 🎯 Quest Leaders")
        print("3. 💝 Most Helpful")
        print("4. 🎨 Meme Kings/Queens")
        print("5. 💯 Top Reputation")
        print("6. 📊 My Personal Analytics")
        print("0. Back to Main Menu")
        print("="*50)
        
        choice = input("\nChoose an option: ").strip()
        
        if choice == "1":
            show_richest()
        
        elif choice == "2":
            show_quest_leaders()
        
        elif choice == "3":
            show_most_helpful()
        
        elif choice == "4":
            show_meme_kings()
        
        elif choice == "5":
            show_top_reputation()
        
        elif choice == "6":
            student_id = input("\nEnter Student ID for analytics: ").strip()
            if student_id:
                show_analytics(student_id)
        
        elif choice == "0":
            break
        
        else:
            print("❌ Invalid choice! Please try again.")
            input("Press Enter to continue...")


# ============= TESTING (Only runs when this file is run directly) =============

if __name__ == "__main__":
    print("="*60)
    print("TESTING MEMBER 6: LEADERBOARDS & ANALYTICS".center(60))
    print("="*60)
    
    leaderboard_menu()
