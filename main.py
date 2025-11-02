from datetime import datetime
import random
import pandas as pd
import smtplib

MY_EMAIL = "tanishasinghamrita2003@gmail.com"
MY_PASSWORD = "pligwdmfahxoehbs"

# 1. Get today's date
today = datetime.now()
today_tuple = (today.month, today.day)

# 2. Read the CSV file
data = pd.read_csv("birthdays.csv")

# 3. Create a dictionary with (month, day) as key
birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}

# 4. Check if today matches any birthday
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    # 5. Pick a random letter template
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        # IMPORTANT: store the replaced string back into contents
        contents = contents.replace("[NAME]", birthday_person["name"])

    # 6. Send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )

    print("🎉 Birthday email sent successfully!")
else:
    print("No birthdays today.")


