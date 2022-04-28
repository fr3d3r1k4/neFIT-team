## 	@file 	Makefile
# 	@brief 	Makefile for easier compilation and running specific fragments of application or application as whole.
# 	@author ROMANA DURACIOVA
# 	@date 	2022-04-28
# 	use in Linux command line

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