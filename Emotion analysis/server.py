''' This app takes not of the emotion regarding the input string '''
from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_analyzer():
    '''This function takes a string input and displays emotion classification'''

    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear},"
        f" 'joy': {joy} and 'sadness': {sadness}. " 
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    '''This function renders index.html'''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5001)
