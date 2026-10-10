import os

file_name = input("Enter the file name: ")

while True:
 print("1. create a file")
 print("2. write to a file")
 print("3. read a file")
 print("4. append to a file")
 print("5. check if file exists")
 print("6. delete a file")
 print("7. exit")

 choice = input("Enter your choice: ")

 if choice == "1":
  with open(file_name, "w") as file:
   print(f"{file_name} created successfully.")
 elif choice == "2":
  with open(file_name, "w") as file:
   content = input("Enter content to write: ")
   file.write(content)
   print(f"Content written to {file_name} successfully.")
 elif choice == "3":
  if os.path.exists(file_name):
   with open(file_name, "r") as file:
    content = file.read()
    print(f"content of {file_name}:")
    print(content)
  else:
   print(f"{file_name} does not exist.")
 elif choice == "4":
  with open(file_name, "a") as file:
   content = input("Enter content to append: ")
   file.write(content)
   print(f"Content appended to {file_name} successfully.")
 elif choice == "5":
  if os.path.exists(file_name):
   print(f"{file_name} exists.")
  else:
   print(f"{file_name} does not exist.")
 elif choice == "6":
  if os.path.exists(file_name):
   input(f"Are you sure you want to delete {file_name}? (yes/no): ") == "yes" and os.remove(file_name) and print(f"{file_name} deleted successfully.")
  else:
   print(f"{file_name} does not exist.")
 elif choice == "7":
  break
 else:
  print("Invalid choice. Please try again.")