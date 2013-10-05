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
#In the ~/stat157.cfg file, edit docid, that is where the error is
worksheet = spreadsheet.get_worksheet(0)
print docid
data_hw2 = worksheet.get_all_records()
data_hw2_1 = worksheet.get_all_values()
hw2_newlist = []
for row in data_hw2_1 :
   hw2_newlist.append(row[1])
    
testing_exports = open("157_hw2_colimn.txt",  'w')
testing_exports.write(hw2_newlist[1])
testing_exports.close()


