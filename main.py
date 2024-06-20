# Hospital Management Software Class
from getpass import getpass

class Mangeshkar_hospital:
    def __init__(self):
        self.Patient_db = {}
        self.Doctor_db = {}
        self.admin_password = "1234"
        self.tries = 0

    def run(self):
        while True:
            print("\n\n  >>>> Welcome to Mangeshkar Hospital <<<<  \n")
            print("Please choose an option below: ")
            print("1. Admin ")
            print("2. User ")
            print("3. Exit\n\n")
            user_choice = input("Enter your choice : ")

            if user_choice == "1":
                self.admin_mode()
            elif user_choice == "2":
                self.user_mode()
            elif user_choice == "3":
                print("\nThank you!")
                break
            else:
                print("Please enter a valid option (1, 2, or 3).")

    def admin_mode(self):
        print("\n  >> Welcome to admin <<  \n")
        password = getpass("Please enter your password: ")

        if password == self.admin_password:
            while True:
                print("1. Manage patients  \n"
                      "2. Manage doctors  \n"
                      "3. Manage appointments \n"
                      "B. Go back      \n")
                admin_options = input("Enter your choice: ")
                admin_options = admin_options.upper()

                if admin_options == "1": 
                    self.manage_patients()

                elif admin_options == "2":  
                    self.manage_doctors()

                elif admin_options == "3":  
                    self.manage_appointments()

                elif admin_options == "B":
                    break

                else:
                    print("Please enter a correct choice\n")

        else:
            if self.tries < 2:
                password = input("Password incorrect, please try again: ")
                self.tries += 1
            else:
                print("Incorrect password, no more tries")
                return

    def manage_patients(self):
        while True:
            print("\n\n")
            print("1. Add a new patient")
            print("2. Display patient")
            print("3. Delete patient data")
            print("4. Edit patient data")
            print("B. Go back")
            print("\n\n")
            admin_choice = input("Enter option: ")
            admin_choice = admin_choice.upper()

            if admin_choice == "1":  
                self.add_patient()

            elif admin_choice == "2":  
                self.display_patient()

            elif admin_choice == "3":  
                self.delete_patient()

            elif admin_choice == "4":  
                self.edit_patient()

            elif admin_choice == "B":  
                break

            else:
                print("Please enter a correct choice\n")

    def add_patient(self):
        try:
            patient_ID = int(input("Enter patient ID: "))
            while patient_ID in self.Patient_db:
                patient_ID = int(input("This ID is unavailable, please try another ID: "))
            department = input("Enter patient department: ")
            doctor_name = input("Enter name of doctor following the case: ")
            name = input("Enter patient name: ")
            age = input("Enter patient age: ")
            gender = input("Enter patient gender: ")
            address = input("Enter patient address: ")
            room_number = input("Enter patient room number: ")
            self.Patient_db[patient_ID] = [department, doctor_name, name, age, gender, address, room_number]
            print("Patient added successfully")
        except ValueError:
            print("Patient ID should be a number")

    def display_patient(self):
        try:
            patient_ID = int(input("Enter patient ID: "))
            while patient_ID not in self.Patient_db:
                patient_ID = int(input("Incorrect ID, Please Enter patient ID: "))
            Patient_db = self.Patient_db[patient_ID]
            print("\nPatient name        : ", Patient_db[2])
            print("Patient age         : ", Patient_db[3])
            print("Patient gender      : ", Patient_db[4])
            print("Patient address     : ", Patient_db[5])
            print("Patient room number : ", Patient_db[6])
            print("Patient is in " + Patient_db[0] + " department")
            print("Patient is followed by doctor : " + Patient_db[1])
        except ValueError:
            print("Patient ID should be an integer number")

    def delete_patient(self):
        try:
            patient_ID = int(input("Enter patient ID: "))
            while patient_ID not in self.Patient_db:
                patient_ID = int(input("Incorrect ID, Please Enter patient ID: "))
            self.Patient_db.pop(patient_ID)
            print("Patient data deleted successfully")
        except ValueError:
            print("Patient ID should be an integer number")

    def edit_patient(self):
        try:
            patient_ID = int(input("Enter patient ID: "))
            while patient_ID not in self.Patient_db:
                patient_ID = int(input("Incorrect ID, Please Enter patient ID: "))
            while True:
                print("\n\n")
                print("1. Edit patient Department")
                print("2. Edit Doctor following case ")
                print("3. Edit patient Name")
                print("4. Edit patient Age")
                print("5. Edit patient Gender")
                print("6. Edit patient Address")
                print("7. Edit patient Room mumber")
                print("B. Go back")
                print("\n\n")
                admin_choice = input("Enter your choice: ")
                admin_choice = admin_choice.upper()
                if admin_choice == "1":
                    self.Patient_db[patient_ID][0] = input("\nEnter patient department: ")
                    print("Patient Department edited successfully")
                elif admin_choice == "2":
                    self.Patient_db[patient_ID][1] = input("\nEnter Doctor following case: ")
                    print("Doctor following case edited successfully")
                elif admin_choice == "3":
                    self.Patient_db[patient_ID][2] = input("\nEnter patient name: ")
                    print("Patient name edited successfully")
                elif admin_choice == "4":
                    self.Patient_db[patient_ID][3] = input("\nEnter patient Age: ")
                    print("Patient age edited successfully")
                elif admin_choice == "5":
                    self.Patient_db[patient_ID][4] = input("\nEnter patient gender: ")
                    print("Patient gender edited successfully")
                elif admin_choice == "6":
                    self.Patient_db[patient_ID][5] = input("\nEnter patient address: ")
                    print("Patient address edited successfully")
                elif admin_choice == "7":
                    self.Patient_db[patient_ID][6] = input("\nEnter patient RoomNumber: ")
                    print("Patient RoomNumber edited successfully")
                elif admin_choice == "B":
                    break
                else:
                    print("Please enter a correct choice")
        except ValueError:
            print("Patient ID should be an integer number")

    def manage_doctors(self):
        while True:
            print("\n\n")
            print("1. Add a new doctor")
            print("2. Display doctor")
            print("3. Delete doctor data")
            print("4. Edit doctor data")
            print("B. Go back")
            print("\n\n")
            admin_choice = input("Enter your choice: ")
            admin_choice = admin_choice.upper()

            if admin_choice == "1": 
                self.add_doctor()

            elif admin_choice == "2": 
                self.display_doctor()

            elif admin_choice == "3":  
                self.delete_doctor()

            elif admin_choice == "4": 
                self.edit_doctor()

            elif admin_choice == "B":  
                break

            else:
                print("Please enter a correct choice")

    def add_doctor(self):
        try:
            doctor_ID = int(input("Enter doctor ID: "))
            while doctor_ID in self.Doctor_db:
                doctor_ID = int(input("This ID is unavailable, please try another ID: "))
            department = input("Enter Doctor department: ")
            name = input("Enter Doctor name: ")
            address = input("Enter Doctor address: ")
            self.Doctor_db[doctor_ID] = [[department, name, address]]
            print("Doctor added successfully")
        except ValueError:
            print("Doctor ID should be an integer number")

    def display_doctor(self):
        try:
            doctor_ID = int(input("Enter doctor ID: "))
            while doctor_ID not in self.Doctor_db:
                doctor_ID = int(input("Incorrect ID, Please Enter doctor ID: "))
            doctor_data = self.Doctor_db[doctor_ID][0]
            print("Doctor name    : ", doctor_data[1])
            print("Doctor address : ", doctor_data[2])
            print("Doctor is in " + doctor_data[0] + " department")
        except ValueError:
            print("Doctor ID should be an integer number")

    def delete_doctor(self):
        try:
            doctor_ID = int(input("Enter doctor ID: "))
            while doctor_ID not in self.Doctor_db:
                doctor_ID = int(input("Incorrect ID, Please Enter doctor ID: "))
            self.Doctor_db.pop(doctor_ID)
            print("Doctor data deleted successfully")
        except ValueError:
            print("Doctor ID should be an integer number")

    def edit_doctor(self):
        try:
            doctor_ID = int(input("Enter doctor ID: "))
            while doctor_ID not in self.Doctor_db:
                doctor_ID = int(input("Incorrect ID, Please Enter doctor ID: "))
            while True:
                print("\n\n")
                print("1. Edit doctor's department")
                print("2. Edit doctor's name")
                print("3. Edit doctor's address")
                print("B. Go back")
                print("\n\n")
                admin_choice = input("Enter your choice: ")
                admin_choice = admin_choice.upper()
                if admin_choice == "1":
                    self.Doctor_db[doctor_ID][0][0] = input("Enter Doctor's Department: ")
                    print("Doctor's department edited successfully")
                elif admin_choice == "2":
                    self.Doctor_db[doctor_ID][0][1] = input("Enter Doctor's Name: ")
                    print("Doctor's name edited successfully")
                elif admin_choice == "3":
                    self.Doctor_db[doctor_ID][0][2] = input("Enter Doctor's Address: ")
                    print("Doctor's address edited successfully")
                elif admin_choice == "B":
                    break
                else:
                    print("Please enter a correct choice")
        except ValueError:
            print("Doctor ID should be an integer number")

    def manage_appointments(self):
        while True:
            print("\n\n")
            print("1. Book an appointment")
            print("2. Edit an appointment")
            print("3. Cancel an appointment")
            print("B. To go back")
            print("\n\n")
            admin_choice = input("Enter your choice: ")
            admin_choice = admin_choice.upper()

            if admin_choice == "1":  
                self.book_appointment()

            elif admin_choice == "2":  
                self.edit_appointment()

            elif admin_choice == "3":  
                self.cancel_appointment()

            elif admin_choice == "B":  
                break

            else:
                print("Please enter a correct choice")

    def book_appointment(self):
        try:
            doctor_ID = int(input("Enter the ID of doctor: "))
            while doctor_ID not in self.Doctor_db:
                doctor_ID = int(input("Doctor ID incorrect, Please enter a correct doctor ID: "))

            print("\n\n")
            print("1. Book an appointment for an existing patient\n"
                  "2. Book an appointment for a new patient\n"
                  "3. Go back")
            print("\n\n")
            admin_choice = input("Enter your choice: ")
            admin_choice = admin_choice.upper()

            if admin_choice == "1":
                patient_ID = int(input("Enter patient ID: "))
                while patient_ID not in self.Patient_db:
                    patient_ID = int(input("Incorrect ID, please Enter a correct patient ID: "))

            elif admin_choice == "2":
                patient_ID = int(input("Enter patient ID: "))
                while patient_ID in self.Patient_db:
                    patient_ID = int(input("This ID is unavailable, please try another ID: "))
                department = self.Doctor_db[doctor_ID][0][0]
                doctor_name = self.Doctor_db[doctor_ID][0][1]
                name = input("Enter patient name: ")
                age = input("Enter patient age: ")
                gender = input("Enter patient gender: ")
                address = input("Enter patient address: ")
                room_number = ""
                self.Patient_db[patient_ID] = [department, doctor_name, name, age, gender, address, room_number]

            elif admin_choice == "B":
                return

            session_start = input("Session starts at: ")
            while session_start[:2] == "11" or session_start[:2] == "12":
                session_start = input("Appointments should be between 01:00PM to 10:00PM,"
                                      "Please enter a time between working hours: ")

            for appointment in self.Doctor_db[doctor_ID]:
                if type(appointment[0]) != str:
                    while session_start >= appointment[1] and session_start < appointment[2]:
                        session_start = input("This appointment is already booked, "
                                              "Please Enter another time for the start of session: ")
            session_end = input("Session ends at: ")

            new_appointment = [patient_ID, session_start, session_end]
            self.Doctor_db[doctor_ID].append(new_appointment)
            print("Appointment booked successfully")

        except ValueError:
            print("Doctor ID should be an integer number")

    def edit_appointment(self):
        try:
            patient_ID = int(input("Enter patient ID: "))
            while patient_ID not in self.Patient_db:
                patient_ID = int(input("Incorrect Id, Please Enter correct patient ID: "))

            try:
                appointment_index, pair_key = self.appointment_index_in_Doctor_db(patient_ID)
                session_start = input("Please enter the new start time: ")
                while session_start[:2] == "11" or session_start[:2] == "12":
                    session_start = input("Appointments should be between 01:00PM to 10:00PM,"
                                          "Please enter a time between working hours: ")

                for appointment in self.Doctor_db[pair_key]:
                    if type(appointment[0]) != str:
                        while session_start >= appointment[1] and session_start < appointment[2]:
                            session_start = input("This appointment is already booked, "
                                                  "Please Enter another time for the start of session: ")
                session_end = input("Please enter the new end time: ")
                self.Doctor_db[pair_key][appointment_index] = [patient_ID, session_start, session_end]
                print("Appointment edited successfully")
            except ValueError:
                print("No Appointment for this patient")

        except ValueError:
            print("Patient ID should be an integer number")

    def cancel_appointment(self):
        try:
            patient_ID = int(input("Enter patient ID: "))
            while patient_ID not in self.Patient_db:
                patient_ID = int(input("Incorrect ID, Please Enter patient ID: "))

            try:
                appointment_index, pair_key = self.appointment_index_in_Doctor_db(patient_ID)
                self.Doctor_db[pair_key].pop(appointment_index)
                print("Appointment canceled successfully")
            except ValueError:
                print("No Appointment for this patient")

        except ValueError:
            print("Patient ID should be an integer number")

    def appointment_index_in_Doctor_db(self, patient_ID):
        for i, appointments in enumerate(self.Doctor_db):
            if type(appointments[0]) != str:
                for j, appointment in enumerate(appointments):
                    if patient_ID == appointment[0]:
                        return j, i
        raise ValueError("No Appointment for this patient")

    def user_mode(self):
        print("\n >> Welcome to user mode << \n")
        while True:
            print("\n\n")
            print("1. View hospital's departments")
            print("2. View hospital's doctors")
            print("3. View patients' residents")
            print("4. View patient's details")
            print("5. View doctor's appointments")
            print("B. Go back")
            print("\n\n")
            user_choice = input("Enter your choice: ")
            user_choice = user_choice.upper()

            if user_choice == "1": 
                self.view_departments()

            elif user_choice == "2":  
                self.view_doctors()

            elif user_choice == "3":  
                self.view_patients_residents()

            elif user_choice == "4":  
                self.view_patient_details()

            elif user_choice == "5": 
                self.view_doctor_appointments()

            elif user_choice == "B":  
                break

            else:
                print("Please Enter a correct choice")

    def view_departments(self):
        print("Hospital's departments:")
        for doctor_id in self.Doctor_db:
            print("	" + self.Doctor_db[doctor_id][0][0])

    def view_doctors(self):
        print("Hospital's doctors:")
        for doctor_id in self.Doctor_db:
            doctor_data = self.Doctor_db[doctor_id][0]
            print("	" + doctor_data[1] + " in " + doctor_data[0] + " department, from " + doctor_data[2])

    def view_patients_residents(self):
        for patient_id in self.Patient_db:
            Patient_db = self.Patient_db[patient_id]
            print("	Patient: " + Patient_db[2] + " in " + Patient_db[0] + " department and followed by " +
                  Patient_db[1] + ", age: " + Patient_db[3] + ", from: " + Patient_db[5] + ", RoomNumber: " +
                  Patient_db[6])

    def view_patient_details(self):
        try:
            patient_ID = int(input("Enter patient's ID: "))
            while patient_ID not in self.Patient_db:
                patient_ID = int(input("Incorrect ID, Please enter patient ID: "))
            Patient_db = self.Patient_db[patient_ID]
            print("	Patient name        : ", Patient_db[2])
            print("	Patient age         : ", Patient_db[3])
            print("	Patient gender      : ", Patient_db[4])
            print("	Patient address     : ", Patient_db[5])
            print("	Patient room number : ", Patient_db[6])
            print("	Patient is in " + Patient_db[0] + " department")
            print("	Patient is followed by doctor: " + Patient_db[1])
        except ValueError:
            print("Patient ID should be an integer number")

    def view_doctor_appointments(self):
        try:
            doctor_ID = int(input("Enter doctor's ID: "))
            while doctor_ID not in self.Doctor_db:
                doctor_ID = int(input("Incorrect ID, Please enter doctor ID: "))
            doctor_name = self.Doctor_db[doctor_ID][0][1]
            print(doctor_name + " has appointments:")
            for appointment in self.Doctor_db[doctor_ID]:
                if type(appointment[0]) == str:
                    continue
                else:
                    print("	from: " + appointment[1] + " to: " + appointment[2] + ", patient ID: " + str(appointment[0]))
        except ValueError:
            print("Doctor ID should be an integer number")


if __name__ == "__main__":
    hms = Mangeshkar_hospital()
    hms.run()
