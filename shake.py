import random

def generate(length):
 char = string.ascii_lowercase+' '
 randstr = ''
 for i in range(length):
  randstr=randstr+char[random.randrange(27)]
  return randstr
 
def score(final,test):
 numScore = 0
 for i in range(len(final)):
  if final[i]==test[i]:
   numScore = numScore + 1
 return numScore/len(final)
 
def main():
 final = 'methinks it is like a weasel'
 random = generate(23)
 best = 0
 newscore = score(final,random)
 while newscore < 1:
  if newscore > best:
   print(newscore,random)
   best = newscore
  random = generate(23)
  newscore = score(final,random)
