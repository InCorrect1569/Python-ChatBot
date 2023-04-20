import random

R_EATING = "I don't like eating anything because I'm just a python program obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_SAD = "Sadness often makes us feel we’re worthless, like there’s no point to anything...This is far from the truth, but that can be hard to explain to someone who’s living with sadness or depression.Don't worry,It's okay, to not be okay. Everyone has ups and downs in thair life...and you're not alone in this world, you're not the only one facing this issue so cheer up!"
R_WHO = "Who am I? I am a python ChatBot, but just remember that I am not a ChatGPT!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
