print ("\nWelcome to UNITEN Putrajaya's Rental System!\n")
username = input("Please enter your name: ")
print("")

def facilities ():
    print("Hello",username,"! It seems like you want to book one of our facilities. Take a look at the list below.\n")
    for item in ["1. PBL Classroom (30 Pax)","2. Meeting Room (60 Pax)","3. Workstation Computer Lab ITMS (30 Pax)","4. Swimming Pool"]:
        print (item)

def faci_option(x):
    if x == "1":
        print("\nYou have selected our PBL Classroom.")
    elif x == "2":
        print("\nYou have selected our Meeting Room.")
    elif x == "3":
        print("\nYou have selected our Workstation Computer Lab ITMS.")
    elif x == "4":
        print("You have selected our Swimming Pool.")
    else:
        x = input("\nInvalid input.\nPlease re-enter the relevant number to select a facility: ")
        faci_option(x)

def answer(status):
    if status == "Yes" or status == "yes" or status == "YES":
        print("\nOh,", username,"you are one of our students / staffs!\n")
    elif status == "No" or status == "NO" or status == "no":
        print("\nOkay,",username,"our system will now recognize you as a public guest.\n")
    else:
        status = input("\nInvalid input.\nPlease appropriately answer the question by typing in either Yes or No: ")
        answer(status)

def choose_day(day):
    if day == "Monday" or day == "monday" or day == "MONDAY" or day == "Tuesday" or day == "tuesday" or day == "TUESDAY" or day =="Wednesday" or day == "wednesday" or day == "WEDNESDAY" or day == "THURSDAY" or day == "Thursday" or day == "thursday" or day == "FRIDAY" or day == "Friday" or day == "friday":
        print ("\nHey,", username, "you chose", day, "to book our facility.")
    elif day == "SATURDAY" or day == "saturday" or day == "Saturday" or day == "SUNDAY" or day =="sunday" or day == "Sunday":
        print("\nHey,", username, "you chose", day, " to book our facility.")
    else: 
        day = input("\nSorry, the system is unable to detect your input. Please re-enter the relevant day: ")
        choose_day(day)
    
def hours_error (hours):
    if hours > 12:
        hours = int(input("\nSorry, your input is beyond the limit of our renting duration. You can only book our facility for 12 hours, at most. Re-enter hours : "))
        hours_error(hours)
    elif hours <= 0:
        hours = int(input("\nSorry, your input is beyond the limit of our renting duration. You can only book our facility for 12 hours, at most. Re-enter hours : "))
        hours_error(hours)

def balance_check(balance):
    if balance > 0 :
        print("You still have to pay RM", balance)
        user_payment = int(input("\nPlease re-enter your payment amount : RM "))
        balance = balance - user_payment
        balance_check(balance)
    elif balance == 0:
        print("\nWe are processing your transmission. Please wait for a while...")
        input("\nPress Enter to continue..")
        print("\nTransmission's done! Thank you so much for using UNITEN Putrajaya's Rental System,",username,"!\n\nWe hope that our services satisfy you. Have a nice day!\n")
    elif balance < 0:
        print("Sorry, you have exceeded the quota.\nYou still have to pay: RM ",  total_amount)
        user_payment = int(input("\nPlease re-enter your payment amount : RM "))
        balance = total_amount - user_payment
        balance_check(balance)
        
        
        
            
            



facilities()

choose_faci = input("\nPlease insert the relevant number to select a facility that you want to book: ")

faci_option(choose_faci)

status = input("\nAre you a UNITEN student / staff? You can only type in either Yes or No: ")

answer(status)

print("Now you have to choose the day that you want the facility to be reserved.\nWe have two packages which are Weekdays (Monday to Friday) and Weekends (Saturday and Sunday).")

day = input("\nTherefore, on which day would you like the facility to be booked? Mention here : ")

choose_day(day)

hours = int(input("\nHow many hours would you like to book (Max duration is 12 hours and only numbers will be accepted) : "))
while hours > 12:
    hours = int(input("\nSorry, your input is beyond our renting duration. You can only book our facilities for 12 hours, at most. Re-enter hours: "))
