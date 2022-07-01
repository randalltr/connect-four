def make_board():
    cell = "| |"
    rows = 7
    cols = 6
    column = ""
    print(" 1  2  3  4  5  6  7 ")
    for i in range(cols):
        for j in range(rows):
            column += cell
        print(column)
        column = ""
    print("---------------------")


make_board()
