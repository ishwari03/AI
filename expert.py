# Define a simple rule-based Expert System for disease diagnosis

# A dictionary of diseases and their symptoms (in reality, this would be much more complex)
diseases = {
    "Flu": {"fever", "headache", "cough", "body aches"},
    "Cold": {"cough", "sore throat", "runny nose", "sneezing"},
    "COVID-19": {"fever", "cough", "shortness of breath", "fatigue", "loss of taste or smell"},
    "Malaria": {"fever", "chills", "sweating", "headache", "nausea"},
    "Chickenpox": {"fever", "itchy rash", "blisters", "headache"}
}

# Extract all unique symptoms from all diseases, ensuring no duplicates.
all_symptoms = set()
for symptom_set in diseases.values():
    all_symptoms.update(symptom_set)

# Function to ask the user for symptoms and diagnose
def diagnose():
    print("Welcome to the Hospital Expert System.")
    print("Please answer the following questions with 'yes' or 'no'.")

    # Initialize a set to store symptoms entered by the user
    user_symptoms = set()

    # Ask about all known symptoms
    for symptom in all_symptoms:
        answer = input(f"Do you have {symptom}? (yes/no): ").lower()
        if answer == 'yes':
            user_symptoms.add(symptom)

    # Diagnose disease based on symptoms
    matched_diseases = []
    # Check which diseases match user's symptoms
    for disease, disease_symptoms in diseases.items():
        if disease_symptoms.issubset(user_symptoms):  # If the user's symptoms match a disease
            matched_diseases.append(disease)

    if matched_diseases:
        print("\nBased on your symptoms, you may have the following diseases:")
        for disease in matched_diseases:
            print(f"- {disease}")
    else:
        print("\nSorry,  no disease could be confidently diagnosed based on the symptoms.")
        print("It is recommended to consult a doctor for further tests and evaluation.")
# Main function to start the expert system
if __name__ == "__main__":
    diagnose()

# def evaluate_employee():
#     print("🔍 Employee Performance Evaluation System\n")

#     # Input section
#     attendance = input("1. Attendance (Good / Average / Poor): ").strip().lower()
#     project = input("2. Project Completion (On Time / Delayed / Incomplete): ").strip().lower()
#     teamwork = input("3. Teamwork (Excellent / Good / Poor): ").strip().lower()
#     punctuality = input("4. Punctuality (Always on time / Often late): ").strip().lower()

#     # Score system
#     score = 0

#     # Attendance score
#     if attendance == "good":
#         score += 3
#     elif attendance == "average":
#         score += 2
#     elif attendance == "poor":
#         score += 0

#     # Project completion score
#     if project == "on time":
#         score += 3
#     elif project == "delayed":
#         score += 1
#     elif project == "incomplete":
#         score += 0

#     # Teamwork score
#     if teamwork == "excellent":
#         score += 3
#     elif teamwork == "good":
#         score += 2
#     elif teamwork == "poor":
#         score += 0

#     # Punctuality score
#     if punctuality == "always on time":
#         score += 2
#     elif punctuality == "often late":
#         score += 0

#     # Decision logic
#     print("\n📊 Evaluation Result:",score)
    
#     if score >= 9:
#         print("⭐ Performance: Excellent")
#     elif score >= 6:
#         print("✅ Performance: Good")
#     elif score >= 3:
#         print("⚠️ Performance: Needs Improvement")
#     else:
#         print("❌ Performance: Poor")

# # Run the expert system
# evaluate_employee()


# 🧠 General Conceptual Questions
# 1. What is an Expert System?
# Answer:
# An expert system is a computer program that simulates the decision-making ability of a human expert. It uses rules and facts to make deductions and solve problems in a specific domain.

# 2. What type of expert system is this?
# Answer:
# This is a rule-based expert system, which uses if-then logic to infer conclusions (diagnoses) based on user input (symptoms).

# 3. What is the knowledge base in your code?
# Answer:
# The diseases dictionary is the knowledge base, where each disease is associated with a set of symptoms.

# 4. What is inference in expert systems?
# Answer:
# Inference is the process of reasoning based on known facts and rules to draw conclusions. In this system, inference checks if the user's symptoms match the rules for a disease.

# 5. What is the inference technique used in this system?
# Answer:
# This system uses forward chaining — it starts from the given facts (symptoms) and checks which rules (diseases) they satisfy.

# 🧪 Code-Based Questions
# 6. What data structure is used to represent symptoms? Why?
# Answer:
# Sets are used to represent symptoms because they allow efficient membership checking, automatic elimination of duplicates, and easy comparison using set operations like issubset().

# 7. How does the system collect symptoms from the user?
# Answer:
# It iterates over all known symptoms and asks the user if they have each symptom using input().

# 8. What does the issubset() function do in your code?
# Answer:
# It checks whether all symptoms of a disease are present in the user’s input symptoms.

# 9. Why is all_symptoms created separately?
# Answer:
# To avoid asking duplicate symptoms for diseases that share them, and to generate a unique list of all possible symptoms.

# 10. Can your system diagnose multiple diseases at once?
# Answer:
# Yes, if the user's symptoms satisfy more than one disease rule, it lists all matching diseases.

# ⚙️ Functionality Questions
# 11. What will happen if the user has some, but not all, symptoms of a disease?
# Answer:
# That disease will not be diagnosed, as the code only matches diseases where all symptoms are present (issubset).

# 12. How can the system be improved to support partial matches or probabilities?
# Answer:
# By introducing a threshold or similarity score, we could match diseases based on partial symptoms or using machine learning.

# 13. Is the system dynamic? Can it learn new diseases?
# Answer:
# No, it is static. New diseases or symptoms must be manually added to the diseases dictionary.

# 14. How would you handle conflicting diagnoses in a more advanced system?
# Answer:
# Use weights, confidence levels, or consult additional medical data or decision trees to resolve ambiguity.

# 💡 Extension/Thought Questions
# 15. How would you add severity to symptoms in this system?
# Answer:
# By asking follow-up questions to rate each symptom's severity (e.g., mild, moderate, severe) and modifying diagnosis rules to consider this.

# 16. Can this system be integrated into a GUI or web app?
# Answer:
# Yes, the core logic can be integrated into a front-end using Flask (for web) or Tkinter (for GUI).

# 17. What ethical concerns should be considered before deploying such a system?
# Answer:
# It should have a disclaimer that it's not a replacement for professional medical advice, and data privacy must be ensured.
