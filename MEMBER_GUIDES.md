# 👥 INDIVIDUAL MEMBER GUIDES
## What Each Person Needs to Build & Present

---

## 📊 MEMBER 1: STUDENT PROFILE SYSTEM

### What You're Responsible For
You handle everything related to student accounts - registration, login, profile viewing, and achievements.

### Your Data File: `students.txt`
**Format:**
```
student_id|name|coins|level|title|reputation|nft_collection|achievements
NSU210101|Rahat Ahmed|420|5|Meme Lord|850|Drake,Boyfriend|First Blood,Night Owl
NSU210505|Nadia Khan|280|3|Regular|520|Pepe|First Blood
```

### Functions You Need to Build

#### 1. `register_student()` - Create new account
```python
def register_student():
    """Register a new student"""
    print("\n=== 📝 Student Registration ===")
    
    # Get student info
    student_id = input("Enter Student ID (e.g., NSU210101): ")
    name = input("Enter Full Name: ")
    
    # Check if ID already exists
    if student_exists(student_id):
        print("❌ This Student ID is already registered!")
        return False
    
    # Create default student data
    coins = 100  # Starting coins
    level = 1    # Starting level
    title = "Noob"
    reputation = 0
    nft_collection = ""
    achievements = ""
    
    # Save to file
    with open("data/students.txt", "a") as f:
        line = f"{student_id}|{name}|{coins}|{level}|{title}|{reputation}|{nft_collection}|{achievements}\n"
        f.write(line)
    
    print(f"✅ Welcome, {name}! You've been registered successfully!")
    print(f"🪙 Starting balance: {coins} MemeCoins")
    return True
```

#### 2. `login_student()` - Login existing student
```python
def login_student():
    """Login to system"""
    print("\n=== 🔑 Student Login ===")
    student_id = input("Enter Student ID: ")
    
    # Check if student exists
    student = get_student_by_id(student_id)
    if student:
        print(f"✅ Welcome back, {student['name']}!")
        return student_id
    else:
        print("❌ Student ID not found!")
        return None
```

#### 3. `display_profile(student_id)` - Show student stats
```python
def display_profile(student_id):
    """Display full student profile"""
    student = get_student_by_id(student_id)
    
    if not student:
        print("❌ Student not found!")
        return
    
    print("\n" + "="*50)
    print("👤 STUDENT PROFILE".center(50))
    print("="*50)
    print(f"🆔 ID:          {student['id']}")
    print(f"👨 Name:        {student['name']}")
    print(f"🪙 MemeCoins:   {student['coins']}")
    print(f"⭐ Level:       {student['level']}")
    print(f"🏆 Title:       {student['title']}")
    print(f"💯 Reputation:  {student['reputation']}")
    
    # Display NFT collection
    if student['nft_collection']:
        nfts = student['nft_collection'].split(",")
        print(f"🎨 NFTs:        {len(nfts)} owned")
        for nft in nfts:
            print(f"   - {nft}")
    else:
        print(f"🎨 NFTs:        None yet")
    
    # Display achievements
    if student['achievements']:
        achievements = student['achievements'].split(",")
        print(f"🏅 Achievements: {len(achievements)} unlocked")
        for achievement in achievements:
            print(f"   ✓ {achievement}")
    else:
        print(f"🏅 Achievements: None yet")
    
    print("="*50)
```

#### 4. `unlock_achievement(student_id, achievement_name)` - Add achievement
```python
def unlock_achievement(student_id, achievement_name):
    """Unlock an achievement for student"""
    students = get_all_students()
    
    for student in students:
        if student['id'] == student_id:
            # Check if already has achievement
            if student['achievements']:
                current = student['achievements'].split(",")
                if achievement_name in current:
                    return False  # Already has it
                current.append(achievement_name)
                student['achievements'] = ",".join(current)
            else:
                student['achievements'] = achievement_name
            
            # Save back to file
            save_all_students(students)
            print(f"🏅 Achievement Unlocked: {achievement_name}!")
            return True
    
    return False
```

