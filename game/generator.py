from random import randint

class Generator:
    
    def __init__(self):
        self.__player1_code = randint(1000, 9999)
        self.__player2_code = randint(1000, 9999)
        self.__player1_state = "****"
        self.__player2_state = "****"
        self.__player1_hidden = "----"
        self.__player2_hidden = "----"
        
    def get_player1_status(self):
        status = f"{self.__player1_hidden}, {self.__player1_state}"
        return status
    
    def get_player2_status(self):
        status = f"{self.__player2_hidden}, {self.__player2_state}"
        return status
 
    def get_player1_code(self):
        return str(self.__player1_code)
    
    def get_player2_code(self):
        return str(self.__player2_code)
        
    def set_player1_state(self, value):
        self.__player1_state = value
    
    def set_player2_state(self, value):
        self.__player2_state = value
    
    def set_player1_hidden(self, value):
        self.__player1_hidden = value
    
    def set_player2_hidden(self, value):
        self.__player2_hidden = value
