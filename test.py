from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        # app.config['TESTING'] = True

    def test_in(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>RECORDS</h1>', html)

    def test_homepage(self):
        

        with self.client:
            response = self.client.get('/')
            # print(response.data)
            self.assertIn('board', session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('nplays'))
            

    def test_valid_word(self):
        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"]]
        response = client.get('/check?word=cat')
        print(response)
        print(dir(response))
        self.assertEqual(response.json['result'], 'ok')
            

    def test_session(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                
                change_session['nplays'] = 1

        res = client.get('/')
        
        
        print(change_session['nplays'])


        self.assertEqual(change_session['nplays'], 1)
   


