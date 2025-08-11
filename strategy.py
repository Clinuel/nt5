def generate_signal(market_data, equity, risk_percent):
    price = market_data.get('current_price')
    if not price:
        return {'error': 'Price not detected'}

    direction = 'BUY' if price % 2 == 0 else 'SELL'
    stop_loss = price - 2 if direction == 'BUY' else price + 2
    take_profit = price + 6 if direction == 'BUY' else price - 6

    risk_amount = equity * (risk_percent / 100)
    pip_value = 1
    lot_size = round(risk_amount / abs(price - stop_loss), 2)

    return {
        'symbol': market_data['symbol'],
        'timeframe': market_data['timeframe'],
        'direction': direction,
        'entry': price,
        'stop_loss': stop_loss,
        'take_profit': take_profit,
        'lot_size': lot_size,
        'risk_reward': round(abs(take_profit - price) / abs(price - stop_loss), 2)
    }
