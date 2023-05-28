import csv

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