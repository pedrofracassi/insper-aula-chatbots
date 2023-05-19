import json
from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import chaves

watson_api_key = chaves.WATSON_API_KEY
workspace_id = chaves.WATSON_WORKSPACE_ID

authenticator = IAMAuthenticator(watson_api_key)
assistant = AssistantV1(version='2021-11-27', authenticator=authenticator)
assistant.set_service_url('https://api.us-south.assistant.watson.cloud.ibm.com/instances/9f353bed-9a4a-4aa6-980c-2f4d392785dc')
assistant.set_http_config({'timeout': 100})



response = assistant.message(workspace_id=workspace_id, input={'text': 'Olá'}).get_result()
print(json.dumps(response, indent=2))