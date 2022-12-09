#Enter your name
#Enter your staff id
#Enter your email
#If you requiere a new password type: Password change
#Enter description of problem:
#Your new password is:
#Do you have another problem to submit? (Y/N)Y

import random

LETTERS = 'abcdefghijklmnñopqrstuvwxyz123456789'
TICKETS = []
USERS = []


class User(object):
    def __init__(self, staffId, staffName, staffEmail, password):
        self.staffId = staffId
        self.staffName = staffName
        self.staffEmail = staffEmail
        self.password = password


class Ticket(object):
    ticket_id = 2000

    def __init__(self, user, problemDescription, status='open'):
        self.user = user
        self.problemDescription = problemDescription
        self.status = status
        self.id = int(Ticket.ticket_id)
        self.response = ''
        Ticket.ticket_id = Ticket.ticket_id + 1

    def closeTicket(self, response):
        self.response = response
        self.status = 'closed'

    def openTicket(self, updatedProbme):
        self.problemDescription = updatedProbme
        self.status = 'open'


class Menu_List():

    def PasswordGenerator(self):
        generatedPassword = ''
        passwordLength = random.randint(8, 12)
        for character in range(0, passwordLength):
            generatedPassword = generatedPassword + LETTERS[random.randint(0, len(LETTERS) - 1)]
        return generatedPassword

    @staticmethod

    def Print_Menu():
        print("\nSelect from the following choices: ")

        print("\n0: Exit ")
        print("1: Submit helpdesk ticket ")
        print("2: Show all tickets ")
        print("3: Respond to ticket by number ")
        print("4: Re-open resolved ticket ")
        print("5: Display ticket stats ")
        print("-------------------------------------------------------------------")

        enter_menu_selection = int(input("Enter Menu Selection 0 - 5: "))
        print("--------------------------------------------")
        return enter_menu_selection;


def Process_Input(selection, menu):
    if selection == 0:
        print('Bye');
        exit(0);
    if selection == 1:
        Sumbit_helpdesk_ticket(menu);
    if selection == 2:
        show_tickets()
    if selection == 3:
        answer_ticket_by_id()
    if selection == 4:
        open_ticket_by_id()
    if selection == 5:
        display_ticket_stats()


def Sumbit_helpdesk_ticket(menu):
    staffId = str(input("Enter your staff id: "))
    staffName = str(input("Enter your name: "))
    staffEmail = str(input("Enter your email: "))
    print("If you require a new password type: Password change");
    user = User(staffId, staffName, staffEmail, '');
    problemDescription = str(input("Enter description of problem: "))
    ticket = Ticket(user, problemDescription)

    if problemDescription == "Password change":
        password = menu.PasswordGenerator();
        print("Your new password is: " + password)
        ticket.closeTicket("User password was set to: " + password)

    USERS.append(user)
    TICKETS.append(ticket)
    print("Ticket has been submitted to the helpdesk queue")
    extra_problem = str(input("Do you have another problem to submit? (Y/N)"))
    if extra_problem == "Y":
        Sumbit_helpdesk_ticket(menu)


def show_tickets():
    for ticket in TICKETS:
        print('Ticket: ' + str(ticket.id))
        print('Submitted by staff id' + str(ticket.user.staffId))
        print('ticket owner' + ticket.user.staffName)
        print('contact email' + ticket.user.staffEmail)
        print('Description of issue: ' + ticket.problemDescription)
        print('Status ' + ticket.status)
        print('Response: ' + ticket.response)


def answer_ticket_by_id():
    ticket_number = int(input("Which ticket would you like to answer?"))
    ticket = findTicketId(ticket_number)
    print("Description of the problem: " + ticket.problemDescription)
    ticket_response = str(input("Write your response: "))
    ticket.closeTicket(ticket_response)


def open_ticket_by_id():
    ticket_number = int(input("Which ticket would you like to open?"))
    ticket = findTicketId(ticket_number)
    ticket.openTicket(str(input("Write the updated problem?")))


def display_ticket_stats():
    totalTickets = 0
    resolved = 0
    open = 0

    for ticket in TICKETS:
        totalTickets = totalTickets + 1
        if ticket.status == 'closed':
            resolved = resolved + 1
        elif ticket.status == 'open':
            open = open + 1
    print('Submitted Tickets:' + str(totalTickets))
    print('Resolved Tickets:' + str(resolved))
    print('Open Tickets:' + str(open))


def findTicketId(id):
    for ticket in TICKETS:
        if ticket.id == id:
            return ticket


def Main():
    menu = Menu_List();
    selected_option = menu.Print_Menu()
    Process_Input(selected_option, menu)
    Main()


# where program should start
Main()
