sent = "Hi, there. How are you?"

my_upper = sent.upper()

my_lower = sent.lower()

my_upper1 = "This is a new sentence!"

my_para = "Whereof one cannot speak, thereof one must be silent. Whereof one cannot speak, thereof one must be silent WHEREOF ONE CANNOT SPEAK, THEREOF ONE MUST BE SILENT. whereof one cannot speak, thereof one must be silent."

count_speak = my_para.count("speak")

if(count_speak == 3):
    print("I need to call someone")
elif(count_speak == 6):
    print("I need to do shopping")
else:
    print("I am lazy!!")

my_para.isdigit()

age = "3"

age.isdigit()

firstname = "sumit"
lastname = 3
middlename = 6

firstname + " " + lastname

lastname + middlename

my_name_and_address = ["Mouse","Disney","Mickey","Disney","Disney","Mickey","Disney","Mickey","Mouse","Disney","Mickey","Mouse","Disney","Mickey","Mouse","Disney"]

my_full_name = my_name_and_address[0] + " " + my_name_and_address[1]

my_full_name

listlen = len(my_name_and_address)
#print(listlen)
#for x in range(listlen):  
#    print(my_name_and_address[x])
if(listlen > 20):
    print("This is too much!")
elif(listlen < 15):
    print("This is too easy!")
else:
    print("Never mind!")

my_dict1 = {"first":36, "second":45,"final":100} #these are the number of students
my_dict2 = {"first":7, "second":10,"final":15} #average age of students
my_class = {0:my_dict1, 1:my_dict2}
my_school = {0:my_class, 1:my_class}

my_school[1]["age"]["final"]

len(my_dict1)

for x in range(2):
    for y in range(2):
        print(my_school[x][y]["final"])
    