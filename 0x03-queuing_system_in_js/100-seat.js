import {createClient} from 'redis'

const redis = require('redis')
const redis = require('redis')
const kue = require('kue')
  , reserve_seat = kue.createQueue()
const express = require('express')
const {promisify} = require("util")

const getAsync = promisify(client.get).bind(client)
const client = createClient()
const app = express()
const port = 1245

function reserveSeat(number) {
  client.set(available_seats, number)
}

async function getCurrentAvailableSeats() {
  const pr = await getAsync(available_seats)
}

app.get('/available_seats', function (req, res) {
  getCurrentAvailableSeats()
}

app.get('/reserve_seat', function (req, res) {
  if (!reservationEnabled) {
    return jsonify({"status": "Reservation are blocked"})
  }
  let job_1 = push_notification_code_2.create('que', jobs[i]).save(
    function(err) {
      if(!err) {
        return jsonify({ "status": "Reservation in process" })
      }
      else {
        return jsonify({ "status": "Reservation failed" })
      }
    }).attempts(3).backoff( true ).on('complete', function(result){
      console.log(`Seat reservation job ${job_1.id} completed`)
    }).on('failed', function(errorMessage){
      console.log(`Seat reservation job ${job_1.id} failed:`, errorMessage)
    })
})

app.get('/process', function (req, res) {
  if (getCurrentAvailableSeats())
    reserveseat()
  else
    reservationEnabled = false
  if (!getCurrentAvailableSeats())
    Error('Not enough seats available')
  
  return jsonify({"status": "Queue processing"})
