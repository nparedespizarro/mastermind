
class Players:
    """ A simple piece of code created to manage players.
    class responsibility: store and return player names
    
        Stereotype:
        Service Provider
        
        Attributes: 
        __player1: stores a player's name
        __player2: stores a player's name
    
    """
    
    def __init__(self):
        """
        The class constructor
        """
        
        self.__player1 = "player1"
        self.__player2 = "player2"
        self.__wordlist_player1 = []
        self.__wordlist_player2 = []
        
    def get_player1(self):
        return self.__player1

    def get_player2(self):
        return self.__player2

    def set_player1(self, player):
        self.__player1 = player

    def set_player2(self, player):
        self.__player2 = player
        
    def get_wordlist_player1(self):
        return self.__wordlist_player1

    def get_wordlist_player2(self):
        return self.__wordlist_player2
    
    def update_wordlist_player1(self, word):
        self.__wordlist_player1.append(word)

    def update_wordlist_player2(self, word):
        self.__wordlist_player2.append(word)

