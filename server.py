from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app=Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    max_emotion = max(result, key=result.get)

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is <b>{max_emotion}</b>."
    )

    return response_text


if __name__ == "__main__":
    app.run()
