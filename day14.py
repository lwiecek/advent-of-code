###
# Day 14 - adventofcode.com
# Lukasz Wiecek 2015-2016
###

import operator


def get_reindeer_parameters(line):
    speed, flying_time, rest_time = (int(s) for s in line.split() if s.isdigit())
    return speed, flying_time, rest_time


def calculate_distance(elapsed_time, speed, flying_time, rest_time):
    cycle_time = flying_time + rest_time
    cycles = elapsed_time // cycle_time
    full_cycles_distance = cycles * flying_time * speed 
    last_cycle_distance = min(elapsed_time % cycle_time, flying_time) * speed
    return full_cycles_distance + last_cycle_distance


def part_one(lines, race_time):
    '''
    This year is the Reindeer Olympics! Reindeer can fly at high speeds, but
    must rest occasionally to recover their energy. Santa would like to know
    which of his reindeer is fastest, and so he has them race.

    Reindeer can only either be flying (always at their top speed) or resting
    (not moving at all), and always spend whole seconds in either state.

    For example, suppose you have the following Reindeer:

    Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
    After one second, Comet has gone 14 km, while Dancer has gone 16 km. After
    ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the
    eleventh second, Comet begins resting (staying at 140 km), and Dancer
    continues on for a total distance of 176 km. On the 12th second, both
    reindeer are resting. They continue to rest until the 138th second, when
    Comet flies for another ten seconds. On the 174th second, Dancer flies for
    another 11 seconds.

    In this example, after the 1000th second, both reindeer are resting, and
    Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by
    that point). So, in this situation, Comet would win (if the race ended at
    1000 seconds).

    Given the descriptions of each reindeer (in your puzzle input), after
    exactly 2503 seconds, what distance has the winning reindeer traveled?
    '''
    max_distance = 0
    for line in lines:
        max_distance = max(
            max_distance,
            calculate_distance(race_time, *get_reindeer_parameters(line)),
        )
    return max_distance



def part_two(lines, race_time):
    '''
    Seeing how reindeer move in bursts, Santa decides he's not pleased with the
    old scoring system.

    Instead, at the end of each second, he awards one point to the reindeer
    currently in the lead. (If there are multiple reindeer tied for the lead,
    they each get one point.) He keeps the traditional 2503 second time limit,
    of course, as doing otherwise would be entirely ridiculous.

    Given the example reindeer from above, after the first second, Dancer is in
    the lead and gets one point. He stays in the lead until several seconds
    into Comet's second burst: after the 140th second, Comet pulls into the
    lead and gets his first point. Of course, since Dancer had been in the lead
    for the 139 seconds before that, he has accumulated 139 points by the 140th
    second.

    After the 1000th second, Dancer has accumulated 689 points, while poor
    Comet, our old champion, only has 312. So, with the new scoring system,
    Dancer would win (if the race ended at 1000 seconds).

    Again given the descriptions of each reindeer (in your puzzle input), after
    exactly 2503 seconds, how many points does the winning reindeer have?
    '''

    max_distance = 0

    reindeers = []
    scores = []
    for line in lines:
        reindeers.append(get_reindeer_parameters(line))
        scores.append(0)

    for second in range(1, race_time + 1):
        distances = [0,] * len(reindeers)
        for i, reindeer in enumerate(reindeers):
            distances[i] = calculate_distance(second, *reindeer)
        max_distance = max(distances)
        scores = map(operator.add, scores, [int(d == max_distance) for d in distances])
    return max(scores)


def main():
    example = [
        'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
        'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.',
    ]
    assert part_one(example, 1000) == 1120
    assert part_two(example, 1000) == 689

    with open('input/day14.txt') as f:
        lines_strip = (line.strip() for line in f)
        lines = [line for line in lines_strip if line]

    print(part_one(lines, 2503))
    print(part_two(lines, 2503))


if __name__ == '__main__':
    main()

