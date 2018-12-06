#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "???"

import cProfile
import pstats
import timeit
from collections import defaultdict


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    def inner_func(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = func(*args, **kwargs)
        pr.disable()
        sortby = "cumulative"
        ps = pstats.Stats(pr).sort_stats(sortby)
        ps.print_stats()
        return result
    return inner_func


def read_movies(src):
    """Read a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()

def is_duplicate(title, movies):
    """Case insensitive search within a list"""
    for movie in movies:
        if movie == title:
            return True
    return False

@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicate = []
    movies_dict = {}
    for movie in movies:
        if movie not in movies_dict:
            movies_dict[movie] = [movie]
        else:
            duplicate.append(movie)
         
    return duplicate
    


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(stmt='find_duplicate_movies("movies.txt")',
                     setup='from __main__ import find_duplicate_movies')
    results = t.repeat(repeat=7, number=3)

    print min(results) / float(3)




def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))
    
    

if __name__ == '__main__':
    main()
