import datetime

from board import ParagonBoard
from node import ParagonNode, Rarity


def build_board():
    board = ParagonBoard(entry_points=[(0, 4)], rows=15, columns=9)

    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 0, 3)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 0, 4)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 0, 5)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 1, 2)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 1, 3)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 1, 4)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 1, 5)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 1, 6)
    board.add_node(ParagonNode({}, rarity=Rarity.MAGIC), 2, 2)
    board.add_node(ParagonNode({}, rarity=Rarity.MAGIC), 2, 6)
    board.add_node(ParagonNode({}, rarity=Rarity.RARE), 3, 2)
    board.add_node(ParagonNode({}, rarity=Rarity.MAGIC), 3, 3)
    board.add_node(ParagonNode({}, rarity=Rarity.MAGIC), 3, 5)
    board.add_node(ParagonNode({}, rarity=Rarity.RARE), 3, 6)
    board.add_node(ParagonNode({}, rarity=Rarity.MAGIC), 4, 2)
    board.add_node(ParagonNode({}, rarity=Rarity.MAGIC), 4, 3)
    board.add_node(ParagonNode({}, rarity=Rarity.MAGIC), 4, 5)
    board.add_node(ParagonNode({}, rarity=Rarity.MAGIC), 4, 6)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 5, 3)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 5, 5)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 6, 2)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 6, 3)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 6, 4)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 6, 5)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 6, 6)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 7, 1)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 7, 2)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 7, 3)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 7, 4)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 7, 5)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 7, 6)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 7, 7)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 8, 0)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 8, 1)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 8, 2)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 8, 3)
    board.add_node(ParagonNode({}, rarity=Rarity.GLYPH), 8, 4)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 8, 5)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 8, 6)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 8, 7)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 8, 8)
    board.add_node(ParagonNode({}, rarity=Rarity.MAGIC), 9, 1)
    board.add_node(ParagonNode({}, rarity=Rarity.MAGIC), 9, 2)
    board.add_node(ParagonNode({}, rarity=Rarity.MAGIC), 9, 3)
    board.add_node(ParagonNode({}, rarity=Rarity.MAGIC), 9, 5)
    board.add_node(ParagonNode({}, rarity=Rarity.MAGIC), 9, 6)
    board.add_node(ParagonNode({}, rarity=Rarity.MAGIC), 9, 7)
    board.add_node(ParagonNode({}, rarity=Rarity.MAGIC), 10, 2)
    board.add_node(ParagonNode({}, rarity=Rarity.RARE), 10, 3)
    board.add_node(ParagonNode({}, rarity=Rarity.RARE), 10, 5)
    board.add_node(ParagonNode({}, rarity=Rarity.MAGIC), 10, 6)
    board.add_node(ParagonNode({}, rarity=Rarity.MAGIC), 11, 3)
    board.add_node(ParagonNode({}, rarity=Rarity.MAGIC), 11, 5)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 12, 3)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 12, 5)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 13, 3)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 13, 4)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 13, 5)
    board.add_node(ParagonNode({}, rarity=Rarity.COMMON), 14, 4)

    return board

def read_board_file(file_obj):
    lines = file_obj.readlines()
    rows = int(lines[0].split('=')[1])
    columns = int(lines[1].split('=')[1])

    entry_points = []
    entry_points_pairs = lines[2].split('=')[1].split(';')
    for pair in entry_points_pairs:
        (r,c) = pair.split(',')
        (r,c) = (int(r), int(c))
        print(f'({r}, {c})')
        entry_points.append((r,c))

    board = ParagonBoard(entry_points=entry_points, rows=rows, columns=columns)

    current_row = 0
    for line in lines[3:]:
        if line == '---\n':
            continue

        print(f'{current_row}: {line}')

        for i in range(columns):
            if i >= len(line):
                break

            if line[i] == 'c':
                board.add_node(ParagonNode({}, rarity=Rarity.COMMON), current_row, i)
            if line[i] == 'm':
                board.add_node(ParagonNode({}, rarity=Rarity.MAGIC), current_row, i)
            if line[i] == 'r':
                board.add_node(ParagonNode({}, rarity=Rarity.RARE), current_row, i)
            if line[i] == 'g':
                board.add_node(ParagonNode({}, rarity=Rarity.GLYPH), current_row, i)

        current_row = current_row + 1



    return board



def main():
    print(f"[*] Running main from {__file__}")

    with open('board_files/initial.board','r') as board_file:
        board = read_board_file(board_file)

    #board = build_board()

    print(board)

    start_time = datetime.datetime.now()

    path = board.shortest_path(
        board.get_node_by_coordinates(0,3),
        board.get_node_by_coordinates(14,4)
    )
    node = board.get_node_by_coordinates(14,4)
    while node.parent != None:
        node = node.parent

    end_time = datetime.datetime.now()

    print(board)
    print(f'[*] Start time: {start_time}')
    print(f'[*] End time: {end_time}')

    target_points = [
        board.get_node_by_coordinates(0, 4),
        board.get_node_by_coordinates(3, 6),
        board.get_node_by_coordinates(8, 4),
        board.get_node_by_coordinates(10, 3),
        board.get_node_by_coordinates(14, 4),
    ]

    # Render the results
    (dist, walked) = board.get_minimum_spanning_tree(target_points)
    print(board)
    print(f'Total distance: {dist}')

if __name__ == "__main__":
    main()