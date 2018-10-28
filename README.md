# Challenge 1

https://tranquil-temple-79124.herokuapp.com/messages/my_message

*Heroku may take ~30 seconds to spin up the webserver when asleep*

This webserver uses an in-process cache for the messages. This limits it to a single process which bottlenecks the throughput. To scale it larger, a dedicated cache like Redis should be used, as we could then add more workers that talk to Redis.

To Test:
```
URL='https://tranquil-temple-79124.herokuapp.com'
curl -X POST -H "Content-Type: application/json" -d '{"message": "foo"}' $URL/messages
curl $URL/messages/2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae
curl -i $URL/messages/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

# Challenge 2

My program runs in O(N) time and O(N) space. The first loops loads the prices into memory and looks for any exact matches. The second loop finds the closest match under our budget if we couldn't find an exact match.

To Test:
```
cd Challenge-2
python find-pair.py prices.txt 2500
python find-pair.py prices.txt 2300
python find-pair.py prices.txt 10000
python find-pair.py prices.txt 1100
```
