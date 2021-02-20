import smtplib
import datetime as dt
import random
import pandas as pd

my_email = ""
my_password = ''
LETTERS = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

birthdays_df = pd.read_csv("birthdays.csv")
birthdays_df["date"] = pd.to_datetime(birthdays_df[['year', 'month', 'day']])

now = dt.datetime.now()
day = now.day
month = now.month

todays_bdays = birthdays_df[(birthdays_df.day == day) & (birthdays_df.month == month)]

with open("quotes.txt", mode="r") as data:
    quotes = data.readlines()

for index, person in todays_bdays.iterrows():
    sel_letter = random.choice(LETTERS)
    with open(f"letter_templates/{sel_letter}", mode="r", encoding="UTF-8") as data:
        letter = data.read()
    letter = letter.replace("[NAME]", person["name"])

    todays_quote = random.choice(quotes)

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.command_encoding = 'utf-8'
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=person["email"],
                        msg=f"Subject:HAPPY BIRTHDAY!!!\n\n{todays_quote}\n\n{letter}")
    connection.close()
