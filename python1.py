
# Student Feedback Sentiment Scoring System

# Predefined positive and negative keywords
positive_keywords = [
    "good", "excellent", "helpful", "clear",
    "interesting", "great", "best", "friendly"
]

negative_keywords = [
    "bad", "poor", "boring", "difficult",
    "unclear", "worst", "slow", "confusing"
]

# Predefined classification thresholds
POSITIVE_THRESHOLD = 2
NEGATIVE_THRESHOLD = -2


def analyze_feedback(feedback):
    """Analyze feedback and calculate its sentiment score."""

    words = feedback.lower().split()

    positive_count = sum(
        1 for word in words
        if word.strip(".,!?;:") in positive_keywords
    )

    negative_count = sum(
        1 for word in words
        if word.strip(".,!?;:") in negative_keywords
    )

    score = positive_count - negative_count

    if score >= POSITIVE_THRESHOLD:
        sentiment = "Positive"
    elif score <= NEGATIVE_THRESHOLD:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return positive_count, negative_count, score, sentiment


# Multiple student feedback sentences
feedback_list = [
    "The teacher is good and helpful.",
    "The classes are boring and confusing.",
    "The explanation is clear and interesting.",
    "The teaching is good but the speed is slow.",
    "The course is okay."
]

# Analyze and display results
print("STUDENT FEEDBACK SENTIMENT ANALYSIS")
print("-" * 70)

for number, feedback in enumerate(feedback_list, start=1):
    positive, negative, score, sentiment = analyze_feedback(feedback)

    print(f"\nFeedback {number}: {feedback}")
    print(f"Positive indicators : {positive}")
    print(f"Negative indicators : {negative}")
    print(f"Sentiment score     : {score}")
    print(f"Classification      : {sentiment}")
