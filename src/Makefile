all: run

run: calc_GUI.py
	python calc_GUI.py

test: tests.py
	pytest tests.py

doc: Doxyfile
	doxygen Doxyfile

#profile: profiling.py
	#python profiling.py

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf ../.idea
	rm mathLibrary.pyc

pack: clean
	zip -r ../../../xdurac01_xkmeto00_xplank03_xjanco03.zip ../../repo ../../doc ../../install