import praw
import time

###############
#CONFIGURABLES#
###############

SLEEP = 20 # Sets the time between updates (approximate) in seconds. Recommended at least 5.
mute = False # If True, no audio notifications will play.
username = "phenomist" # Your username, if you want notifications when people comment on your rounds.

###############

# Initialization
r = praw.Reddit(user_agent = 'PictureGame Notifier v0.1 by /u/phenomist')
rp = 0 # most recent post
rc = 0 # most recent comment
solved = False # is the current round solved?
host = "" # host of the round

def notify_post(p):
  print('NEW ROUND UP!')
  print('['+time.ctime(p.created_utc)+']', p.author._case_name, 'posted', p.title)
  if not mute:
    print('\a \a')

def notify_comment(p):
  if p.author._case_name not in ["AutoModerator", "r_PictureGame"]:
    print('['+time.ctime(p.created_utc)+']', p.author._case_name, 'posted', p.body)
  if p.body.find('+correct') != -1 and p.author._case_name == host:
    print('ROUND OVER!')
    solved = True
    if not mute:
      print('\a \a \a')
  if host == username and not mute:
    print('\a')

def update_post(a):
  global rp
  for p in a:
    if p.created_utc > rp and p.link_flair_text=="UNSOLVED":
      rp = p.created_utc
      solved = False
      host = p.author._case_name
      notify_post(p)
      return p
    if p.created_utc == rp: # This occurs if the most recent message(s) are mod messages.
      return p


def check(m):
  mt = m.created_utc
  if m.created_utc > rc:
    notify_comment(m)
  for p in m._replies:
    mt = max(mt, check(p))
  return mt

def update_comments(a): # returns maximum time
  mt = 0
  for p in a:
    mt = max(mt, check(p))
  return mt

while True:
  time.sleep(SLEEP)
  s = r.get_subreddit('PictureGame').get_new(limit=10)
  a = list(s)
  # if no unsolved round: detect new round
  # if new round: PING, go to solving mode
  p = a[0] # p is the active round
  if a[0].created_utc > rp:
    p = update_post(a)
    #print("test")
  if not solved and p:
    rc = update_comments(p.comments)
  # if unsolved round: detect new answers
    # if +correct detected: PING, go to unsolved mode
    # if your unsolved round: asks you whether it's correct or not
