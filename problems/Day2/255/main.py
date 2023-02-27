coordinate_of_queen_1 = int(input())
coordinate_of_queen_2 = int(input())
coordinate_of_figure_1 = int(input())
coordinate_of_figure_2 = int(input())

if coordinate_of_queen_1 == coordinate_of_figure_1 or coordinate_of_figure_2 == coordinate_of_figure_2:
    print("YES")
elif coordinate_of_queen_1 + coordinate_of_figure_1 == coordinate_of_queen_2 + coordinate_of_figure_2:
    print("YES")
elif coordinate_of_queen_1 - coordinate_of_figure_1 == coordinate_of_queen_2 - coordinate_of_figure_2:
    print("YES")
else:
    print("NO")