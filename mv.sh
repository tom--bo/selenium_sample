file=data.csv
while true
do
    time=$(date "+%T")
    if [ -e $file ]; then
        mv data.csv "d${time}.csv"
    fi
    echo "hello"
    sleep 1s
done

