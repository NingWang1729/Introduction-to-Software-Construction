#!/bin/bash

echo $#
echo $0
foo=$1
echo ${foo:=100}
