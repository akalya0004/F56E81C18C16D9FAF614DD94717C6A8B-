# define the base class player
class player:
  def __init__(self):
    def play(self):
      print("the player is playing cricket")
# define the derived class batsman
class batsman (player):
  def play(self):
   print("the batsman is batting")
# define the derived class bowler
class bowler(player):
  def play(self):
   print("the bowler is bowling ")
#create object of batsman and bowler classes
b1=batsman()
b2=bowler()
#call the play() method for each object
b1.play()
b2.play()


  
