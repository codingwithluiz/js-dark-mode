# Dark Mode Toggle ☀️🌙

A complete light/dark theme switching system with preference persistence.

## ✨ Features

- **Instant toggle** between light/dark themes
- **Preference memory** (localStorage)
- **Smooth transitions** between modes
- **Fully customizable** via CSS
- **Responsive design** for all devices
- **Accessible button** with intuitive emojis
- **Flicker prevention** (inline HTML script)

## 🗂️ File Structure

```
darkmode-project/
├── index.html        # Main page with flicker prevention
├── style.css         # Styles with CSS variables
└── darkmode.js       # Complete dark mode logic
```

## 🚀 Quick Start

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/darkmode-project.git
   cd darkmode-project
   ```

2. Open `index.html` in your browser

3. Click the 🌙/☀️ button to toggle

## 🎨 Customization

### Colors (edit in `style.css`)
```css
:root {
  --base-color: white;          /* Light background */
  --text-color: #111528;        /* Light text */
  --accent-color: #0071ff;      /* Accent color */
}

:root.darkmode {
  --base-color: #070b1d;        /* Dark background */
  --text-color: #ffffff;        /* Dark text */
}
```

## ⚙️ Technical Details

1. **Flicker Prevention**: Inline script loads first
2. **Initialization**: Checks localStorage on load
3. **Toggle**: Switches classes and updates storage
4. **Styling**: Dynamic CSS variables control themes

## 📄 License

MIT License - Free to use and modify