#### 5. Helper Functions (you need these too!)
```python
def get_all_students():
    """Read all students from file"""
    students = []
    try:
        with open("data/students.txt", "r") as f:
            for line in f:
                data = line.strip().split("|")
                student = {
                    "id": data[0],
                    "name": data[1],
                    "coins": int(data[2]),
                    "level": int(data[3]),
                    "title": data[4],
                    "reputation": int(data[5]),
                    "nft_collection": data[6],
                    "achievements": data[7]
                }
                students.append(student)
    except FileNotFoundError:
        pass  # File doesn't exist yet
    return students

def get_student_by_id(student_id):
    """Find specific student"""
    students = get_all_students()
    for student in students:
        if student['id'] == student_id:
            return student
    return None

def student_exists(student_id):
    """Check if student ID exists"""
    return get_student_by_id(student_id) is not None

def save_all_students(students):
    """Save all students back to file"""
    with open("data/students.txt", "w") as f:
        for student in students:
            line = f"{student['id']}|{student['name']}|{student['coins']}|{student['level']}|{student['title']}|{student['reputation']}|{student['nft_collection']}|{student['achievements']}\n"
            f.write(line)

def update_student_coins(student_id, amount):
    """Add or remove coins from student"""
    students = get_all_students()
    for student in students:
        if student['id'] == student_id:
            student['coins'] += amount
            
            # Check for level up
            new_level = student['coins'] // 100  # Level up every 100 coins
            if new_level > student['level']:
                student['level'] = new_level
                
                # Update title
                if new_level >= 10:
                    student['title'] = "Legend"
                elif new_level >= 7:
                    student['title'] = "Meme Lord"
                elif new_level >= 4:
                    student['title'] = "Regular"
                else:
                    student['title'] = "Noob"
                
                print(f"🎉 LEVEL UP! You're now Level {new_level} - {student['title']}")
            
            save_all_students(students)
            return True
    return False
```

### Your Menu Function
```python
def profile_menu(student_id):
    """Profile management menu"""
    while True:
        print("\n=== 👤 PROFILE MENU ===")
        print("1. View My Profile")
        print("2. Edit Name")
        print("3. View Achievements")
        print("0. Back to Main Menu")
        
        choice = input("Choose: ")
        
        if choice == "1":
            display_profile(student_id)
        elif choice == "2":
            new_name = input("Enter new name: ")
            students = get_all_students()
            for student in students:
                if student['id'] == student_id:
                    student['name'] = new_name
                    save_all_students(students)
                    print("✅ Name updated!")
                    break
        elif choice == "3":
            student = get_student_by_id(student_id)
            if student['achievements']:
                print("\n🏅 YOUR ACHIEVEMENTS:")
                for achievement in student['achievements'].split(","):
                    print(f"  ✓ {achievement}")
            else:
                print("No achievements yet!")
        elif choice == "0":
            break
        else:
            print("❌ Invalid choice!")
```

### What to Present (2 minutes)
1. **Explain** (30 seconds):
   - "I built the student profile system"
   - "It handles registration, login, and profile management"
   - "Students have levels, titles, and achievements"

2. **Show Data Structure** (30 seconds):
   - Show the students.txt file format
   - Explain each field

3. **Demo** (1 minute):
   - Register a new student
   - Login
   - Show profile
   - Unlock an achievement (simulate level up)

---

## 🎯 MEMBER 2: QUEST/CHALLENGE MANAGER

### What You're Responsible For
You handle all quests - creating them, accepting them, completing them, and distributing rewards.

### Your Data File: `quests.txt`
**Format:**
```
quest_id|title|description|reward|type|difficulty|creator_id|status|participants
Q001|Help 5 Juniors|Tutor 5 junior students|50|Academic|Medium|NSU210101|Active|NSU210202,NSU210303
Q002|Organize Event|Setup study group|30|Social|Easy|NSU210505|Completed|NSU210101
```

