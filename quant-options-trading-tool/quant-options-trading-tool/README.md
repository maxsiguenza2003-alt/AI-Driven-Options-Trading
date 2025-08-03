# Quant Options Trading Tool 📈

A custom-built AI-driven Python tool that helps identify high-probability options trading opportunities using technical indicators and quantitative models.

## 🚀 Key Features

- 📊 Real-time technical analysis (RSI, MACD, VWAP, DMI)
- 💡 Signal generation for Calls/Puts
- 🧠 Quant models: Black-Scholes + Kelly Criterion
- 🔄 Integrates with ThinkorSwim data
- 🧪 Backtesting and ROI analytics

## 🛠 Tech Stack

- Python (Pandas, NumPy, Matplotlib)
- ThinkorSwim Integration (via exported chart data)
- Technical Indicators
- Quantitative Models (custom Black-Scholes + Kelly formula)

## 📈 Sample Output

```bash
BUY SIGNAL — PLTR 0DTE CALL
Entry: $0.45 | Target: $0.78 | Volume Surge + MACD crossover | Risk-Adjusted via Kelly: 12.6%
```

## 📂 File Structure

- `main.py` – Entry script
- `models/` – Contains Black-Scholes and Kelly Criterion formulas
- `indicators/` – Technical indicator implementations
- `charts/` – Chart drawing utilities
- `data/` – Sample data folder

## 🔒 Disclaimer

This project is for **educational use only** and not financial advice. Trade responsibly.
