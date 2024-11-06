'''This app is to measure sentiment from string inputs'''
# Import Flask, render_template, request from the flask pramework package :
from flask import Flask, render_template, request

# Import the sentiment_analyzer function from the package created:
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

#Initiate the flask app :
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = sentiment_analyzer(text_to_analyze)

    # Extract the label and score from the response
    label = response['label']
    score = response['score']

# Check if the label is None, indicating an error or invalid input
    if label is None:
        return "Invalid input! Try again."
    # Return a formatted string with the sentiment label and score
    return (f"The given text has been identified"
           f" as {label.split('_')[1]} with a score of {score}.")

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8080)