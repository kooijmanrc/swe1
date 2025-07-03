import tkinter as tk
from tkinter import messagebox
import configparser
import os

# --- Configuration ---
CONFIG_FILE = 'config.ini'
MESSAGE_SECTION = 'Settings'
MESSAGE_KEY = 'greeting_message'
DEFAULT_MESSAGE = 'Hello, World!' # Fallback message if config fails

def create_config_file():
    """
    Creates a configuration file with the default message if it doesn't exist.
    """
    if not os.path.exists(CONFIG_FILE):
        config = configparser.ConfigParser()
        config[MESSAGE_SECTION] = {MESSAGE_KEY: "hello swe swe"}
        with open(CONFIG_FILE, 'w') as configfile:
            config.write(configfile)
        print(f"Created default configuration file: {CONFIG_FILE}")

def get_message_from_config():
    """
    Reads the message from the configuration file.
    If the file or key is not found, it returns a default message.
    """
    config = configparser.ConfigParser()
    try:
        config.read(CONFIG_FILE)
        message = config[MESSAGE_SECTION][MESSAGE_KEY]
        return message
    except (configparser.Error, KeyError) as e:
        print(f"Error reading configuration file: {e}. Using default message.")
        return DEFAULT_MESSAGE

def show_message():
    """
    Function called when the button is pressed.
    It retrieves the message from the config and displays it in a messagebox.
    """
    message = get_message_from_config()
    messagebox.showinfo("Message", message)

# --- Main Application Window ---
def main():
    # Ensure the configuration file exists before starting the GUI
    create_config_file()

    root = tk.Tk()
    root.title("Message App")
    root.geometry("300x150") # Set initial window size

    # Create a button
    # The 'command' argument links the button click to the 'show_message' function
    message_button = tk.Button(root, text="Click Me!", command=show_message)
    message_button.pack(pady=40) # Add some padding around the button

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()