import {createClient} from 'redis'

const client = createClient({
  socket: {
    host: '127.0.0.1',
    port: '6379'
  },
})
client.on('error', function(err) {
  console.log('Redis client not connected to the server:', err)
})
console.log('Redis client connected to the server')
