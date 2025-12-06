# QM
The Holy Quran was revelaed in Arabic language around 1400 years ago. The arabic alphabets carry distinct weights in matter  of numbers. In this project the weights of individual letters,  words, verses, chapters and complete holy book are calculated. Those interested to explore the patterns of these numerical weights may benefit from this repo. 

search-text.py is the main code file to compute weights of the letters and other catgories. It also saves them in.csv files.

The computed weights are given in separate .csv files. 
dictQM_LL_.csv holds letter weights, dictQM_WW_.csv holds word weights, dictQM_AA_.csv holds verse weights, dictQM_SS_.csv holds chapter weights and dictQM_QM_.csv holds combined weight of the entire Quran Majeed.
QM-weight-18-October-2024-1st-version-ver-2.txt contains the abovementioned weight-lists in one big file. The lists are separated by descriptive commnets.

compute_single_digit_values.py is a general code which reads any of the main dictQM_*.csv file and generates single-digit Rbic-weight for each row containing letter, word, verse or chapter.

We tried to compute Fibonacci sequence for the arabic weights of letters and words but the effort was unsuccessful since the computations could not proceed beyond Fibonacci sum integer exceeding 4300 places. Then we conducted the same experiment with single-digit values of verses and chapters. This result is given in the respective files inidcated by their names.

Students and hobbyists may find interesting patterns in thses listings of the weight when placed along geometric shapes and placed according to other innovative designs.

It is much expected that enthusisasts of Cryptology may benefit from the patterns of Holy Quran.
