"""
    Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
        This function initiates the rendering of the main application
        page over the Flask channel
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_emotion_detector():
    """
        This code receives the text from the HTML interface and 
        runs emotion detector over it using emotion_detector()
        function.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    analyze_result = emotion_detector(text_to_analyze)
    if not analyze_result.get('dominant_emotion'):
        return 'Invalid text! Please try again!'
    result = f"""For the given statement, the system response is
        'anger': {analyze_result.get('anger', '')}, 
        'disgust': {analyze_result.get('disgust', '')}, 
        'fear': {analyze_result.get('fear', '')}, 
        'joy': {analyze_result.get('joy', '')} 
        and 'sadness': {analyze_result.get('sadness', '')}. 
        The dominant emotion is {analyze_result.get('dominant_emotion', '')}.
    """
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
