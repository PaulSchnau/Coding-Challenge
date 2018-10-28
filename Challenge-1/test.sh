URL='https://tranquil-temple-79124.herokuapp.com'
# URL='http://127.0.0.1:5000'
set -x
curl -X POST -H "Content-Type: application/json" -d '{"message": "foo"}' $URL/messages
curl $URL/messages/2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae
curl -i $URL/messages/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
