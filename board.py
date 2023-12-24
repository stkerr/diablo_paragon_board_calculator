from node import ParagonNode


class ParagonBoard(object):

    def __init__(self, entry_points:list(tuple[int, int]), rows=5, columns=5):
        assert rows > 0
        assert columns > 0
        assert entry_points is not None

        # Define a rectangular grid with rows and columns.
        self.rows = rows
        self.columns = columns
        self.cells = [[ParagonNode() for x in range(columns)] for y in range(rows)] # Make a 2 dimensional array of rows by columns

        self.entry_points = entry_points

    def pretty_print(self, walk:list[tuple]=None):
        results = ""
        for row in range(len(self.cells)):
            for column in range(len(self.cells[row])):
                entry = self.cells[row][column]

                if (row, column) in self.entry_points:
                   results = results + "(V) "
                elif entry.blank:
                    results = results + "    "
                else:
                    if walk is None or (walk is not None and (row,column) in walk):
                        results = results + f"({str(entry)}) "
                    else:
                        results = results + "    "
            results = results + "\n"
        return results

    def __str__(self):
        return self.pretty_print()

    def add_node(self, node: ParagonNode, row:int, column:int):
        # Add a node to the given coordinates. The grid is 0-based
        assert node is not None
        assert row >= 0
        assert column >= 0
        assert row < self.rows
        assert column < self.columns

        self.cells[row][column] = node

    def get_node_by_coordinates(self, row:int, column:int):
        assert row >= 0
        assert column >= 0
        assert row < self.rows
        assert column < self.columns

        return self.cells[row][column]

    def get_node(self, coordinates: tuple):
        assert coordinates is not None
        assert len(coordinates) == 2
        return self.get_node_by_coordinates(coordinates[0], coordinates[1])

    def get_neighbor_coordinates(self, row:int, column:int):

        results = []

        if (row-1) >= 0 and self.cells[row-1][column].blank == False:
            results.append((row-1, column))
        if (row+1) < self.rows and self.cells[row+1][column].blank == False:
            results.append((row+1, column))
        if (column-1) >= 0 and self.cells[row][column-1].blank == False:
            results.append((row, column-1))
        if (column+1) < self.columns and self.cells[row][column+1].blank == False:
            results.append((row, column+1))

        return results

    def get_neighbor_nodes(self, row:int, column:int):
        coordinates = self.get_neighbor_coordinates(row, column)

        results = []
        for coordinate in coordinates:
            node = self.get_node_by_coordinates(coordinate[0], coordinate[1])
            results.append(node)

        return results

    def get_coordinates(self, node: ParagonNode):
        for r in range(len(self.cells)):
            for c in range(len(self.cells[r])):
                if node == self.cells[r][c]:
                    return (r,c)
        return (None, None)

    def reset(self):
        # Reset board iteration state variables
        for r in range(len(self.cells)):
            for c in range(len(self.cells[r])):
                self.cells[r][c].marked = False
                self.cells[r][c].explored = False
                self.cells[r][c].parent = None

    def path_length(self, node: ParagonNode):
        count = -1 # Start at -1 since we dont count ourselves
        while node is not None:
            node = node.parent
            count = count + 1
        return count

    def shortest_path(self, source: ParagonNode, destination: ParagonNode):

        # Reset the board first
        self.reset()

        # Use a breadth-first search to find the shortest path
        queue = []
        source.explored = True

        queue.append(source)
        while len(queue) > 0:
            v: ParagonNode = queue.pop(0)
            if v == destination:
                temp = v
                while temp is not None:
                    temp.marked = True
                    temp = temp.parent

                return v
            v_coordinates = self.get_coordinates(v)
            for w in self.get_neighbor_nodes(v_coordinates[0], v_coordinates[1]):

                if w.explored is not True:
                    w.explored = True
                    w.parent = v
                    queue.append(w)

    def get_path(self, node: ParagonNode):
        path = []
        while node is not None:
            path.append(node)
            node = node.parent
        return path

    def path_str(self, node: ParagonNode):
        path = self.get_path(node)
        results = ""
        for item in path:
            results = results + f'{self.get_coordinates(item)} '
        return results

    def get_minimum_spanning_tree(self, target_points: list[ParagonNode]):
        # Construct a minimum spanning tree
        # Loosely follows the algorithm in the CLR book
        # for 3rd edition, page 634

        self.reset()

        import collections
        weight_matrix = collections.defaultdict(lambda: collections.defaultdict(int))
        path_matrix = collections.defaultdict(lambda: collections.defaultdict(list))

        for source in target_points:
            for dest in target_points:
                if source == dest:
                    weight_matrix[source][dest] = None
                    path_matrix[source][dest] = None

                path_matrix[source][dest] = self.get_path(self.shortest_path(source, dest))
                print(f'adding path: {path_matrix[source][dest]}')
                weight_matrix[source][dest] = self.path_length(self.shortest_path(source, dest))

        for source in weight_matrix.keys():
            for dest in weight_matrix[source]:
                print(f'{weight_matrix[source][dest]} ', end="")
            print('\n')

        import math
        key = collections.defaultdict(lambda: math.inf)
        pi = collections.defaultdict(lambda: None)

        root = target_points[0]

        key[root] = 0
        queue = list(target_points)

        self.reset()

        root.marked = True

        while queue is not None and len(queue) > 0:
            # This is extract_min
            dests = queue
            min_node = None
            print(queue)
            for (k, item) in key.items():
                if min_node is None or key[min_node] > item:
                    if k in queue:
                        min_node = k

            del queue[queue.index(min_node)]

            # This is the algorithm body

            u = min_node

            for v in target_points:  # Probably not right - need adjancency set here. Works ok for now but can be optimized
                if v in queue and weight_matrix[u][v] < key[v]:
                    pi[v] = u
                    key[v] = weight_matrix[u][v]

        # Mark the interim nodes we visited and return the full path
        walked_path = []
        total_distance = 0
        for (k, i) in pi.items():
            print(f'{k}({self.get_coordinates(k)}) -> {i}({self.get_coordinates(i)})  - {key[k]}')
            total_distance = total_distance + key[k]
            path = path_matrix[k][i]
            walked_path.extend(path_matrix[k][i])
            for node in path:
                node.marked = True


        return (total_distance, walked_path)