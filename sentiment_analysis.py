# copilot generated code needs review
# idea: use NLP to conduct sentiment analysis, so patients can voice their opinions, then
# NLP will categorize reviews into categories: good/neutral/bad, happy/angry, etc.  and can then
# give follow-up questions

from transformers import pipeline

# Initialize the sentiment analysis pipeline
sentiment_analysis = pipeline('sentiment-analysis')

def analyze_sentiment(feedback):
    result = sentiment_analysis(feedback)
    sentiment = result['label']
    score = result['score']
    print(f'Sentiment: {sentiment}, Score: {score}')
    return sentiment, score

def categorize_sentiment(sentiment):
    if sentiment == 'POSITIVE':
        return 'good', 'happy'
    elif sentiment == 'NEGATIVE':
        return 'bad', 'angry'
    else:
        return 'neutral', 'neutral'

def follow_up_questions(category):
    questions = {
        'good': "We're glad you had a good experience! Can you tell us what you liked the most?",
        'happy': "It's great to hear you're happy! Is there anything specific that made your experience positive?",
        'bad': "We're sorry to hear that. Can you tell us what went wrong?",
        'angry': "We apologize for any inconvenience. Can you provide more details on what made you upset?",
        'neutral': "Thank you for your feedback. Is there anything we can do to improve your experience?"
    }
    return questions.get(category, "Thank you for your feedback.")

def main():
    feedback = input("Please enter the feedback: ")
    sentiment, score = analyze_sentiment(feedback)
    category, emotion = categorize_sentiment(sentiment)
    follow_up = follow_up_questions(category)
    print(f'Follow-up question: {follow_up}')

if __name__ == '__main__':
    main()
