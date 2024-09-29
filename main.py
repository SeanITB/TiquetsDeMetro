
class TiketMachine:

    def __init__(self):
        self.stopCode = "4321"
        self.namesTypeTickets = ["Bitllet_senzill", "TCasual", "TUsual", "TFamiliar", "TJove"]
        self.billetSenzillZonePrice = [2.55, 3.65, 4.80, 6.15, 7.85, 9.15]
        self.tCasualZonePrice = [12.15, 23.90, 32.55, 41.85, 48.10, 51.15]
        self.tUsualZonePrice = [21.35, 28.75, 40.35, 49.40, 56.65, 60.70]
        self.tFamiliarZonePrice = [10.70, 20.30, 28.40, 37.35, 42.70, 44,85]
        self.tJoveZonePrice =


    #Tipus de bitllet
    def ticketType(self, typeTicket) -> str:
        nameTicket: str
        if typeTicket == 0 :
            nameTicket = self.namesTypeTickets[0]
        elif typeTicket == 1 :
            nameTicket = self.namesTypeTickets[1]
        elif typeTicket == 2 :
            nameTicket = self.namesTypeTickets[2]
        elif typeTicket == 3 :
            nameTicket = self.namesTypeTickets[3]
        else:
            nameTicket = self.namesTypeTickets[4]
        return nameTicket

    #Number of tickets
    def zoneNumber(self, nameTicket) -> str:
        textForChooseZone: str
        if nameTicket == self.namesTypeTickets[4]:
            textForChooseZone = "You have 6 zones"
        else:
            textForChooseZone = "Which zone you prefer"
        return textForChooseZone

    #Preu Total
    def totalPrice(self, ticket):
        totalPrice: float
        if ticket.type == self.ticketType[4]:
            totalPrice =

    #Tiquet
