# dffastquery

[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

## Description

Pandas dataframe queries are slow. Especially if you have millions of rows. The reason is when you do a `df.query()` pandas starts a single core loop through every row and then evaluates the expression in `query`. Pandas provides and describes many methods to speedup the expression evaluation (cython, numba, numexpr) but the bottleneck for large dataframes is the single core loop.
One of the best solutions would be if pandas does the query in parallel on a trie structure, but it doesn't. But you can use a small workaround called dffastquery ;-) .

## How does it work

With dffastquery you can query for strings in columns of your dataframe (only exact matches at the moment). It creates an set index for the unique string values of each string columns. A query is just a intersection of those sets and faster than a `df.query()`. But TANSTAAFL the index has to be build first.

## Installation

## Usage
