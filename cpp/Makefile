all:
	g++ -std=c++20 -O2 -Wall -Wextra test.cpp -o test

run: all
	./test < input.txt

out: all
	./test < input.txt > output.txt

template:
	cp template.cpp test.cpp

clean:
	rm -f test
	: > input.txt
