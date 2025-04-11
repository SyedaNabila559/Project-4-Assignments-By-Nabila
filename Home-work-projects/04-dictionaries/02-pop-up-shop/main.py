def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0

    print("\n🥭🍇 Welcome to fruits shop! 🍉🍎")

    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input(f"How many ({fruit_name}s) do you want to buy? ") or 0)
        total_cost += (price * amount_bought)

    print(f"Your total is ${total_cost}")



if __name__ == '__main__':
    main()