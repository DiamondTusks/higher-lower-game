#logo
from art import logo
from art import vs
import game_data
import random
from replit import clear

print(logo)
game_over = False
count = 0
  # pick random from distionary
followers = []
def get_random_account():
  """Picks a random account from game_data.py and returns readable format."""
  account = random.choice(game_data.data)
  followers.append(account["follower_count"])
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name} - {description} from {country} "
# print input - A vs B
# compare followers
random_a = get_random_account()
random_b = get_random_account()
if random_b == random_a:
  random_b = get_random_account()

while not game_over:
  print(f"Compare A: {random_a}")
  print(vs)
  print(f"Against B: {random_b}")
  # print(followers)

  def compare(a, b):
    if a > b:
      return "a"
    else:
      return "b"
  
  more_followers = compare(followers[0], followers[1])
  answer = input("\nWho has more followers? Type 'A' or 'B': ").lower()
  
  if answer == more_followers:
    clear()
    print(logo)
    count += 1
    print(f"You are correct! You got {count} correct so far.\n")
    followers.remove(followers[0])
    random_a = random_b
    random_b = get_random_account()
    
  else:
    print(f"Incorrect. You got {count} correct.")
    game_over = True

