from json_tool import JSONTool


tool = JSONTool()

while True:
    print("\n🧾 JSON FORMATTER & VALIDATOR")
    print("1. Format JSON")
    print("2. Validate JSON")
    print("3. Load JSON File")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        text = input("Enter JSON: ").strip()

        if text:
            tool.format_json(text)
        else:
            print("JSON cannot be empty. ❌")

    elif choice == "2":
        text = input("Enter JSON: ").strip()

        if text:
            tool.validate_json(text)
        else:
            print("JSON cannot be empty. ❌")

    elif choice == "3":
        filename = input("Enter JSON file name: ").strip()

        if filename:
            tool.load_file(filename)
        else:
            print("File name cannot be empty. ❌")

    elif choice == "4":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice! ❌")