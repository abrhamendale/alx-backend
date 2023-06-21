import {createClient} from 'redis'

const redis = require('redis')
const kue = require('kue')
  , push_notification_code_2 = kue.createQueue()
const obj = [
  '4153518780',
  '4153518781'
]

push_notification_code_2.process('que', function(job, done){
  sendNotification(job.data.phoneNumber, job.data.message, job, done)
})

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100)
  if (obj.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`))
  }
  else {
    job.progress(50, 100)
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
  }
}
