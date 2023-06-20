import {createClient} from 'redis'

const redis = require('redis')
const kue = require('kue')
  , push_notification_code_3 = kue.createQueue()

function createPushNotificationsJobs(jobs, queue) {
  if (!isarray(jobs)) {
    Error('Jobs is not an array')
  }
  for (let i = 0; i < jobs.length; i++) {
    let job_1 = push_notification_code_3.create('que', jobs[i]).save(
      function(err) {
        if(!err) {
	  console.log(`Notification job created: ${job_1.id}`)
	}
      }).attempts(3).backoff( true ).on('complete', function(result){
        console.log(`Notification job ${job_1.id}completed`)
      }).on('failed', function(errorMessage){
        console.log(`Notification job ${job_1.id} failed:`, errorMessage)
      }).on('progress', function(progress, data){
	console.log(`Notification ${job_1.id} ${progress}% complete`)
      }).removeOnComplete(true).save()
  }
}
