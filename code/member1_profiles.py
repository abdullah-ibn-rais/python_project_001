"""
MEMBER 1: STUDENT PROFILE SYSTEM
Author: [Your Name Here]
Description: Handles registration, login, profiles, coins, achievements
"""

import os

# ============= DATA FILE PATHS =============

DATA_DIR = "data"
STUDENTS_FILE = os.path.join(DATA_DIR, "students.txt")

# Ensure data directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# ============= HELPER FUNCTIONS =============

def get_all_students():
    """Read all students from file and return as list of dictionaries"""
    students = []
    if os.path.exists(STUDENTS_FILE):
        with open(STUDENTS_FILE, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) >= 8:
                    student = {
                        "id": parts[0],
                        "name": parts[1],
                        "coins": int(parts[2]),
                        "level": int(parts[3]),
                        "title": parts[4],
                        "reputation": int(parts[5]),
                        "nft_collection": parts[6],
                        "achievements": parts[7]
                    }
                    students.append(student)
    return students


def save_all_students(students):
    """Save all students back to file"""
    with open(STUDENTS_FILE, "w") as f:
        for student in students:
            line = f"{student['id']}|{student['name']}|{student['coins']}|{student['level']}|{student['title']}|{student['reputation']}|{student['nft_collection']}|{student['achievements']}\n"
            f.write(line)


def get_student_by_id(student_id):
    """Find and return a specific student by ID"""
    students = get_all_students()
    for student in students:
        if student['id'] == student_id:
            return student
    return None


def student_exists(student_id):
    """Check if a student ID already exists"""
    return get_student_by_id(student_id) is not None


# ============= MAIN FUNCTIONS (CALLED BY OTHER MODULES) =============

def register_student():
    """Register a new student - INTERACTIVE"""
    print("\n" + "="*50)
    print("📝 STUDENT REGISTRATION".center(50))
    print("="*50)
    
    student_id = input("Enter Student ID (e.g., NSU210101): ").strip()
    
    if student_exists(student_id):
        print("❌ This Student ID is already registered!")
        input("\nPress Enter to continue...")
        return False
    
    name = input("Enter Full Name: ").strip()
    
    # Create new student with default values
    with open(STUDENTS_FILE, "a") as f:
        # Format: id|name|coins|level|title|reputation|nft_collection|achievements
        line = f"{student_id}|{name}|100|1|Noob|0||\n"
        f.write(line)
    
    print(f"\n✅ Welcome, {name}!")
    print(f"🪙 Starting balance: 100 MemeCoins")
    print(f"⭐ Starting level: 1 (Noob)")
    input("\nPress Enter to continue...")
    return True


def login_student():
    """Login existing student - INTERACTIVE - Returns student_id or None"""
    print("\n" + "="*50)
    print("🔑 STUDENT LOGIN".center(50))
    print("="*50)
    
    student_id = input("Enter Student ID: ").strip()
    
    student = get_student_by_id(student_id)
    if student:
        print(f"\n✅ Welcome back, {student['name']}!")
        print(f"🪙 Balance: {student['coins']} MemeCoins")
        print(f"⭐ Level: {student['level']} ({student['title']})")
        input("\nPress Enter to continue...")
        return student_id
    else:
        print("\n❌ Student ID not found!")
        input("Press Enter to continue...")
        return None


def display_profile(student_id):
    """Display complete student profile"""
    student = get_student_by_id(student_id)
    
    if not student:
        print("❌ Student not found!")
        input("Press Enter to continue...")
        return
    
    print("\n" + "="*60)
    print("👤 STUDENT PROFILE".center(60))
    print("="*60)
    print(f"🆔 ID:          {student['id']}")
    print(f"👨 Name:        {student['name']}")
    print(f"🪙 MemeCoins:   {student['coins']}")
    print(f"⭐ Level:       {student['level']}")
    print(f"🏆 Title:       {student['title']}")
    print(f"💯 Reputation:  {student['reputation']}")
    
    # Display NFT collection
    if student['nft_collection']:
        nfts = student['nft_collection'].split(",")
        print(f"\n🎨 NFT Collection ({len(nfts)} owned):")
        for nft in nfts:
            print(f"   • {nft}")
    else:
        print(f"\n🎨 NFT Collection: None yet")
    
    # Display achievements
    if student['achievements']:
        achievements = student['achievements'].split(",")
        print(f"\n🏅 Achievements ({len(achievements)} unlocked):")
        for achievement in achievements:
            print(f"   ✓ {achievement}")
    else:
        print(f"\n🏅 Achievements: None yet")
    
    print("="*60)
    input("\nPress Enter to continue...")


