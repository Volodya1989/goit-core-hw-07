from addressbook import AddressBook
from record import Record

# Create an AddressBook instance
address_book = AddressBook()

# Create a record for a person
record1 = Record("John Doe")
record1.add_phone("1234567890")

# Add record to the address book
address_book.add_record(record1)

# Print the address book
print(address_book)

# Find a record
print(address_book.find("John Doe"))

# Edit phone number
record1.edit_phone("0987654321", "1234567890")

# Print updated address book
print(address_book)