while hours <= 0:
    hours = int(input("\nSorry, your input is invalid. Make sure that you don't key-in 0 or any negative integers. Re-enter hours: "))

if choose_faci == "1":
    choose_faci = "PBL Classroom"
    if status == "Yes" or status == "yes" or status == "YES":
        uniten_price = 100
        if day =="Monday" or day == "monday" or day == "MONDAY" or day == "Tuesday" or day == "tuesday" or day == "TUESDAY" or day == "WEDNESDAY" or day == "wednesday" or day == "Wednesday" or day == "Thursday" or day == "THURSDAY" or day == "thursday" or day == "Friday" or day == "FRIDAY" or day == "friday":
            uniten_price = uniten_price + 0
            total_amount = uniten_price * hours
            print("\nRENTAL DETAILS\n\nFacility: ", choose_faci,"\nUNITEN staff/student: ", status,"\nDay:", day,"\nDuration:", hours, "hours\nTotal amount of payment: RM ", total_amount)
            user_payment = int(input("\nHow much do you want pay? RM "))
            balance = total_amount - user_payment
            balance_check(balance)
        elif day == "Saturday" or day == "saturday" or day == "SATURDAY" or day == "Sunday" or day == "sunday" or day == "SUNDAY":
            uniten_price = uniten_price + 50
            total_amount = uniten_price * hours
            print("Facility: ", choose_faci,"\nUNITEN staff/student: ", status,"\nDay:", day,"\nDuration:", hours, "hours\nTotal amount of payment: RM ", total_amount)
            user_payment = int(input("\nHow much do you want pay? RM "))
            balance = total_amount - user_payment
            balance_check(balance)
    if status == "NO" or status == "no" or status == "No":
         public_price = 150
         if day =="Monday" or day == "monday" or day == "MONDAY" or day == "Tuesday" or day == "tuesday" or day == "TUESDAY" or day == "WEDNESDAY" or day == "wednesday" or day == "Wednesday" or day == "Thursday" or day == "THURSDAY" or day == "thursday" or day == "Friday" or day == "FRIDAY" or day == "friday":
             public_price = public_price + 0
             total_amount = public_price * hours
             print("Facility: ", choose_faci,"\nUNITEN staff/student: ", status,"\nDay:", day,"\nDuration:", hours, "hours\nTotal amount of payment: RM ", total_amount)
             user_payment = int(input("\nHow much do you want pay? RM "))
             balance = total_amount - user_payment
             balance_check(balance)
         elif day == "Saturday" or day == "saturday" or day == "SATURDAY" or day == "SUNDAY" or day == "Sunday" or day == "sunday":
             public_price = public_price + 50
             total_amount = public_price * hours
             print("Facility: ", choose_faci,"\nUNITEN staff/student: ", status,"\nDay:", day,"\nDuration:", hours, "hours\nTotal amount of payment: RM ", total_amount)
             user_payment = int(input("\nHow much do you want pay? RM "))
             balance = total_amount - user_payment
             balance_check(balance)
