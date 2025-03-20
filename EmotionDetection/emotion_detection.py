import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    JSON_DATA = { 
        "raw_document": { 
            "text": text_to_analyze 
        }
    }
    res = requests.post(url=URL, json=JSON_DATA, headers=HEADERS)
    if res.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
        }
    # Convert text response to json
    res_json = json.loads(res.text)
    emotions = res_json.get('emotionPredictions')[0].get('emotion')
    # Find highest score
    max_score = max(emotions.values())
    # Find Dominant Emotion
    for name, score in emotions.items():
        if score == max_score:
            dominant_emotion = name
            break
    emotions['dominant_emotion'] = dominant_emotion
    return emotions