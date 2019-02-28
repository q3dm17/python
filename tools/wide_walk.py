def extract_adjacent(url):
    print(str.center("visiting \t{}\t".format(url),80,"*"))
    # print("url_a")
    yield "url_a"
    # print("url_b")
    yield "url_b"
    # print("url_c")
    yield "url_c"
    # print(url + "visited")
    yield url + "visited"


def chain(*iterables):
    for iterable in iterables:
        for i in iterable:
            yield i


def unique(iterable, seen=None):
    seen = set(seen or [])
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item


def wide_walk(start, depth):
    first_level = unique(extract_adjacent(start))
    second_level = []
    for node in first_level:
        second_level = chain(second_level, extract_adjacent(node))
    return unique(chain(first_level, second_level))


def step(nodes, visited):
    next_nodes = []
    for node in nodes:
        if node in visited:
            continue
        next_nodes = chain(next_nodes, extract_adjacent(node))
        visited.add(node)
    return next_nodes


def wide_walk_new(start, depth):
    # BUG: можем зайти в узел, который уже заходили, если он был на прошлых уровнях
    visited = set([])
    zero_level_list = list(step([start], visited))
    all_levels_iterator = chain(zero_level_list)
    previous_level_nodes_list = zero_level_list
    for i in range(depth):
        previous_level_nodes_list = list(unique(step(previous_level_nodes_list, visited), visited))
        all_levels_iterator = chain(all_levels_iterator, previous_level_nodes_list)
    return all_levels_iterator


def main():
    for node in wide_walk_new("start_url", 3):
        print(node)


if __name__ == "__main__":
    main()
