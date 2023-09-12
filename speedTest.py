import speedtest
import tkinter as tk

def run_speed_test():

    test = speedtest.Speedtest()
    download = test.download()
    upload = test.upload()

    download_label.config(text= f"Speed of Download: {download / 1_000_000:.2f}Mbps")
    upload_label.config(text= f"Speed of Upload: {upload / 1_000_000:.2f}Mbps")

root = tk.Tk()
root.title("Speed Test")

download_label = tk.Label(root, text="", font=("Helvetica",14))
download_label.pack(pady=10)
upload_label = tk.Label(root, text="", font=("Helvetica",14))
upload_label.pack(pady=10)

test_button = tk.Button(root, text="Start Speed Test", command=run_speed_test)
test_button.pack(pady=10)

root.mainloop()