### Quest Types
- **Academic**: Tutoring, study groups, sharing notes
- **Social**: Organizing events, helping new students
- **Creative**: Making memes, creating content
- **Campus**: Attending seminars, competitions

### Functions You Need to Build

#### 1. `view_quests()` - Display all available quests
```python
def view_quests():
    """Show all active quests"""
    quests = get_all_quests()
    active_quests = [q for q in quests if q['status'] == 'Active']
    
    if not active_quests:
        print("\n❌ No active quests available!")
        return
    
    print("\n" + "="*60)
    print("🎯 AVAILABLE QUESTS".center(60))
    print("="*60)
    
    for i, quest in enumerate(active_quests, 1):
        print(f"\n{i}. {quest['title']} [{quest['difficulty']}]")
        print(f"   Type: {quest['type']}")
        print(f"   Description: {quest['description']}")
        print(f"   Reward: {quest['reward']} MemeCoins 🪙")
        print(f"   Quest ID: {quest['id']}")
        print(f"   Created by: {quest['creator_id']}")
        
        if quest['participants']:
            print(f"   Participants: {len(quest['participants'].split(','))}")
    
    print("="*60)
```

#### 2. `create_quest(creator_id)` - Create new quest
```python
def create_quest(creator_id):
    """Create a new quest"""
    print("\n=== ➕ CREATE NEW QUEST ===")
    
    # Get quest details
    title = input("Quest Title: ")
    description = input("Description: ")
    reward = int(input("Reward (MemeCoins): "))
    
    print("\nQuest Types:")
    print("1. Academic")
    print("2. Social")
    print("3. Creative")
    print("4. Campus")
    type_choice = input("Choose type (1-4): ")
    
    types = {"1": "Academic", "2": "Social", "3": "Creative", "4": "Campus"}
    quest_type = types.get(type_choice, "Academic")
    
    print("\nDifficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    diff_choice = input("Choose difficulty (1-3): ")
    
    difficulties = {"1": "Easy", "2": "Medium", "3": "Hard"}
    difficulty = difficulties.get(diff_choice, "Medium")
    
    # Generate quest ID
    quests = get_all_quests()
    quest_id = f"Q{len(quests) + 1:03d}"
    
    # Save quest
    with open("data/quests.txt", "a") as f:
        line = f"{quest_id}|{title}|{description}|{reward}|{quest_type}|{difficulty}|{creator_id}|Active|\n"
        f.write(line)
    
    print(f"\n✅ Quest created! ID: {quest_id}")
    print(f"🪙 Reward: {reward} MemeCoins")
    return quest_id
```

#### 3. `accept_quest(student_id, quest_id)` - Accept a quest
```python
def accept_quest(student_id, quest_id):
    """Student accepts a quest"""
    quests = get_all_quests()
    
    for quest in quests:
        if quest['id'] == quest_id:
            if quest['status'] != 'Active':
                print("❌ This quest is not active!")
                return False
            
            # Add student to participants
            if quest['participants']:
                participants = quest['participants'].split(",")
                if student_id in participants:
                    print("❌ You already accepted this quest!")
                    return False
                participants.append(student_id)
                quest['participants'] = ",".join(participants)
            else:
                quest['participants'] = student_id
            
            # Save back
            save_all_quests(quests)
            print(f"✅ Quest accepted: {quest['title']}")
            print(f"🎯 Complete it to earn {quest['reward']} coins!")
            return True
    
    print("❌ Quest not found!")
    return False
```

