import random,string

# shakespeare = 'methinks it is a weasel'
shakespeare = 'a'
quoteLen = len(shakespeare)

def generate():
 char = string.ascii_lowercase+' '
 randchars = ''.join(random.choice(char) for _ in range(quoteLen))
 return randchars

def score():
 scorenum = 0
 randchars = generate()
 shake = shakespeare.split()
 randlist = randchars.split()
 for i,j in zip(shake,randlist):
  if i==j:
   scorenum = scorenum+1
 scorecount = (scorenum / quoteLen) * 100
 return scorecount

def main():
 run = 0
 curScore = 0
 while not(curScore==100):
  curScore = score()
  if (curScore != 0):      
    print(run, " = ", curScore)
  run = run + 1;

if __name__ == '__main__':
 main()
