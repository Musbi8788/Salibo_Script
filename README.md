🕌 Salibo Script
A simple Python program that gives you Salibo (Eid money) based on the length of your name.
User data is stored in a local JSON file, so when you return, the program remembers you!

✨ Features
✅ Calculates Salibo as length of your name × 50 Dalasis
✅ Stores your name in a salibo.json file
✅ Asks for confirmation if you are an existing user
✅ Friendly command-line interface
✅ Simple and fun beginner project

🚀 How to Run
Clone or download this project:

```
git clone https://github.com/your-username/salibo-script.git
cd salibo-script
Run the Python script:
```

```
python salibo.py
```
💻 How It Works
If you run the script for the first time, it asks for your name and stores it.

If you run it again, it asks: Is this your name?
→ If "yes", it calculates your Salibo and displays it.
→ If "no", you can enter a new name.

The Salibo amount is calculated like this:

python
```
salibo_money = len(username) * 50
```
🛠️ Project Structure

```
salibo.py          # Main Python script
salibo.json        # Auto-generated file to store username
README.md          # Project documentation
📚 Requirements
Python 3.x (tested with Python 3.9+)
```

No external libraries required (uses built-in json module)

🎉 Future Improvements
Add multiple users

Add history of Salibo calculations

GUI version (Tkinter or Web App with Flask)

Add unit tests

🙏 Acknowledgements
Built by Musbi Jawo — learning and building fun Python projects!
Inspired by Eid traditions in The Gambia 🇬🇲✨

If you'd like, I can also:
✅ generate the README.md file as actual Markdown so you can copy it
✅ suggest a simple project logo or banner for your GitHub repo

Want me to do that too? 🚀✨
