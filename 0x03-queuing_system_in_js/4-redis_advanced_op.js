import {createClient} from 'redis'

const redis = require('redis')

const client = createClient()

client.on('error', function(err) {
  console.log('Redis client not connected to the server:', err)
})
console.log('Redis client connected to the server')

client.hset('HolbertonSchools', 'Portland', '50', 'Seattle', '80', 'New York', '20', 'Bogota', '20', 'Cali', '40', 'Paris', '2', redis.print)

client.hgetall('HolbertonSchools', function(err, reply) {
  console.log(reply)
})
