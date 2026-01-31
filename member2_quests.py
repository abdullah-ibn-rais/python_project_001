"""
MEMBER 2: QUEST/CHALLENGE MANAGER
Handles: Creating quests, accepting quests, completing quests, rewards
"""

import os
from datetime import datetime

# Import Member 1's functions for updating coins
import member1_profiles as profiles

# ============= HELPER FUNCTIONS =============

def get_all_quests():
    """Read all quests from file"""
    quests = []
    if os.path.exists("data/quests.txt"):
        with open("data/quests.txt", "r") as f:
            for line in f:
                data = line.strip().split("|")
                if len(data) >= 8:
                    quest = {
                        "id": data[0],
                        "title": data[1],
                        "description": data[2],
                        "reward": int(data[3]),
                        "type": data[4],
                        "difficulty": data[5],
                        "creator_id": data[6],
                        "status": data[7],
                        "participants": data[8] if len(data) > 8 else ""
                    }
                    quests.append(quest)
    return quests


def save_all_quests(quests):
    """Save all quests back to file"""
    with open("data/quests.txt", "w") as f:
        for quest in quests:
            line = f"{quest['id']}|{quest['title']}|{quest['description']}|{quest['reward']}|{quest['type']}|{quest['difficulty']}|{quest['creator_id']}|{quest['status']}|{quest['participants']}\n"
            f.write(line)


def count_completed_quests(student_id):
    """Count how many quests a student has completed"""
    quests = get_all_quests()
    count = 0
    for quest in quests:
        if quest['status'] == 'Completed' and quest['participants'] and student_id in quest['participants']:
            count += 1
    return count


# ============= MAIN FUNCTIONS =============

def view_quests():
    """Display all available quests"""
    quests = get_all_quests()
    active_quests = [q for q in quests if q['status'] == 'Active']
    
    if not active_quests:
        print("\n❌ No active quests available right now!")
        input("Press Enter to continue...")
        return
    
    print("\n" + "="*70)
    print("🎯 AVAILABLE QUESTS".center(70))
    print("="*70)
    
    for i, quest in enumerate(active_quests, 1):
        print(f"\n{i}. {quest['title']} [{quest['difficulty']}]")
        print(f"   📋 Type: {quest['type']}")
        print(f"   📝 Description: {quest['description']}")
        print(f"   🪙 Reward: {quest['reward']} MemeCoins")
        print(f"   🆔 Quest ID: {quest['id']}")
        print(f"   👤 Created by: {quest['creator_id']}")
        
        if quest['participants']:
            participant_count = len(quest['participants'].split(','))
            print(f"   👥 Participants: {participant_count}")
    
    print("="*70)
    input("\nPress Enter to continue...")


