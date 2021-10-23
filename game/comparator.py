
class Comparator:
    
    def __init__(self):
        pass
        
    def compare(self, code, user_input):
        new_status = []
        winner = False
        
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
        return state, status, winner

# ~ caca = Comparator()        
# ~ print(caca.compare("1234", "1111"))
