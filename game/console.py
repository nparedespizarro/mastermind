
class Console:
    """ A simple console code.
    class responsibility: display text on the standart output and return inputs
    
        Stereotype:
        Service Provider, Interfacer
        
        Attributes: 
        - message: to display a message when "master_in" is called.
        -output_value: a string to display on the console thru print function.
    
    """
    
    def __init__(self):
        #Prints a welcome message. 
        welcome = """ 
        
                      _                          
        __      _____| | ___ ___  _ __ ___   ___ 
        \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \\
         \ V  V /  __/ | (_| (_) | | | | | |  __/
          \_/\_/ \___|_|\___\___/|_| |_| |_|\___|

        """
        
        print(welcome)
        
        
    
    def master_out(self, output_value):
        #displays a string
        print(output_value)    
        
    def master_in(self, message):
        #returns an input given by the user
        x = input(message)
        return x

    def stepper(self):
        #prints the string "--------------------"
        print("--------------------")
    
    def new_line(self):
        #prints a new line
        print()
