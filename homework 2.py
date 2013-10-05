# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

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
#spreadsheet = client.open_by_key(docid)
#worksheet = spreadsheet.get_worksheet(0)
print docid

# <codecell>