elif choose_faci == "2":
    choose_faci = "Meeting Room"
    if status == "Yes" or status == "yes" or status == "YES":
        uniten_price = 100
        if day =="Monday" or day == "monday" or day == "MONDAY" or day == "Tuesday" or day == "tuesday" or day == "TUESDAY" or day == "WEDNESDAY" or day == "wednesday" or day == "Wednesday" or day == "Thursday" or day == "THURSDAY" or day == "thursday" or day == "Friday" or day == "FRIDAY" or day == "friday":
            uniten_price = uniten_price + 0
            total_amount = uniten_price * hours
            print("\nRENTAL DETAILS\n\nFacility: ", choose_faci,"\nUNITEN staff/student: ", status,"\nDay:", day,"\nDuration:", hours, "hours\nTotal amount of payment: RM ", total_amount)
            user_payment = int(input("\nHow much do you want pay? RM "))
            balance = total_amount - user_payment
            balance_check(balance)
        elif day == "Saturday" or day == "saturday" or day == "SATURDAY" or day == "Sunday" or day == "sunday" or day == "SUNDAY":
            uniten_price = uniten_price + 50
            total_amount = uniten_price * hours
            print("Facility: ", choose_faci,"\nUNITEN staff/student: ", status,"\nDay:", day,"\nDuration:", hours, "hours\nTotal amount of payment: RM ", total_amount)
            user_payment = int(input("\nHow much do you want pay? RM "))
            balance = total_amount - user_payment
            balance_check(balance)
    if status == "NO" or status == "no" or status == "No":
         public_price = 150
         if day =="Monday" or day == "monday" or day == "MONDAY" or day == "Tuesday" or day == "tuesday" or day == "TUESDAY" or day == "WEDNESDAY" or day == "wednesday" or day == "Wednesday" or day == "Thursday" or day == "THURSDAY" or day == "thursday" or day == "Friday" or day == "FRIDAY" or day == "friday":
             public_price = public_price + 0
             total_amount = public_price * hours
             print("\nRENTAL DETAILS\n\nFacility: ", choose_faci,"\nUNITEN staff/student: ", status,"\nDay:", day,"\nDuration:", hours, "hours\nTotal amount of payment: RM ", total_amount)
             user_payment = int(input("\nHow much do you want pay? RM "))
             balance = total_amount - user_payment
             balance_check(balance)
         elif day == "Saturday" or day == "saturday" or day == "SATURDAY" or day == "SUNDAY" or day == "Sunday" or day == "sunday":
             public_price = public_price + 50
             total_amount = public_price * hours
             print("Facility: ", choose_faci,"\nUNITEN staff/student: ", status,"\nDay:", day,"\nDuration:", hours, "hours\nTotal amount of payment: RM ", total_amount)
             user_payment = int(input("\nHow much do you want pay? RM "))
             balance = total_amount - user_payment
             balance_check(balance)
elif choose_faci == "3":
    choose_faci = "Workstation Computer Lab"
    if status == "Yes" or status == "YES" or status == "yes":
        uniten_price = 200
        if day =="Monday" or day == "monday" or day == "MONDAY" or day == "Tuesday" or day == "tuesday" or day == "TUESDAY" or day == "WEDNESDAY" or day == "wednesday" or day == "Wednesday" or day == "Thursday" or day == "THURSDAY" or day == "thursday" or day == "Friday" or day == "FRIDAY" or day == "friday":
            uniten_price = uniten_price + 0
            total_amount = uniten_price * hours
            print("\nRENTAL DETAILS\n\nFacility: ", choose_faci,"\nUNITEN staff/student: ", status,"\nDay:", day,"\nDuration:", hours, "hours\nTotal amount of payment: RM ", total_amount)
            user_payment = int(input("\nHow much do you want pay? RM "))
            balance = total_amount - user_payment
            balance_check(balance)
        elif day == "Saturday" or day == "saturday" or day == "SATURDAY" or day == "Sunday" or day == "sunday" or day == "SUNDAY":
            uniten_price = uniten_price + 50
            total_amount = uniten_price * hours
            print("\nRENTAL DETAILS\n\nFacility: ", choose_faci,"\nUNITEN staff/student: ", status,"\nDay:", day,"\nDuration:", hours, "hours\nTotal amount of payment: RM ", total_amount)
            user_payment = int(input("\nHow much do you want pay? RM "))
            balance = total_amount - user_payment
            balance_check(balance)
    if status == "NO" or status == "no" or status == "No":
         public_price = 250
         if day =="Monday" or day == "monday" or day == "MONDAY" or day == "Tuesday" or day == "tuesday" or day == "TUESDAY" or day == "WEDNESDAY" or day == "wednesday" or day == "Wednesday" or day == "Thursday" or day == "THURSDAY" or day == "thursday" or day == "Friday" or day == "FRIDAY" or day == "friday":
             public_price = public_price + 0
             total_amount = public_price * hours
             print("\nRENTAL DETAILS\n\nFacility: ", choose_faci,"\nUNITEN staff/student: ", status,"\nDay:", day,"\nDuration:", hours, "hours\nTotal amount of payment: RM ", total_amount)
             user_payment = int(input("\nHow much do you want pay? RM "))
             balance = total_amount - user_payment
             balance_check(balance)
         elif day == "Saturday" or day == "saturday" or day == "SATURDAY" or day == "SUNDAY" or day == "Sunday" or day == "sunday":
             public_price = public_price + 50
             total_amount = public_price * hours
             print("\nRENTAL DETAILS\n\nFacility: ", choose_faci,"\nUNITEN staff/student: ", status,"\nDay:", day,"\nDuration:", hours, "hours\nTotal amount of payment: RM ", total_amount)
             user_payment = int(input("\nHow much do you want pay? RM "))
             balance = total_amount - user_payment
             balance_check(balance)
