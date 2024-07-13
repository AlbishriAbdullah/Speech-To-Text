import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import mysql.connector
import threading

# Recognize speech and insert it into text box and database
def recognize_speech():
    start_button.config(state=tk.DISABLED)  # Disable button during recognition
    loading_label.config(text="Listening...")
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source)
            loading_label.config(text="Processing...")
            text = recognizer.recognize_sphinx(audio)
            if not text:
                raise sr.UnknownValueError("No text recognized")
            text_box.insert(tk.END, text + '\n')
            save_to_database(text)
            loading_label.config(text="Done")
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Could not understand audio. Please speak more clearly.")
            loading_label.config(text="")
        except sr.RequestError as e:
            messagebox.showerror("Error", f"Could not request results; {e}")
            loading_label.config(text="")
    start_button.config(state=tk.NORMAL)  # Re-enable button after recognition

# Save text to MySQL database
def save_to_database(text):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="speech_text_db"
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO speech_text (text) VALUES (%s)", (text,))
        conn.commit()
        cursor.close()
        conn.close()
        print("Text saved to database successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        messagebox.showerror("Database Error", f"Error: {err}")

# Start the speech recognition in a new thread
def start_recognition_thread():
    threading.Thread(target=recognize_speech).start()

# User Interface
root = tk.Tk()
root.title("Speech to Text recognition")

text_box_frame = tk.Frame(root)
text_box_frame.pack(pady=10)
text_box_scrollbar = tk.Scrollbar(text_box_frame)
text_box_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_box = tk.Text(text_box_frame, height=10, width=50, yscrollcommand=text_box_scrollbar.set)
text_box.pack()
text_box_scrollbar.config(command=text_box.yview)

loading_label = tk.Label(root, text="")
loading_label.pack()

start_button = tk.Button(root, text="Start Recording",bg="RED",command=start_recognition_thread)
start_button.pack(pady=10)

root.mainloop()
