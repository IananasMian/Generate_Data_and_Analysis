from faker import Faker
import csv
import datetime
from faker.providers import internet
import random

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
                "Link": fake.url()
            })  
         
        print(i)   
if __name__ == '__main__':
    definition = 100
    headers = ["Temporary_Group_ID", "Name", "Birth Date", "Phone Number", "Country", "Link"]
    generate_fakedata_1(definition, headers)
    print("CSV has been generated.")
    
#--------------------Another method--------------------#
#generate randomly 1 row
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

# generate_fakedata_2()


