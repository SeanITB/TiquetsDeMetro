#Main program
from FirtsTry.ticket_machin import ticket_machin
from FirtsTry.user_interface import user_interface
from utils.utils import try_int

my_machine = ticket_machin()
my_user_interface = user_interface(my_machine.get_tickets())

imp_ticket_type : str = ""
proces_state = my_user_interface.get_proces_state()
while imp_ticket_type == my_machine.get_stop_machine():
    integer_number = int(imp_ticket_type)

    imp_ticket_type = input(my_user_interface.show_ticket_tipe())
    int_correct = try_int(integer_number)
    if int_correct == True:
        if proces_state == 1:
            print(my_machine.give_ticket_type(integer_number))

        #toDo: no sale el print


