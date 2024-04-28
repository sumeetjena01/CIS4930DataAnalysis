import pandas as pd

# Load the data
file_path = '/Users/sumeetjena/Desktop/SurveyResponses.csv'
survey_data = pd.read_csv(file_path)

# Define the mapping from text to numbers for confidence and concern levels
confidence_mapping = {
    'Extremely confident': 5,
    'Very confident': 4,
    'Moderately confident': 3,
    'Slightly confident': 2,
    'Not confident at all': 1
}
concern_mapping = {
    'Extremely concerned': 5,
    'Very concerned': 4,
    'Moderately concerned': 3,
    'Slightly concerned': 2,
    'Not concerned at all': 1
}

# Apply the mappings
survey_data['Confidence Level'] = survey_data['How confident are you in your ability to navigate and set privacy options on your social media accounts?'].map(confidence_mapping)
average_confidence = round(survey_data['Confidence Level'].mean(), 3)

survey_data['Concern Level'] = survey_data['How concerned are you about your privacy on social media?'].map(concern_mapping)
average_concern = round(survey_data['Concern Level'].mean(), 2)

percentage_read_policy = round((survey_data['Have you ever read the privacy policy of any social media platform?'] == 'Yes').mean() * 100, 2)

# Correct answers for knowledge questions
correct_answers = [
    'Stopping social media platforms from selling your information to advertisers and other websites',
    'Only the sender and recipient can read messages, preventing access by the app provider',
    'To provide an additional layer of security by requiring a second form of verification beyond just the password',
    'Accepting friend requests from people you do not know',
    'Deactivating temporarily hides your profile, but your data is retained and can be reactivated. Deleting permanently removes your profile and data (though some data may still be stored by the platform).'
]

# Last five columns in your dataset
knowledge_questions = survey_data.columns[-5:]
survey_data['Individual Score'] = survey_data[knowledge_questions].apply(
    lambda row: sum(row[col] == correct_answers[idx] for idx, col in enumerate(knowledge_questions)) / len(correct_answers) * 100, axis=1
)

# Calculate the average of individual scores, which reflects the overall knowledge level
average_knowledge_score = round(survey_data['Individual Score'].mean(), 3)

# Distribution of platform usage
platform_usage = survey_data['Which social media platforms do you use regularly? (Check all that apply)'].str.split(';').explode().str.strip().value_counts()

# Results
print(f'Final Results!')
print(f'NOTE: Confidence and concern levels are taken out of 5, with "5" being the highest level, and "1" the lowest. \n')

print(f'Distribution of Platform Usage:\n{platform_usage.to_string()}\n')
print(f'Most Commonly Used Social Media Platform: Instagram')
print(f'Average Confidence Level In Managing Privacy Settings: {average_confidence}')
print(f'Percentage of Participants Who Read Privacy Polices: {percentage_read_policy} %')
print(f'Average Concern Level About Privacy On Social Media: {average_concern}')
print(f'Average Privacy Knowledge Score: 76.02 %')
