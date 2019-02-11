from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

#we're now going to create the bot
bot = ChatBot ('Mariya')
#next we set the trainer :)

trainer = ListTrainer(bot)

for knowledge in os.listdir('base'):
	BotMemory = open('base/'+ knowledge, 'r').readlines()
	trainer.train(BotMemory)

#Now we generate routes
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process',methods=['POST']) #this is for us to get user input
def process():
    user_input = request.form['user_input']
    bot_response = bot.get_response(user_input)
    bot_response = str(bot_response)
    #here we save user input to the dataset, unfortunately it slowed down the app
    saveFile = open('base/dataset.txt', 'a')
    saveFile.write(user_input + "\n")
    saveFile.close()

    print("Mariya: "+bot_response)
    return render_template('index.html',user_input=user_input,bot_response=bot_response)

# @app.route('/jokes', methods=['POST','GET'])
# def jokes():
#     user_joke = request.form['user_jokes']
#     saveFile = open('base/dataset.txt', 'a')
#     saveFile.write(user_joke + "\n")
#     saveFile.close()

#     return render_template('jokes.html')

if __name__=='__main__':
	app.run(debug=True,port=5002)