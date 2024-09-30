class TicketMachine:

    def __init__(self):
        self.stopCode = "4321"
        self.namesTypeTickets = ["Bitllet_senzill", "TCasual", "TUsual", "TFamiliar", "TJove"]
        self.price_zone = [
            [2.55, 3.65, 4.80, 6.15, 7.85, 9.15],
            [12.15, 23.90, 32.55, 41.85, 48.10, 51.15],
            [21.35, 28.75, 40.35, 49.40, 56.65, 60.70],
            [10.70, 20.30, 28.40, 37.35, 42.70, 44, 85]
        ]
        self.tJoveZonePrice = 42.70

    #Show the diferent type of tickets
    def show_tickets(self) -> str:
        ticket_type : str = ""
        for t in range(len(self.namesTypeTickets)):
            ticket_type += f"{t + 1} -> {self.namesTypeTickets[t]}\n"
        return ticket_type

    #Tipus de bitllet
    def ticketType(self, typeTicket) -> str:
        return self.namesTypeTickets[typeTicket - 1]

    #Number of tickets
    def zoneNumber(self, type_ticket) -> str:
        textForChooseZone: str
        if type_ticket - 1 == 4: # -1 is for the index conflict
            textForChooseZone = "You have 6 zones"
        else:
            for z in range(len(self.price_zone[type_ticket - 1])):
                textForChooseZone += z+1 + " -> " + self.price_zone[type_ticket - 1][z] + "\n"
        return textForChooseZone

    #Preu Total
    def total_price(self, shopping_cart) -> str:
        total_price: float
        for c in range(len(shopping_cart)):
            total_price += self.price_zone[c.type][c.zone]
        return total_price

    #Tiquet