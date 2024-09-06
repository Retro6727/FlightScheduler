import tkinter as tk
from tkinter import messagebox

class Flightscheduler:
    def __init__(self, root):
        self.flight_list = {}
        self.root = root
        self.root.title("Flight Scheduler")

        # Create Labels and Entry fields for adding/updating flights
        tk.Label(root, text="Flight No:").grid(row=0, column=0)
        tk.Label(root, text="Flight Name:").grid(row=1, column=0)
        tk.Label(root, text="Source:").grid(row=2, column=0)
        tk.Label(root, text="Destination:").grid(row=3, column=0)
        tk.Label(root, text="Time Arrived:").grid(row=4, column=0)
        tk.Label(root, text="Departure Time:").grid(row=5, column=0)
        tk.Label(root, text="Gate:").grid(row=6, column=0)
        tk.Label(root, text="Remarks:").grid(row=7, column=0)

        self.flight_no_entry = tk.Entry(root)
        self.flight_name_entry = tk.Entry(root)
        self.source_entry = tk.Entry(root)
        self.destination_entry = tk.Entry(root)
        self.time_arrived_entry = tk.Entry(root)
        self.departure_time_entry = tk.Entry(root)
        self.gate_entry = tk.Entry(root)
        self.remarks_entry = tk.Entry(root)

        self.flight_no_entry.grid(row=0, column=1)
        self.flight_name_entry.grid(row=1, column=1)
        self.source_entry.grid(row=2, column=1)
        self.destination_entry.grid(row=3, column=1)
        self.time_arrived_entry.grid(row=4, column=1)
        self.departure_time_entry.grid(row=5, column=1)
        self.gate_entry.grid(row=6, column=1)
        self.remarks_entry.grid(row=7, column=1)

        # Buttons for operations
        tk.Button(root, text="Add Flight", command=self.adddata).grid(row=8, column=0)
        tk.Button(root, text="Search Flight", command=self.searchflight).grid(row=8, column=1)
        tk.Button(root, text="Show All Flights", command=self.showdata).grid(row=9, column=0, columnspan=2)

        # Text widget to display results
        self.result_box = tk.Text(root, height=10, width=50)
        self.result_box.grid(row=10, column=0, columnspan=2)

    def adddata(self):
        flight_no = self.flight_no_entry.get()
        flight_name = self.flight_name_entry.get()
        source = self.source_entry.get()
        destination = self.destination_entry.get()
        time_arrived = self.time_arrived_entry.get()
        departure_time = self.departure_time_entry.get()
        gate = self.gate_entry.get()
        remarks = self.remarks_entry.get()

        if flight_no and flight_name and source and destination:
            self.flight_list[flight_no] = {
                "flight_name": flight_name,
                "source": source,
                "destination": destination,
                "time_arrived": time_arrived,
                "departure_time": departure_time,
                "gate": gate,
                "remarks": remarks
            }
            messagebox.showinfo("Success", f"Flight {flight_no} added successfully.")
        else:
            messagebox.showwarning("Input Error", "Please fill out all fields.")

    def searchflight(self):
        flight_no = self.flight_no_entry.get()
        if flight_no in self.flight_list:
            details = self.flight_list[flight_no]
            self.result_box.delete(1.0, tk.END)
            self.result_box.insert(tk.END, f"Flight {flight_no} found:\n")
            self.result_box.insert(tk.END, f"{details['flight_name']}, {details['source']}, {details['destination']}, {details['time_arrived']}, {details['departure_time']}, {details['gate']}, {details['remarks']}\n")
        else:
            messagebox.showwarning("Not Found", f"Flight {flight_no} not found.")
    
    def showdata(self):
        self.result_box.delete(1.0, tk.END)
        if self.flight_list:
            for flight_no, details in self.flight_list.items():
                self.result_box.insert(tk.END, f"{flight_no}: {details['flight_name']}, {details['source']}, {details['destination']}, {details['time_arrived']}, {details['departure_time']}, {details['gate']}, {details['remarks']}\n")
        else:
            self.result_box.insert(tk.END, "No flight data available.\n")

# Create a root window and pass it to the Flightscheduler
root = tk.Tk()
app = Flightscheduler(root)
root.mainloop()
