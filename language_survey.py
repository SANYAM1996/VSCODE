from test_class import AnonymousSurvey
question = 'what language did you learn first?'
my_survey = AnonymousSurvey(question)
my_survey.show_question()
print('enter q at any time to quit')
while True:
    response = input('language')
    if response == 'q':
        break
    my_survey.store_response(response)
print('thank you everyone for paeticipating in the survey')
my_survey.show_results()
    