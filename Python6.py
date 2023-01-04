filename=(input("Enter the filename:"))

Extension= filename.split(".")

print("File extension is :",Extension[1]) if len(Extension) > 1 else print("Unknown extension")
          
