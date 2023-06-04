import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import datetime
import threading
import time

class ReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reminder App")
        self.root.geometry("251x275")
        self.root.resizable(False, False)

        self.scrollbar_style = ttk.Style()
        self.scrollbar_style.configure("My.Vertical.TScrollbar", background="#000000")

        self.events = []

        self.event_label = tk.Label(root, text="Event:")
        self.event_label.pack()
        self.event_entry = tk.Entry(root)
        self.event_entry.pack()

        self.time_label = tk.Label(root, text="Time (HH:MM):")
        self.time_label.pack()
        self.time_entry = tk.Entry(root)
        self.time_entry.pack()

        self.days_label = tk.Label(root, text="Number of Days (optional):")
        self.days_label.pack()
        self.days_entry = tk.Entry(root)
        self.days_entry.pack()

        self.add_button = tk.Button(root, text="Add Reminder", command=self.show_popup)
        self.add_button.pack()

        self.scrollbar = ttk.Scrollbar(root, style="My.Vertical.TScrollbar")
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.reminders_canvas = tk.Canvas(root, yscrollcommand=self.scrollbar.set)
        self.reminders_canvas.pack(fill=tk.BOTH, expand=True)

        self.reminders_frame = tk.Frame(self.reminders_canvas)
        self.reminders_frame.pack(fill=tk.BOTH, expand=True)

        self.scrollbar.config(command=self.reminders_canvas.yview)
        self.reminders_canvas.create_window((0, 0), window=self.reminders_frame, anchor=tk.NW)

        self.reminders_frame.bind("<Configure>", self.adjust_canvas_scrollregion)

    def show_popup(self):
        event = self.event_entry.get().strip()
        time_text = self.time_entry.get().strip()
        days_text = self.days_entry.get().strip()

        if not event or not time_text:
            self.show_error("Event and time are required.")
            return

        event_time = self.parse_time(time_text)
        if event_time is None:
            self.show_error("Invalid time format. Please use HH:MM.")
            return

        if days_text:
            try:
                days = int(days_text)
            except ValueError:
                self.show_error("Invalid number of days. Please enter a valid integer.")
                return
        else:
            days = 0

        reminder = {
            "event": event,
            "time": event_time,
            "days": days
        }
        self.events.append(reminder)
        self.display_reminder(reminder)

        self.event_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.days_entry.delete(0, tk.END)

        threading.Thread(target=self.start_countdown, args=(reminder,), daemon=True).start()

    def display_reminder(self, reminder):
        reminder_frame = tk.Frame(self.reminders_frame)
        reminder_frame.pack()

        reminder_text = f"Event: {reminder['event']} - Time: {reminder['time'].strftime('%H:%M')}"
        reminder_label = tk.Label(reminder_frame, text=reminder_text)
        reminder_label.pack(side=tk.LEFT)

        cancel_button = tk.Button(reminder_frame, text="Cancel", command=lambda: self.cancel_reminder(reminder, reminder_frame))
        cancel_button.pack(side=tk.LEFT)

    def start_countdown(self, reminder):
        event_time = reminder["time"]
        days = reminder["days"]

        current_time = datetime.datetime.now()
        target_date = current_time + datetime.timedelta(days=days)
        target_time = datetime.datetime.combine(target_date.date(), event_time)

        countdown_label = tk.Label(self.reminders_frame, text="")
        countdown_label.pack()

        while True:
            current_time = datetime.datetime.now()
            remaining_time = target_time - current_time

            if remaining_time.total_seconds() <= 0:
                self.show_reminder_popup(reminder, countdown_label)
                break

            countdown = self.format_countdown(remaining_time.total_seconds())
            countdown_label.config(text=countdown, fg="black" if countdown != "00:00:00" else "red")
            time.sleep(1)

    def format_countdown(self, seconds):
        minutes, seconds = divmod(int(seconds), 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def show_reminder_popup(self, reminder, countdown_label):
        reminder_text = f"Event: {reminder['event']}"
        popup_window = tk.Toplevel(self.root)
        popup_window.title("Reminder")
        popup_window.geometry("300x200")
        popup_window.resizable(False, False)
        popup_label = tk.Label(popup_window, text=reminder_text, font=("Arial", 14), fg="red")
        popup_label.pack(pady=20)
        ok_button = tk.Button(popup_window, text="OK", font=("Arial", 12), command=popup_window.destroy)
        ok_button.pack()
        popup_window.focus_force()
        countdown_label.destroy()

    def cancel_reminder(self, reminder, reminder_frame):
        self.events.remove(reminder)
        reminder_frame.destroy()

    def parse_time(self, time_text):
        try:
            event_time = datetime.datetime.strptime(time_text, "%H:%M").time()
            return event_time
        except ValueError:
            return None

    def show_error(self, message):
        messagebox.showerror("Error", message)

    def adjust_canvas_scrollregion(self, event):
        self.reminders_canvas.configure(scrollregion=self.reminders_canvas.bbox("all"))

if __name__ == "__main__":
    root = tk.Tk()
    app = ReminderApp(root)
    root.mainloop()
