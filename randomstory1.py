import random as r



Sentence_starter = ['About 100 years ago', ' In the 20 BC', 'Once upon a time']
character = [' there lived a king.',' there was a man named Jack.',
            ' there lived a farmer.']
time = [' One day', ' One full-moon night']
story_plot = [' he was passing by',' he was going for a picnic to']
place = [' the mountains', ' the garden']
second_character = [' he saw a man', ' he saw a young lady']
age = [' who seemed to be in late 20s', ' who seemed very old and feeble']
work = [' searching something.', ' digging a well on roadside.']

def main():
    print(r.choice(Sentence_starter)+r.choice(character)+
    r.choice(time)+r.choice(story_plot) +
    r.choice(place)+r.choice(second_character)+
    r.choice(age)+r.choice(work))


main()
