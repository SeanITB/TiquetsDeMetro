#Main program
from FirtsTry.ticket_machin import ticket_machin
from FirtsTry.user_interface import user_interface

my_machine = ticket_machin()
my_user_interface = user_interface(my_machine.get_tickets())

print(my_user_interface.show_ticket_tipe())
#toDO: now proces the inmput of the user