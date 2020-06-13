import os
import dialogflow
from google.api_core.exceptions import InvalidArgument

def get_response(msg):
GOOGLE_APPLICATION_CREDENTIALS = 'Google_key.json'

DIALOGFLOW_PROJECT_ID = 'support-tykfrc'
DIALOGFLOW_LANGUAGE_CODE = 'ru'
SESSION_ID = 'gforse'


session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
query_input = dialogflow.types.QueryInput(text=text_input)
try:
    response = session_client.detect_intent(session=session, query_input=query_input)
except InvalidArgument:
    raise

detect = response.query_result.intent_detection_confidence
Final_text = response.query_result.fulfillment_text
Invalid_out = "Дождитесь ответа специалиста."

if detect = 1.0:
    return final_text
else:
    return Invalid_out
