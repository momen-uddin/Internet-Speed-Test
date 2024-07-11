import tkinter as tk
from tkinter import ttk
import speedtest
import threading

class SpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Internet Speed Test")
        
        self.label = ttk.Label(root, text="Press the button to start the speed test")
        self.label.pack(pady=20)
        
        self.start_button = ttk.Button(root, text="Start Test", command=self.start_test)
        self.start_button.pack(pady=10)
        
        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack(pady=20)
        
    def start_test(self):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Finding the best server...\n")
        self.start_button.config(state=tk.DISABLED)
        
        thread = threading.Thread(target=self.run_speed_test)
        thread.start()
        
    def run_speed_test(self):
        st = speedtest.Speedtest()
        
        st.get_best_server()
        
        self.result_text.insert(tk.END, "Performing download test...\n")
        download_speed = st.download() / 1_000_000  # Convert from bits/s to Mbits/s
        
        self.result_text.insert(tk.END, "Performing upload test...\n")
        upload_speed = st.upload() / 1_000_000  # Convert from bits/s to Mbits/s
        
        ping = st.results.ping
        
        result = (f"Download speed: {download_speed:.2f} Mbps\n"
                  f"Upload speed: {upload_speed:.2f} Mbps\n"
                  f"Ping: {ping:.2f} ms")
        
        self.result_text.insert(tk.END, result)
        self.start_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = SpeedTestApp(root)
    root.mainloop()
