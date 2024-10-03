### Discord Bots Project

This repo contains three AI-powered Discord bots:

- **feedback.py**: Processes proposals and provides AI generated feedback `!feedback`.
- **pre-notes.py**: Handles pre-notes `!pre-notes`.
- **notes.py**: Handles notes with `!notes`

### Setup

1. Clone the repo and install dependencies:
   ```bash
   git clone https://github.com/yourusername/discord-bots.git
   cd discord-bots
   pip install -r requirements.txt
   ```

2. Add bot tokens in a `.env` file:
   ```bash
   DISCORD_PRENOTES_TOKEN=your-token
   ```

3. Run each bot:
   ```bash
   python pre-notes.py
   ```
