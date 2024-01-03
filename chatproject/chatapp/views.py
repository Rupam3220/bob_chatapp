from django.shortcuts import render, redirect
from django.http import HttpResponse
from spacy.lang.en import English

# Chatterbot libraries imported below
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from chatterbot import *



bot = ChatBot('chatbot',read_only = False, 
              logic_adapters = [
                  {
                  
                  'import_path':'chatterbot.logic.BestMatch',
                  'default_response':'I am sorry, but I do not understand. I am still learning.',
                  'maximum_similarity_threshold':0.90
                  
                  }])

list_need_to_train = [
    
    "Are you a robot?",
    "Yes I am a robot, How can I help you?",
]

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)

# list_trainer = ListTrainer(bot)
# list_trainer.train(list_need_to_train)

chatterbotCorpusTrainer.train('chatterbot.corpus.english')

def index(request):
    return render(request,'chatapp/index.html')

def specific(request):
    return HttpResponse("specific Url")

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)