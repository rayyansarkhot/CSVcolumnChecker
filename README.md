# Voter Names🗳️

## Description

This project was designed for a local politician in my county that wanted to sift through over 38,000 possible voters for Muslims so he may secure a political position. This algorithm is slow(big O of N^2) and not general purpose, but it got the job done of whittling down over 91% of candidates. I would gauge that of the over 3,000 names, there is a percent error of 10-15%. This project was made in collaboration with my friend, Arsalan.

## Technologies

This project was designed with Python3 and the csv library provided with the language. Alongside this, a dataset of Arabic names provided by [zakahmad](https://github.com/zakahmad/ArabicNameGenderFinder) was used. The idea was that Muslims generally are named with Arabic words, and thus by comparing voter names with Arabic names, possibile Muslim voters could be found.

