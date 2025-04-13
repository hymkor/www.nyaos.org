#!/usr/bin/perl

print <<HERE
Content-Type: text/html
Location: http://nyaos.org/d/index.cgi?$ENV{QUERY_STRING}
Content-Length: 0

<html><body></body></html>
HERE
