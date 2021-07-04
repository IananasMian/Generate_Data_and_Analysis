from faker import Faker
import csv
import datetime
from faker.providers import internet
import random
import re

def generate_fakedata_1(definition, headers):
    fake = Faker()
    fake1 = Faker('nl_NL')

    with open("generate_fakedata_1.csv", 'wt', errors='ignore') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()
        for i in range(definition):
            
            queing_number = random.randint(0,i)
            full_name = fake1.name()
            temporary_group_id = "group."+ str(queing_number)

            writer.writerow({
                "Temporary_Group_ID" : temporary_group_id,
                "Name": full_name,
                "Birth Date" : fake.date(pattern="%Y-%m-%d"),
                "Phone Number" : fake.phone_number(),
                "Country" : fake1.country(),
                "Email" : fake.email(),
                "Link": fake.url()
            })  
         

if __name__ == '__main__':
    definition = 2000
    headers = ["Temporary_Group_ID", "Name", "Birth Date", "Phone Number", "Country", "Email", "Link"]
    generate_fakedata_1(definition, headers)
    print("CSV has been generated.")
    
    with open('generate_fakedata_1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        print("---------------search for people in certain groups and thier full names ----------------")
        for row in csv_reader:
            #find those people who belong to group.50 or group.100 and thier full names.
            pattern1 = re.compile(r"group\.50,|group\.100,")
            pattern2 = re.compile(r"[a-zA-Z]{3,}\d*@")
            group_target = pattern1.findall(f"{', '.join(row)}")
            if line_count == 0:
                line_count += 1
                print(f"Headers are : {', '.join(row)}")
            elif group_target == []:
                group_target.clear
            else:
                str1 = " "
                strgroup_target = str1.join(group_target)
                full_names = f"{', '.join(row)}".split(',')[1]
                print(strgroup_target + full_names)
            
    print("---------------regular expression on Email ----------------")    
                
                # if strgroup_target in f"{', '.join(row)}":
                # print(f"{', '.join(row)}")
        
                


#--------------------Another method--------------------#
#generate randomly 1 row: data in IT, US or JP.
def generate_fakedata_2():
    fake = Faker(['it_IT', 'en_US', 'ja_JP'])

    data = []
    header = ["Name", "Country", "City"]

    data.append(fake.name())
    data.append(fake.country())  
    data.append(fake.city())          

    with open('generate_fakedata_2.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)

# if __name__ == '__main__':
# generate_fakedata_2()
      
#--------------------Another method--------------------#


