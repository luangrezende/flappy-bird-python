# 🐦 Flappy Bird Python

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![Pygame](https://img.shields.io/badge/pygame-v2.6+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macOS%20%7C%20linux-lightgrey)
![Status](https://img.shields.io/badge/status-active-success.svg)

A clean and simple Flappy Bird clone built with Python and Pygame. What started as a basic recreation turned into a little experiment with configurable gameplay - because sometimes you want the game to be easier, sometimes harder, and sometimes you just want to tweak things until they feel right.

## 🚀 Quick Play Options

**Just want to play?** → [Download the latest .exe](https://github.com/luangrezende/flappy-bird-python/releases/latest) (No Python needed!)

**Want to customize or learn?** → Clone this repo and run from source

**Curious about the code?** → Check out the clean, comment-free Python below ⬇️

## ✨ What Makes This Different

This isn't just another Flappy Bird clone. I wanted to create something that could adapt to different skill levels and preferences:

- **🎮 Visual Difficulty Selection** - No more console menus! Pick your challenge with a clean in-game interface
- **⚖️ Three Balanced Presets** - Easy, Normal, and Hard modes that actually feel different
- **⚙️ JSON Configuration** - Tweak physics and gameplay without touching code
- **📦 Minimal Dependencies** - Just Python and Pygame, nothing fancy
- **🧹 Clean Codebase** - Simple enough to understand and modify

## 🏁 Getting Started

### 💾 Download & Play (Easiest Way)

**Want to play right now without installing anything?**

1. **Go to [Releases](https://github.com/luangrezende/flappy-bird-python/releases)**
2. **Download the latest `FlappyBird.exe`**
3. **Double-click and play!**

*No Python installation required - just download and run!*

### 🐍 Run from Source (For Developers)

**Want to see the code or make changes?**

#### What You'll Need
- Python 3.6 or newer
- That's pretty much it!

#### Installation
1. **Grab the code**
   ```bash
   git clone https://github.com/luangrezende/flappy-bird-python.git
   cd flappy-bird-python
   ```

2. **Install Pygame**
   ```bash
   pip install pygame
   ```

3. **Run it**
   ```bash
   python flappy_bird_game.py
   ```

*Note: The game automatically finds the `config.json` file and `assets/` folder, whether you're running from source or using the standalone executable.*

## 🎮 How to Play

The basics haven't changed - it's still Flappy Bird:

- **SPACEBAR** - Make the bird flap (the only control you need!)
- **ESC** - Quit when you've had enough
- Avoid the green pipes
- Each pipe you pass = 1 point
- Try not to rage quit (harder than it sounds)

When you start the game, you'll see a clean selection screen with three difficulty options. Use the arrow keys to pick one, hit Enter, and you're flying!

## ⚙️ The Configuration System

Here's where things get interesting. The game reads everything from a `config.json` file, so you can customize the experience without diving into Python code.

### 🎯 Difficulty Selection Screen

Instead of a boring console menu, you get a proper in-game interface:

- **🟢 EASY** - Gentle physics, bigger gaps, slower pace (great for beginners or when you're tired)
- **🔵 NORMAL** - The classic Flappy Bird experience, balanced and fair
- **🔴 HARD** - Tight spaces, fast pipes, unforgiving physics (for when you hate yourself)

### 🔧 Behind the Scenes: config.json

The magic happens in this simple JSON file:

```json
{
  "display_settings": {
    "screen_width": 400,
    "screen_height": 600,
    "fps": 60
  },
  "difficulty_presets": {
    "easy": {
      "gravity": 0.2,
      "jump_force": -5,
      "pipe_gap_y": 200,
      "pipe_gap_x": 250,
      "pipe_speed": 1.5
    },
    "normal": {
      "gravity": 0.3,
      "jump_force": -6,
      "pipe_gap_y": 180,
      "pipe_gap_x": 200,
      "pipe_speed": 2
    },
    "hard": {
      "gravity": 0.5,
      "jump_force": -8,
      "pipe_gap_y": 140,
      "pipe_gap_x": 150,
      "pipe_speed": 3
    }
  }
}
```

### 📊 What Each Setting Does

I spent way too much time tweaking these values to get them to feel right:

| Setting | What It Controls | My Notes |
|---------|-----------------|----------|
| `gravity` | How fast the bird falls | 0.2 feels floaty, 0.5 feels like a brick |
| `jump_force` | Strength of each flap | Negative numbers! -5 is gentle, -8 is powerful |
| `pipe_gap_y` | Vertical space between pipes | 200 is forgiving, 140 will test your patience |
| `pipe_gap_x` | Horizontal spacing between pipes | More space = more time to react |
| `pipe_speed` | How fast pipes move toward you | 1.5 is chill, 3 is intense |

## 🎨 Customizing Your Experience

Want to create your own difficulty? Edit the `config.json` file! Here are some ideas:

### ☕ "Chill Mode" (for coffee breaks)
```json
"custom": {
  "gravity": 0.1,
  "jump_force": -4,
  "pipe_gap_y": 250,
  "pipe_gap_x": 300,
  "pipe_speed": 1
}
```

### 💀 "Nightmare Mode" (for masochists)
```json
"nightmare": {
  "gravity": 0.8,
  "jump_force": -12,
  "pipe_gap_y": 120,
  "pipe_gap_x": 120,
  "pipe_speed": 4
}
```

Just add your preset to the `difficulty_presets` section and modify the code to include it in the selection screen.

## 📁 Project Structure

Keeping it simple:

```
flappy-bird-python/
├── flappy_bird_game.py    # The main game (all the magic happens here)
├── config.json            # Game settings (your playground for tweaking)
├── README.md              # You are here
├── LICENSE                # MIT License (use it however you want)
└── assets/                # Graphics and sprites
    ├── background-day.png
    ├── bluebird-downflap.png
    ├── gameover.png
    ├── icon.ico           # Windows executable icon
    └── pipe-green.png
```

## 🔧 Technical Stuff

Built with:
- **Python 3.6+** - Because it's 2025 and we should all be using modern Python
- **Pygame** - The classic choice for 2D games in Python
- **JSON** - For configuration (simple and human-readable)
- **GitHub Actions** - Automatic executable builds for every release
- **PyInstaller** - Converts Python scripts to standalone executables

Performance is solid:
- Runs at 60 FPS on pretty much any modern machine
- Uses about 20MB of RAM (less than a single browser tab)
- CPU usage stays under 3% (won't make your laptop fans spin up)

## 🤖 Automatic Builds

Every time I create a new version tag (like `v1.0.0`), GitHub Actions automatically:

1. **Installs** all dependencies (Pygame, PyInstaller)
2. **Builds** a standalone Windows executable with embedded assets and icon
3. **Creates** a release page with download links
4. **Uploads** the `.exe` file ready to run
5. **Publishes** release notes

The executable includes everything needed - no Python installation required! Just download and double-click to play.

## 🤝 Contributing

Found a bug? Have an idea for improvement? I'd love to hear about it!

This started as a weekend project, but it's been fun to work on. If you want to contribute:

1. Fork it
2. Create a branch for your feature
3. Make your changes
4. Test it (please!)
5. Submit a pull request

### 🔄 Release Process

Want to know how new versions are made?

**Option 1: Automatic (for official releases)**
1. **Code changes** get committed to main branch
2. **Create a tag**: `git tag v1.1.0 && git push origin v1.1.0`
3. **GitHub Actions** automatically builds and releases the executable

**Option 2: Manual (for testing or quick builds)**
1. Go to **GitHub → Actions → "Build and Release"**
2. Click **"Run workflow"**
3. Enter a version name (e.g., `v1.0.1-test`)
4. Click **"Run workflow"** - that's it!

Both methods create a release with the FlappyBird.exe ready for download!

### 💡 Ideas for future improvements:
- Sound effects (the original had that iconic "ding" sound)
- High score persistence
- More visual themes
- Power-ups (maybe controversial for Flappy Bird purists)
- Multiplayer mode (imagine the chaos)

## 📄 License

MIT License - basically, do whatever you want with this code. Build on it, break it, sell it, use it in your portfolio, show it to your cat. I just ask that you keep the original license notice if you redistribute it.

---

**Have fun!** 🎮 

And remember - if the game feels too hard, that's what Easy mode is for. If it feels too easy, well... Hard mode is waiting for you. 

