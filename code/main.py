"""
MAIN MENU - CAMPUS MEME ECONOMY
Coordinator: [Your Name Here]
Description: Main entry point that integrates all 6 modules
"""

import os
import sys

# Add modules directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'modules'))

# Import all member modules
import member1_profiles as profiles
import member2_quests as quests
import member3_memes as memes
import member4_perks as perks
import member5_social as social
import member6_leaderboards as leaderboards

# ============= UTILITY FUNCTIONS =============

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def show_banner():
    """Display welcome banner"""
    print("\n" + "="*60)
    print("🎮 CAMPUS MEME ECONOMY 🎮".center(60))
    print("Level Up Your Campus Life".center(60))
    print("="*60)


# ============= MAIN PROGRAM =============

def main():
    """Main program entry point"""
    
    # Welcome screen
    clear_screen()
    show_banner()
    
    print("\nWelcome to Campus Meme Economy!")
    print("A gamified social credit system for universities.\n")
    
    print("1. 🔑 Login")
    print("2. 📝 Register New Student")
    print("0. ❌ Exit")
    
    choice = input("\nChoose an option: ").strip()
    
    student_id = None
    
    if choice == "1":
        # Login
        student_id = profiles.login_student()
        if not student_id:
            print("\n❌ Login failed!")
            input("Press Enter to exit...")
            return
    
    elif choice == "2":
        # Register
        if profiles.register_student():
            print("\n✅ Registration successful! Now please login.")
            input("Press Enter to continue...")
            student_id = profiles.login_student()
            if not student_id:
                print("\n❌ Login failed!")
                input("Press Enter to exit...")
                return
        else:
            print("\n❌ Registration failed!")
            input("Press Enter to exit...")
            return
    
    elif choice == "0":
        print("\n👋 Thanks for visiting! Goodbye!")
        return
    
    else:
        print("❌ Invalid choice!")
        input("Press Enter to exit...")
        return
    
    # Main menu loop
    while True:
        clear_screen()
        show_banner()
        
        # Show current student info
        student = profiles.get_student_by_id(student_id)
        if student:
            print(f"\n👤 {student['name']}")
            print(f"🪙 {student['coins']} MemeCoins | ⭐ Level {student['level']} ({student['title']}) | 💯 Rep: {student['reputation']}")
        
        print("\n" + "="*60)
        print("MAIN MENU".center(60))
        print("="*60)
        print("1. 👤 My Profile & Achievements")
        print("2. 🎯 Quest Board")
        print("3. 🎨 Meme NFT Marketplace")
        print("4. 🛒 Perk Shop")
        print("5. 💸 Social Credit Engine")
        print("6. 🏆 Leaderboards & Analytics")
        print("0. 🚪 Logout")
        print("="*60)
        
        choice = input("\nChoose an option: ").strip()
        
        if choice == "1":
            # Member 1: Student Profiles
            profiles.profile_menu(student_id)
        
        elif choice == "2":
            # Member 2: Quest System
            quests.quest_menu(student_id)
        
        elif choice == "3":
            # Member 3: Meme Marketplace
            memes.meme_menu(student_id)
        
        elif choice == "4":
            # Member 4: Perk Shop
            perks.perk_menu(student_id)
        
        elif choice == "5":
            # Member 5: Social Credit
            social.social_menu(student_id)
        
        elif choice == "6":
            # Member 6: Leaderboards
            leaderboards.leaderboard_menu()
        
        elif choice == "0":
            # Logout
            student = profiles.get_student_by_id(student_id)
            print(f"\n👋 Goodbye, {student['name']}!")
            print("Thanks for playing Campus Meme Economy!")
            input("\nPress Enter to exit...")
            break
        
        else:
            print("❌ Invalid choice! Please try again.")
            input("Press Enter to continue...")


# ============= RUN THE PROGRAM =============

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("\nPlease report this to your team coordinator.")
        input("Press Enter to exit...")
