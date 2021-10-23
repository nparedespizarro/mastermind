

class Turns:
    
    def __init__(self):
        self.__keep_playing = True
        self.__turn_relay = True
        self.__current_player = ""
        
    def get_keep(self):
        return self.__keep_playing
    
    def turn_msg(self, name):
        message = f"{name}'s turn: \nWhat is your guess? "
        return message
    
    def turn_commute(self):
        if self.__turn_relay:
            self.__turn_relay = False
        else:
            self.__turn_relay = True
    
    def get_turn(self):
        return self.__turn_relay
        
    def set_current_player(self, value):
        self.__current_player = value
    
    def win(self):
        message = f"{self.__current_player} won! "
        return message
    
        
        
        
        