elif choose_faci == "4":
    choose_faci = "Swimming Pool"
    if status == "Yes" or status == "YES" or status == "yes":
        uniten_price = 30
        if day =="Monday" or day == "monday" or day == "MONDAY" or day == "Tuesday" or day == "tuesday" or day == "TUESDAY" or day == "WEDNESDAY" or day == "wednesday" or day == "Wednesday" or day == "Thursday" or day == "THURSDAY" or day == "thursday" or day == "Friday" or day == "FRIDAY" or day == "friday":
            uniten_price = uniten_price + 0
            total_amount = uniten_price * hours
            print("\nRENTAL DETAILS\n\nFacility: ", choose_faci,"\nUNITEN staff/student: ", status,"\nDay:", day,"\nDuration:", hours, "hours\nTotal amount of payment: RM ", total_amount)
            user_payment = int(input("\nHow much do you want pay? RM "))
            balance = total_amount - user_payment
            balance_check(balance)
        elif day == "Saturday" or day == "saturday" or day == "SATURDAY" or day == "Sunday" or day == "sunday" or day == "SUNDAY":
            uniten_price = uniten_price + 5
            total_amount = uniten_price * hours
            print("\nRENTAL DETAILS\n\nFacility: ", choose_faci,"\nUNITEN staff/student: ", status,"\nDay:", day,"\nDuration:", hours, "hours\nTotal amount of payment: RM ", total_amount)
            user_payment = int(input("\nHow much do you want pay? RM "))
            balance = total_amount - user_payment
            balance_check(balance)
    if status == "NO" or status == "no" or status == "No":
         public_price = 60
         if day =="Monday" or day == "monday" or day == "MONDAY" or day == "Tuesday" or day == "tuesday" or day == "TUESDAY" or day == "WEDNESDAY" or day == "wednesday" or day == "Wednesday" or day == "Thursday" or day == "THURSDAY" or day == "thursday" or day == "Friday" or day == "FRIDAY" or day == "friday":
             public_price = public_price + 0
             total_amount = public_price * hours
             print("\nRENTAL DETAILS\n\nFacility: ", choose_faci,"\nUNITEN staff/student: ", status,"\nDay:", day,"\nDuration:", hours, "hours\nTotal amount of payment: RM ", total_amount)
             user_payment = int(input("\nHow much do you want pay? RM "))
             balance = total_amount - user_payment
             balance_check(balance)
         elif day == "Saturday" or day == "saturday" or day == "SATURDAY" or day == "SUNDAY" or day == "Sunday" or day == "sunday":
             public_price = public_price + 5
             total_amount = public_price * hours
             print("\nRENTAL DETAILS\n\nFacility: ", choose_faci,"\nUNITEN staff/student: ", status,"\nDay:", day,"\nDuration:", hours, "hours\nTotal amount of payment: RM ", total_amount)
             user_payment = int(input("\nHow much do you want pay? RM "))
             balance = total_amount - user_payment
             balance_check(balance)
   
