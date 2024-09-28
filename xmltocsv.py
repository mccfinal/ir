import csv
import xmltodict

with open("sample.xml", 'r') as file:
    filedata = file.read()

data_dict = xmltodict.parse(filedata)
employee_data_list = [dict(x) for x in data_dict["employees"]["employee"]]
HEADERS = ['name', 'role' ,'age']
rows = []

for employee in employee_data_list:
    name = employee["name"]
    role= employee["role"]
    age = employee["age"]
    rows.append([name,role,age])

with open('employee_data.csv', 'w',newline="") as f:
    write = csv.writer(f)
    write.writerow(HEADERS)
    write.writerows(rows)


<employees>
   <employee>
      <name>Carolina</name>
        <role>Data Engineer</role>
        <age>24</age>
    </employee>
    <employee>
      <name>Roosaka</name>
        <role>Data Scientist</role>
        <age>27</age>
    </employee>
    <employee>
      <name>Kumar</name>
        <role>Machine Learning Engineer</role>
        <age>31</age>
    </employee>
    <employee>
      <name>Vijay</name>
        <role>Devops Engineer</role>
        <age>26</age>
    </employee>
</employees>
