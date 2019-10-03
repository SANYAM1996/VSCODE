# making a program with functions to help administrative for attending anonymous survey
class AnonymousSurvey():
    '''this function collect anonymous question to peform a survey'''
    def __init__(self,question):
        self.question = question
        self.response = []

    def show_question(self):
        '''show the survey question'''
        print(question)

    def store_response(self,new_response):
        '''store a single response to the survey'''
        self.response.append(new_response)

    def showresult(self):
        '''show all the responses that have been given'''
        print('survey results')
        for response in responses:
            print('-' + response)
