# Step 1: Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3300,
    "MSFT": 300
}

def stock_tracker():
    total_investment = 0
    investment_details = []

    print("📊 Simple Stock Tracker")
    print("Available stocks:", ', '.join(stock_prices.keys()))
    print("Type 'done' to finish input.\n")

    while True:
        stock = input("Enter stock symbol: ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("Stock not found. Try again.")
            continue
        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue

        value = stock_prices[stock] * quantity
        total_investment += value
        investment_details.append(f"{stock} x {quantity} = ${value}")

    print("\n💼 Investment Summary:")
    for detail in investment_details:
        print(detail)
    print(f"\n🧮 Total Investment: ${total_investment}")

    # Optional: Save to a text file
    save = input("\nDo you want to save the result to a file? (yes/no): ").lower()
    if save == "yes":
        with open("investment_summary.txt", "w") as file:
            file.write("Investment Summary:\n")
            for detail in investment_details:
                file.write(detail + "\n")
            file.write(f"\nTotal Investment: ${total_investment}")
        print("✅ Saved to investment_summary.txt")

# Run the tracker
stock_tracker()
