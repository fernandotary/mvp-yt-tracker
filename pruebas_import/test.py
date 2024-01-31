
"""
blob = TextBlob(text)
sentiment_score = blob.sentiment.polarity
print(sentiment_score)
"""

from pysentimiento import EmotionAnalyzer

emotion_analyzer = EmotionAnalyzer(lang="es")


score = emotion_analyzer.predict("Qué gran jugador es Messi")
print(score)
