from getpass import getpass
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Hospital Management Software Class
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



import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk

class HMSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mangeshkar HMS")
        self.hospital = Mangeshkar_hospital()  # Initialize your HMS

        self.main_menu()

    def main_menu(self):
        menu_frame = tk.Frame(self.root)
        menu_frame.pack(padx=20, pady=20)

        tk.Label(menu_frame, text="Welcome to Mangeshkar Hospital", font=("Helvetica", 16)).pack(pady=10)
        tk.Button(menu_frame, text="Admin Mode", command=self.admin_mode).pack(pady=5)
        tk.Button(menu_frame, text="User Mode", command=self.user_mode).pack(pady=5)
        tk.Button(menu_frame, text="Exit", command=self.root.destroy).pack(pady=5)

    def admin_mode(self):
        admin_password = tk.simpledialog.askstring("Admin Password", "Please enter your password:")

        if admin_password == self.hospital.admin_password:
            admin_frame = tk.Toplevel(self.root)
            admin_frame.title("Admin Mode")

            # GUI
            tk.Button(admin_frame, text="Add Patient", command=self.add_patient).pack(pady=5)
            tk.Button(admin_frame, text="Manage Doctors", command=self.manage_doctors).pack(pady=5)
            tk.Button(admin_frame, text="Manage Appointments", command=self.manage_appointments).pack(pady=5)
            

        else:
            messagebox.showerror("Invalid Password", "Incorrect password. Please try again.")
    
    def main_menu(self):
        menu_frame = tk.Frame(self.root, width=1500, height=900) 
        menu_frame.pack(padx=1, pady=1)

        #background image
        background_image = Image.open("hos.jpg")  
        background_photo = ImageTk.PhotoImage(background_image)

        background_label = tk.Label(menu_frame, image=background_photo)
        background_label.image = background_photo  
        background_label.place(x=0, y=0)

        # Add other widgets on top of the background
        tk.Label(menu_frame, text="Welcome to Mangeshkar Hospital", font=("Helvetica", 16)).pack(pady=10)
        tk.Button(menu_frame, text="Admin Mode", command=self.admin_mode).pack(pady=5)
        tk.Button(menu_frame, text="User Mode", command=self.user_mode).pack(pady=5)
        tk.Button(menu_frame, text="Exit", command=self.root.destroy).pack(pady=5)



    def display_patient(self):
        try:
            patient_ID = int(simpledialog.askstring("Display Patient", "Enter patient ID: "))
            while patient_ID not in self.Patient_db:
                patient_ID = int(simpledialog.askstring("Display Patient", "Incorrect ID, Please Enter patient ID: "))
            patient_data = self.Patient_db[patient_ID]
            messagebox.showinfo("Patient Details",
                                f"Patient name        : {patient_data[2]}\n"
                                f"Patient age         : {patient_data[3]}\n"
                                f"Patient gender      : {patient_data[4]}\n"
                                f"Patient address     : {patient_data[5]}\n"
                                f"Patient room number : {patient_data[6]}\n"
                                f"Patient is in {patient_data[0]} department\n"
                                f"Patient is followed by doctor : {patient_data[1]}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Patient ID should be an integer number")

    def delete_patient(self):
        try:
            patient_ID = int(simpledialog.askstring("Delete Patient", "Enter patient ID: "))
            while patient_ID not in self.Patient_db:
                patient_ID = int(simpledialog.askstring("Delete Patient", "Incorrect ID, Please Enter patient ID: "))
            self.Patient_db.pop(patient_ID)
            messagebox.showinfo("Success", "Patient data deleted successfully")
        except ValueError:
            messagebox.showerror("Invalid Input", "Patient ID should be an integer number")

    def edit_patient(self):
        try:
            patient_ID = int(simpledialog.askstring("Edit Patient", "Enter patient ID: "))
            while patient_ID not in self.Patient_db:
                patient_ID = int(simpledialog.askstring("Edit Patient", "Incorrect ID, Please Enter patient ID: "))
            while True:
                admin_choice = simpledialog.askstring("Edit Patient", 
                                                      "1. Edit patient Department\n"
                                                      "2. Edit Doctor following case\n"
                                                      "3. Edit patient Name\n"
                                                      "4. Edit patient Age\n"
                                                      "5. Edit patient Gender\n"
                                                      "6. Edit patient Address\n"
                                                      "7. Edit patient Room number\n"
                                                      "B. Go back\n"
                                                      "Enter your choice: ").upper()
                if admin_choice == "1":
                    self.Patient_db[patient_ID][0] = simpledialog.askstring("Edit Patient", "Enter patient department: ")
                    messagebox.showinfo("Success", "Patient Department edited successfully")
                elif admin_choice == "2":
                    self.Patient_db[patient_ID][1] = simpledialog.askstring("Edit Patient", "Enter Doctor following case: ")
                    messagebox.showinfo("Success", "Doctor following case edited successfully")
                elif admin_choice == "3":
                    self.Patient_db[patient_ID][2] = simpledialog.askstring("Edit Patient", "Enter patient name: ")
                    messagebox.showinfo("Success", "Patient name edited successfully")
                elif admin_choice == "4":
                    self.Patient_db[patient_ID][3] = simpledialog.askstring("Edit Patient", "Enter patient Age: ")
                    messagebox.showinfo("Success", "Patient age edited successfully")
                elif admin_choice == "5":
                    self.Patient_db[patient_ID][4] = simpledialog.askstring("Edit Patient", "Enter patient gender: ")
                    messagebox.showinfo("Success", "Patient gender edited successfully")
                elif admin_choice == "6":
                    self.Patient_db[patient_ID][5] = simpledialog.askstring("Edit Patient", "Enter patient address: ")
                    messagebox.showinfo("Success", "Patient address edited successfully")
                elif admin_choice == "7":
                    self.Patient_db[patient_ID][6] = simpledialog.askstring("Edit Patient", "Enter patient RoomNumber: ")
                    messagebox.showinfo("Success", "Patient RoomNumber edited successfully")
                elif admin_choice == "B":
                    break
                else:
                    messagebox.showerror("Invalid Input", "Please enter a correct choice")
        except ValueError:
            messagebox.showerror("Invalid Input", "Patient ID should be an integer number")

    def manage_doctors(self):
        while True:
            admin_choice = simpledialog.askstring("Manage Doctors", 
                                                  "1. Add a new doctor\n"
                                                  "2. Display doctor\n"
                                                  "3. Delete doctor data\n"
                                                  "4. Edit doctor data\n"
                                                  "B. Go back\n"
                                                  "Enter your choice: ").upper()

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
                messagebox.showerror("Invalid Input", "Please enter a correct choice")

    def add_doctor(self):
        try:
            doctor_ID = int(simpledialog.askstring("Add Doctor", "Enter doctor ID: "))
            while doctor_ID in self.Doctor_db:
                doctor_ID = int(simpledialog.askstring("Add Doctor", "This ID is unavailable, please try another ID: "))
            department = simpledialog.askstring("Add Doctor", "Enter Doctor department: ")
            name = simpledialog.askstring("Add Doctor", "Enter Doctor name: ")
            address = simpledialog.askstring("Add Doctor", "Enter Doctor address: ")
            self.Doctor_db[doctor_ID] = [[department, name, address]]
            messagebox.showinfo("Success", "Doctor added successfully")
        except ValueError:
            messagebox.showerror("Invalid Input", "Doctor ID should be an integer number")

    def display_doctor(self):
        try:
            doctor_ID = int(simpledialog.askstring("Display Doctor", "Enter doctor ID: "))
            while doctor_ID not in self.Doctor_db:
                doctor_ID = int(simpledialog.askstring("Display Doctor", "Incorrect ID, Please Enter doctor ID: "))
            doctor_data = self.Doctor_db[doctor_ID][0]
            messagebox.showinfo("Doctor Details",
                                f"Doctor name    : {doctor_data[1]}\n"
                                f"Doctor address : {doctor_data[2]}\n"
                                f"Doctor is in {doctor_data[0]} department")
        except ValueError:
            messagebox.showerror("Invalid Input", "Doctor ID should be an integer number")

    def delete_doctor(self):
        try:
            doctor_ID = int(simpledialog.askstring("Delete Doctor", "Enter doctor ID: "))
            while doctor_ID not in self.Doctor_db:
                doctor_ID = int(simpledialog.askstring("Delete Doctor", "Incorrect ID, Please Enter doctor ID: "))
            self.Doctor_db.pop(doctor_ID)
            messagebox.showinfo("Success", "Doctor data deleted successfully")
        except ValueError:
            messagebox.showerror("Invalid Input", "Doctor ID should be an integer number")

    def edit_doctor(self):
        try:
            doctor_ID = int(simpledialog.askstring("Edit Doctor", "Enter doctor ID: "))
            while doctor_ID not in self.Doctor_db:
                doctor_ID = int(simpledialog.askstring("Edit Doctor", "Incorrect ID, Please Enter doctor ID: "))
            while True:
                admin_choice = simpledialog.askstring("Edit Doctor", 
                                                      "1. Edit doctor's department\n"
                                                      "2. Edit doctor's name\n"
                                                      "3. Edit doctor's address\n"
                                                      "B. Go back\n"
                                                      "Enter your choice: ").upper()
                if admin_choice == "1":
                    self.Doctor_db[doctor_ID][0][0] = simpledialog.askstring("Edit Doctor", "Enter Doctor's Department: ")
                    messagebox.showinfo("Success", "Doctor's department edited successfully")
                elif admin_choice == "2":
                    self.Doctor_db[doctor_ID][0][1] = simpledialog.askstring("Edit Doctor", "Enter Doctor's Name: ")
                    messagebox.showinfo("Success", "Doctor's name edited successfully")
                elif admin_choice == "3":
                    self.Doctor_db[doctor_ID][0][2] = simpledialog.askstring("Edit Doctor", "Enter Doctor's Address: ")
                    messagebox.showinfo("Success", "Doctor's address edited successfully")
                elif admin_choice == "B":
                    break
                else:
                    messagebox.showerror("Invalid Input", "Please enter a correct choice")
        except ValueError:
            messagebox.showerror("Invalid Input", "Doctor ID should be an integer number")



    def view_departments(self):
        departments_window = tk.Toplevel(self.root)
        departments_window.title("Hospital Departments")
        
        departments_text = tk.Text(departments_window, wrap=tk.WORD, height=20, width=50)
        departments_text.pack(padx=10, pady=10)
        
        departments = []  
        for department in departments:
            departments_text.insert(tk.END, f"- {department}\n")

        close_button = tk.Button(departments_window, text="Close", command=departments_window.destroy)
        close_button.pack(pady=5)

    def view_doctors(self):
        doctors_window = tk.Toplevel(self.root)
        doctors_window.title("Hospital Doctors")
        
        doctors_text = tk.Text(doctors_window, wrap=tk.WORD, height=20, width=50)
        doctors_text.pack(padx=10, pady=10)
        
        doctors = []  
        for doctor in doctors:
            doctors_text.insert(tk.END, f"- {doctor}\n")

        close_button = tk.Button(doctors_window, text="Close", command=doctors_window.destroy)
        close_button.pack(pady=5)

    def view_patients_residents(self):
        residents_window = tk.Toplevel(self.root)
        residents_window.title("Patient Residents")
        
        residents_text = tk.Text(residents_window, wrap=tk.WORD, height=20, width=50)
        residents_text.pack(padx=10, pady=10)
        
        residents = []  
        for resident in residents:
            residents_text.insert(tk.END, f"- {resident}\n")

        close_button = tk.Button(residents_window, text="Close", command=residents_window.destroy)
        close_button.pack(pady=5)


    def view_patient_details(self):
        try:
            patient_ID = int(simpledialog.askstring("View Patient Details", "Enter patient ID: "))
            while patient_ID not in self.hospital.Patient_db:
                patient_ID = int(simpledialog.askstring("View Patient Details", "Incorrect ID, Please Enter patient ID: "))
            patient_data = self.hospital.Patient_db[patient_ID]
            messagebox.showinfo("Patient Details",
                                f"Patient name        : {patient_data[2]}\n"
                                f"Patient age         : {patient_data[3]}\n"
                                f"Patient gender      : {patient_data[4]}\n"
                                f"Patient address     : {patient_data[5]}\n"
                                f"Patient room number : {patient_data[6]}\n"
                                f"Patient is in {patient_data[0]} department\n"
                                f"Patient is followed by doctor : {patient_data[1]}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Patient ID should be an integer number")



    def manage_doctors(self):
        doctors_window = tk.Toplevel(self.root)
        doctors_window.title("Manage Doctors")

        tk.Label(doctors_window, text="Manage Doctors", font=("Helvetica", 16)).pack(pady=10)

        tk.Button(doctors_window, text="Add Doctor", command=self.add_doctor).pack(pady=5)
        tk.Button(doctors_window, text="Display Doctor", command=self.display_doctor).pack(pady=5)
        tk.Button(doctors_window, text="Delete Doctor", command=self.delete_doctor).pack(pady=5)
        tk.Button(doctors_window, text="Edit Doctor", command=self.edit_doctor).pack(pady=5)

        tk.Button(doctors_window, text="Go back", command=doctors_window.destroy).pack(pady=10)


