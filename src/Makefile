all: run

run: calc_GUI.py
	python3 calc_GUI.py

test: tests.py
	pytest tests.py

doc: Doxyfile
	rm -rf ../../doc
	doxygen Doxyfile