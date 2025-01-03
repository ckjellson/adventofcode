import re
import sys
import typing

sys.setrecursionlimit(100000)


def turn_right(curdir):
    if curdir == (0, 1):
        return (1, 0)
    if curdir == (0, -1):
        return (-1, 0)
    if curdir == (1, 0):
        return (0, -1)
    if curdir == (-1, 0):
        return (0, 1)


def turn_left(curdir):
    if curdir == (0, 1):
        return (-1, 0)
    if curdir == (0, -1):
        return (1, 0)
    if curdir == (1, 0):
        return (0, 1)
    if curdir == (-1, 0):
        return (0, -1)


def lmap(func, *iterables):
    return list(map(func, *iterables))


def ints(s: str) -> typing.List[int]:
    return lmap(int, re.findall(r"-?\d+", s))


def ints_inds(s: str) -> typing.List[int]:
    return [
        (int(m.string[m.start() : m.end()]), (m.span()[0], m.span()[1]))
        for m in re.finditer(r"-?\d+", s)
    ]


def positive_ints(s: str) -> typing.List[int]:
    return lmap(int, re.findall(r"\d+", s))


def positive_ints_inds(s: str) -> typing.List[int]:
    return [
        (int(m.string[m.start() : m.end()]), (m.span()[0], m.span()[1]))
        for m in re.finditer(r"\d+", s)
    ]


def negative_ints_inds(s: str) -> typing.List[int]:
    return [
        (int(m.string[m.start() : m.end()]), (m.span()[0], m.span()[1]))
        for m in re.finditer(r"-\d+", s)
    ]


def floats(s: str) -> typing.List[float]:
    return lmap(float, re.findall(r"-?\d+(?:\.\d+)?", s))


def floats_inds(s: str) -> typing.List[int]:
    return [
        (float(m.string[m.start() : m.end()]), (m.span()[0], m.span()[1]))
        for m in re.finditer(r"-?\d+(?:\.\d+)?", s)
    ]


def positive_floats(s: str) -> typing.List[float]:
    return lmap(float, re.findall(r"\d+(?:\.\d+)?", s))


def positive_floats_inds(s: str) -> typing.List[int]:
    return [
        (float(m.string[m.start() : m.end()]), (m.span()[0], m.span()[1]))
        for m in re.finditer(r"\d+(?:\.\d+)?", s)
    ]


def negative_floats_inds(s: str) -> typing.List[int]:
    return [
        (float(m.string[m.start() : m.end()]), (m.span()[0], m.span()[1]))
        for m in re.finditer(r"-\d+(?:\.\d+)?", s)
    ]


def words(s: str) -> typing.List[str]:
    return re.findall(r"[a-zA-Z]+", s)
