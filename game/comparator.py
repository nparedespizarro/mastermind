
class Comparator:
    
    def __init__(self):
        pass
        
    def compare(self, code, user_input, wordlist):
        new_status = []
        winner = False
        word_state = False
        state = False
        
        if user_input not in wordlist:
            word_state = True
        
            if len(user_input) == 4 and user_input.isnumeric():
                state = True
                for i, o in zip(code, user_input):
                    if i in o:
                        new_status.append("X")
                    else:
                        if o in code:
                            new_status.append("O")
                        else:
                            new_status.append("*")

                status = "".join(new_status)
            else:
                status = "----"
                state = False
            
            if status.count("X") == 4:
                winner = True
                
        else:
            word_state = False
            state = False
            status = "----"
        
            
        return state, status, winner, word_state

# ~ caca = Comparator()        
# ~ print(caca.compare("1234", "1111"))
