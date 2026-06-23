import csv
import os

STOCK_PRICES = {
    "AAPL":  180,
    "TSLA":  250,
    "GOOGL": 140,
    "AMZN":  185,
    "MSFT":  415,
    "NFLX":  620,
    "META":  500,
    "NVDA":  900,
}

def display_available_stocks():
    print("\n📈 Available Stocks:")
    print(f"{'Symbol':<10} {'Price (USD)':>12}")
    print("-" * 25)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<10} ${price:>11,.2f}")

def get_portfolio():
    portfolio = {}
    print("\n💼 Enter your stock holdings.")
    print("Type 'done' when finished.\n")
    while True:
        symbol = input("Stock symbol (e.g. AAPL): ").strip().upper()
        if symbol.lower() == "done":
            if not portfolio:
                print("⚠ You haven't added any stocks yet.")
                continue
            break
        if symbol not in STOCK_PRICES:
            print(f"⚠ '{symbol}' not found. Available: {', '.join(STOCK_PRICES.keys())}")
            continue
        try:
            quantity = int(input(f"Quantity of {symbol}: ").strip())
            if quantity <= 0:
                print("⚠ Quantity must be a positive number.")
                continue
        except ValueError:
            print("⚠ Please enter a valid whole number.")
            continue
        if symbol in portfolio:
            portfolio[symbol] += quantity
            print(f"✅ Updated {symbol}: total {portfolio[symbol]} shares.")
        else:
            portfolio[symbol] = quantity
            print(f"✅ Added {symbol} x{quantity}.")
    return portfolio

def calculate_portfolio(portfolio):
    print("\n" + "=" * 45)
    print("          📊 PORTFOLIO SUMMARY")
    print("=" * 45)
    print(f"{'Stock':<8} {'Qty':>5} {'Price':>10} {'Value':>12}")
    print("-" * 45)
    total = 0
    results = []
    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        results.append((symbol, qty, price, value))
        print(f"{symbol:<8} {qty:>5} ${price:>9,.2f} ${value:>11,.2f}")
    print("-" * 45)
    print(f"{'TOTAL INVESTMENT':>35}: ${total:>11,.2f}")
    print("=" * 45)
    return results, total

def save_to_file(results, total):
    save = input("\n💾 Save results to file? (yes/no): ").strip().lower()
    if save != "yes":
        print("Results not saved.")
        return
    fmt = input("Save as (csv/txt): ").strip().lower()
    filename = f"portfolio.{fmt}" if fmt in ("csv", "txt") else "portfolio.txt"
    if fmt == "csv":
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price (USD)", "Value (USD)"])
            for symbol, qty, price, value in results:
                writer.writerow([symbol, qty, price, value])
            writer.writerow([])
            writer.writerow(["Total Investment", "", "", total])
    else:
        with open(filename, "w") as f:
            f.write("PORTFOLIO SUMMARY\n")
            f.write("=" * 45 + "\n")
            for symbol, qty, price, value in results:
                f.write(f"{symbol:<8} {qty:>5} ${price:>9,.2f} ${value:>11,.2f}\n")
            f.write(f"{'TOTAL':>35}: ${total:>11,.2f}\n")
    print(f"✅ Saved as '{filename}'")

def main():
    print("\n=============================")
    print("   STOCK PORTFOLIO TRACKER")
    print("=============================")
    display_available_stocks()
    portfolio = get_portfolio()
    results, total = calculate_portfolio(portfolio)
    save_to_file(results, total)
    print("\nThank you for using Stock Portfolio Tracker! 📈")

if __name__ == "__main__":
    main()
