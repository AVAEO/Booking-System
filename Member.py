import random

class Member:
    def __init__(self, data):
        self.member_ID = data[0]
        self.surname = data[1]
        self.year_joined = int(data[2])
        self.member_status = data[3]
        self.nights_booked = int(data[4])
        self.points = int(data[5])
        if self.member_ID == "":
            self.set_member_ID()
            self.set_member_status()
    #end def
    
    def set_member_ID(self):
        self.member_ID = self.surname[0:3] + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(self.year_joined)[2:4]
    #end def
        
    def set_member_status(self):
        if self.nights_booked >= 100:
            self.member_status = "Platinum"
        elif self.nights_booked >= 30:
            self.member_status = "Gold"
        else:
            self.member_status = "Silver"
    #end def
    
    def to_string_format(self):
        string = self.member_ID + "," + self.surname + "," + str(self.year_joined) + "," + self.member_status + "," + str(self.nights_booked) + "," + str(self.points) + "\n"
        return string
    #end def
    
    def redeem_points(self):
        nights = int(input("How many nights do you want to redeem: "))
        if self.points >= 25000 * nights:
            self.points -= 25000 * nights
            self.nights_booked += nights
        else:
            print("Not enough points")
        self.set_member_status()
    #end def
    
    def record_nights(self):
        try:
            nights = int(input("How many nights do you want to add: "))
            self.nights_booked += nights
            if nights > 14:
                print("You can only add a maximum of 14 days at a time")
            else:
                if self.member_status == "Silver":
                    self.points += nights * 2500
                elif self.member_status == "Gold":
                    self.points += nights * 3000
                else:
                    self.points += nights * 4000
        except:
            print("Error recording nights booked")
        self.set_member_status()
    #end def
    
    @staticmethod
    def get_attributes():
        member_attributes = ["member ID", "surname", "year joined", "member status", "nights booked", "points"]
        return member_attributes       
    #end def    
#end class