# command line options

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

        self.view_departments_button = tk.Button(root, text="View Hospital's Departments", command=self.view_departments)
        self.view_departments_button.pack()

        self.view_doctors_button = tk.Button(root, text="View Hospital's Doctors", command=self.view_doctors)
        self.view_doctors_button.pack()

        self.view_patients_button = tk.Button(root, text="View Patients' Residents", command=self.view_patients_residents)
        self.view_patients_button.pack()

        self.view_patient_details_button = tk.Button(root, text="View Patient Details", command=self.view_patient_details)
        self.view_patient_details_button.pack()

    def display_patient(self):
        try:
            patient_ID = int(input("Enter patient ID: "))
            while patient_ID not in self.Patient_db:
                patient_ID = int(input("Incorrect ID, Please Enter patient ID: "))
            patient_data = self.Patient_db[patient_ID]
            print("\nPatient name        : ", patient_data[2])
            print("Patient age         : ", patient_data[3])
            print("Patient gender      : ", patient_data[4])
            print("Patient address     : ", patient_data[5])
            print("Patient room number : ", patient_data[6])
            print("Patient is in " + patient_data[0] + " department")
            print("Patient is followed by doctor : " + patient_data[1])
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
                appointment_index, pair_key = self.appointment_index_in_doctors_database(patient_ID)
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
                appointment_index, pair_key = self.appointment_index_in_doctors_database(patient_ID)
                self.Doctor_db[pair_key].pop(appointment_index)
                print("Appointment canceled successfully")
            except ValueError:
                print("No Appointment for this patient")

        except ValueError:
            print("Patient ID should be an integer number")

    def appointment_index_in_doctors_database(self, patient_ID):
        for i, appointments in enumerate(self.Doctor_db):
            if type(appointments[0]) != str:
                for j, appointment in enumerate(appointments):
                    if patient_ID == appointment[0]:
                        return j, i
        raise ValueError("No Appointment for this patient")



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
            patient_data = self.Patient_db[patient_id]
            print("	Patient: " + patient_data[2] + " in " + patient_data[0] + " department and followed by " +
                  patient_data[1] + ", age: " + patient_data[3] + ", from: " + patient_data[5] + ", RoomNumber: " +
                  patient_data[6])

    def view_patient_details(self):
        try:
            patient_ID = int(input("Enter patient's ID: "))
            while patient_ID not in self.Patient_db:
                patient_ID = int(input("Incorrect ID, Please enter patient ID: "))
            patient_data = self.Patient_db[patient_ID]
            print("	Patient name        : ", patient_data[2])
            print("	Patient age         : ", patient_data[3])
            print("	Patient gender      : ", patient_data[4])
            print("	Patient address     : ", patient_data[5])
            print("	Patient room number : ", patient_data[6])
            print("	Patient is in " + patient_data[0] + " department")
            print("	Patient is followed by doctor: " + patient_data[1])
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

    def add_patient(self):
        # Create a new window for adding a patient
        add_patient_window = tk.Toplevel()
        add_patient_window.title("Add Patient")

        # Create labels and entry fields
        patient_id_label = tk.Label(add_patient_window, text="Patient ID:")
        patient_id_entry = tk.Entry(add_patient_window)
        department_label = tk.Label(add_patient_window, text="Department:")
        department_entry = tk.Entry(add_patient_window)
        doctor_name_label = tk.Label(add_patient_window, text="Doctor Name:")
        doctor_name_entry = tk.Entry(add_patient_window)
        name_label = tk.Label(add_patient_window, text="Name:")
        name_entry = tk.Entry(add_patient_window)
        age_label = tk.Label(add_patient_window, text="Age:")
        age_entry = tk.Entry(add_patient_window)
        gender_label = tk.Label(add_patient_window, text="Gender:")
        gender_entry = tk.Entry(add_patient_window)
        address_label = tk.Label(add_patient_window, text="Address:")
        address_entry = tk.Entry(add_patient_window)
        room_number_label = tk.Label(add_patient_window, text="Room Number:")
        room_number_entry = tk.Entry(add_patient_window)

        # Add labels and entry fields to the window
        patient_id_label.grid(row=0, column=0)
        patient_id_entry.grid(row=0, column=1)
        department_label.grid(row=1, column=0)
        department_entry.grid(row=1, column=1)
        doctor_name_label.grid(row=2, column=0)
        doctor_name_entry.grid(row=2, column=1)
        name_label.grid(row=3, column=0)
        name_entry.grid(row=3, column=1)
        age_label.grid(row=4, column=0)
        age_entry.grid(row=4, column=1)
        gender_label.grid(row=5, column=0)
        gender_entry.grid(row=5, column=1)
        address_label.grid(row=6, column=0)
        address_entry.grid(row=6, column=1)
        room_number_label.grid(row=7, column=0)
        room_number_entry.grid(row=7, column=1)

        def save_patient():
            try:
                patient_ID = int(patient_id_entry.get())
                while patient_ID in self.hospital.Patient_db:
                    patient_ID = int(input("This ID is unavailable, please try another ID: "))
                department = department_entry.get()
                doctor_name = doctor_name_entry.get()
                name = name_entry.get()
                age = age_entry.get()
                gender = gender_entry.get()
                address = address_entry.get()
                room_number = room_number_entry.get()
                self.hospital.Patient_db[patient_ID] = [department, doctor_name, name, age, gender, address, room_number]
                messagebox.showinfo("Success", "Patient added successfully")
                add_patient_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Patient ID should be a number")

        # Create a "Save" button to save patient details
        save_button = tk.Button(add_patient_window, text="Save", command=save_patient)
        save_button.grid(row=8, columnspan=2)

    def manage_doctors(self):
        # Create a new window for managing doctors
        manage_doctors_window = tk.Toplevel()
        manage_doctors_window.title("Manage Doctors")

        # Create labels and entry fields
        doctor_id_label = tk.Label(manage_doctors_window, text="Doctor ID:")
        doctor_id_entry = tk.Entry(manage_doctors_window)
        department_label = tk.Label(manage_doctors_window, text="Department:")
        department_entry = tk.Entry(manage_doctors_window)
        name_label = tk.Label(manage_doctors_window, text="Name:")
        name_entry = tk.Entry(manage_doctors_window)
        address_label = tk.Label(manage_doctors_window, text="Address:")
        address_entry = tk.Entry(manage_doctors_window)

        # Add labels and entry fields to the window
        doctor_id_label.grid(row=0, column=0)
        doctor_id_entry.grid(row=0, column=1)
        department_label.grid(row=1, column=0)
        department_entry.grid(row=1, column=1)
        name_label.grid(row=2, column=0)
        name_entry.grid(row=2, column=1)
        address_label.grid(row=3, column=0)
        address_entry.grid(row=3, column=1)

        def save_doctor():
            try:
                doctor_ID = int(doctor_id_entry.get())
                while doctor_ID in self.hospital.Doctor_db:
                    doctor_ID = int(input("This ID is unavailable, please try another ID: "))
                department = department_entry.get()
                name = name_entry.get()
                address = address_entry.get()
                self.hospital.Doctor_db[doctor_ID] = [[department, name, address]]
                messagebox.showinfo("Success", "Doctor added successfully")
                manage_doctors_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Doctor ID should be a number")

        # Create a "Save" button to save doctor details
        save_button = tk.Button(manage_doctors_window, text="Save", command=save_doctor)
        save_button.grid(row=4, columnspan=2)

    def manage_appointments(self):
        # Create a new window for managing appointments
        manage_appointments_window = tk.Toplevel()
        manage_appointments_window.title("Manage Appointments")

        # Create labels and entry fields
        patient_id_label = tk.Label(manage_appointments_window, text="Patient ID:")
        patient_id_entry = tk.Entry(manage_appointments_window)
        doctor_id_label = tk.Label(manage_appointments_window, text="Doctor ID:")
        doctor_id_entry = tk.Entry(manage_appointments_window)
        session_start_label = tk.Label(manage_appointments_window, text="Session Start:")
        session_start_entry = tk.Entry(manage_appointments_window)
        session_end_label = tk.Label(manage_appointments_window, text="Session End:")
        session_end_entry = tk.Entry(manage_appointments_window)

        # Add labels and entry fields to the window
        patient_id_label.grid(row=0, column=0)
        patient_id_entry.grid(row=0, column=1)
        doctor_id_label.grid(row=1, column=0)
        doctor_id_entry.grid(row=1, column=1)
        session_start_label.grid(row=2, column=0)
        session_start_entry.grid(row=2, column=1)
        session_end_label.grid(row=3, column=0)
        session_end_entry.grid(row=3, column=1)

        def save_appointment():
            try:
                patient_ID = int(patient_id_entry.get())
                doctor_ID = int(doctor_id_entry.get())
                session_start = session_start_entry.get()
                session_end = session_end_entry.get()

                # Check if the doctor exists
                if doctor_ID not in self.hospital.Doctor_db:
                    messagebox.showerror("Error", "Doctor ID does not exist")
                    return

                # Check if the patient exists
                if patient_ID not in self.hospital.Patient_db:
                    messagebox.showerror("Error", "Patient ID does not exist")
                    return

                # Add appointment to the doctor's schedule
                new_appointment = [patient_ID, session_start, session_end]
                if doctor_ID in self.hospital.Doctor_db:
                    self.hospital.Doctor_db[doctor_ID].append(new_appointment)
                    messagebox.showinfo("Success", "Appointment booked successfully")
                    manage_appointments_window.destroy()
                else:
                    messagebox.showerror("Error", "Doctor ID does not exist")

            except ValueError:
                messagebox.showerror("Error", "Invalid input")

        # Create a "Save" button to save the appointment
        save_button = tk.Button(manage_appointments_window, text="Save", command=save_appointment)
        save_button.grid(row=4, columnspan=2)

    def view_departments(self):
        # Create a new window to view hospital departments in user mode
        view_departments_window = tk.Toplevel()
        view_departments_window.title("Hospital Departments")

        # Display hospital's departments
        department_text = ""
        for doctor_id in self.hospital.Doctor_db:
            department_data = self.hospital.Doctor_db[doctor_id][0]
            department_text += f"{department_data[0]}\n"
        departments_label = tk.Label(view_departments_window, text=department_text)
        departments_label.pack()

    def view_doctors(self):
        # Create a new window to view hospital doctors in user mode
        view_doctors_window = tk.Toplevel()
        view_doctors_window.title("Hospital Doctors")

        # Display hospital's doctors
        doctors_text = ""
        for doctor_id in self.hospital.Doctor_db:
            doctor_data = self.hospital.Doctor_db[doctor_id][0]
            doctors_text += f"Name: {doctor_data[1]}, Department: {doctor_data[0]}, Address: {doctor_data[2]}\n"
        doctors_label = tk.Label(view_doctors_window, text=doctors_text)
        doctors_label.pack()

    def view_patients_residents(self):
        # Create a new window to view patients and residents in user mode
        view_patients_window = tk.Toplevel()
        view_patients_window.title("Patients and Residents")

        # Display patients and residents
        patients_text = ""
        for patient_id in self.hospital.Patient_db:
            patient_data = self.hospital.Patient_db[patient_id]
            patients_text += f"Patient: {patient_data[2]}, Department: {patient_data[0]}, " \
                            f"Doctor: {patient_data[1]}, Age: {patient_data[3]}, " \
                            f"Address: {patient_data[5]}, Room Number: {patient_data[6]}\n"
        patients_label = tk.Label(view_patients_window, text=patients_text)
        patients_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = HMSApp(root)
    root.mainloop()
