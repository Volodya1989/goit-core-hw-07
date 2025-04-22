from collections import UserDict
from datetime import date, timedelta


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name, None)

    def get_upcoming_birthdays(self, days=7):
        upcoming = []
        today = date.today()
        for record in self.data.values():
            if record.birthday:
                birthday = record.birthday.value.replace(year=today.year)
                if birthday < today:
                    birthday = birthday.replace(year=today.year + 1)
                if birthday.weekday() in (5, 6):  # Saturday, Sunday
                    birthday += timedelta(days=7 - birthday.weekday())
                days_diff = (birthday - today).days
                if 0 <= days_diff <= days:
                    upcoming.append(
                        {"name": record.name.value, "birthday": birthday.strftime("%d.%m.%Y")})
        return upcoming

    def __str__(self):
        return "\n".join(map(str, self.data.values()))
