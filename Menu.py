class Menu():
    
    def __init__(self, options, menu_type):
        self.options = options
        self.menu_type = menu_type
    #end def
        
    def get_quit_index(self):
        index_of_quit = 1
        for option in self.options:
            if option == "Quit":
                return index_of_quit
            index_of_quit += 1
        return None
    #end def
    
    def get_menu_type(self):
        return str(self.menu_type)
    #end def

    def show_menu(self):
        index = 1
        print("   " + self.menu_type + " Menu")
        for option in self.options:
            print(str(index) + ". " + option)
            index += 1
    #end def

    def update_options(self, options, menu_type):
        self.options = options
        self.menu_type = menu_type
    #end def

    def validate_choice(self, choice):
        try:
            choice = int(choice)
        except:
            print("You need to enter a valid number")
            return False
        try:
            if self.options[choice-1] != "": return True
        except:
            print("You need to enter a valid option")
        return False
    #end def

#end class