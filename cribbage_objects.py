class Card():
    def __init__(self, card_data):
        self.data = card_data
        
        #10 will be different format
        if len(card_data) == 3:
            self.name = card_data[0:2]
            self.suit = card_data[2]
        else:
            self.name = card_data[0]
            self.suit = card_data[1]
            
        #find the card's value
        if self.name.isalpha():
            if self.name == "a":
                self.value = 1
                self.rank = 1
            else:
                self.value = 10
                if self.name == "j":
                    self.rank = 11
                elif self.name == "q":
                    self.rank = 12
                else:
                    self.rank = 13
        else:
            self.value = int(self.name)
            self.rank = self.value
        
        #helpful value during count
        self.is_usable = True

            