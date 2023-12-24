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

def main():
    print(f"[*] Running main from {__file__}")

    board = build_board()

    print(board)

    start_time = datetime.datetime.now()

    path = board.shortest_path(
        board.get_node_by_coordinates(0,3),
        board.get_node_by_coordinates(14,4)
    )
    node = board.get_node_by_coordinates(14,4)
    while node.parent != None:
        node = node.parent

    # depth = 13
    # results = ParagonWalk.walk(board, max_depth=depth)

    end_time = datetime.datetime.now()

    print(board)
    print(f'[*] Start time: {start_time}')
    print(f'[*] End time: {end_time}')


    target_points = [
        board.get_node_by_coordinates(0, 4),
        board.get_node_by_coordinates(3, 6),
        board.get_node_by_coordinates(8, 4),
        board.get_node_by_coordinates(10, 3),
        board.get_node_by_coordinates(14, 4)
    ]

    import collections
    weight_matrix = collections.defaultdict(lambda: collections.defaultdict(int))
    path_matrix = collections.defaultdict(lambda: collections.defaultdict(list))

    for source in target_points:
        for dest in target_points:
            if source == dest:
                weight_matrix[source][dest] = None
                path_matrix[source][dest] = None

            path_matrix[source][dest] = board.get_path(board.shortest_path(source, dest))
            print(f'adding path: {path_matrix[source][dest]}')
            weight_matrix[source][dest] = board.path_length(board.shortest_path(source, dest))

    for source in weight_matrix.keys():
        for dest in weight_matrix[source]:
            print(f'{weight_matrix[source][dest]} ', end="")
        print('\n')

    # Construct a minimum spanning tree
    # Loosely follows the algorithm in the CLR book
    # for 3rd edition, page 634

    import math
    key = collections.defaultdict(lambda: math.inf)
    pi = collections.defaultdict(lambda: None)

    root = target_points[0]

    key[root] = 0
    queue = list(target_points)

    board.reset()

    root.marked = True

    while queue is not None and len(queue) > 0:
        # This is extract_min
        dests = queue
        min_node = None
        print(queue)
        for (k, item) in key.items():
            if min_node is None or key[min_node] > item:
                if k in queue:
                    print(f'adding a min node: {k}')
                    min_node = k

        del queue[queue.index(min_node)]

        # This is the algorithm body

        u = min_node

        for v in target_points: # Probably not right - need adjancency set here
            if v in queue and weight_matrix[u][v] < key[v]:
                pi[v] = u
                key[v] = weight_matrix[u][v]

    # Render the results
    board.reset()

    total_distance = 0
    for (k,i) in pi.items():
        print(f'{k}({board.get_coordinates(k)}) -> {i}({board.get_coordinates(i)})  - {key[k]}')
        total_distance = total_distance + key[k]
        path = path_matrix[k][i]
        for node in path:
            node.marked = True
    print(board)
    print(f'Total distance: {total_distance}')



if __name__ == "__main__":
    main()