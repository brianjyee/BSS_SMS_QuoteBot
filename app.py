from flask import Flask
from flask import request
from flask import url_for
from flask import render_template
from twilio import twiml
from twilio.util import TwilioCapability
from twilio.rest import TwilioRestClient
import os
from random import choice
from local_settings import *

# SONYA_APP_SID
# BSS_SPAM_ID

# Declare and configure application
app = Flask(__name__, static_url_path='/static')
app.config['ACCOUNT_SID'] = ACCOUNT_SID
app.config['AUTH_TOKEN'] = AUTH_TOKEN
app.config['BSSSPAM_APP_SID'] = BSSSPAM_APP_SID
app.config['BSS_SPAM_ID'] = BSS_SPAM_ID


@app.route('/')
def index():
    reason = quotes()
    capability = TwilioCapability(app.config['ACCOUNT_SID'],
        app.config['AUTH_TOKEN'])
    capability.allow_client_outgoing(app.config['BSSSPAM_APP_SID'])
    token = capability.generate()
    return render_template('index.html', token=token, reason=reason)


@app.route('/sms', methods=['POST'])
def sms():
    r = twiml.Response()
    reason = quotes()
    r.sms(reason)
    return str(r)


def quotes():
    reasons = [
            'Our offense is like the Pythagorean Theorem.  There is no answer. - Shaq',
            'I am the number one Ninja and I have killed all the Shoguns in front of me. - Shaq',
            'I\'m like tax. You\'re going to pay one way or the other. - Shaq',
            'Nietzsche was so intelligent and advanced.  And that\'s how I am. I\'m the black, basketball-playing Nietzsche - Shaq',
            'I\'m like toilet paper, Pampers and toothpaste. I\'m definitely proven to be effective. - Shaq',
            'It\'s hard being the NBA\'s sex symbol, but somebody has to do it. - Shaq',
            'I just said to myself, Damn, I\'m a great player. - Shaq',
            'Just like your basic karate movie where the young guys come to the old guys with beards who have them do weird stuff to get to the other side. That\'s who I am, the old guy with a long beard. - Shaq',
            'If you\'re going to hire an assassin, let him go out and kill someone. I can\'t be Shaq taking six or seven shots. - Shaq',
            'I\'m like President Bush. You may not like me, you may not respect me, but you voted me in. - Shaq on his All Star selection']
    return choice(reasons)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='0.0.0.0', port=port)
