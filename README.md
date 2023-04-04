# python-challenge

Had a lot of trouble with PyBank; I initially tried to hold and compare two variables from the profit/ loss column as the interator went through the rows - absolute horror show; it started iterating twice at a time. I had to go line by line to see what caused it to skip, and once I realized what went wrong I decided to find a different way: keeping PL in a list and manipulating the data through that list.
Stackoverflow introduced me to numpy.max/min and numpy.argmax/min which worked perfectly for PyBank, the rest was application from class. 

PyPoll was easier, though my solution to the code was inelegant (it should only work for very small lists of candidates) I'm wondering if I could use a dictionary of lists, each key associated to each candidate, but retrieving the highest vote from that dictionary was unintuitive. Printing it without brackets also looks needlessly complicated. Maybe Pandas will provide a better way of handling this.