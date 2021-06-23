from prettytable import PrettyTable

x = PrettyTable()

x.field_names = ["Name of Student", "Roll No.", "Marks"]
x.add_row(["Devansh", 25, 51])
x.add_row(["Megh", 33, 95])
x.add_row(["Dwija", 3, 75])
x.add_row(["Sujal", 61, 70])
x.add_row(["Kirtan", 35, 80])
x.add_row(["Jainam", 52, 79])
x.add_row(["Dhruvil", 50, 92])

print(x)