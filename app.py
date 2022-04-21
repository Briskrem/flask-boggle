from boggle import Boggle
import string
import random
from flask import Flask,render_template,session, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'filesystem'

boggle_game = Boggle()

# print(boggle_game.words)


@app.route('/')
def board():
    print('hello')
    board=boggle_game.make_board()
    session['board'] = board
    return render_template('board.html', board=board)


@app.route('/check')
def check():
    print('idkk')
    word = request.args['word']
    result = boggle_game.check_valid_word(session['board'], word)
    return jsonify({'result': result})


@app.route('/storage', methods= ['POST'])
def storage():
    print('storage')
    
    
    session['nplays'] = session.get('nplays', 0) + 1
    
 
    score = request.json['Highscore']
    
    highscore = session.get("highscore", 0)
    session['highscore'] = max(score, highscore)
   
    print(session)
    return jsonify({ 'nplays': session['nplays'], 'Highscore': highscore})


