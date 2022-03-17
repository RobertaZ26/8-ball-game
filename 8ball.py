#this the compriments section
import random
name = input("what is you name? ")
compriments = ["hy ", "hello ", "ok" , " fuck this ", " fuck you "]
say = random.choice(compriments)
print(say + " " + name + "!!!")
#thid the answer section
quest = input("what you need? ")
answer = ['It is certain.', 'It is decidedly so.', ' Without a doubt.', 'Yes definitely.', 'You may rely on it.', 'As I see it, yes.', ' Most likely.', ' Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', 'Dont count on it.', 'My reply is no.', ' My sources say no.', ' Outlook not so good.', 'Very doubtful.']

tell = random.choice(answer)

print(tell)