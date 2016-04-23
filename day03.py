###
# Day 3 - adventofcode.com
# Lukasz Wiecek 2015-2016
###

DIRECTIONS = {
    '<': (-1, 0),
    '>': (1, 0),
    '^': (0, 1),
    'v': (0, -1),
}


def new_position(position, c):
    d = DIRECTIONS[c]
    return position[0] + d[0], position[1] + d[1]


def part_one(s):
    '''
    Santa is delivering presents to an infinite two-dimensional grid of houses.

    He begins by delivering a present to the house at his starting location,
    and then an elf at the North Pole calls him via radio and tells him where
    to move next. Moves are always exactly one house to the north (^), south
    (v), east (>), or west (<). After each move, he delivers another present to
    the house at his new location.

    However, the elf back at the north pole has had a little too much eggnog,
    and so his directions are a little off, and Santa ends up visiting some
    houses more than once. How many houses receive at least one present?
    '''
    santa_position = (0, 0)
    visited = {santa_position}
    for c in s:
        santa_position = new_position(santa_position, c)
        visited.add(santa_position)
    return len(visited)


def part_two(s):
    '''
    The next year, to speed up the process, Santa creates a robot version of
    himself, Robo-Santa, to deliver presents with him.

    Santa and Robo-Santa start at the same location (delivering two presents to
    the same starting house), then take turns moving based on instructions from
    the elf, who is eggnoggedly reading from the same script as the previous
    year.

    This year, how many houses receive at least one present?
    '''
    santa_position = (0, 0)
    robo_position = (0, 0)
    visited = {santa_position, robo_position}
    for santa_c, robo_c in zip(s[::2], s[1::2]):
        santa_position = new_position(santa_position, santa_c)
        robo_position = new_position(robo_position, robo_c)
        visited.update({santa_position, robo_position})
    if len(s) % 2:
        visited.add(new_position(santa_position, s[-1]))
    return len(visited)


def main():
    assert part_one('>') == 2
    assert part_one('^>v<') == 4
    assert part_one('^v^v^v^v^v') == 2

    assert part_two('^v') == 3
    assert part_two('^>v<') == 3
    assert part_two('^v^v^v^v^v') == 11
    assert part_two('^') == 2

    with open('input/day03.txt') as f:
        s = f.read().strip()

    print(part_one(s))
    print(part_two(s))


if __name__ == '__main__':
    main()

