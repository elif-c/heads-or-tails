while True:
    text = input("Enter text to see character count: ")
    mode = input("All characters or ignore whitespaces? (all/ignore/exit): ")
    match mode:
        case "all":
            print(f"There's {len(text.strip())} characters.")
        case "ignore":
            text = text.strip().replace(" ", "")
            print(text)
            print(f"There's {len(text)} characters without whitespaces.")
        case "exit":
            break
        case _:
            print("Try again.")
            continue
print("Bye ^^")
exit()
