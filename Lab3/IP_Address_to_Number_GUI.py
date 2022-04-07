import IP_Address_to_Number_Integrating_Tests as solution
from tkinter import *

#tkinter set
window = Tk()
window.title("IP Address to Number")
window.geometry("600x210")
window.minsize(600, 210)
window.maxsize(700, 220)

#data inputs
ip_to_num_input = ""
num_to_ip_input = -1

#entries functions
def convert_ip_to_num():
    funcName = "ipToNum"
    data = left_entry.get()

    left_result["text"] = test_result(solution.send_user_request(funcName, data))

def convert_num_to_ip():
    funcName = "numToIp"
    data = right_entry.get()
    test_input_data(data)
    if (test_input_data(data)):
        right_result["text"] = test_result(solution.send_user_request(funcName, data))
    else:
        right_result["text"] = "Inputed data is incorrect"

#Check returned data
def test_result(result):
    if (type(result) == int or type(result) == str):
        return result
    else:
        return "Inputed data is incorrect"

#Check input data
def test_input_data(data):
    return data.isdecimal()

#Design

#frames
left_frame = Frame(window, bg='#95baf5')
left_frame.pack_propagate(0)
left_frame.pack(fill='both', side='left', expand='True')
right_frame = Frame(window, bg='#41b55e')
right_frame.pack_propagate(0)
right_frame.pack(fill='both', side='right', expand='True')

#entries
left_entry = Entry(left_frame, width=36)
right_entry = Entry(right_frame, width=36)
left_entry.insert(END, '192.168.0.1')
right_entry.insert(END, '3232235521')
left_entry.pack(pady=25)
right_entry.pack(pady=25)

#buttons
ip_to_num_button = Button(left_frame, text="Convert IP to number", command=convert_ip_to_num,  padx=50, pady=5)
num_to_ip_button = Button(right_frame, text="Convert number to ip", command=convert_num_to_ip, padx=50, pady=5)
ip_to_num_button.pack(pady=0)
num_to_ip_button.pack(pady=0)

#labels
left_label = Label(left_frame, bg='#95baf5')
right_label = Label(right_frame, bg='#41b55e')
left_label.config(font =("Courier", 14), text = "Result:")
right_label.config(font =("Courier", 14), text = "Result:")
left_label.pack(pady=15)
right_label.pack(pady=15)

#results
left_result = Label(left_frame, bg='#95baf5')
right_result = Label(right_frame, bg='#41b55e')
left_result.config(font =("Courier", 11), text = "")
right_result.config(font =("Courier", 11), text = "")
left_result.pack(pady=0)
right_result.pack(pady=0)

mainloop()