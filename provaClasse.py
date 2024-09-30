class provaClasse:
    def __init__(self):
        self.namesTypeTickets = ["Bitllet_senzill", "TCasual", "TUsual", "TFamiliar", "TJove"]

    def show_tickets(self):
        return "\n".join([f"{i + 1} -> {ticket}" for i, ticket in enumerate(self.namesTypeTickets)])