def update_student_coins(student_id, amount):
    """
    Add or remove coins from a student
    Called by other modules (Quests, Perks, Social, Memes)
    Returns True if successful, False otherwise
    """
    students = get_all_students()
    
    for student in students:
        if student['id'] == student_id:
            old_coins = student['coins']
            old_level = student['level']
            
            student['coins'] += amount
            
            # Prevent negative coins
            if student['coins'] < 0:
                student['coins'] = 0
            
            # Calculate level (every 100 coins = 1 level, starting from level 1)
            new_level = (student['coins'] // 100) + 1
            if new_level > 10:
                new_level = 10  # Cap at level 10
            
            # Check for level up
            if new_level != old_level:
                student['level'] = new_level
                
                # Update title based on level
                if new_level >= 10:
                    student['title'] = "Legend"
                elif new_level >= 7:
                    student['title'] = "Meme Lord"
                elif new_level >= 4:
                    student['title'] = "Regular"
                else:
                    student['title'] = "Noob"
                
                print(f"\n🎉 LEVEL UP! You're now Level {new_level} - {student['title']}!")
                
                # Unlock level achievements
                if new_level == 5:
                    unlock_achievement(student_id, "Halfway There")
                elif new_level == 10:
                    unlock_achievement(student_id, "Campus Legend")
            
            # Save changes
            save_all_students(students)
            return True
    
    return False


def unlock_achievement(student_id, achievement_name):
    """
    Unlock an achievement for a student
    Called by other modules when conditions are met
    Returns True if newly unlocked, False if already had it
    """
    students = get_all_students()
    
    for student in students:
        if student['id'] == student_id:
            # Check if already has this achievement
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
            print(f"\n🎉 ACHIEVEMENT UNLOCKED: {achievement_name}!")
            return True
    
    return False


def add_nft_to_collection(student_id, nft_name):
    """
    Add an NFT to student's collection
    Called by Member 3 (Memes) when NFT is created or purchased
    """
    students = get_all_students()
    
    for student in students:
        if student['id'] == student_id:
            if student['nft_collection']:
                current = student['nft_collection'].split(",")
                current.append(nft_name)
                student['nft_collection'] = ",".join(current)
            else:
                student['nft_collection'] = nft_name
            
            save_all_students(students)
            return True
    
    return False


def remove_nft_from_collection(student_id, nft_name):
    """
    Remove an NFT from student's collection
    Called by Member 3 (Memes) when NFT is sold
    """
    students = get_all_students()
    
    for student in students:
        if student['id'] == student_id:
            if student['nft_collection']:
                current = student['nft_collection'].split(",")
                if nft_name in current:
                    current.remove(nft_name)
                    student['nft_collection'] = ",".join(current) if current else ""
                    save_all_students(students)
                    return True
    
    return False


def update_reputation(student_id, points):
    """
    Add reputation points to a student
    Called by Member 5 (Social Credit) when transactions are verified
    """
    students = get_all_students()
    
    for student in students:
        if student['id'] == student_id:
            student['reputation'] += points
            save_all_students(students)
            return True
    
    return False


# ============= MENU FUNCTIONS =============

def edit_profile(student_id):
    """Edit student name"""
    print("\n" + "="*50)
    print("✏️  EDIT PROFILE".center(50))
    print("="*50)
    
    student = get_student_by_id(student_id)
    if not student:
        print("❌ Student not found!")
        input("Press Enter to continue...")
        return
    
    print(f"Current name: {student['name']}")
    new_name = input("Enter new name (or press Enter to cancel): ").strip()
    
    if new_name:
        students = get_all_students()
        for s in students:
            if s['id'] == student_id:
                s['name'] = new_name
                save_all_students(students)
                print("✅ Name updated successfully!")
                break
    
    input("\nPress Enter to continue...")


def view_achievements_list():
    """Display all possible achievements"""
    achievements = {
        "First Blood": "Complete your first quest",
        "Quest Master": "Complete 10 quests",
        "Helper": "Help 5 other students",
        "Social Butterfly": "Send coins to 10 different students",
        "Meme Dealer": "Create your first meme",
        "Meme Master": "Create 5 memes",
        "Collector": "Own 10 NFTs",
        "Rich": "Accumulate 500 coins",
        "Halfway There": "Reach Level 5",
        "Campus Legend": "Reach Level 10",
        "Night Owl": "Complete a quest after midnight",
        "Early Bird": "Complete a quest before 8 AM",
    }
    
    print("\n" + "="*60)
    print("🏅 ALL POSSIBLE ACHIEVEMENTS".center(60))
    print("="*60)
    for name, description in achievements.items():
        print(f"✓ {name}")
        print(f"  └─ {description}\n")
    print("="*60)
    input("\nPress Enter to continue...")


def profile_menu(student_id):
    """Main profile menu - INTERACTIVE"""
    while True:
        print("\n" + "="*50)
        print("👤 PROFILE MENU".center(50))
        print("="*50)
        print("1. View My Profile")
        print("2. Edit Name")
        print("3. My Achievements")
        print("4. All Achievements List")
        print("0. Back to Main Menu")
        print("="*50)
        
        choice = input("\nChoose an option: ").strip()
        
        if choice == "1":
            display_profile(student_id)
        
        elif choice == "2":
            edit_profile(student_id)
        
        elif choice == "3":
            student = get_student_by_id(student_id)
            if student and student['achievements']:
                print("\n" + "="*50)
                print("🏅 YOUR ACHIEVEMENTS".center(50))
                print("="*50)
                for achievement in student['achievements'].split(","):
                    print(f"✓ {achievement}")
                print("="*50)
            else:
                print("\n❌ No achievements unlocked yet!")
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            view_achievements_list()
        
        elif choice == "0":
            break
        
        else:
            print("❌ Invalid choice! Please try again.")
            input("Press Enter to continue...")


# ============= TESTING (Only runs when this file is run directly) =============

if __name__ == "__main__":
    print("="*60)
    print("TESTING MEMBER 1: STUDENT PROFILE SYSTEM".center(60))
    print("="*60)
    
    print("\n1. Register a new student")
    print("2. Login with existing student")
    choice = input("Choose: ").strip()
    
    if choice == "1":
        if register_student():
            print("\nNow logging in...")
            student_id = login_student()
            if student_id:
                profile_menu(student_id)
    elif choice == "2":
        student_id = login_student()
        if student_id:
            profile_menu(student_id)
