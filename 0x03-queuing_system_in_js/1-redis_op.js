import {createClient} from 'redis'

const redis = require('redis')

const client = createClient()

client.on('error', function(err) {
  console.log('Redis client not connected to the server:', err)
})
console.log('Redis client connected to the server')

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print)
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, function(err, reply) {
    console.log(reply)
  })
}

displaySchoolValue('Holberton')
setNewSchool('HolbertonSanFrancisco', '100')
displaySchoolValue('HolbertonSanFrancisco')