#### 4. `complete_quest(student_id, quest_id)` - Complete quest & get reward
```python
def complete_quest(student_id, quest_id):
    """Mark quest as completed and give reward"""
    quests = get_all_quests()
    
    for quest in quests:
        if quest['id'] == quest_id:
            # Check if student accepted this quest
            if not quest['participants'] or student_id not in quest['participants']:
                print("❌ You haven't accepted this quest!")
                return False
            
            # Check if already completed
            if quest['status'] == 'Completed':
                print("❌ Quest already completed!")
                return False
            
            # Mark as completed
            quest['status'] = 'Completed'
            save_all_quests(quests)
            
            # Give reward (call Member 1's function)
            import member1_profiles as profiles
            profiles.update_student_coins(student_id, quest['reward'])
            
            print(f"\n🎉 QUEST COMPLETED!")
            print(f"📜 {quest['title']}")
            print(f"🪙 Earned {quest['reward']} MemeCoins!")
            
            # Check for achievement
            completed_count = count_completed_quests(student_id)
            if completed_count == 1:
                profiles.unlock_achievement(student_id, "First Quest")
            elif completed_count == 10:
                profiles.unlock_achievement(student_id, "Quest Master")
            
            return True
    
    print("❌ Quest not found!")
    return False
```

#### 5. Helper Functions
```python
def get_all_quests():
    """Read all quests from file"""
    quests = []
    try:
        with open("data/quests.txt", "r") as f:
            for line in f:
                data = line.strip().split("|")
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
    except FileNotFoundError:
        pass
    return quests

def save_all_quests(quests):
    """Save all quests back to file"""
    with open("data/quests.txt", "w") as f:
        for quest in quests:
            line = f"{quest['id']}|{quest['title']}|{quest['description']}|{quest['reward']}|{quest['type']}|{quest['difficulty']}|{quest['creator_id']}|{quest['status']}|{quest['participants']}\n"
            f.write(line)

def count_completed_quests(student_id):
    """Count how many quests a student completed"""
    quests = get_all_quests()
    count = 0
    for quest in quests:
        if quest['status'] == 'Completed' and quest['participants'] and student_id in quest['participants']:
            count += 1
    return count
```

### Your Menu Function
```python
def quest_menu(student_id):
    """Quest management menu"""
    while True:
        print("\n=== 🎯 QUEST BOARD ===")
        print("1. View All Quests")
        print("2. Create Quest")
        print("3. Accept Quest")
        print("4. Complete Quest")
        print("5. My Quests")
        print("0. Back to Main Menu")
        
        choice = input("Choose: ")
        
        if choice == "1":
            view_quests()
        
        elif choice == "2":
            create_quest(student_id)
        
        elif choice == "3":
            view_quests()
            quest_id = input("\nEnter Quest ID to accept: ")
            accept_quest(student_id, quest_id)
        
        elif choice == "4":
            # Show student's accepted quests
            quests = get_all_quests()
            my_quests = [q for q in quests if q['participants'] and student_id in q['participants'] and q['status'] == 'Active']
            
            if not my_quests:
                print("❌ No active quests!")
                continue
            
            print("\nYour Active Quests:")
            for i, quest in enumerate(my_quests, 1):
                print(f"{i}. {quest['title']} - {quest['reward']} coins")
            
            quest_id = input("\nEnter Quest ID to complete: ")
            complete_quest(student_id, quest_id)
        
        elif choice == "5":
            quests = get_all_quests()
            my_quests = [q for q in quests if q['participants'] and student_id in q['participants']]
            
            if not my_quests:
                print("❌ You haven't joined any quests yet!")
            else:
                print("\n📋 YOUR QUESTS:")
                for quest in my_quests:
                    status_emoji = "✅" if quest['status'] == 'Completed' else "🔄"
                    print(f"{status_emoji} {quest['title']} - {quest['reward']} coins")
        
        elif choice == "0":
            break
        else:
            print("❌ Invalid choice!")
```

### What to Present (2 minutes)
1. **Explain**: Quest system, types of quests, rewards
2. **Show Data**: quests.txt file format
3. **Demo**: Create quest → Accept → Complete → Earn coins

---

## 🎨 MEMBER 3: MEME NFT MARKETPLACE

