#!/bin/bash

########################################
# Author - Ruturaj Kiran Vaidya
########################################


########################################
# Usage:
# Put ext1.dot in root of our directory
# bash projectOneGrader.bash
########################################

grade()
{	
touch grade.txt
# 2 Points by default
echo "2 " >> grade.txt
# Build the project
if g++ -std=c++11 dfa.cpp;
then
	#If project compiles, add 3 points
	echo "3 " >> grade.txt
fi
temp=$(./a.out ../../ex1.dot adijh)
echo $temp
if [ $temp == 0 ];
then
	# DFA can reject a simple string that stays on a
	# path but does not end in a final state, add 1 point
	echo "1 " >> grade.txt
fi
temp=$(./a.out ../../ex1.dot aea)
echo $temp
if [ $temp == 0 ];
then
	# DFA can reject a simple string that does not
	# correspond to a valid path
	echo "1 " >> grade.txt
fi
temp=$(./a.out ../../ex1.dot adjz)
echo $temp
if [ $temp == 0 ];
then
	# DFA can reject a simple string that uses
	# characters for which there are no edges
	echo "1 " >> grade.txt
fi
temp=$(./a.out ../../ex1.dot bc)
echo $temp
if [ $temp == 1 ];
then
	# DFA can accept a simple string that does not
	# require a loop through the automaton
	echo "1 " >> grade.txt
fi
temp=$(./a.out ../../ex1.dot adiiiiiijgk)
echo $temp
if [ $temp == 1 ];
then
	# DFA can accept a simple string that requires
	# a loop through the automaton
	echo "1 " >> grade.txt
fi
temp=$(awk '{ sum += $1 } END { print sum }' grade.txt)
echo "" >> grade.txt
echo "Total Grade: " >> grade.txt
echo "$temp" >> grade.txt
}

PWD='pwd'

# Remove all of the text files
rm ./*.txt

for f in *; do
	if [ "$f" == "projectOneGrader.bash" ] ; then
		continue;
	elif [ "$f" == "ex1.dot" ] ; then
		continue;
	fi
	mkdir "$f".dir
	mv "$f" "$f".dir
	cd "$f".dir
	unzip "$f"
	tar xvzf "$f"
	tar xvjf "$f"
	tar xvf "$f"
	tar xzvf "$f"
	if cd "p1"; 
	then
		grade
		cd ../..
		continue
	elif cd "Project1";
	then
		grade
		cd ../..
		continue
	fi
	cd ..
done
