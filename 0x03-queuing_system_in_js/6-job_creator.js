import {createClient} from 'redis'

const redis = require('redis')
const kue = require('kue')
  , push_notification_code = kue.createQueue()

const obj = {
  phoneNumber: String,
  message: String
}

let kue_job = push_notification_code.create('sendNotification', obj).save(
  function(err) {
    if(!err) {
      console.log(`Notification job created: ${kue_job.id}`)
    }
  }
)
kue_job.attempts(3).backoff( true )
kue_job.on('complete', function(result){
  console.log('Notification job completed', result)
}).on('failed attempt', function(errorMessage, doneAttempts){
  console.log('Notification job failed');
})
/*
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`)
}
push_notification_code.process('sendNotification', function(job, done){
  sendNotification(job.phoneNumber, job.message);
});
*/
