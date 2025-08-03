from indicators.rsi import calculate_rsi
from indicators.macd import calculate_macd
from models.black_scholes import black_scholes_price
from models.kelly_criterion import kelly_criterion

sample_price_data = [24.2, 24.5, 24.0, 24.3, 24.7]

rsi = calculate_rsi(sample_price_data)
macd = calculate_macd(sample_price_data)
option_price = black_scholes_price(S=24.5, K=25, T=0.01, r=0.01, sigma=0.45, option_type="call")
kelly = kelly_criterion(win_prob=0.6, win_loss_ratio=1.5)

print(f"RSI: {rsi}, MACD: {macd}, Option Price: {option_price}, Kelly %: {kelly * 100:.2f}%")
