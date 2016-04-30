#!/usr/bin/env python3

###
# Day 8 - adventofcode.com
# Lukasz Wiecek 2015-2016
###


def diff_str_and_memory(s):
    # simple len(s) - len(eval(s)) would also work here
    # but eval() is EVIL and should be avoided even
    # if I can assume that the input is sane
    diff = 2  # ""
    s = s[1:-1]
    diff += s.count(r'\"')
    s = s.replace(r'\"', '')
    diff += s.count(r'\\')
    s = s.replace(r'\\', '')
    diff += 3 * s.count(r'\x')
    return diff


def diff_encoded_and_str(s):
    encoded = '"{0}"'.format(s.replace('\\', r'\\').replace('"', r'\"'))
    return len(encoded) - len(s)


def part_one(lines):
    r'''
    Space on the sleigh is limited this year, and so Santa will be bringing his
    list as a digital copy. He needs to know how much space it will take up
    when stored.

    It is common in many programming languages to provide a way to escape
    special characters in strings. For example, C, JavaScript, Perl, Python,
    and even PHP handle special characters in very similar ways.

    However, it is important to realize the difference between the number of
    characters in the code representation of the string literal and the number
    of characters in the in-memory string itself.
    
    Santa's list is a file that contains many double-quoted string literals,
    one on each line. The only escape sequences used are \\ (which represents a
    single backslash), \" (which represents a lone double-quote character), and
    \x plus two hexadecimal characters (which represents a single character
    with that ASCII code).

    Disregarding the whitespace in the file, what is the number of characters
    of code for string literals minus the number of characters in memory for
    the values of the strings in total for the entire file?
    '''
    return sum(diff_str_and_memory(line) for line in lines)


def part_two(lines):
    r'''
    Now, let's go the other way. In addition to finding the number of
    characters of code, you should now encode each code representation as a new
    string and find the number of characters of the new encoded representation,
    including the surrounding double quotes.

    Your task is to find the total number of characters to represent the newly
    encoded strings minus the number of characters of code in each original
    string literal.
    '''
    return sum(diff_encoded_and_str(line) for line in lines)


def main():
    assert diff_str_and_memory(r'""') == 2
    assert diff_str_and_memory(r'"abc"') == 2
    assert diff_str_and_memory(r'"aaa\"aaa"') == 3
    assert diff_str_and_memory(r'"\x27"') == 5

    assert diff_encoded_and_str(r'""') == 4
    assert diff_encoded_and_str(r'"abc"') == 4
    assert diff_encoded_and_str(r'"aaa\"aaa"') == 6
    assert diff_encoded_and_str(r'"\x27"') == 5

    with open('input/day08.txt') as f:
        lines_strip = (line.strip() for line in f)
        lines = [line for line in lines_strip if line]

    print(part_one(lines))
    print(part_two(lines))

if __name__ == '__main__':
    main()

