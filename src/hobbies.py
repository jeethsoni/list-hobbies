def main():
    hobbies = list(input("Enter your beloved hobbies: ").split(","))

    # first element in the list
    print(f"Your favorite hobby is: {hobbies[0]}")

    # last element in the list
    for hobby in reversed(hobbies):
        print(f"The last element in the list is: {hobby}")
        break

    # length of the hobbies list
    print(f"You have {len(hobbies)} beloved hobbies")

    # uppercase all hobbies
    print("hobbies all uppercased: ")
    for h in hobbies:
        print(h.upper(), end=",")

    # sorting the list
    hobbies.sort()
    print(f"\nYour sorted hobbies are: {hobbies}")


if __name__ == "__main__":
    main()
