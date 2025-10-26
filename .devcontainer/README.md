# GitHub Codespaces Setup

This repository is configured to work seamlessly with **GitHub Codespaces** - a cloud-based development environment that runs in your browser.

## 🚀 Quick Start (No Installation Required!)

### Option 1: Open in Codespaces (Recommended for Students)

1. **Fork the repository** to your GitHub account (if you haven't already)
   - Click the **"Fork"** button at the top-right of the repository page
   - This creates your own copy of the course

2. **Go to your forked repository** on GitHub

3. **Click the green "<> Code" button** on your repository page

4. **Select the "Codespaces" tab**

5. **Click "Create codespace on main"**

6. Wait 30-60 seconds for the environment to load

7. Start coding immediately in your browser!

### Option 2: Local Development

If you prefer working on your own computer:

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/pythonpro26.git
cd pythonpro26

# Ensure Python 3.11+ is installed
python --version

# Start working on tasks
cd part1/part1Exercises/tasks
python 1_emoticon.py
```

## 📦 What's Pre-Installed in Codespaces

Your Codespace comes with everything you need:

- ✅ **Python 3.11** - Latest stable Python version
- ✅ **VS Code** - Full-featured browser-based editor
- ✅ **Python Extensions** - Syntax highlighting, IntelliSense, debugging
- ✅ **Git** - Version control for commits and pushes
- ✅ **Terminal** - Built-in bash terminal for running commands

### Pre-configured Extensions

- **Python** - Full language support
- **Pylance** - Fast IntelliSense and type checking
- **Python Debugger** - Step through code with breakpoints
- **autoDocstring** - Generate docstrings automatically
- **Python Indent** - Smart indentation
- **GitHub Copilot** - AI pair programmer (if you have access)

## 🎯 Workflow in Codespaces

### 1. Navigate to a Task
```bash
cd part1/part1Exercises/tasks
```

### 2. Open and Edit a Task File
- Click on any `.py` file in the Explorer (left sidebar)
- Read the docstring instructions
- Write your solution below the `# TODO` line

### 3. Run Your Task
```bash
# In the integrated terminal (Terminal → New Terminal)
python 1_emoticon.py
```

### 4. Test Your Solutions
```bash
# Grade all Part 1 tasks
python grade_part1.py

# Check your progress
cat ../../../.progress/marksheet.md
```

### 5. Save Your Work to GitHub
```bash
# Stage changes
git add .

# Commit with a message
git commit -m "Complete Part 1: tasks 1-5"

# Push to GitHub
git push
```

## ⚙️ Codespace Settings

### Auto-Save
Files automatically save after 1 second of inactivity. No need to press Ctrl+S constantly!

### Theme
Default dark theme for comfortable coding. Change via:
- Command Palette (Ctrl+Shift+P)
- Type "Preferences: Color Theme"

### Terminal
Integrated bash terminal at the bottom. Open multiple terminals:
- Terminal → New Terminal (or Ctrl+Shift+`)

## 🔄 Managing Your Codespace

### Pausing Work
- Codespaces automatically pause after 30 minutes of inactivity
- All your files and progress are saved
- Resume anytime by clicking "Open in Codespaces" again

### Stopping Your Codespace
- Click your profile icon (bottom left)
- Select "Stop Current Codespace"
- Or let it auto-stop after inactivity

### Deleting a Codespace
- Go to github.com/codespaces
- Find your codespace
- Click "..." → "Delete"

### Free Usage Limits
GitHub provides free Codespaces hours:
- **60 hours/month** for free accounts (2-core machine)
- **90 hours/month** for Pro accounts

**Tip:** Stop your Codespace when not actively using it to conserve hours!

## 🐛 Troubleshooting

### Codespace Won't Start
- Wait a few minutes and try again
- Check GitHub Status: https://www.githubstatus.com/
- Try deleting and recreating the Codespace

### Python Not Found
```bash
# Verify Python is installed
which python
python --version

# Should show: Python 3.11.x
```

### Can't Run Grader
```bash
# Make sure you're in the correct directory
cd part1/part1Exercises/tasks
pwd  # Should end with /part1/part1Exercises/tasks

# Run with full Python path
python grade_part1.py
```

### Changes Not Saving to GitHub
```bash
# Check git status
git status

# If changes aren't staged:
git add .
git commit -m "Your message"
git push

# If push fails, pull first:
git pull
git push
```

### Extensions Not Loading
- Reload window: Ctrl+Shift+P → "Developer: Reload Window"
- Or restart Codespace

## 📱 Mobile/Tablet Support

Codespaces works on mobile devices via:
- **Browser:** github.dev (lightweight editor)
- **GitHub Mobile App** → Repository → Code → Codespaces
- **Best experience:** Tablet with keyboard

## 🔒 Security & Privacy

- Your code runs in an isolated container
- Only you can access your Codespace
- Progress files (.progress/) persist across sessions
- All changes are yours - no sharing unless you push to GitHub

## 💡 Tips for Codespaces Users

1. **Use Command Palette:** Ctrl+Shift+P for quick actions
2. **Split Editor:** Right-click file → "Split Editor Right" to view two files
3. **Integrated Terminal:** Bottom panel for running Python
4. **File Explorer:** Left sidebar for navigating tasks
5. **Search:** Ctrl+Shift+F to search across all files
6. **Git Integration:** Source Control panel (left) for commits
7. **Keyboard Shortcuts:** Ctrl+K Ctrl+S to view all shortcuts

## 🎓 Recommended Workflow

### For Each Part:
1. Open Codespace
2. Navigate to `partN/partNExercises/tasks/`
3. Work through tasks in order
4. Run each task to test: `python X.Y.Z_task.py`
5. Grade when done: `python grade_partN.py`
6. Commit and push: `git add . && git commit -m "..." && git push`
7. Check marksheet: `cat .progress/marksheet.md`

### Daily Routine:
- **Morning:** Open Codespace, pull latest: `git pull`
- **Work:** Complete 3-5 tasks
- **Evening:** Grade, commit, push: `python grade_partX.py && git add . && git commit -m "..." && git push`
- **Stop Codespace** to save hours

## 🆘 Getting Help

### In Codespaces:
- **Python Errors:** Check the terminal output
- **Git Issues:** Use integrated Source Control panel
- **VS Code Help:** Help → Welcome → Interactive Playground

### External Resources:
- **GitHub Codespaces Docs:** https://docs.github.com/en/codespaces
- **VS Code Docs:** https://code.visualstudio.com/docs
- **Python Docs:** https://docs.python.org/3/

## 🎉 Benefits of Using Codespaces

✅ **No Setup:** Works immediately - no Python install needed  
✅ **Consistent Environment:** Everyone has the same setup  
✅ **Cloud-Based:** Access from any device with a browser  
✅ **Pre-configured:** All tools and extensions ready  
✅ **Auto-Save:** Never lose work  
✅ **Git Integrated:** Easy commits and pushes  
✅ **Free Tier:** 60 hours/month for students  
✅ **Mobile Friendly:** Code on tablet or phone  
✅ **No Local Storage:** Doesn't fill up your hard drive  

---

**Ready to start?** Click the green "Code" button → "Codespaces" → "Create codespace on main"

**Happy Coding! 🐍**
