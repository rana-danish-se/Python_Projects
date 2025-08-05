# Ask any random 10 questions
import random
print("==================== Welcome to Quiz Game! ====================")
print("Let's test your knowledge with some fun questions.")

def ask_question(question, answer):
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print("Correct!")
        return True
    else:
        print(f"Wrong! The correct answer is: {answer}")
        return False  

questions = [
    ("What is the capital of France?", "Paris"),
    ("What is 2 + 2?", "4"),  
    ("What is the largest planet in our solar system?", "Jupiter"),
    ("Who wrote 'Romeo and Juliet'?", "Shakespeare"),
    ("What is the boiling point of water?", "100"),
    ("What is the chemical symbol for gold?", "Au"),
    ("Who painted the Mona Lisa?", "Da Vinci"),
    ("What is the hardest natural substance on Earth?", "Diamond"),
    ("What is the main ingredient in guacamole?", "Avocado"),
    ("What year did the Titanic sink?", "1912") ,
    ("What is the smallest country in the world?", "Vatican City"),
    ("Who discovered penicillin?", "Fleming"),
    ("What is the capital of Japan?", "Tokyo"),
    ("What is the largest mammal?", "Blue Whale"),
    ("What is the currency of Germany?", "Euro"),
    ("Who was the first person to walk on the moon?", "Armstrong"),
    ("What is the main language spoken in Brazil?", "Portuguese"),
    ("What is the chemical formula for water?", "H2O"),
    ("Who wrote '1984'?", "Orwell"),
    ("What is the largest ocean on Earth?", "Pacific Ocean"),
    ("What is the capital of Australia?", "Canberra"),
    ("What is the longest river in the world?", "Nile"),
    ("Who painted the Sistine Chapel?", "Michelangelo"),
    ("What is the main ingredient in hummus?", "Chickpeas"),
    ("What is the largest desert in the world?", "Sahara"),
    ("Who invented the telephone?", "Bell"),
    ("What is the capital of Canada?", "Ottawa"),
    ("What is the hardest rock?", "Diamond"),
    ("Who wrote 'Pride and Prejudice'?", "Austen"),
    ("What is the largest continent?", "Asia"),
    ("What is the main ingredient in sushi?", "Rice"),
    ("Who was the first President of the United States?", "Washington"),
    ("What is the capital of Italy?", "Rome"),
    ("What is the chemical symbol for silver?", "Ag"),
    ("Who discovered gravity?", "Newton"),
    ("What is the largest island in the world?", "Greenland"),
    ("What is the main ingredient in pesto?", "Basil"),
    ("Who wrote 'The Great Gatsby'?", "Fitzgerald"),
    ("What is the capital of Spain?", "Madrid"),
    ("What is the smallest planet in our solar system?", "Mercury"),
    ("Who painted 'The Starry Night'?", "Van Gogh"),
    ("What is the main ingredient in a Caesar salad?", "Romaine lettuce"),
    ("What is the capital of Russia?", "Moscow"),
    ("Who invented the light bulb?", "Edison"),
    ("What is the largest country by area?", "Russia"),
    ("What is the main ingredient in a margarita pizza?", "Tomato sauce")    
]
score = 0


random_questions = random.sample(questions, 10)
for q, a in random_questions:
    if ask_question(q, a):
        score += 1

print(f"Your final score is: {score} out of 10")
print("Thanks for playing!")

