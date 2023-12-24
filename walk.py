from board import ParagonBoard


class ParagonWalk(object):
    def __init__(self):
        pass

    @staticmethod
    def deduplicate_walks(walks):

        results = set()
        for walk in walks:
            results.add(frozenset(walk))  # Use a frozenset so that the list is hashable and can be put in a set
        return list(results)

    @staticmethod
    def walk(board:ParagonBoard, max_depth=None):
        assert board is not None

        def walk_helper(board: ParagonBoard, current_coordinates: tuple, previously_visited: list[tuple], existing_neighbors: list[tuple], current_depth, max_depth=None):
            assert max_depth >= 0
            assert current_depth >= 0

            walked = []

            if current_depth >= max_depth:
                return [previously_visited] # Return as a list to represent the whole walk

            new_neighbors = board.get_neighbor_coordinates(current_coordinates[0], current_coordinates[1])
            new_neighbors.extend(list(existing_neighbors)) # Use any existing neighbors we have as well

            neighbors = []
            for n in new_neighbors:
                # This loop is important to remove unneeded nodes to speed up the future recursive calls
                if n not in previously_visited:
                    # Only add non-blank nodes and nodes we've not seen before
                    neighbors.append(n)

            for neighbor in neighbors:

                visited = list(previously_visited)  # Make a copy, not alter the existing one in place
                visited.append(neighbor)


                neighbor_walk = walk_helper(board, neighbor, visited, neighbors, max_depth=max_depth, current_depth=current_depth+1)

                walked.extend(neighbor_walk)

            walked = ParagonWalk.deduplicate_walks(walked)
            return walked

        # This is the top level walk function that takes a board as input and walks all its entry points
        results = []
        for entry_point in board.entry_points:
            #visited = [entry_point] # Reset the visited list at the entry points

            print(f"[*] Entry point: {entry_point}")
            results.extend(walk_helper(board, entry_point, [entry_point], board.entry_points, current_depth=1, max_depth=max_depth))


        print(f'[*] Found {len(results)} before deduplicating.')
        print('[*] Deduplicating.')
        results = ParagonWalk.deduplicate_walks(results)

        return results
