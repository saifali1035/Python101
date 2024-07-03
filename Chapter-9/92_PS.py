import random

def update_score(num):
    with open('/workspaces/Python101/Chapter-9/score.txt','w') as f:
        num=str(num)
        f.write(num)
    print("High Score Recorded !! ")


print("A New High Score Reached")
new_score=random.randint(5555,9999)
update_score(new_score)