### Your Data File: `memes.txt`
```
nft_id|name|description|creator_id|rarity|price|owner_id|likes
NFT001|CSE Power Cut|That blackout moment|NSU210101|Legendary|100|NSU210505|89
NFT002|Drake Hotline|Classic meme|NSU210202|Rare|50|NSU210101|45
```

### Rarity Levels
- **Common**: Worth 10-20 coins
- **Rare**: Worth 30-50 coins
- **Epic**: Worth 60-80 coins
- **Legendary**: Worth 100+ coins

### Functions You Need (Similar structure as above)
1. `create_meme(creator_id)` - Create new meme NFT
2. `browse_marketplace()` - Show all memes for sale
3. `buy_meme(buyer_id, nft_id)` - Purchase a meme
4. `view_collection(student_id)` - Show owned memes
5. `like_meme(student_id, nft_id)` - Like a meme

---

## 🛒 MEMBER 4: PERK SHOP

### Your Data Files
**perks.txt:**
```
perk_id|name|cost|quantity|type|seller_id|validity
PERK01|Queue Skip Pass|30|10|Instant|ADMIN|1 day
PERK02|Premium Notes|50|5|Item|NSU210101|1 week
```

**inventory.txt:**
```
student_id|perk_id|purchase_date|status
NSU210101|PERK01|2025-01-31|Active
NSU210505|PERK02|2025-01-30|Used
```

### Functions You Need
1. `view_perks()` - Show available perks
2. `purchase_perk(student_id, perk_id)` - Buy a perk
3. `view_inventory(student_id)` - Show owned perks
4. `redeem_perk(student_id, perk_id)` - Use a perk

---

## 💸 MEMBER 5: SOCIAL CREDIT ENGINE

### Your Data File: `transactions.txt`
```
txn_id|from_id|to_id|amount|reason|verified|timestamp
T001|NSU210101|NSU210505|10|Helped with code|True|2025-01-31 14:30
T002|NSU210202|NSU210101|15|Quest reward|True|2025-01-31 15:00
```

### Functions You Need
1. `send_coins(from_id, to_id, amount, reason)` - Transfer coins
2. `view_transactions(student_id)` - Transaction history
3. `verify_transaction(txn_id)` - Mark transaction as verified
4. `calculate_reputation(student_id)` - Calculate rep score

---

## 🏆 MEMBER 6: LEADERBOARDS & ANALYTICS

### What You Do
You READ from ALL files and calculate rankings.

### Functions You Need
1. `show_richest()` - Top students by coins
2. `show_quest_leaders()` - Most quests completed
3. `show_most_helpful()` - Most transactions sent
4. `show_meme_kings()` - Most memes created
5. `show_analytics(student_id)` - Individual student stats

---

## 📦 COMPLETE CODE TEMPLATE

Each member gets a file that looks like this:

```python
# memberX_module.py
"""
Module: [Your Module Name]
Member: [Your Name]
Description: [What this module does]
"""

# ============= HELPER FUNCTIONS (INTERNAL USE) =============

def _read_data_file():
    """Read from your data file"""
    pass

def _save_data_file(data):
    """Save to your data file"""
    pass

# ============= MAIN FUNCTIONS (PUBLIC) =============

def function1():
    """Description"""
    pass

def function2():
    """Description"""
    pass

# ============= MENU FUNCTION =============

def module_menu(student_id):
    """Your module's menu"""
    while True:
        print("\n=== YOUR MODULE MENU ===")
        print("1. Option 1")
        print("2. Option 2")
        print("0. Back")
        
        choice = input("Choose: ")
        
        if choice == "1":
            function1()
        elif choice == "2":
            function2()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")
```

---

## 🎯 SUCCESS CHECKLIST

Each member should have:
- [ ] 5-8 functions working
- [ ] Data file reading/writing correctly
- [ ] Menu system functional
- [ ] Integration with other modules tested
- [ ] Presentation prepared (2 min)
- [ ] Demo ready to show

**You got this! 🚀**
