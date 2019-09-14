
# ---------------------------------------------------------------------
#   PROGRAM SPEC 
#   NAME: AUTO-REPORT
#   DATE OF CREATION: 13 SEPTEMBER 2019
#   PROGRAM TYPE: REPORT GENERATOR 
#   SUMMARY: This program uses pulls the most popular hashtag twitter topic
#            produces a series of complex analysis and writes to html
#            file that gets uploaded automatically to my website 
#           
# ---------------------------------------------------------------------



import datetime
import os
from ipywidgets import IntProgress
from IPython.display import display
from IPython.display import clear_output
import time
import sys
# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the tweepy library
import tweepy
import get_trends
import get_token  

# ---------------------------------------------------------------------
#   AUTHENTICATION 
# ---------------------------------------------------------------------
auth = get_token.auth
api  = get_token.api


# ---------------------------------------------------------------------
#   GRABBING TOPIC  
# ---------------------------------------------------------------------
import random 
TOPIC = get_trends.TOPIC