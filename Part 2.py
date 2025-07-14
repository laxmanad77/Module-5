# CSU Global Bookstore Book Club Rewards Program

def display_intro():
    print("="*60)
    print("      Welcome to the CSU Global Bookstore Book Club")
    print("="*60)
    print("Earn reward points based on the number of books you purchase:")
    print("--------------------------------------------------------------")
    print("  0–1 books   :   0 points")
    print("  2–3 books   :   5 points")
    print("  4–5 books   :  15 points")
    print("  6–7 books   :  30 points")
    print("  8+ books    :  60 points")
    print("--------------------------------------------------------------\n")

def get_books_purchased():
    while True:
        try:
            books = int(input("Enter the number of books you purchased this month: "))
            if books < 0:
                print("⚠️  Number of books cannot be negative. Please try again.")
            else:
                return books
        except ValueError:
            print("⚠️  Invalid input. Please enter a whole number.")

def calculate_points(books):
    if books >= 8:
        return 60
    elif books >= 6:
        return 30
    elif books >= 4:
        return 15
    elif books >= 2:
        return 5
    else:
        return 0

def display_summary(books, points):
    print("\n================== 📚 Monthly Summary ==================")
    print(f"Books Purchased : {books}")
    print(f"Reward Points   : {points}")
    if points == 0:
        print("💡 Tip: Purchase 2 or more books to start earning points!")
    else:
        print("🎉 Great job! Your reading is earning you rewards.")
    print("=========================================================")

def main():
    display_intro()
    books = get_books_purchased()
    points = calculate_points(books)
    display_summary(books, points)

if __name__ == "__main__":
    main()
