import {createClient} from 'redis'

const redis = require('redis')
const kue = require('kue')
  , reserve_seat = kue.createQueue()
const express = require('express')
const {promisify} = require("util")

const getAsync = promisify(client.get).bind(client)
const client = createClient()
const app = express();
const port = 1245
const listProducts = [
  Suitcase 250,
  Suitcase 450,
  Suitcase 650,
  Suitcase 1050,
]

client.on('error', function(err) {
  console.log('Redis client not connected to the server:', err)
})


function getItemById(id) {
  listproducts[id]
}

function reserveStockById(itemId, stock) {
  client.set(initialAvailableQuantity, stock)
}

async function getCurrentReservedStockById(itemId) {
  const pr = await getAsync(initialAvailableQuantity)
  return pr
}

app.get('/list_products', function (req, res) {
  return jsonify({listproducts})
});

app.get('/list_products/:itemId', function (req, res) {
  const prd = getCurrentReservedStockById(itemId)
  if (prd)
    return jsonify({prd})
  else
    return jsonify({"status":"Product not found"})
})

app.get('/reserve_product/:itemId', function (req, res) {
  const rsrv = reserveStockById(itemId, stock)
  if (!rsrv) {
    return jsonify({"status":"Product not found"})
  }

app.listen(port, function () {
  console.log(`Example app listening on port ${port}!`);
});
