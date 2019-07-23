import pandas as pd
import matplotlib.pyplot as plt

def highest_vol(df):
    print("\nPrice With Highest Volume")
    return df.loc[df['Volume_BTC'].idxmax()]

def VWAP_vs_volume(df):
    plt.title("Volume vs Weighted Price")
    plt.plot(df.Weighted_Price.iloc[::500], linewidth=1, color='blue', label='WP')
    plt.plot(df.Volume_BTC.iloc[::500], linewidth=1, color='red', label='Volume')


def price(df):
    plt.cla()
    plt.title("Price")
    plt.plot(df.High, linewidth=1, color='blue', label='Price')
    
def price_vs_volume_high(df):
    mean = df.High.mean()
    plt.figure(figsize=(8,5))
    plt.title("Volume vs Prices Above Mean")
    plt.plot(df.High[df.High>mean].iloc[::500], linewidth=2, label='Price')
    plt.plot(df.Volume_BTC.iloc[::500], linewidth=1, color='red', label='Volume')

def price_vs_volume_low(df):
    mean = df.High.mean()
    plt.figure(figsize=(8,5))
    plt.title("Prices Below Mean")
    plt.plot(df.High[df.High<mean].iloc[::500], linewidth=2, label='Price')

def volume_stats(df):
    print("BTC Volume Statictics...")
    return df.Volume_BTC.describe()

def high_vs_vol(df):
    plt.figure(figsize=(8,5))
    plt.plot(df.High.iloc[::500], linewidth=2, label='Price')
    plt.plot(df.Volume_BTC.iloc[::500], linewidth=1, color='red', label='Volume')
    plt.title('Price vs Volume')
    plt.show()

def main():
    file = "new_database.csv"
    df = pd.read_csv(file)
    
    high_vs_vol(df)
    
    print(volume_stats(df))
    
    price_vs_volume_low(df)
    
    price_vs_volume_high(df)
    
    VWAP_vs_volume(df)
    
    print(highest_vol(df))
    
    price(df)
    
    print("==========First 250000 Prices==========")
    print(df['High'].head(250000))
    print("==========First 250000 Volumes==========")
    print(df['Volume_BTC'].head(250000))
    
    
if __name__ == '__main__':
    main()