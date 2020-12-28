from Menu import Menu
from Member import Member
from Utils import Utils
import os

class ChristmasProject:
    def __init__(self):
        self.menu = Menu(["Add member", "View bookings", "Edit member", "Quit"], "Main")
        self.filename = Utils.get_filename()
    #end def
    
    def add_member(self):
        self.set_new_member()
        Utils.append_to_file(self.filename, self.new_member.to_string_format())
    #end def
    
    def set_new_member(self):
        data = []
        for key in Member.get_attributes():
            if key == "member ID" or key == "member status":
                data.append("")
            else:
                info_to_add = input("Enter the " + key + ": ")
                data.append(info_to_add)
        self.new_member = Member(data)
    #end def

    def view_bookings(self):
        self.print_members(self.get_members())
    #end def
        
    def print_members(self, members):
        print("-------------------------------------------------------------------------------------------------")
        print("|Member ID      |Surname        |Year joined    |Member status  |Nights booked  |Points balance |")
        print("-------------------------------------------------------------------------------------------------")
        for member in members:
            for attribute in member:
                num_of_spaces = 15 - len(attribute)
                print("|" + attribute + " " * num_of_spaces, end = "")
            print("|")
        print("-------------------------------------------------------------------------------------------------")                
    #end def
        
    def get_members(self):
        members = []
        file = open(self.filename, "r")
        for line in file:
            data = Utils.split_line(line)
            if data is not None:
                members.append(data)        
        return members
    #end def
        
    def get_choice(self):
        choice = ""
        quit_index = 0
        while choice != str(self.menu.get_quit_index()):
            self.menu.show_menu()
            choice = input("Enter a choice: ")
            if not self.menu.validate_choice(choice): continue
            
            if choice == "1":
                self.add_member() if self.menu.get_menu_type() == "Main" else self.record_nights_booked()
            if choice == "2":
                self.view_bookings() if self.menu.get_menu_type() == "Main" else self.redeem_points()
            if choice == "3":
                self.edit_member_menu() if self.menu.get_menu_type() == "Main" else self.menu.update_options(["Add member", "View bookings", "Edit member", "Quit"], "Main")
    #end def
    
    def redeem_points(self):
        try:
            found = False
            member_wanted = input("Enter the Member ID of the member you want to edit: ")
            if len(member_wanted) == 8:
                with open(self.filename, "r") as read_file, open("temp.txt", "w") as write_file: 
                    for line in read_file:
                        if member_wanted in line:
                            found = True
                            data = Utils.split_line(line)
                            if data is not None:
                                self.selected_member = Member(data)
                                self.selected_member.redeem_points()
                                write_file.write(self.selected_member.to_string_format())
                                print("Successfully recorded points redeemed")
                        else:
                            write_file.write(line)
                    if found != True:
                        print("Member not found")
                os.remove(self.filename)
                os.rename("temp.txt", self.filename)
            else:
                print("That's not a valid Member ID")
            
        except:
            os.remove("temp.txt")
            print("Error saving data")
    #end def
    
    def edit_member_menu(self):
        self.menu.update_options(["Record nights booked", "Redeem pionts", "Back"], "Sub-menu")
    #end def
                    
    def record_nights_booked(self):
        try:
            found = False
            member_wanted = input("Enter the Member ID of the member you want to edit: ")
            if len(member_wanted) == 8:
                with open(self.filename, "r") as read_file, open("temp.txt", "w") as write_file: 
                    for line in read_file:
                        if member_wanted in line:
                            data = Utils.split_line(line)
                            if data is not None:
                                self.selected_member = Member(data)
                                self.selected_member.record_nights()
                                write_file.write(self.selected_member.to_string_format())
                                print("Successfully recorded nights booked")
                        else:
                            write_file.write(line)
                    if found != True:
                        print("Member not found")                    
                os.remove(self.filename)
                os.rename("temp.txt", self.filename)
            else:
                print("That's not a valid Member ID")            
            
        except:
            os.remove("temp.txt")
            print("Error saving data")                    
    #end def
#end class

def main():
    project = ChristmasProject()
    project.get_choice()
#end def

main()