all: init run

init:
	pip3 install -r requirements.txt

run:	
	python3 calc_GUI.py

test: tests.py
	python3 tests.py

doc: Doxyfile
	rm -rf ../documentationDoxy
	doxygen Doxyfile
