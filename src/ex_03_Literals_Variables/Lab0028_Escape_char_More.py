def escape_char_demo():
    print("Demonstrating Python Escape Characters:\n")

    print("1. Newline (\\n):")
    print("Hello\nWorld")

    print("\n2. Tab (\\t):")
    print("Name\t:\tJohn")

    print("\n3. Backslash (\\\\):")
    print("This is a backslash: \\")

    print("\n4. Single Quote (\\') and Double Quote (\\\"):")
    print('It\'s a sunny day')
    print("He said, \"Hello!\"")

    print("\n5. Carriage Return (\\r):")
    print("12345\rABCDE")  # Output may overwrite the beginning

    print("\n6. Backspace (\\b):")
    print("Hello\b World")  # Removes 'o' before printing ' World'

    print("\n7. Form Feed (\\f):")
    print("Hello\fWorld")  # Output may vary depending on terminal

    print("\n8. Bell/Alert (\\a):")
    print("This will trigger a sound (if supported)\a")

    print("\n9. Octal and Hex values (\\ooo and \\xhh):")
    print("Octal \\141 = " + "\141")  # 'a'
    print("Hex \\x61 = " + "\x61")    # 'a'

# Run the demo
escape_char_demo()
