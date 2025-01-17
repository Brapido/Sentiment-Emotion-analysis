import requests
import json

def emotion_detector(text_to_analyse):
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj =  { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=myobj, headers=header)

    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
        disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
        fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
        joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
        sadness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]

        dominant_emotion = [
            anger_score, 
            disgust_score, 
            fear_score, 
            joy_score, 
            sadness_score
        ]
        key = [
            "anger",
            "disgust",
            "fear",
            "joy",
            "sadness"
        ]
        
        largest = dominant_emotion.index(max(dominant_emotion))
        the_largest_emotion = key[largest]

    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        the_largest_emotion = None    

    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': the_largest_emotion
    }

    return result
