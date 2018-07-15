Nepali Autocomplete 
===

Autocompletes Nepali words (in Unicode). Completion also takes into account the preceding word. 

## How to install:
	
	git clone https://github.com/bpanthi977/autocomplete
	pip install -r requirements.txt
	
## How to run:

	cd autocomplete
	python3 ac.py	

For the first run, it takes some time to train on the data. 

Now head over to http://localhost:8080/नेपा/10 for non-contextual completion
and to http://localhost:8080/मेरो/क/10 for completion based on preceding word.

### note
The data (nepali text corpus) was collected from (about 36 thousands) news snippets from various online portals over.
