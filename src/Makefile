## 	@file 	Makefile
# 	@brief 	Makefile for easier compilation and running specific fragments of application or application as whole.
# 	@author ROMANA DURACIOVA
# 	@date 	2022-04-28

all: run

run: calc_GUI.py
	python3 calc_GUI.py

test: tests.py
	pytest ./tests.py

doc: Doxyfile
	doxygen Doxyfile

profile: profiling.py
	python3 profiling.py

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf ../.idea

pack: clean doc
	zip -r ../../../xdurac01_xkmeto00_xplank03_xjanco03.zip ../../repo ../../doc