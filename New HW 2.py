import os.path
import ConfigParser
import gspread
home = os.path.expanduser("~")

configfile = os.path.join(home, 'stat157.cfg')
config = ConfigParser.SafeConfigParser()
config.read(configfile)
username = config.get('google', 'username')
password = config.get('google', 'password')
print username
docid = config.get('questionnaire', 'docid')
client = gspread.login(username, password)
spreadsheet = client.open_by_key("0Aj1QXjQixf-SdENDS1FzR1FGNE1kLUk0WGR1SW5peVE")
#In the ~/project1/stat157.cfg file, edit docid, that is where the error is
worksheet = spreadsheet.get_worksheet(0)
print docid

le = "What is your learning style?"
pe = "Where did you gain personal experience?"
columns = [le, pe]
data_for_HW2 = []
for row in worksheet.get_all_records():
    data_for_HW2.append({k:v for k,v in row.iteritems()
                        if k in columns})
                        
HW2 = []
with open("Learning.txt", "w") as f, open("personal.txt", "w") as f2:
    for row in data_for_HW2:
        LE = row[le] +"\n"
        print LE
        PE = row[pe] + "\n"
        print PE 
        f.write(LE.encode("utf-8"))
        f2.write(PE.encode("utf-8"))
