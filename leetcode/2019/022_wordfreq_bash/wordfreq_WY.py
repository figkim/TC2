# Read from the file words.txt and output the word frequency list to stdout.

cat words.txt | tr "\n" " " | awk '{for(word=1; word<=NF; ++word) dict[$word]+=1} END {for(element in dict) print element,dict[element]}' | sort -r -n -k2