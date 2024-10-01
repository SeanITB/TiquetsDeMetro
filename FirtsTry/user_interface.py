#Where the user will interact with the machine, it will display menus and the respectful chosen tickets
class user_interface:

    def __init__(self, tickets):
        self.proces_state = 0
        self.tickets = tickets

    def show_ticket_tipe(self) -> str:
        outMsg: str = "Chose which ticket do you prefer:\n"
        for key, value in self.tickets.items():
            outMsg += f"{key} --> {value}\n"
        return outMsg

