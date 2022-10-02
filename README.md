README
======

Turning this into something actually useful.

Unix Socket
===========
Stealthy opens a Unix socket since some Google research confirmed the intuitive
assumption that it is much faster than local TCP. Not benchmarked, but makes 
sense. 

Things to do
============
Writing a small client library and examples that connect to Stealthy and request
multiple page loads sequentially and then in parallel.

Bencharking & Profiling
=======================
Goal is to find out what network bandwidth, memory size, and type and number of
CPU cores are needed for the best experience.

HTML Parsing and Javascript analysis
====================================
This comes later.
