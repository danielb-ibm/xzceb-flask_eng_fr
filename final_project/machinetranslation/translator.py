""" Python Module to Translate English to French and Vice Versa"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey=os.environ['apikey']
url=os.environ['url']

authenticator = IAMAuthenticator(apikey)

translator_instance=LanguageTranslatorV3(version='2018-05-01',authenticator= authenticator)
translator_instance.set_service_url(url)

def english_to_french(english_text):
    """ function to translate english to french"""
    translation = translator_instance.translate(text=english_text, model_id='en-fr').get_result()
    french_translation = list(translation.items())[:1]
    french_text = json.dumps(dict(french_translation))[35:-4]
    return french_text

def french_to_english(french_text):
    """ function to translate french to english"""
    translation = translator_instance.translate(text=french_text, model_id='fr-en').get_result()
    english_translation = list(translation.items())[:1]
    english_text = json.dumps(dict(english_translation))[35:-4]
    return english_text.rstrip()

