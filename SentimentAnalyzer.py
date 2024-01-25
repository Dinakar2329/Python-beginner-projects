import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from tkinter import *

# Download the VADER lexicon used by SentimentIntensityAnalyzer
# nltk.download('vader_lexicon')

def analyze_sentiment_and_update_label(text, label):
    # Create a SentimentIntensityAnalyzer object
    sia = SentimentIntensityAnalyzer()

    # Get sentiment compound score
    sentiment_score = sia.polarity_scores(text)['compound']

    # Determine sentiment label
    if sentiment_score >= 0.05:
        sentiment = "positive"
    elif sentiment_score <= -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    # Display results
    result_text = f"Sentiment: {sentiment}\nSentiment Score: {sentiment_score}"
    
    # Update Label2 with the sentiment result
    label.config(text=result_text)

root = Tk()

Label1 = Label(root, text="Enter Text To Analyze", font=10)
text_box = Entry(root, font=10, width=25)
button_1 = Button(root, text="Analyze Sentiment", command=lambda: analyze_sentiment_and_update_label(text_box.get(), Label2))
Label2 = Label(root, text="Result:")

Label1.pack(pady=25)
text_box.pack()
button_1.pack(pady=15)
Label2.pack()

# Center the window on the screen
# root.state('zoomed')
root.eval('tk::PlaceWindow . center')

root.mainloop()
