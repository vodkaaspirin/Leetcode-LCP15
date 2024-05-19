from utils import calculate_cross_product, is_turn

def find_path(points, direction):
    N = len(points)
    directions = [None] * (N * N)
    
    # Preprocess all point pair turn directions
    for i in range(N):
        for j in range(N):
            if i != j:
                directions[i * N + j] = {}
                for k in range(N):
                    if k != i and k != j:
                        if is_turn(points[i], points[j], points[k], 'L'):
                            directions[i * N + j][k] = 'L'
                        else:
                            directions[i * N + j][k] = 'R'
    
    def dfs(path, used):
        if len(path) == N:
            return path
        
        last = path[-1]
        second_last = path[-2] if len(path) > 1 else None
        
        for i in range(N):
            if i not in used:
                if second_last is None or directions[second_last * N + last].get(i) == direction[len(path) - 2]:
                    path.append(i)
                    used.add(i)
                    result = dfs(path, used)
                    if result:
                        return result
                    path.pop()
                    used.remove(i)
        return None
    
    for start in range(N):
        for end in range(N):
            if start != end:
                result = dfs([start, end], {start, end})
                if result:
                    return result

if __name__ == "__main__":
    # Example test cases
    points = [[1,1], [1,4], [3,2], [2,1]]
    direction = "LL"
    print(find_path(points, direction))  # Output example [0, 2, 1, 3] or any valid path

    points = [[1,3], [2,4], [3,3], [2,1]]
    direction = "LR"
    print(find_path(points, direction))  # Output example [0, 3, 1, 2] or any valid path
