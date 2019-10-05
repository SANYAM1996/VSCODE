import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    '''test for the anonymous survey'''
    def test_store_single_response(self):
        '''test that single response is stored'''
        question = "what language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('engish')
        self.assertIn('english',my_survey.response)
unittest.main()