import pandas
import datetime as dt
import random
import smtplib

today =(dt.datetime.now().month, dt.datetime.now().day)

my_email = "dabanafash@gmail.com"
my_password = "vqiqgjoaeintsroh"


data=pandas.read_csv("birthdays.csv")

new_dit ={(data_row["month"],data_row["day"]): data_row for (index, data_row)in data.iterrows()}

if today in new_dit:
    birthday_Person = new_dit[today]
    fill_path= f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(fill_path) as f:
        content = f.read()
        content= content.replace("[NAME]",birthday_Person["name"])



    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_Person["email"],
                            msg=f"Subject: Happy Birthday!\n\n{content}")



