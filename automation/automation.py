import re

with open('../potential_contacts.txt') as f:
    content=f.read()
# print(content)




# for emails
emails=re.findall(r'[a-zA-z0-9]+@[a-zA-z]+.[a-zA-Z]+', content)
# another one for emails 

# #  (find phone number based on xxx-yyy-zzzz format )
Phone_numbers=re.findall(r'\.\d{3}-+\d{3}-+\d{4}', content)


#(find phone number based on (xxx) yyy-zzzz format )
Phone_numbers2=re.findall(r'\(\d{3}\)+\d{3}-+\d{4}', content)



#(find phone number based on yyy-zzzz format )
Phone_numbers3=re.findall(r'\s+\d{3}-+\d{4}', content)


# # phone numbers with missing area code should presume 206, all of them are in this format 

Phone_numbers4=re.findall(r'\.\d{3}-+\d{2}-+\d{4}', content)


# # clean phone numbers
Phone_numbers=[item[1::] for item in Phone_numbers ]


# # clean phone numbers , phone numbers with missing area code should presume 206
Phone_numbers4=[item[1::] for item in Phone_numbers4 ]
Phone_numbers4=[item[0:4:]+'206'+item[6::] for item in Phone_numbers4 ]


# all phone numbers should be stored in xxx-yyy-zzzz
Phone_numbers2=[item[1:4:]+'-'+item[5::] for item in Phone_numbers2 ]

total_numbers=Phone_numbers+Phone_numbers2+Phone_numbers3+Phone_numbers4

# # Duplicate entries are not allowed.
total_num_clean=set(total_numbers)
new_total=list(total_num_clean)

# The information should be sorted in ascending order.

new_total.sort()

allphone_num=""""""

for index in range(len(new_total)):
    allphone_num+=new_total[index]
    allphone_num+='\n'


with open('../phone_numbers.txt',mode='w') as file:
    file.write(allphone_num)

# now we will print the emails in their file
unique_emails=set(emails)
all_emails=list(unique_emails)
all_emails.sort()

all_emails_text=""""""

for index in range(len(all_emails)):
    all_emails_text+=all_emails[index]
    all_emails_text+='\n'


with open('../emails.txt',mode='w') as file:
    file.write(all_emails_text)
