import praw
import time
r = praw.Reddit(user_agent = 'PictureGame Notifier Bot v0.1 by /u/phenomist')
rp = 0
rc = 0
solved = False
SLEEP = 20

def notify_post(p):
  print('NEW ROUND UP!')
  print(p.author, ' posted ', p.title)

def update_post(a):
  i = 0
  while i<len(a):
    if a[i].created > rp and a[i].link_flair_text!="MOD MESSAGE":
      rp = a[i].created
      notify_post(a[i])
      return
    if a[i].created = rp: # This occurs if the most recent message(s) are mod messages.
      return
    i++

while True:
  time.wait(SLEEP)
  s = r.get_subreddit('PictureGame').get_new(limit=10)
  a = [x for x in s]
  if a[0]
  # if no unsolved round: detect new round
    # if new round: PING, go to solving mode
  # if unsolved round: detect new answers
    # if +correct detected: PING, go to unsolved mode
    # if your unsolved round: asks you whether it's correct or not
