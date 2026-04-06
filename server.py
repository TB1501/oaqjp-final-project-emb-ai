"""Flask server for emotion detection application."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app=Flask(__name__)


@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """Analyze text and return detected emotions with dominant emotion."""
    text_to_analyze = request.args.get("textToAnalyze")

    # 🔴 Handle blank input
    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!", 400

    result = emotion_detector(text_to_analyze)

    # 🔴 Handle case where all values are None
    if all(value is None for value in result.values()):
        return "Invalid text! Please try again!", 400

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
    app.run(debug=True)
