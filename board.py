cell = "| |"
rows = 7
cols = 6
column = ""

for i in range(cols):
    for j in range(rows):
        column += cell
    print(column)
    column = ""
