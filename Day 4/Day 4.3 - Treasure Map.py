# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Enter the coordinates with no spaces. ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# column first, row second

h_pos = int(position[0])
v_pos = int(position[1])
# selected_row = map[v_pos - 1]
# selected_row[h_pos -1 ] = "X"
map[v_pos - 1][h_pos - 1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")