def create_quest(creator_id):
    """Create a new quest"""
    print("\n" + "="*50)
    print("➕ CREATE NEW QUEST".center(50))
    print("="*50)
    
    title = input("Quest Title: ").strip()
    description = input("Description: ").strip()
    
    try:
        reward = int(input("Reward (MemeCoins): "))
    except ValueError:
        print("❌ Invalid reward amount!")
        input("Press Enter to continue...")
        return
    
    print("\nQuest Types:")
    print("1. Academic (Tutoring, study groups)")
    print("2. Social (Events, helping others)")
    print("3. Creative (Memes, content)")
    print("4. Campus (Seminars, competitions)")
    type_choice = input("Choose type (1-4): ").strip()
    
    types = {"1": "Academic", "2": "Social", "3": "Creative", "4": "Campus"}
    quest_type = types.get(type_choice, "Academic")
    
    print("\nDifficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    diff_choice = input("Choose difficulty (1-3): ").strip()
    
    difficulties = {"1": "Easy", "2": "Medium", "3": "Hard"}
    difficulty = difficulties.get(diff_choice, "Medium")
    
    # Generate quest ID
    quests = get_all_quests()
    quest_id = f"Q{len(quests) + 1:03d}"
    
    # Save quest
    with open("data/quests.txt", "a") as f:
        line = f"{quest_id}|{title}|{description}|{reward}|{quest_type}|{difficulty}|{creator_id}|Active|\n"
        f.write(line)
    
    print(f"\n✅ Quest created successfully!")
    print(f"🎯 Quest ID: {quest_id}")
    print(f"🪙 Reward: {reward} MemeCoins")
    input("\nPress Enter to continue...")


def accept_quest(student_id, quest_id):
    """Student accepts a quest"""
    quests = get_all_quests()
    
    for quest in quests:
        if quest['id'] == quest_id:
            if quest['status'] != 'Active':
                print("❌ This quest is not active!")
                input("Press Enter to continue...")
                return False
            
            # Check if student is the creator
            if quest['creator_id'] == student_id:
                print("❌ You cannot accept your own quest!")
                input("Press Enter to continue...")
                return False
            
            # Add student to participants
            if quest['participants']:
                participants = quest['participants'].split(",")
                if student_id in participants:
                    print("❌ You already accepted this quest!")
                    input("Press Enter to continue...")
                    return False
                participants.append(student_id)
                quest['participants'] = ",".join(participants)
            else:
                quest['participants'] = student_id
            
            # Save back
            save_all_quests(quests)
            print(f"\n✅ Quest accepted: {quest['title']}")
            print(f"🎯 Complete it to earn {quest['reward']} MemeCoins!")
            input("\nPress Enter to continue...")
            return True
    
    print("❌ Quest not found!")
    input("Press Enter to continue...")
    return False


def complete_quest(student_id, quest_id):
    """Complete a quest and earn reward"""
    quests = get_all_quests()
    
    for quest in quests:
        if quest['id'] == quest_id:
            # Check if student accepted this quest
            if not quest['participants'] or student_id not in quest['participants']:
                print("❌ You haven't accepted this quest!")
                input("Press Enter to continue...")
                return False
            
            # Check if already completed
            if quest['status'] == 'Completed':
                print("❌ This quest is already completed!")
                input("Press Enter to continue...")
                return False
            
            # Mark as completed
            quest['status'] = 'Completed'
            save_all_quests(quests)
            
            # Give reward
            profiles.update_student_coins(student_id, quest['reward'])
            
            print("\n" + "="*50)
            print("🎉 QUEST COMPLETED!".center(50))
            print("="*50)
            print(f"📜 Quest: {quest['title']}")
            print(f"🪙 Earned: {quest['reward']} MemeCoins")
            print("="*50)
            
            # Check for achievements
            completed_count = count_completed_quests(student_id)
            if completed_count == 1:
                profiles.unlock_achievement(student_id, "First Blood")
            elif completed_count == 10:
                profiles.unlock_achievement(student_id, "Quest Master")
            
            input("\nPress Enter to continue...")
            return True
    
    print("❌ Quest not found!")
    input("Press Enter to continue...")
    return False


def view_my_quests(student_id):
    """View quests you created or joined"""
    quests = get_all_quests()
    
    created = [q for q in quests if q['creator_id'] == student_id]
    joined = [q for q in quests if q['participants'] and student_id in q['participants']]
    
    print("\n" + "="*60)
    print("📋 MY QUESTS".center(60))
    print("="*60)
    
    if created:
        print("\n🎯 Quests You Created:")
        for quest in created:
            status_emoji = "✅" if quest['status'] == 'Completed' else "🔄"
            print(f"  {status_emoji} {quest['id']}: {quest['title']} ({quest['reward']} coins)")
    
    if joined:
        print("\n👤 Quests You Joined:")
        for quest in joined:
            status_emoji = "✅" if quest['status'] == 'Completed' else "🔄"
            print(f"  {status_emoji} {quest['id']}: {quest['title']} ({quest['reward']} coins)")
    
    if not created and not joined:
        print("\n❌ You haven't created or joined any quests yet!")
    
    print("="*60)
    input("\nPress Enter to continue...")


# ============= MENU FUNCTION =============

def quest_menu(student_id):
    """Main quest menu"""
    while True:
        print("\n" + "="*50)
        print("🎯 QUEST BOARD".center(50))
        print("="*50)
        print("1. View All Quests")
        print("2. Create New Quest")
        print("3. Accept Quest")
        print("4. Complete Quest")
        print("5. My Quests")
        print("0. Back to Main Menu")
        print("="*50)
        
        choice = input("\nChoose an option: ").strip()
        
        if choice == "1":
            view_quests()
        
        elif choice == "2":
            create_quest(student_id)
        
        elif choice == "3":
            view_quests()
            quest_id = input("\nEnter Quest ID to accept: ").strip().upper()
            accept_quest(student_id, quest_id)
        
        elif choice == "4":
            # Show student's active quests
            quests = get_all_quests()
            my_quests = [q for q in quests if q['participants'] and student_id in q['participants'] and q['status'] == 'Active']
            
            if not my_quests:
                print("\n❌ You have no active quests to complete!")
                input("Press Enter to continue...")
                continue
            
            print("\n📋 Your Active Quests:")
            for quest in my_quests:
                print(f"  🎯 {quest['id']}: {quest['title']} - {quest['reward']} coins")
            
            quest_id = input("\nEnter Quest ID to complete: ").strip().upper()
            complete_quest(student_id, quest_id)
        
        elif choice == "5":
            view_my_quests(student_id)
        
        elif choice == "0":
            break
        
        else:
            print("❌ Invalid choice! Please try again.")
            input("Press Enter to continue...")


# ============= TESTING CODE =============

if __name__ == "__main__":
    if not os.path.exists("data"):
        os.makedirs("data")
    
    # Test with a sample student ID
    test_id = "NSU210101"
    quest_menu(test_id)
