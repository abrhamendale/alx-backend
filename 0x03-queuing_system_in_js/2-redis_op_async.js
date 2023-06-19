import {createClient} from 'redis'

const redis = require('redis')
const {promisify} = require("util")

const client = createClient()
const getAsync = promisify(client.get).bind(client)

client.on('error', function(err) {
  console.log('Redis client not connected to the server:', err)
})
console.log('Redis client connected to the server')

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print)
}

async function displaySchoolValue(schoolName) {
  const pr = await getAsync(schoolName)
  console.log(pr)
}

displaySchoolValue('Holberton')
setNewSchool('HolbertonSanFrancisco', '100')
displaySchoolValue('HolbertonSanFrancisco')
