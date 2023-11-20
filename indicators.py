import pandas as pd

def simple_moving_average(df, trade_column, date_column):
    """
    Implement the buy and sell strategy based on the average over the last week.

    Parameters:
    - df: DataFrame containing trade data
    - trade_column: Column name representing trade consideration
    - date_column: Column name representing dates
    - shares_to_trade: Number of shares to buy or sell

    Returns:
    - DataFrame with a table of all Buy and Sell trades, entry and exit prices, and P&L calculation per trade.
    """
    df_copy = df.copy()

    # Assuming df has a date_column (e.g., 'timestamp') representing dates
    df_copy.set_index(date_column, inplace=True)

    # Calculate Simple Moving Average (SMA) over the last week for trade_consideration
    df_copy['indicator'] = df_copy[trade_column].rolling(window=5).mean()
    return df_copy

def exponential_moving_average(df, trade_column, date_column):
    """
    Implement the buy and sell strategy based on the average over the last week.

    Parameters:
    - df: DataFrame containing trade data
    - trade_column: Column name representing trade consideration
    - date_column: Column name representing dates
    - shares_to_trade: Number of shares to buy or sell

    Returns:
    - DataFrame with a table of all Buy and Sell trades, entry and exit prices, and P&L calculation per trade.
    """
    df_copy = df.copy()

    # Assuming df has a date_column (e.g., 'timestamp') representing dates
    df_copy.set_index(date_column, inplace=True)

    # Calculate Simple Moving Average (SMA) over the last week for trade_consideration
    df_copy['indicator'] = df_copy[trade_column].ewm(span=5, adjust=False).mean()
    return df_copy

def moving_average_convergence_divergence(df, price_column):
    """
    Calculate Moving Average Convergence Divergence (MACD) for a given DataFrame.

    Parameters:
    - df: DataFrame containing price data
    - price_column: Column name representing the price values

    Returns:
    - DataFrame with additional columns for MACD, Signal Line, and MACD Histogram
    """
    df_copy = df.copy()

    # Calculate Short-term EMA
    df_copy['Short EMA'] = df_copy[price_column].ewm(span=12, adjust=False).mean()

    # Calculate Long-term EMA
    df_copy['Long EMA'] = df_copy[price_column].ewm(span=26, adjust=False).mean()

    # Calculate MACD
    df_copy['MACD'] = df_copy['Short EMA'] - df_copy['Long EMA']

    # Calculate Signal Line (Signal Line EMA)
    df_copy['Signal Line'] = df_copy['MACD'].ewm(span=9, adjust=False).mean()

    # Calculate MACD Histogram
    df_copy['MACD Histogram'] = df_copy['MACD'] - df_copy['Signal Line']

    return df_copy

def stochastic_oscillator(df, high_column, low_column, close_column, k_period, d_period):
    """
    Calculate Stochastic Oscillator for a given DataFrame.

    Parameters:
    - df: DataFrame containing price data
    - high_column: Column name representing the high prices
    - low_column: Column name representing the low prices
    - close_column: Column name representing the closing prices
    - k_period: Period for %K calculation
    - d_period: Period for %D calculation (Smoothing period)

    Returns:
    - DataFrame with additional columns for %K and %D
    """
    df_copy = df.copy()

    # Calculate %K
    df_copy['%K'] = ((df_copy[close_column] - df_copy[low_column].rolling(window=k_period).min()) /
                     (df_copy[high_column].rolling(window=k_period).max() - df_copy[low_column].rolling(window=k_period).min())) * 100

    # Calculate %D (Smoothing %K with a simple moving average)
    df_copy['%D'] = df_copy['%K'].rolling(window=d_period).mean()

    return df_copy

def calculate_obv(df, volume_column, close_column):
    """
    Calculate On Balance Volume (OBV) for a given DataFrame.

    Parameters:
    - df: DataFrame containing price and volume data
    - volume_column: Column name representing the volume
    - close_column: Column name representing the closing prices

    Returns:
    - DataFrame with an additional column for OBV
    """
    df_copy = df.copy()

    # Calculate OBV
    df_copy['OBV'] = df_copy.apply(lambda row: row[volume_column] if row[close_column] >= row[close_column - 1] else -row[volume_column], axis=1)
    df_copy['OBV'] = df_copy['OBV'].cumsum()

    return df_copy

def calculate_market_profile(df, price_column, volume_column, bin_width=1):
    """
    Calculate Market Profile metrics including Point of Control (POC),
    Value Area High (VAH), and Value Area Low (VAL) for a given DataFrame.

    Parameters:
    - df: DataFrame containing price and volume data
    - price_column: Column name representing the price
    - volume_column: Column name representing the volume
    - bin_width: Width of each price bin for market profile calculation

    Returns:
    - Dictionary with POC, VAH, and VAL values
    """
    df_copy = df.copy()

    # Calculate price bins
    df_copy['Price Bin'] = df_copy[price_column] // bin_width * bin_width

    # Calculate volume at each price level
    volume_at_price = df_copy.groupby('Price Bin')[volume_column].sum()

    # Find Point of Control (POC)
    poc = volume_at_price.idxmax()

    # Find Value Area High (VAH) and Value Area Low (VAL)
    value_area = volume_at_price.sort_values(ascending=False).cumsum()
    value_area_high = value_area[value_area <= value_area.max() * 0.7].idxmax()
    value_area_low = value_area[value_area <= value_area.max() * 0.7].idxmax()

    return {'Point of Control': poc, 'Value Area High': value_area_high, 'Value Area Low': value_area_low}

def tracking_trades(df_copy,  trade_column, shares_to_trade):
    # Initialize variables for tracking trades
    in_trade = False
    entry_price = 0
    trade_data = {'Date': [], 'Action': [], 'Entry Price': [], 'Exit Price': [], 'P&L': []}

    # Iterate through the DataFrame to generate trade signals and track trades
    for index, row in df_copy.iterrows():
        if row[trade_column] > row['indicator'] and not in_trade:
            # Buy signal
            entry_price = row[trade_column]
            in_trade = True
            trade_data['Date'].append(index)
            trade_data['Action'].append('Buy')
            trade_data['Entry Price'].append(entry_price)
            trade_data['Exit Price'].append(0)  # Placeholder until the sell signal
            trade_data['P&L'].append(0)  # Placeholder until the sell signal
        elif row[trade_column] < row['indicator'] and in_trade:
            # Sell signal
            exit_price = row[trade_column]
            in_trade = False
            trade_data['Date'].append(index)
            trade_data['Action'].append('Sell')
            trade_data['Entry Price'].append(entry_price)
            trade_data['Exit Price'].append(exit_price)
            trade_data['P&L'].append((exit_price - entry_price) * shares_to_trade)

    # Create a DataFrame from the trade data
    trades_df = pd.DataFrame(trade_data)
    
    return trades_df

def profit_loss(data, trades_df):
    # Calculate P&L of simply buying and holding 1000 Barclays shares
    buy_and_hold_df = data.copy()
    buy_and_hold_df['P&L'] = (buy_and_hold_df['trade_consideration'] - buy_and_hold_df['trade_consideration'].shift(1)).cumsum() * 1000

    # Combine the two P&L series into a single DataFrame
    pnl_df = pd.DataFrame({
        'Date': data['agreed_time'],
        'Strategy P&L': trades_df['P&L'].cumsum(),
        'Buy and Hold P&L': buy_and_hold_df['P&L']
        })
    print(pnl_df)
    return trades_df, pnl_df
