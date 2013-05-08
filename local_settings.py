'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
ACCOUNT_SID = "ACf4f5921d13aa32d94b4c9d0cd2d638b9" 
AUTH_TOKEN = "80bf0c9dfa10064ac929ac992eebe5a3"
BSSSPAM_APP_SID = "APa6f3ed362748dd13d971e9345745f20d"
BSS_SPAM_ID = "+18573421656"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
BSSSPAM_APP_SID = os.environ['BSSSPAM_APP_SID']
BSS_SPAM_ID = os.environ['BSS_SPAM_ID']
