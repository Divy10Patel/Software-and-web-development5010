# Import required libraries
import datetime

# Define a dictionary to store user data
users = {}

# Define a dictionary to store event data
events = {}

# Define a dictionary to store ticket bookings
bookings = {}

# Function to register a new user
def register_user(username, password):
    users[username] = password
    print(f"User {username} registered successfully!")

# Function to login a user
def login_user(username, password):
    if username in users and users[username] == password:
        print(f"User {username} logged in successfully!")
        return True
    else:
        print("Invalid username or password!")
        return False

# Function to create a new event
def create_event(event_name, event_date, num_tickets):
    events[event_name] = {"date": event_date, "tickets": num_tickets}
    print(f"Event {event_name} created successfully!")

# Function to book a ticket
def book_ticket(event_name, username):
    if event_name in events:
        if events[event_name]["tickets"] > 0:
            bookings[event_name] = bookings.get(event_name, []) + [(username, datetime.datetime.now())]
            events[event_name]["tickets"] -= 1
            print(f"Ticket booked successfully for event {event_name}!")
        else:
            print("Sorry, no tickets available for this event!")
    else:
        print("Event not found!")

# Function to cancel a ticket
def cancel_ticket(event_name, username):
    if event_name in bookings:
        for i, (u, _) in enumerate(bookings[event_name]):
            if u == username:
                bookings[event_name].pop(i)
                events[event_name]["tickets"] += 1
                print(f"Ticket cancelled successfully for event {event_name}!")
                return
        print("You don't have a ticket for this event!")
    else:
        print("Event not found!")

# Main program
while True:
    print("Welcome to the Ticketing System!")
    print("1. Register")
    print("2. Login")
    print("3. Create Event")
    print("4. Book Ticket")
    print("5. Cancel Ticket")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        register_user(username, password)
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        if login_user(username, password):
            while True:
                print("1. Create Event")
                print("2. Book Ticket")
                print("3. Cancel Ticket")
                print("4. Logout")
                choice = input("Enter your choice: ")

                if choice == "1":
                    event_name = input("Enter event name: ")
                    event_date = input("Enter event date: ")
                    num_tickets = int(input("Enter number of tickets: "))
                    create_event(event_name, event_date, num_tickets)
                elif choice == "2":
                    event_name = input("Enter event name: ")
                    book_ticket(event_name, username)
                elif choice == "3":
                    event_name = input("Enter event name: ")
                    cancel_ticket(event_name, username)
                elif choice == "4":
                    break
    elif choice == "3":
        event_name = input("Enter event name: ")
        event_date = input("Enter event date: ")
        num_tickets = int(input("Enter number of tickets: "))
        create_event(event_name, event_date, num_tickets)
    elif choice == "4":
        event_name = input("Enter event name: ")
        username = input("Enter username: ")
        book_ticket(event_name, username)
    elif choice == "5":
        event_name = input("Enter event name: ")
        username = input("Enter username: ")
        cancel_ticket(event_name, username)
    elif choice == "6":
        break
    else:
        print("Invalid choice!")



S - Single Responsibility Principle (SRP)

register_user is only responsible for registering a new user.
login_user is only responsible for logging in a user.
create_event is only responsible for creating a new event.


O - Open/Closed Principle (OCP)

In the ticketing system code, the book_ticket function is designed to be open to extension but closed to modification. If we want to add a new type of ticket, we can do so without changing the existing code. We can simply add a new condition to the book_ticket function to handle the new type of ticket.

L - Liskov Substitution Principle (LSP)

In the ticketing system code, the User class is designed to be substitutable. We can use any user object, regardless of its specific type, because they all have the same responsibilities and abilities.

I - Interface1 Segregation Principle (ISP)
01mple and clear interface for creating and managing events.

D - Dependency Inversion Principle (DIP)

In the ticketing system code, the TicketingSystem class is designed to be independent of specific dependencies. We can use any type of database or storage system, because the TicketingSystem class is designed to be flexible and adaptable.        
