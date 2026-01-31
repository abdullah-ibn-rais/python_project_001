# 🚀 HOW TO RUN THE CAMPUS MEME ECONOMY

## ✅ GUARANTEED TO WORK - JUST FOLLOW THESE STEPS!

---

## 📂 FILE STRUCTURE (What You Have)

```
campus_meme_economy/
├── code/
│   ├── main.py                          ← COORDINATOR RUNS THIS
│   └── modules/
│       ├── member1_profiles.py          ← Member 1's code
│       ├── member2_quests.py            ← Member 2's code
│       ├── member3_memes.py             ← Member 3's code
│       ├── member4_perks.py             ← Member 4's code
│       ├── member5_social.py            ← Member 5's code
│       └── member6_leaderboards.py      ← Member 6's code
```

When you run the program, a `data/` folder will be created automatically!

---

## 🎯 STEP-BY-STEP INSTRUCTIONS

### STEP 1: Install Python

**If you don't have Python:**
1. Go to https://python.org
2. Download Python 3.10 or higher
3. **IMPORTANT:** Check "Add Python to PATH" during installation
4. Click "Install Now"

**Check if Python is installed:**
```bash
python --version
```
Should show: `Python 3.10.x` or higher

---

### STEP 2: Navigate to the Code Folder

**On Windows:**
1. Open File Explorer
2. Go to the `campus_meme_economy/code` folder
3. Type `cmd` in the address bar
4. Press Enter

**On Mac/Linux:**
1. Open Terminal
2. Type: `cd /path/to/campus_meme_economy/code`
3. Press Enter

---

### STEP 3: Run the Program

Type this command and press Enter:

```bash
python main.py
```

**That's it!** The program will start! 🎉

---

## 🎮 HOW TO USE THE PROGRAM

### First Time Running:

1. **Choose option 2** - Register New Student
2. Enter your Student ID (e.g., `NSU210101`)
3. Enter your name
4. ✅ You're registered!
5. **Login** with the same Student ID
6. Explore all 6 modules!

### Main Menu Options:

```
1. My Profile          → View stats, achievements
2. Quest Board         → Create/accept/complete quests
3. Meme Marketplace    → Create and trade memes
4. Perk Shop           → Buy perks with coins
5. Social Credit       → Send coins, verify transactions
6. Leaderboards        → See rankings and analytics
```

---

## 👥 TESTING INDIVIDUAL MODULES

Each member can test their module independently!

### Member 1 (Profiles):
```bash
cd modules
python member1_profiles.py
```

### Member 2 (Quests):
```bash
cd modules
python member2_quests.py
```

### Member 3 (Memes):
```bash
cd modules
python member3_memes.py
```

### Member 4 (Perks):
```bash
cd modules
python member4_perks.py
```

### Member 5 (Social):
```bash
cd modules
python member5_social.py
```

### Member 6 (Leaderboards):
```bash
cd modules
python member6_leaderboards.py
```

**Each module can run standalone for testing!**

---

## 📁 DATA FILES (Created Automatically)

After you run the program, you'll see a `data/` folder with:

```
data/
├── students.txt           ← Student profiles
├── quests.txt             ← All quests
├── memes.txt              ← Meme NFTs
├── perks.txt              ← Available perks (pre-populated)
├── inventory.txt          ← Student perk inventories
└── transactions.txt       ← All coin transfers
```

**You don't need to create these!** They're made automatically.

---

## 🎯 QUICK START DEMO

Try this to see everything work:

### 1. Register Two Students
```
Run: python main.py
Choose: 2 (Register)
Student 1: NSU210101, "Ahmed"
Student 2: NSU210102, "Rahat"
```

### 2. Login as Ahmed (NSU210101)
```
Choose: 1 (Login)
Enter: NSU210101
```

### 3. Create a Quest
```
Main Menu → 2 (Quest Board)
Choose: 2 (Create Quest)
Title: "Help with Python"
Description: "Debug my code"
Reward: 20
Type: 1 (Academic)
Difficulty: 2 (Medium)
```

### 4. Logout and Login as Rahat
```
Main Menu → 0 (Logout)
Login as NSU210102
```

### 5. Accept and Complete Quest
```
Main Menu → 2 (Quest Board)
Choose: 3 (Accept Quest)
Enter Quest ID: Q001
Choose: 4 (Complete Quest)
Enter Quest ID: Q001
```

**🎉 Rahat just earned 20 coins!**

### 6. Check Leaderboards
```
Main Menu → 6 (Leaderboards)
Choose: 1 (Richest Students)
```

You'll see both students ranked by coins!

---

## 🐛 TROUBLESHOOTING

### Error: "python: command not found"
**Solution:** Try `python3 main.py` instead

### Error: "No module named 'member1_profiles'"
**Solution:** Make sure you're in the `code/` folder, not `modules/`

### Error: "Permission denied"
**Solution:** On Mac/Linux, try `chmod +x main.py` first

### Program looks weird / no colors
**Solution:** That's okay! It works fine in plain text too

### Want to start fresh?
**Solution:** Delete the `data/` folder and run again

---

## 💡 PRO TIPS

### Running in VS Code:
1. Open the `code` folder in VS Code
2. Right-click `main.py`
3. Choose "Run Python File in Terminal"

### Running in PyCharm:
1. Open the `code` folder as a project
2. Right-click `main.py`
3. Choose "Run 'main'"

### Running in IDLE:
1. Open `main.py` in IDLE
2. Press F5 or choose Run → Run Module

---

## 🎨 WHAT EACH MEMBER CAN DEMO

### Coordinator (YOU):
- Show main menu
- Navigate between modules
- Full system demo

### Member 1:
- Register a student
- Login
- View profile
- Show achievements

### Member 2:
- Create a quest
- Accept quest
- Complete quest
- Show rewards

### Member 3:
- Create a meme NFT
- Browse marketplace
- Buy a meme
- Show collection

### Member 4:
- Browse perks
- Purchase a perk
- View inventory
- Redeem perk

### Member 5:
- Send coins to someone
- View transactions
- Verify a transaction
- Show reputation

### Member 6:
- Show richest students
- Show quest leaders
- Show personal analytics
- Explain ranking algorithms

---

## ✅ VERIFICATION CHECKLIST

Before presentation, verify:

- [ ] Python is installed
- [ ] All 7 files are in the correct folders
- [ ] `python main.py` runs without errors
- [ ] You can register a student
- [ ] You can login
- [ ] All 6 modules are accessible
- [ ] Data persists (close and reopen program)
- [ ] Each team member can demo their module

---

## 🎉 YOU'RE READY!

This code is **COMPLETE** and **WORKING**. 

Just run `python main.py` and everything works!

No setup needed. No libraries to install. No configuration files.

**MAGIC!** ✨

---

## 📞 NEED HELP?

If something doesn't work:

1. **Check you're in the right folder** (`code/`, not `modules/`)
2. **Try `python3` instead of `python`**
3. **Make sure all 7 files exist**
4. **Delete `data/` folder and try again**

Still stuck? Show the error message to your coordinator!

---

**Happy Gaming! 🎮💰🏆**
