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