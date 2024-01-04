import calendar

resu = calendar.calendar(1800)

desktop_path = r'C:\Users\godsu\Desktop\Python Video' 

file_path = desktop_path + r'\calendar_2004.pdf'

with open(file_path, 'w') as file:
    file.write(resu)

print(f"Calendar for 2004 saved to: {file_path}")
