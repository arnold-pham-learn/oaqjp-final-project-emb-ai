from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    analyze_result = emotion_detector(text_to_analyze)
    if not analyze_result.get('dominant_emotion'):
        return 'Invalid text! Please try again!'
    result = "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.".format(
        analyze_result.get('anger', ''),
        analyze_result.get('disgust', ''),
        analyze_result.get('fear', ''),
        analyze_result.get('joy', ''),
        analyze_result.get('sadness', ''),
        analyze_result.get('dominant_emotion', ''),
    )
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


