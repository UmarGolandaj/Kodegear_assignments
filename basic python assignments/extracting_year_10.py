import datetime
birthday = input("insert the date (in DD/MM/YYYY) :")
birthdate = datetime.datetime.strptime(birthday, "%d/%m/%Y").date()
print("Year : "+birthdate.strftime('%Y'))
