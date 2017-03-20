while read i
do
    mv log/$i log/$(python move.py $i)
done < log.txt