from datetime import date

class ServiceRequest:
    # Constructor to initialize a new service request
    def __init__(self, service_request_id, name, surname, address, mobile_number, service_description, date_posted):
        """
        Initialize a new ServiceRequest object with the required attributes.
        """
        self.service_request_id = service_request_id  # Unique ID for the service request
        self.name = name  # Name of the PetOwner
        self.surname = surname  # Surname of the PetOwner
        self.address = address  # Address of the PetOwner
        self.mobile_number = mobile_number  # Contact number of the PetOwner
        self.service_description = service_description  # Description of the service requested
        self.date_posted = date_posted  # Date when the service request was posted
        self.date_filled = None  # Date when the service request was filled (initially None)
        self.pet_care_professional_hired = None  # Reference to the PetCareProfessional hired for this request (initially None)

    # Method to create a new service request
    def create_request(self):
        """
        Logic to create a new service request. This could involve saving the request in the database.
        """
        # Placeholder for actual database save logic (Django ORM)
        print(f"Service request for {self.name} {self.surname} created.")

    # Method to update an existing service request
    def update_request(self, new_service_description=None, new_address=None, new_mobile_number=None):
        """
        Logic to update an existing service request with new information.
        """
        if new_service_description:
            self.service_description = new_service_description
        if new_address:
            self.address = new_address
        if new_mobile_number:
            self.mobile_number = new_mobile_number
        print(f"Service request {self.service_request_id} updated.")

    # Method to cancel an existing service request
    def cancel_request(self):
        """
        Logic to cancel the service request. May include flagging it as canceled in the database.
        """
        # Placeholder for actual cancellation logic
        print(f"Service request {self.service_request_id} canceled.")

    # Method to mark the request as filled by a hired professional
    def mark_filled(self, pet_care_professional):
        """
        Logic to mark the service request as filled by a specific PetCareProfessional.
        """
        self.pet_care_professional_hired = pet_care_professional  # Associate the hired professional
        self.date_filled = date.today()  # Set the date when the service was filled
        print(f"Service request {self.service_request_id} filled by {self.pet_care_professional_hired}.")

    # Method to display the service request details
    def display_request_details(self):
        """
        Logic to display the details of the service request.
        """
        print(f"Service Request ID: {self.service_request_id}")
        print(f"Owner: {self.name} {self.surname}")
        print(f"Service Description: {self.service_description}")
        print(f"Date Posted: {self.date_posted}")
        print(f"Date Filled: {self.date_filled if self.date_filled else 'Not yet filled'}")
        print(f"Pet Care Professional Hired: {self.pet_care_professional_hired if self.pet_care_professional_hired else 'None'}")

# Example usage:
if __name__ == "__main__":
    # Creating a new service request
    service_request = ServiceRequest(
        service_request_id="SR001",
        name="John",
        surname="Doe",
        address="123 Pet Street",
        mobile_number="123-456-7890",
        service_description="Dog grooming",
        date_posted=date.today()
    )

    # Displaying the service request details
    service_request.display_request_details()

    # Updating the service request
    service_request.update_request(new_service_description="Cat grooming", new_address="456 Pet Avenue")

    # Marking the request as filled
    service_request.mark_filled("Jane Smith, Groomer")

    # Displaying updated details
    service_request.display_request_details()

    # Canceling the request
    service_request.cancel_request()
