# 🎰 Discord Betting Bot with Ethereum Integration

A full-featured Discord bot that allows users to enter matchmaking queues, place coin-based bets on match outcomes, and interact with an in-app coin system backed by Ethereum. This project uses Discord Cogs, async SQLite for lightweight storage, and `web3.py` for blockchain interaction.

---

## 🚀 Features

- 🎮 **Queue System**: Users can join a matchmaking queue with `!queue`.
- 🧠 **Automatic Matchmaking**: Automatically creates matches between queued players.
- 💰 **Coin System**: Every user starts with 1000 coins.
- 💵 **Betting**: Place bets on match outcomes using `!bet`.
- 🏆 **Match Result Handling**: Moderators declare winners and redistribute coins accordingly.
- 💼 **Wallet Integration**: Users can link their Ethereum wallet.
- ⛽ **ETH Withdrawals**: Users can withdraw coins as ETH.
- 🔁 **Buy Coins**: Users can purchase coins using ETH.
- 📊 **Active Bets View**: View ongoing bets.
- 🔐 **Admin Commands**: Restricted match control using Discord roles.

---

## 🧩 Project Structure

```
discord_betting_bot/
│
├── bot.py                  # Entry point for running the bot
├── .env                    # Environment variables (not committed to Git)
│
├── cogs/
│   ├── betting.py          # All betting-related commands
│   ├── match.py            # Match queueing and result handling
│   ├── wallet.py           # Ethereum wallet connection and transactions
│   └── utils.py            # Common helper functions (gas price, etc.)
│
├── db/
│   └── bets.db             # SQLite database (autocreated on run)
│
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/discord-betting-bot.git
cd discord-betting-bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env` file

Create a `.env` file in the root directory with the following content:

```env
BOT_TOKEN=your_discord_bot_token
BOT_WALLET_ADDRESS=0xYourBotWalletAddress
BOT_WALLET_PRIVATE_KEY=your_private_key_here
WEB3_PROVIDER=https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID
```

> ✅ **Important**: Do not share your `.env` file or commit it to GitHub. It contains private credentials.

### 4. Run the bot

```bash
python bot.py
```

---

## 🧪 Commands Overview

| Command | Description |
|--------|-------------|
| `!queue` | Join the matchmaking queue |
| `!balance` | Check your current coin balance |
| `!connect_wallet <wallet_address>` | Connect your Ethereum wallet |
| `!bet <match_id> <amount> <player1/player2>` | Place a bet |
| `!active_bets` | See your ongoing bets |
| `!withdraw <amount>` | Convert coins to ETH and withdraw |
| `!buy_coins <eth_amount>` | Buy coins with ETH |
| `!gas_price` | Check current Ethereum gas price |
| `!start_match <player1> <player2>` | (Moderator only) Start a custom match |
| `!result <match_id> <player1/player2>` | (Moderator only) Declare match winner |

---

## 🔐 Role Permissions

- The `!start_match` and `!result` commands require the user to have a **Discord role named `Moderator`**.
- All other commands are open to any user.

---

## ⚠️ Security & Limitations

- This bot uses a single Ethereum wallet (the bot's) to handle all transactions.
- Users do **not** control their wallet keys through the bot; deposits and purchases should be verified via ETH transactions.
- Real ETH transactions incur gas fees — use a testnet (like Goerli or Sepolia) for development and testing.
- Be cautious with `BOT_WALLET_PRIVATE_KEY` in production.

---

## 📌 Future Improvements

- ✅ Add transaction listeners for automatic coin credit after user deposits ETH.
- 🔒 Secure wallet operations using a microservice or custodial service.
- 🧾 Add match history and user leaderboards.
- 🧠 Use an AI-based odds system to adjust winnings dynamically.

---

## 🤝 Contributing

PRs are welcome! For major changes, please open an issue first to discuss your proposal.

---

## 📄 License

This project is licensed under the MIT License.