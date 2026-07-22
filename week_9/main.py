from ticket import create_ticket
from display import show_ticket

def main():
    ticket_data = create_ticket()
    
    priority = ticket_data["priority"].capitalize()
    
    if priority == "High":
        technician = "Ahmad"
    elif priority == "Medium":
        technician = "Siti"
    elif priority == "Low":
        technician = "Ali"
    else:
        technician = "Unknown"
        
    show_ticket(ticket_data, technician)

if __name__ == "__main__":
    main()