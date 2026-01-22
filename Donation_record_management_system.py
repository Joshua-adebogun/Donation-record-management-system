donation_records = []

def add_donation():
    donor = input("Enter donor name: ")
    amount = float(input("Enter donation amount: "))
    donation_records.append({
        "donor": donor,
        "amount": amount
    })
    print("Donation recorded successfully")

def view_donations():
    if not donation_records:
        print("No donations recorded")
    else:
        for d in donation_records:
            print("Donor:", d["donor"], "| Amount:", d["amount"])

def main():
    while True:
        print("1. Add Donation")
        print("2. View Donations")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_donation()
        elif choice == "2":
            view_donations()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()
