while read i
do
    cat data/$i >> all-data.json
done < data.txt

while read i
do
    cat log/$i >> all-log.log
done < log.txt