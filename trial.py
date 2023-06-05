import csv
import sys

# Parses CLI arguments into vars.
fileOne = sys.argv[1]   
fileTwo = sys.argv[2] 
fileOneHeaders = None
fileTwoHeaders = None
ctr = 0

# Opens a file and creates a file for output.
with open(fileOne, 'r') as one, open('output.csv', 'w') as output:
    oneReader = csv.DictReader(one)
    fileOneHeaders = list(next(oneReader))

    # Prints column headers of file one.
    for element in fileOneHeaders:
        ctr += 1
        print(ctr,") ", element)
    
    # Gets first column needed to be compared.
    fileOneRowIndex = int(input("Enter the index of the column you want to compare from file one: "))
    print("\nYou have chosen the", fileOneHeaders[fileOneRowIndex-1], "index.\n")

with open(fileTwo, 'r') as two:
    twoReader = csv.DictReader(two)
    fileTwoHeaders = list(next(twoReader))

    # Prints column headers.
    ctr = 0
    for element in fileTwoHeaders:
        ctr += 1
        print(ctr,") ", element)
    
    # Gets second column needed to be compared.
    fileTwoRowIndex = int(input("Enter the index of the column you want to compare from file two: "))
    print("\nYou have chosen the", fileTwoHeaders[fileTwoRowIndex-1], "index.\n")

    
print("1) Combine both files' columns of matching rows\n2) Output file one's matching rows\n3) Output file two's matching rows")
fileDecision = int(input("Enter the index of your desired function: "))
if(fileDecision == 3):    
    with open(fileTwo, 'r') as two, open('output.csv', 'w') as output:    
        twoReader = csv.DictReader(two)
        writer = csv.DictWriter(output, fieldnames=fileTwoHeaders)
        writer.writeheader()
        for fileTwoElement in twoReader:
            with open(fileOne) as one:
                fileOneReader = csv.DictReader(one)
                for fileOneElement in fileOneReader:
                    if(fileOneElement[fileOneHeaders[fileOneRowIndex-1]].lower() == fileTwoElement[fileTwoHeaders[fileTwoRowIndex-1]].lower()):
                        writer.writerow(fileTwoElement)
elif(fileDecision == 2):    
    with open(fileOne, 'r') as one, open('output.csv', 'w') as output:    
        oneReader = csv.DictReader(one)
        writer = csv.DictWriter(output, fieldnames=fileOneHeaders)
        writer.writeheader()
        for fileOneElement in oneReader:
            with open(fileTwo) as two:
                fileTwoReader = csv.DictReader(two)
                for fileTwoElement in fileTwoReader:
                    if(fileTwoElement[fileTwoHeaders[fileTwoRowIndex-1]].lower() == fileOneElement[fileOneHeaders[fileOneRowIndex-1]].lower()):
                        writer.writerow(fileOneElement)
elif(fileDecision == 1):    
    with open(fileOne, 'r') as one, open('output.csv', 'w',newline='') as output:    
        oneReader = csv.DictReader(one)
        writer = csv.DictWriter(output, fieldnames=fileOneHeaders+fileTwoHeaders)
        writer.writeheader()
        for fileOneElement in oneReader:
            with open(fileTwo) as two:
                fileTwoReader = csv.DictReader(two)
                for fileTwoElement in fileTwoReader:
                    if(fileTwoElement[fileTwoHeaders[fileTwoRowIndex-1]].lower() == fileOneElement[fileOneHeaders[fileOneRowIndex-1]].lower()):
                        writer.writerow({**fileOneElement,**fileTwoElement})

'''
with open('voterNames.csv') as voterNames, open('output.csv', 'w') as output:
    voterReader = csv.DictReader(voterNames)
    fields =  ['ID', 'Last Name', 'First Name', 'Middle Name', 'Coordinator', 'Suffix', 'Street No.', 'Street Name', 'District',
                'DOB', 'Party', 'Status', 'Reg Date', 'Voting Priv Date', 'Phone #', 'Congressional Dist', 'Legislative Dist', 'Email', 
                'Phone', 'Coordinator2', 'Change Affiliation Date', 'Pri - Request Mail ballot', 'Pri - Complete Mail Ballot', 
                'Pri- Vote', 'Gen - Request Mail ballot', 'Gen - Complete Mail Ballot', 'Gen- Vote', 'Category']
    writer = csv.DictWriter(output, fieldnames=fields)
    writer.writeheader()

    for voterName in voterReader:
        with open('arabicNames.csv') as arabNames:
            arabReader = csv.DictReader(arabNames)
            for arabName in arabReader:
                if(voterName['First Name'].lower() == arabName['Name'].lower() or voterName['Last Name'].lower() == arabName['Name'].lower()):
                    writer.writerow({
                        'ID': voterName['ID'], 'Last Name': voterName['Last Name'] , 'First Name': voterName['First Name'],
                        'Middle Name': voterName['Middle Name'], 'Coordinator': voterName['Coordinator'], 'Suffix': voterName['Suffix'],
                        'Street No.': voterName['Street No.'], 'Street Name': voterName['Street Name'], 'District': voterName['District'],
                        'DOB': voterName['DOB'], 'Party': voterName['Party'], 'Status': voterName['Status'], 'Reg Date': voterName['Reg Date'],
                        'Voting Priv Date': voterName['Voting Priv Date'], 'Phone #': voterName['Phone #'], 'Congressional Dist': voterName['Congressional Dist'],
                        'Legislative Dist': voterName['Legislative Dist']
                        })
'''