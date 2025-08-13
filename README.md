# 🐦 Flappy Bird Python

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![Pygame](https://img.shields.io/badge/pygame-v2.6+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macOS%20%7C%20linux-lightgrey)
![Status](https://img.shields.io/badge/status-active-success.svg)

A clean and simple Flappy Bird clone built with Python and Pygame. What started as a basic recreation turned into an experiment with dynamic difficulty - because the best games adapt to challenge you as you improve!

## Quick Play Options

**Just want to play?** → [Download the latest .exe](https://github.com/luangrezende/flappy-bird-python/releases/latest) (No Python needed!)

**Want to customize or learn?** → Clone this repo and run from source

**Curious about the code?** → Check out the clean, comment-free Python below ⬇️

## ✨ What Makes This Different

This isn't just another Flappy Bird clone. I wanted to create something that keeps the bird responsive while ramping up the challenge:

- **Dynamic Difficulty** - Pipes get faster and more frequent as you score!
- **Responsive Bird** - Bird physics stay constant for consistent, skill-based gameplay
- **Progressive Challenge** - Configurable level progression unlocks faster pipes and tighter spacing
- **JSON Configuration** - Tweak progression curves without touching code
- **Minimal Dependencies** - Just Python and Pygame, nothing fancy
- **Clean Codebase** - Simple enough to understand and modify
- **Mouse & Keyboard** - Click or press spacebar to play

## 🏁 Getting Started

### Download & Play (Easiest Way)

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

## How to Play

The basics haven't changed - it's still Flappy Bird:

- **SPACEBAR or LEFT CLICK** - Make the bird flap (the only control you need!)
- **ESC** - Quit when you've had enough
- Avoid the green pipes
- Each pipe you pass = 1 point
- Try not to rage quit (harder than it sounds)

The game starts easy and **automatically gets harder** as you progress! The bird stays responsive, but pipes get faster and more frequent. Watch the level and speed counters in the top-left corner.

## Dynamic Difficulty System

Here's where things get interesting. The **bird physics stay constant** for consistent, skill-based gameplay, but the **environment gets more challenging**!

### How It Works

The bird always feels the same, but the world gets faster:

- **Level 1 (0-2 points)**: Slow pipes, comfortable spacing
- **Level 2 (3-5 points)**: Faster pipes, tighter timing
- **Level 3 (6-8 points)**: Much faster pipes, frequent obstacles
- **And so on...** - The speed never stops increasing!

### Behind the Scenes: Smart Progression

**Bird Physics (Always Constant):**
- Gravity: 0.3 (responsive)
- Jump Force: -6 (strong and precise)
- Gap Size: 180px (fair but challenging)

**Dynamic Elements:**

The magic happens through mathematical progression based on your score:

```json
{
  "dynamic_difficulty": {
    "progression_info": {
      "level_up_every": 3,
      "bird_gravity": 0.3,
      "bird_jump_force": -6,
      "pipe_gap_size": 180,
      "starting_pipe_speed": 1.0,
      "max_pipe_speed": 6.0,
      "starting_pipe_frequency": 150,
      "min_pipe_frequency": 80
    }
  }
}
```

### How Difficulty Progression Works

The game keeps bird physics constant but ramps up the challenge:

| Parameter | Starting Value | Effect | Max Value |
|-----------|---------------|--------|-----------|
| `bird_gravity` | 0.3 | How fast the bird falls | 0.3 (constant) |
| `bird_jump_force` | -6 | Strength of each flap | -6 (constant) |
| `pipe_gap_size` | 180px | Vertical space between pipes | 180px (constant) |
| `pipe_speed` | 1.0 | How fast pipes move toward you | 6.0 |
| `pipe_frequency` | 150px | Distance between pipe sets | 80px |

**Formula**: Progressive scoring = faster pipes + more frequent obstacles = skill-based challenge!

##  Customizing the Progression

Want to tweak how the challenge scales? Edit the `config.json` file!

You can adjust:
- **How often difficulty increases** (`level_up_every`)
- **Bird physics** (gravity, jump force - but keeping them constant is recommended)
- **Pipe speed progression** (how much faster each level gets)
- **Pipe frequency** (how much closer pipes get to each other)

The system ensures the bird always feels responsive while providing an escalating challenge!

## Project Structure

Keeping it simple:

```
flappy-bird-python/
├── flappy_bird_game.py    # The main game with dynamic difficulty
├── config.json            # Progression settings (your playground for tweaking)
├── README.md              # You are here
├── LICENSE                # MIT License (use it however you want)
└── assets/                # Graphics and sprites
    ├── background-day.png
    ├── bluebird-downflap.png
    ├── gameover.png
    ├── icon.ico           # Windows executable icon
    └── pipe-green.png
```

## Technical Stuff

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

## Automatic Builds

Every time I create a new version tag (like `v1.0.0`), GitHub Actions automatically:

1. **Installs** all dependencies (Pygame, PyInstaller)
2. **Builds** a standalone Windows executable with embedded assets and icon
3. **Creates** a release page with download links
4. **Uploads** the `.exe` file ready to run
5. **Publishes** release notes

The executable includes everything needed - no Python installation required! Just download and double-click to play.

## Contributing

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

## License

MIT License - basically, do whatever you want with this code. Build on it, break it, sell it, use it in your portfolio, show it to your cat. I just ask that you keep the original license notice if you redistribute it.

---

**Have fun!** 

And remember - the bird always feels the same, but the world gets faster and more challenging as you progress! 

