#!/bin/sh

curl -sS $1 |  grep -Po '(?<=href=")[^"]*';

exit;