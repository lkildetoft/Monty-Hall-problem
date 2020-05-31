import numpy as np 
import matplotlib.pyplot as plt 
import random
author = "Love Kildetoft"
"""
Program which simulates the Monty Hall problem 
at a number of iterations set by the user and 
plots the results when switching and not switching
respectively.
"""
class SwitchingPlayer:

    #class handling the logic for a player which switches from
    #the initial door which was picked

    def __init__(self):
        #constructor, sets doors, shuffles randomly for each instance
        #and picks a random door (the player)
        self.doors = ["win", "lose", "lose"]
        random.shuffle(self.doors)
        self.pick = random.randint(0, 2)

    def host(self):
        #handles the host opening one of the doors yielding a loss.
        #reveals the winning door and returns the available doors.
        win = self.doors.index("win")

        if win == 0:
            revealed_door = random.choice([1, 2])
        if win == 1:
            revealed_door = random.choice([0, 2])
        elif win == 2: 
            revealed_door = random.choice([0, 1])

        available_doors = [self.doors[i] for i in range(len(self.doors)) if i != revealed_door]

        return available_doors

    def switch_doors(self):
        #switches doors for the player using list comprehension.
        #initializes host method and checks the available doors.
        available_doors = self.host()

        if self.doors[self.pick] == available_doors[0]:
            final_pick = available_doors[1]
        else:
            final_pick = available_doors[0]
        
        return final_pick

class NonSwitchingPlayer(SwitchingPlayer):

    #class for handling logic for a non-switching player. 
    #inherits SwitchingPlayer but includes a new method for 
    #keeping the initial door instead of switching.
    
    def __init__(self):
        #initialize SwitchingPlayer constructor
        super().__init__()

    def keep_doors(self):
        #same logic as in SwitchingPlayer.switch_doors but
        #instead of switching, keeps the inital door.
        available_doors = self.host()

        if self.doors[self.pick] == available_doors[0]:
            final_pick = available_doors[0]
        else:
            final_pick = available_doors[1]
        
        return final_pick

class Simulation:

    #class handling the simulation of the monty hall problem at
    #a set number of iterations, as well as plotting the results.

    def __init__(self, iterations):
        #constructor initializing number of iterations set when 
        #creating an instance as well as a bunch of lists for handling
        #the plotting and returning the correct results
        self.iterations = iterations
        self.switch_wins = []
        self.switch_losses = []
        self.non_switch_wins = []
        self.non_switch_losses = []
        self.switch_wontimes = []
        self.non_switch_wontimes = []
        self.switch_losstimes = []
        self.non_switch_losstimes = []

    def simulate_monty(self):
        #method which simulates the monty hall problem and appends
        #the results to different lists for keeping track
        for i in range(self.iterations):
            #initiate instances of the players each iterations
            switching_player = SwitchingPlayer()
            non_switching_player = NonSwitchingPlayer()
            #obtain the result for each iteration and store 
            switch_result = switching_player.switch_doors()
            non_switch_result = non_switching_player.keep_doors()
            #append to approriate lists for results and plotting
            if switch_result == "win":
                self.switch_wins.append("win")
                self.switch_wontimes.append(len(self.switch_wins))
                self.switch_losstimes.append(np.nan)
            elif switch_result == "lose":
                self.switch_losses.append("lose")
                self.switch_wontimes.append(np.nan)
                self.switch_losstimes.append(len(self.switch_losses))

            if non_switch_result == "win":
                self.non_switch_wins.append("win")
                self.non_switch_wontimes.append(len(self.non_switch_wins))
                self.non_switch_losstimes.append(np.nan)

            elif non_switch_result == "lose":
                self.non_switch_losses.append("lose")
                self.non_switch_wontimes.append(np.nan)
                self.non_switch_losstimes.append(len(self.non_switch_losses))

        #print results
        print("Switching resulted in", len(self.switch_wins), "wins and", len(self.switch_losses), "losses")
        print("Not switching resulted in", len(self.non_switch_wins), "wins and", len(self.non_switch_losses), "losses")

    def plot_wins(self):
        #method for plotting each win at each iteration respectively
        iterations = np.linspace(0, self.iterations, self.iterations)
        plt.scatter(iterations, self.switch_wontimes, label="Wins when switching")
        plt.scatter(iterations, self.non_switch_wontimes, label="Wins when not switching")
        plt.xlabel("Iterations")
        plt.ylabel("Times won")
        plt.legend()
        plt.show()

    def plot_losses(self):
        #method for plotting each loss at each iteration respectively
        iterations = np.linspace(0, self.iterations, self.iterations)
        plt.scatter(iterations, self.switch_losstimes, label="Losses when switching")
        plt.scatter(iterations, self.non_switch_losstimes, label="Losses when not switching")
        plt.xlabel("Iterations")
        plt.ylabel("Times won")
        plt.legend()
        plt.show()

def main():
    #main function running everything
    iterations = input("Please input the number of iterations:")
    simulate = Simulation(int(iterations))
    simulate.simulate_monty()
    simulate.plot_wins()
    simulate.plot_losses()

if __name__ == "__main__":
    main()