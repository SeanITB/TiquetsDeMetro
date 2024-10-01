#This works with the interface class, where that one gives the input at the machine and this gives the recuaierd output.
class ticket_machin:
    def __init__(self):
        self.stop_machine = "4321"
        self.tickets_names = {
            1 : "Bitllet_senzill" ,
            2 : "TCasual",
            3 : "TUsual",
            4 : "TFamiliar",
            5 : "TJove"
        }
        self.tickets_zones = {
            1 : [2.55, 3.65, 4.80, 6.15, 7.85, 9.15] ,
            2 : [12.15, 23.90, 32.55, 41.85, 48.10, 51.15] ,
            3 : [21.35, 28.75, 40.35, 49.40, 56.65, 60.70] ,
            4 : [10.70, 20.30, 28.40, 37.35, 42.70, 44, 85] ,
            5 : [42.70]
        }

    #With the previus selection of the user, the machine will give the ticket name.
    def give_ticket_type(self, imp_user) -> str:
        return self.tickets_names[imp_user]

    #Now, the same with: chose_ticket_tipe, but with the zone number.


    #When the user ends the proces, it calculates the price of the chosen tickets.


    def get_tickets(self):
        return self.tickets_names

    def get_stop_machine(self) -> str:
        return self.stop_machine