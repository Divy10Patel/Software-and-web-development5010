"""
question :- build software get staff info and  display it and show status and total spend by staff.
Author:- Divya patel


"""

class RequisitionSystem:
    requisition_id_counter = 0  # global variable for the whole code

    def _init_(self, staff_id, date, staff_name, status="pending"):
        self.requisition_id = RequisitionSystem.requisition_id_counter
        RequisitionSystem.requisition_id_counter += 1
        self.staff_id = staff_id
        self.date = date
        self.staff_name = staff_name
        self.status = status
        self.requisition_items = []
        self.total = 0
        self.approval_reference_number = ""

    def staff_info(self):# staff_info function which get staff information
        return f"Staff ID: {self.staff_id}, Staff Name: {self.staff_name}"

    def requisition_details(self, requisition_items):#requisition_details which give total dollar spend by staff
        self.requisition_items = requisition_items
        self.total = sum(item["cost"] for item in requisition_items)
        return self.total

    def requisition_approval(self):#status of the  requisition

        if self.total <= 1000:# these are  the condition for approval

            self.status = "approved"
            self.approval_reference_number = "APR-" + str(self.requisition_id)
        else:
            self.status = "pending"

    def response_requisition(self, response):#responds from manager 
        if response.lower() == "approved":
            self.status = "approved"
            self.approval_reference_number = "APR-" + str(self.requisition_id)#get approval reference  number

        elif response.lower() == "not approved":
            self.status = "not approved"
#data of staff user 
    def display_requisition(self):
        print(f"Requisition ID of Staff: {self.requisition_id}")
        print(f"Date: {self.date}")
        print(f"Staff member ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print(f"Total cost: {self.total}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {self.approval_reference_number}")
        print("Requisition Items by staff:")
        for item in self.requisition_items:
            print(f"  {item['item_name']}: {item['cost']}")

    def display_requisition_statistic(self): # it will show staff's  requisition statistic

        return {
            "total_requisitions": 1,
            "total_approved": 1 if self.status == "approved" else 0,
            "total_pending": 1 if self.status == "pending" else 0,
            "total_not_approved": 1 if self.status == "not approved" else 0,
        }


def main():
    requisitions = []

    while True: #output which display
        print("1. Create a new requisition for new staff member")
        print("2. Display all requisitions collected")
        print("3. Display requisition statistics")
        print("4. Exit to the program")
        choice = input("Enter your choice: ")

        if choice == "1":
            staff_id = input("Enter staff ID: ")
            date = input("Enter date: ")
            staff_name = input("Enter staff name: ")
            requisition_items = []
            while True:
                item_name = input("Enter item name taken by Staff(or 'done' to finish): ")
                if item_name.lower() == "done":
                    break
                cost = float(input("Enter the amount: "))
                requisition_items.append({"item_name": item_name, "cost": cost})
            requisition = RequisitionSystem(staff_id, date, staff_name)
            requisition.requisition_details(requisition_items)
            requisition.requisition_approval()
            requisitions.append(requisition)
            print("Requisition created successfully for you!")

        elif choice == "2":
            for requisition in requisitions:
                requisition.display_requisition()
                print()

        elif choice == "3":
            total_requisitions = len(requisitions)
            total_approved = sum(1 for requisition in requisitions if requisition.status == "approved")
            total_pending = sum(1 for requisition in requisitions if requisition.status == "pending")
            total_not_approved = sum(1 for requisition in requisitions if requisition.status == "not approved")
            print(f"Total Requisitions: {total_requisitions}")
            print(f"Total Approved: {total_approved}")
            print(f"Total Pending: {total_pending}")
            print(f"Total Not Approved: {total_not_approved}")

        elif choice == "4":
            break

        else:
            print("Invalid number you have selected . Please try again.")


if __name__ == "__main__":
    main()

