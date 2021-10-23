from game.console import Console
from game.players import Players
from game.turns import Turns
from game.generator import Generator
from game.comparator import Comparator

class Director:
    
    def __init__(self):
        self.console = Console()
        self.players = Players()
        self.turns = Turns()
        self.generator = Generator()
        self.comparator = Comparator()
        

    def start_game(self):
        
        self.players.set_player1(self.console.master_in("Enter a name for player 1: "))
        self.players.set_player2(self.console.master_in("Enter a name for player 2: "))
        self.console.new_line()
        
        while self.turns.get_keep():
            self.console.stepper()
            self.console.master_out(f"Player {self.players.get_player1()}: {self.generator.get_player1_status()}")
            self.console.master_out(f"Player {self.players.get_player2()}: {self.generator.get_player2_status()}")
            self.console.stepper()
            if self.turns.get_turn():
                # ~ print(self.generator.get_player1_code())
                self.turns.set_current_player(self.players.get_player1())
                turn = self.console.master_in(self.turns.turn_msg(self.players.get_player1()))
                state, comparation , winner, word_state = self.comparator.compare(self.generator.get_player1_code(), turn, self.players.get_wordlist_player1())
                if word_state:
                    if state:
                        self.generator.set_player1_state(comparation)
                        self.generator.set_player1_hidden(turn)
                        self.turns.turn_commute()
                        self.console.new_line()
                        self.players.update_wordlist_player1(turn)
                    else:
                        self.console.master_out(f"{turn} is not a valid input, try again!")
                else:
                    self.console.master_out(f"You have entered {turn} before")

            else:
                # ~ print(self.generator.get_player2_code())
                self.turns.set_current_player(self.players.get_player2())
                turn = self.console.master_in(self.turns.turn_msg(self.players.get_player2()))
                state, comparation, winner, word_state= self.comparator.compare(self.generator.get_player2_code(), turn, self.players.get_wordlist_player2())
                if word_state:
                    if state:
                        self.generator.set_player2_state(comparation)
                        self.generator.set_player2_hidden(turn)
                        self.turns.turn_commute()
                        self.console.new_line()
                        self.players.update_wordlist_player2(turn)

                    else:
                        self.console.master_out(f"{turn} is not a valid input, try again!")
                else:
                    self.console.master_out(f"You have entered {turn} before")
            if winner:
                self.console.master_out(self.turns.win())
                break
            


        
        
        
