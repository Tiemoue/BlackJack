from deck import card_name, card_value, end_turn_status, end_game_status
from random import randint

def main():
  print("\n----------------------------------------------------------------")
  print("                ♠♣♥♦ WELCOME TO BLACKJACK! ♠♣♥♦")
  print("                          Lets Play!")
  print("----------------------------------------------------------------")
  print("{} \n{} \n{} ".format("-----------", "YOUR TURN", "-----------"))

  user_hand = 0
  draw_count = 0
  hit = "y"

  while user_hand < 21 and hit:
    card = randint(1,13)
    print("Drew a {}".format(card_name(card)))
    user_hand += card_value(card)
    draw_count += 1
    
    if draw_count >= 2 and user_hand < 21:
        hit = input("You have {}.Hit (y/n)? ".format(user_hand)) == "y"
  print("Final hand: {}.".format(user_hand))
  print(end_turn_status(user_hand))

  print("{} \n{} \n{} ".format("-----------", "DEALER TURN", "-----------"))

  dealer_hand = 0
  draw_count = 0
  
  while dealer_hand < 18:
    if draw_count >= 2:
      print("Dealer has {}.".format(dealer_hand))
    
    card = randint(1,13)
    print("Drew a {}".format(card_name(card)))
    dealer_hand += card_value(card)
    draw_count += 1
  print("Final hand: {}.".format(dealer_hand))
  print(end_turn_status(dealer_hand))

  print("{} \n{} \n{} ".format("-----------", "GAME RESULT", "-----------"))

  print(end_game_status(user_hand, dealer_hand))

if __name__ == '__main__':
  main()
