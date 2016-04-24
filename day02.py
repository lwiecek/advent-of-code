#!/usr/bin/env python3

###
# Day 2 - adventofcode.com
# Lukasz Wiecek 2015-2016
###


def dimensions(s):
    return sorted(int(d) for d in s.split('x'))


def part_one(lines):
    '''
    The elves are running low on wrapping paper, and so they need to submit an
    order for more. They have a list of the dimensions (length l, width w, and
    height h) of each present, and only want to order exactly as much as they
    need.

    Fortunately, every present is a box (a perfect right rectangular prism),
    which makes calculating the required wrapping paper for each gift a little
    easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l.
    The elves also need a little extra paper for each present: the area of the
    smallest side.

    All numbers in the elves' list are in feet. How many total square feet of
    wrapping paper should they order?
    '''
    paper = 0
    for line in lines:
        l, w, h = dimensions(line)
        paper += (3 * l * w) + (2 * w * h) + (2 * l * h)
    return paper


def part_two(lines):
    '''
    The elves are also running low on ribbon. Ribbon is all the same width, so
    they only have to worry about the length they need to order, which they
    would again like to be exact.

    The ribbon required to wrap a present is the shortest distance around its
    sides, or the smallest perimeter of any one face. Each present also
    requires a bow made out of ribbon as well; the feet of ribbon required for
    the perfect bow is equal to the cubic feet of volume of the present. Don't
    ask how they tie the bow, though; they'll never tell.

    How many total feet of ribbon should they order?
    '''
    ribbon = 0
    for line in lines:
        l, w, h = dimensions(line)
        ribbon += 2 * (l + w) + (l * w * h)
    return ribbon


def main():
    assert part_one(['2x3x4']) == 58
    assert part_one(['1x1x10']) == 43

    assert part_two(['2x3x4']) == 34
    assert part_two(['1x1x10']) == 14

    with open('input/day02.txt') as f:
        lines_strip = (line.strip() for line in f)
        lines = [line for line in lines_strip if line]

    print(part_one(lines))
    print(part_two(lines))

if __name__ == '__main__':
    main()

