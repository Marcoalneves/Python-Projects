import pyspeedtest
from tkinter import *

app = Tk()
app.title('Speed Tester')
app.geometry('1500x1000')
app.resizable(width=0, height=0)
app.configure(bg='#000000')

ping_speed = StringVar()
down_speed = StringVar()

heading_text = Label(app, text='Internet Speed Checker Application',font='Arial 14 bold', bg='#000000', fg='#ffffff')
heading_text.grid(row=0, column=1, pady=20)
web_url = Label(app, text='Speed Tester',font='Arial 14 bold',bg='#000000', fg='#ffffff')
web_url.grid(row=1, column=0, padx=10)
ping_result = Label(app, text='Ping Result:', font='Arial 14 bold',bg='#000000', fg='#ffffff')
ping_result.grid(row=3, column=0, padx=10)
download_result = Label(app, text='Download Result:', font='Arial 14 bold',bg='#000000', fg='#ffffff')
download_result.grid(row=4, column=0, padx=200, pady=10)

result1 = Label(app, text="", textvariable=ping_speed, font='Arial 14', fg='#ffffff', bg='#000000')
result1.grid(row=3, column=1)
result2 = Label(app, text="", textvariable=down_speed, font='Arial 14', fg='#ffffff', bg='#000000')
result2.grid(row=4, column=1)

url_entry = Entry(app, width=25, font='Arial 14 bold')
url_entry.grid(row=1, column=1)

def speed_test():
    internet = pyspeedtest.SpeedTest(url_entry.get())
    ping_speed.set(internet.ping())
    down_speed.set(internet.download())


btn = Button(app, text="Check Speed Here", fg='#ffffff', bg='#000000', border=5, command=speed_test)
btn.grid(row=2, column=1, pady=10)

app.mainloop()