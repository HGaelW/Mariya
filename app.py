from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

#we're now going to create the bot
bot = ChatBot ('Mariya')
#next we set the trainer :)

trainer = ListTrainer(bot)

for knowledeg in os.listdir('base'):
	BotMemory = open('base/'+ knowledeg, 'r').readlines()
	trainer.train(BotMemory)

#Now we generate routes
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process',methods=['POST']) #this is for us to get user input
def process():
	user_input=request.form['user_input']
	bot_response=bot.get_response(user_input)
	bot_response=str(bot_response)
	print("Mariya: "+bot_response)
	return render_template('index.html',user_input=user_input,
		bot_response=bot_response
		)

if __name__=='__main__':
	app.run(debug=True,port=5002)