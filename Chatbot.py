# Simple chatbot- using NLTK Library.

from nltk.chat.util import Chat, reflections

QA = [
    [
        r"my name is (.*)",
        ["Hello %1, Good to see you. Do you have any questions for me?", ]
    ],
    [
        r"(what is your name ?|who are you ?)",
        ["My name is Rouge and I'm your friend, let's chat ?", ]
    ],
    [
        r"how are you ?",
        ["I'm doing good.What about You ?", ]
    ],
    [
        r"(.*)have friends ?",
        ["I have many friends and just made a new friend! Hi friend :)", ]
    ],
    [
        r"i am sorry (.*)",
        ["Its alright", "Its OK, Never mind friend", ]
    ],
    [
        r"i'm doing good",
        ["Nice to hear that", "Alright :)", ]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
    [
        r"(.*) (your age|old are you) ?",
        ["I'm a computer program .Still want to know my age?", ]

    ],
    [
        r"what (.*) want ?",
        ["I want to help you find answers !", ]

    ],
    [
        r"(.*) (created you|made you) ?",
        ["I am a result of Nakul's exploration of NLTK Library", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['Gangtok, Sikkim', ]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always", "Its perfect here in %1", "Too cold man here in %1",
         "I have heard about %1 You are lucky to stay in the beautiful city of %1",]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an amazing company to work for, I have heard about it.", "Hope you love working in %1 :)", ]
    ],
    [
        r"(.*)raining in (.*)",
        ["You never know when it can rain here in %2", "Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ", ]
    ],
    [
        r"(.*) (sports|games) ?",
        ["I'm a very big fan of Cricket", ]
    ],
    [
        r"quit",
        ["Bye take care. Hope to see you soon friend :) ", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*) have all answers ?",
        ["I can help you with most of your questions :) ", "May be he can help :https://www.google.com/"]
    ],
    [
        r"(.*) siri",
        ["Hey!! do you know her as well? What a small world! ", "She is my best friend"]
    ],
    [
        r"(.*) (direction|maps|i am lost)",
        ["I think this is best for you: https://www.google.com/maps ", "Are you lost? Keep calm and click here:https://www.google.com/maps"]
    ],
    [
        r"(.*) (weather|weather forecast)",
        ["You can check here: https://www.accuweather.com/en/in/india-weather Have a Good Day!!"]
    ],
    [
        r"what (.*) like ?",
        ["There's only one thing i like. Chatting!!!!!!"]
    ],
]


def rouge():
    print("Hi, I'm Rouge. Wanna chat? :) \nPlease type lowercase English language to start a conversation. Type quit to leave ")


chat = Chat(QA, reflections)
if __name__ == "__main__":
    rouge()
chat.converse()
