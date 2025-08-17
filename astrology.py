import random

def generate_prediction(name, dob, tob, place):
    # Simple rule-based demo logic
    zodiacs = [
        "You will find success in your career soon.",
        "A new opportunity in relationships may arise.",
        "Focus on your health and inner peace.",
        "Financial growth is on the horizon.",
        "You may face challenges, but you will overcome them."
    ]
    return f"Hello {name}, based on your details ({dob}, {tob}, {place}), " \
           f"your stars suggest: {random.choice(zodiacs)}"

def answer_question(question):
    # Simple keyword-based responses
    if "career" in question.lower():
        return "Your career path looks promising; stay focused."
    elif "love" in question.lower():
        return "A positive shift in relationships may occur soon."
    elif "health" in question.lower():
        return "Take care of your health by balancing work and rest."
    else:
        return "The stars are unclear, but stay positive and hopeful."