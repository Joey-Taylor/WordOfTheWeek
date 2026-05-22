import random
import os
from WordList import words
from WordSender import send_word

WEBHOOK_URL = os.environ["SLACK_WEBHOOK_URL"]

word = random.choice(words)
send_word(word, WEBHOOK_URL)
