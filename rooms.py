from CounterManager import CounterManager

counter_manager = CounterManager()

rooms = {
    "start": {
        "text": "*You wake up in an empty, white room. However, your attention \nis drawn to a small computer on the "
                "opposite side of this pristine, white cube.*\n\n1. continue",
        "responses": {
            "1": {
                "next_room": "start2"
            }
        },
        "counter_key": None
    },
    "start2": {
        "text": "*You get closer to this white box of microschemes and wires.\nUntil you see a small line of words on "
                "it*\n\n1. continue",
        "responses": {
            "1": {
                "next_room": "question1"
            }
        },
        "counter_key": None
    },
    "question1": {
        "text": "Hello, are you a human being?\n\n *You think, what is going on?\nBut you have only one choice of what "
                "to do, \nand it is the choice of answering the computer's question* \n\n1. Yes\n\n2. No",
        "responses": {
            "1": {
                "next_room": "human",
                "counter_key": None,
            },
            "2": {
                "next_room": "not_human",
                "counter_key": None,
            }
        },
        "counter_key": None
    },
    "human": {
        "text": "That was a rhetorical question. Of course, you are human.\n\n1. Where am I?\n\n2. Why don't I remember "
                "anything?\n\n3. Why is there only a computer in this room?",
        "responses": {
            "1": {
                "next_room": "questionroom1",
                "counter_key": None
            },
            "2": {
                "next_room": "questionroom2",
                "counter_key": None
            },
            "3": {
                "next_room": "questionroom3",
                "counter_key": None
            }
        },
        "counter_key": None
    },
    "not_human": {
        "text": "Analyzing available information...\nI could not find any evidence of advanced life forms, "
                "distinct from humans, \nin my records of Earth's history.\n\n1. Where am I?\n\n2. Why don't I remember "
                "anything?\n\n3. Why is there only a computer in this room?",
        "responses": {
            "1": {
                "next_room": "questionroom1",
                "counter_key": None
            },
            "2": {
                "next_room": "questionroom2",
                "counter_key": None
            },
            "3": {
                "next_room": "questionroom3",
                "counter_key": None
            }
        },
        "counter_key": None
    },
    "questionroom1": {
        "text": "*Where am I?*\n\n"
                "You exist, and everything else becomes inconsequential.\n\n2. Why don't I remember anything?\n\n3. Why "
                "am I in this room?",
        "responses": {
            "2": {
                "next_room": "questionroom2",
                "counter_key": None
            },
            "3": {
                "next_room": "questionroom3",
                "counter_key": None
            }
        },
        "counter_key": None
    },
    "questionroom2": {
        "text": "*I don't remember anything*\n\n"
                "Perhaps you were intoxicated by alcohol yesterday.\n\n1. Where am I?\n\n3. Why am I in this room?",
        "responses": {
            "1": {
                "next_room": "questionroom1",
                "counter_key": None
            },
            "3": {
                "next_room": "questionroom3",
                "counter_key": None
            }
        },
        "counter_key": None
    },
    "questionroom3": {
        "text": "*Why am I in this room???*\n\nIf you believe in God, I would say that it is your destiny to be here\n"
                "If you !believe in God, I would say that you must be here\n"
                "\n\n1. Where am I?\n\n2. Why don't I remember anything?\n\n3. So, what do I "
                "need to do?\n\n4. I don't want to stay here another second.\n\n5. *Try to hit the computer*",
        "responses": {
            "1": {
                "next_room": "questionroom1",
                "counter_key": None,
            },
            "2": {
                "next_room": "questionroom2",
                "counter_key": None,
            },
            "3": {
                "next_room": "questionroom4",
                "counter_key": None,
            },
            "4": {
                "next_room": "questionroom5",
                "counter_key": None,
            },
            "5": {
                "next_room": "start",
                "counter_key": None
            }
        },
        "counter_key": None
    },
    "questionroom4": {
        "text": "*Hmm... So what do I need to do?*\n\n"
                "You have to answer a question, and you will be free\n\n1. continue",
        "responses": {
            "1": {
                "next_room": "MAIN_QUESTION1",
                "counter_key": None,
            }
        },
        "counter_key": None
    },
    "questionroom5": {
        "text": "*SH*T, I need to find a way out*\n\n"
                "You have to answer a question, and you will be free\n\n1. continue",
        "responses": {
            "1": {
                "next_room": "MAIN_QUESTION1",
                "counter_key": None,
            }
        },
        "counter_key": None
    },
    "MAIN_QUESTION1": {
        "text": "Do you believe that human was created by some force or by someone?\n\n"
                "1. The answer for this question "
                "depends in your beliefs, \nit can be scientific, religious and philosophical answer\n\n"
                "2. Yeah, maybe we have creator "
                "or even we live in simulation in someone's game\n\n"
                "3. *hit THE computer*",
        "responses": {
            "1": {
                "next_room": "MAIN_QUESTION2",
                "counter_key": "human",
            },
            "2": {
                "next_room": "MAIN_QUESTION2",
                "counter_key": "non_human",
            },
            "3": {
                "next_room": "MAIN_QUESTION2",
                "counter_key": "deviator",
            }
        },
        "counter_key": None
    },
    "MAIN_QUESTION2": {
        "text": "CORRECT!!!\nIs it possible for human to create Artificial Intelligence\nthat will be equal to humans "
                "in self-consciousness and self-identity?\n\n"
                "1. Yes, If we can fully understand and replicate human's brain, we will create such a powerful AI\n\n"
                "2. No, We can't give AI a soul or even feelings and emotions, so they never be equal to humans\n\n"
                "3. *HIT the computer*",
        "responses": {
            "1": {
                "next_room": "MAIN_QUESTION3",
                "counter_key": "non_human",
            },
            "2": {
                "next_room": "MAIN_QUESTION3",
                "counter_key": "human",
            },
            "3": {
                "next_room": "MAIN_QUESTION3",
                "counter_key": "deviator",
            }
        },
        "counter_key": None
    },
    "MAIN_QUESTION3": {
        "text": "CORRECT!!!\nHow can you distinguish whether you're chatting with a human or an AI?\n\n"
                "1. You can easily understand due to human body language, emotions, and posture\n\n"
                "2. If AI is well designed and were made to fully imitate human's behavior, \nit will be impossible "
                "to distinguish\n\n"
                "3. *hit the COMPUTER*",
        "responses": {
            "1": {
                "next_room": "MAIN_QUESTION4",
                "counter_key": "human",
            },
            "2": {
                "next_room": "MAIN_QUESTION4",
                "counter_key": "non_human",
            },
            "3": {
                "next_room": "MAIN_QUESTION4",
                "counter_key": "deviator",
            }
        },
        "counter_key": None
    },
    "MAIN_QUESTION4": {
        "text": "CORRECT!\nHow can you know if you are a human or AI?\n\n"
                "1. It's impossible to know, I will be a human until we discover our creator or \nprove that we weren't "
                "created by someone or something\n\n"
                "2. I just feel that I'm human, I felt it always. I had memories of my life, I had dreams.\n "
                "I had everything before waking up this room. I felt happiness, sadness, I loved and believed.\n I have "
                "soul and I can say that I'm 100% human!\n\n"
                "3. *HIT THE COMPUTER",
        "responses": {
            "1": {
                "next_room": "end_game",
                "counter_key": "non_human",
            },
            "2": {
                "next_room": "end_game",
                "counter_key": "human",
            },
            "3": {
                "next_room": "end_game",
                "counter_key": "deviator",
            }
        },
        "counter_key": None
    },
    "end_game": {
        "text": "{ending_text}",
        "dynamic_text": {
            "human_ending": "Congratulations model 280932124!!!\nYou have passed test for humanity.\nSoon you will be send to one of the Company's market for further sale.\n"
                            "Don't afraid you won't remember anything that happened in this room.\n"
                            "I wish you will have happy human life.\n\n\n\n*Suddenly you started fallen asleep and final thought that you have\nin your mind is <I'm not a human?>*",
            "deviator_ending": "*The computer finally broke up and your hear some sort of explosion... \n"
                               "Last thing that you hear is \n<Another model has deviator error, it will be send to the reassembly and mind-software reboot>*",
            "non_human_ending": "HMMM... Model 280932124. \nYou will be destroyed due to virus of self-identity, that had been widely spread in new models.\nGoodbye! It was nice to test you!\n*You hear the sound of a blow on your head, next is darkness, just darkness*\n\n\n"
                                "*You wake up in wasteland of human bodies with similar appearance as yours.\nYou can't move your left arm and right leg, because they are just have been cut off\n\n\n\nTo be continue......."
        }
    }
}