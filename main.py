import os
import pandas
import datetime as dt
import random
import smtplib

today = (dt.datetime.now().month, dt.datetime.now().day)
print("Today:", today)

my_email = os.environ["MY_EMAIL"]
my_password = os.environ["MY_PASSWORD"]

data = pandas.read_csv("birthdays.csv")

new_dict = {
    (row["month"], row["day"]): row
    for (_, row) in data.iterrows()
}

print("Birthdays:", list(new_dict.keys()))

if today in new_dict:
    birthday_person = new_dict[today]
    print("Birthday found:", birthday_person["name"])
    print("Sending to:", birthday_person["email"])

    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as f:
        content = f.read().replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{content}"
        )

    print("Email sent successfully!")

else:
    print("No birthday today.")