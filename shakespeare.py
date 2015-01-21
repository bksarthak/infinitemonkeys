import random,string

shakespeare = 'methinks it is a weasel'

def generate():
 char = string.ascii_lowercase+' '
 randchars = ''.join(random.choice(char) for _ in range(27))
 return randchars

def score():
 scorenum = 0
 randchars = generate()
 print randchars
 shake = shakespeare.split()
 randlist = randchars.split()
 for i,j in zip(shake,randlist):
  if i==j:
   scorenum = scorenum+1
  scorecount = (scorenum/27)*100
 return scorecount

def main():
 run = 0
 while not(score()==100):
  score()
  run = run + 1
  print run
  if run ==1000:
   print score()

if __name__ == '__main__':
 main()
