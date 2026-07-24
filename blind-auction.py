print("------------------------------------")
print("Welcome to the Secret Blind Auction.")
print("------------------------------------")


def get_name():
    # Get a valid player name
    while True:
        key = input("What is your name? ").capitalize().strip()
        if key.isalpha():
            return key
        print("Invalid choice, please try again.")


def get_bid():
    # Get a valid bid
    while True:
        value = input("Enter your bid: ").strip()
        if value.isdigit():
            return int(value)
        print("Invalid choice, please try again.")


def yes_no(question):
    while True:
        ans = input(question).lower().strip()
        if ans in ["yes", "no"]:
            return ans
        print("Invalid choice, please try again.")


def blind_auction():
    bids = {}

    while True:
        name = get_name()
        bid = get_bid()
        bids[name] = bid

        print("\n" * 20)

        if yes_no("Are there any more players? (yes or no): ") == "yes":
            continue

        winner = max(bids, key=bids.get)
        print(f"{winner} wins the auction with a bid of ${bids[winner]}.")

        if yes_no("Play again? (yes or no): ") == "yes":
            print("Starting a new auction.\n")
            bids = {}
            continue

        print("Goodbye.")
        break


blind_auction()