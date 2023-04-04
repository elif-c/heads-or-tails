while True:
    user_input = input("Toss a coin and enter head or tail (or type exit): ")
    match user_input:
        case "head":
            with open("record.txt", "r") as file:
                h = int(file.readline().strip('\n'))
                t = int(file.readline())
            h += 1
            with open("record.txt", "w") as file:
                file.write(f"{h}\n")
                file.write(f"{t}")
            print(f"Heads probability: {h / (h+t) * 100}%")
            continue
        case "tail":
            with open("record.txt", "r") as file:
                h = int(file.readline().strip('\n'))
                t = int(file.readline())
            t += 1
            with open("record.txt", "w") as file:
                file.write(f"{h}\n")
                file.write(f"{t}")
            print(f"Heads probability: {h / (h + t) * 100}%")
            continue
        case "exit":
            user_input = input("Do you want to exit? (y/n): ")
            if user_input.lower() == "n":
                continue
            user_input1 = input("Would you like to clear the records? (y/n): ")
            if user_input1 == "y":
                user_input2 = input("Are you sure? (y/n): ")
                if user_input2 == "y":
                    with open("record.txt", "w") as file:
                        file.write("0\n")
                        file.write("0")
            break
        case _:
            print("Please type the correct input.")
            print()
            continue
print("Bye ^^")
exit()
