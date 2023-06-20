import {createClient} from 'redis'

const redis = require('redis')

const client = createClient()

client.on('error', function(err) {
  console.log('Redis client not connected to the server:', err)
})
console.log('Redis client connected to the server')

client.on('message', function (channel, message) {
  if (message == 'KILL_SERVER') {
    client.unsubscribe()
    client.quit()
  }
  console.log(message)
})
client.subscribe('holberton school channel');
