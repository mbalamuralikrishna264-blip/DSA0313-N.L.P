dialog = input("Enter dialog: ")

if dialog.endswith("?"):
    print("Dialog Act: Question")

elif dialog.lower() in ["hi", "hello"]:
    print("Dialog Act: Greeting")

else:
    print("Dialog Act: Statement")
