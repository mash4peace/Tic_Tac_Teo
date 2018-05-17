class FootballPlayer:
    name = "Chris Smalling"
    team = "Man United"
    years_in_leage = 0

    def printPlayer(self):
        print(self.name + " playing for the "+ self.team)

    def isGood(self):
        print("Error ! is Good is not defined !")
        return False
#Quarterback is the child of FootballPlayer, and it inherets characteristics of the parent.
class Quarterback(FootballPlayer):
    pass_attempted = 0
    completion = 0
    pass_yard = 0
    def compltionRate(self):
        return self.completion/self.pass_attempted

    def yardsPerAttempt(self):
        return self.pass_yard/self.pass_attempted

class Runningback(FootballPlayer):
    rushes = 0
    rush_yards = 0
    def yardsPerRush(self):
        return self.rush_yards/self.rushes
#Create instance of the class
player1  = Quarterback()
player1.name = "Luke Show"
player1.team = "Man United"
player1.pass_attempted = 45
player1.pass_yard = 190
player1.completion = 40
player2 = Runningback()
player2.name = "Antonio Valencia"
player2.team = "Man United"
player2.rush_yards = 90
player2.rushes = 600
playerList = []
playerList.append(player1)
playerList.append(player2)
for player in playerList:
    player.printPlayer()
    if (player.isGood()):
        print("Is a good player!")
    else:
        print("Is not a good player")

