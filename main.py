"""
MAIN MENU - CAMPUS MEME ECONOMY
Coordinator: Integrates all 6 modules
"""

import os
import sys

# Import all member modules
sys.path.append('modules')
import member1_profiles as profiles
import member2_quests as quests
# import member3_memes as memes
# import member4_perks as perks
# import member5_social as social
# import member6_leaderboards as leaderboards

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def show_banner():
    """Display welcome banner"""
    print("\n" + "="*60)
    print("🎮 CAMPUS MEME ECONOMY 🎮".center(60))
    print("Level Up Your Campus Life".center(60))
    print("="*60)


def main():
    """Main program entry point"""
    # Create data directory if it doesn't exist
    if not os.path.exists("data"):
        os.makedirs("data")
    
    # Welcome screen
    clear_screen()
    show_banner()
    
    print("\n1. 🔑 Login")
    print("2. 📝 Register")
    print("0. ❌ Exit")
    
    choice = input("\nChoose an option: ").strip()
    
    student_id = None
    
    if choice == "1":
        student_id = profiles.login_student()
        if not student_id:
            return
    
    elif choice == "2":
        if profiles.register_student():
            student_id = profiles.login_student()
            if not student_id:
                return
        else:
            return
    
    elif choice == "0":
        print("\n👋 Thanks for visiting! See you next time!")
        return
    
    else:
        print("❌ Invalid choice!")
        return
    
    # Main menu loop
    while True:
        clear_screen()
        show_banner()
        
        # Show student info
        student = profiles.get_student_by_id(student_id)
        if student:
            print(f"\n👤 {student['name']} | 🪙 {student['coins']} coins | ⭐ Lvl {student['level']} {student['title']}")
        
        print("\n" + "="*60)
        print("MAIN MENU".center(60))
        print("="*60)
        print("1. 👤 My Profile")
        print("2. 🎯 Quest Board")
        print("3. 🎨 Meme NFT Marketplace [Coming Soon]")
        print("4. 🛒 Perk Shop [Coming Soon]")
        print("5. 💸 Social Credit [Coming Soon]")
        print("6. 🏆 Leaderboards [Coming Soon]")
        print("0. 🚪 Logout")
        print("="*60)
        
        choice = input("\nChoose an option: ").strip()
        
        if choice == "1":
            profiles.profile_menu(student_id)
        
        elif choice == "2":
            quests.quest_menu(student_id)
        
        elif choice == "3":
            # memes.meme_menu(student_id)
            print("\n🚧 Meme NFT Marketplace - Coming Soon!")
            input("Press Enter to continue...")
        
        elif choice == "4":
            # perks.perk_menu(student_id)
            print("\n🚧 Perk Shop - Coming Soon!")
            input("Press Enter to continue...")
        
        elif choice == "5":
            # social.social_menu(student_id)
            print("\n🚧 Social Credit - Coming Soon!")
            input("Press Enter to continue...")
        
        elif choice == "6":
            # leaderboards.leaderboard_menu()
            print("\n🚧 Leaderboards - Coming Soon!")
            input("Press Enter to continue...")
        
        elif choice == "0":
            print(f"\n👋 Goodbye, {student['name']}! See you next time!")
            input("Press Enter to exit...")
            break
        
        else:
            print("❌ Invalid choice! Please try again.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Thanks for playing! Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please report this to your team coordinator.")
