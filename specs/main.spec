import assert from 'assert'
import prettyjson from 'prettyjson'

import Block from '../block'
import Blockchain from '../blockchain'
import { Datafactory } from '../datafactory'

let savjeeCoin

describe('basic blockchain', function () {
  it('it should create a blockchain and accept blocks', function () {
    savjeeCoin = new Blockchain()
    let firstBlock = new Block(
      1, 
      new Date().getTime(), 
      Datafactory.genData({amount: 4}))
    savjeeCoin.add(firstBlock) // why am I giving it these first values in the block??

    let secondBlock = new Block(
      2, 
      new Date().getTime(), 
      Datafactory.genData({amount: 10}))
    savjeeCoin.add(secondBlock)

    console.log(prettyjson.render(savjeeCoin))

    assert(true)
  })

  it('should correctly validate its chain when valid', function () {
    assert(Blockchain.validateChain(savjeeCoin.chain))
  })

  it('should not validate its chain when containing illegal descendent', function () {
    let prev = savjeeCoin.chain[1].prev

    console.log('from\n', prettyjson.render(savjeeCoin.chain[1]), '\n')

    savjeeCoin.chain[1].prev = 'invalid'

    console.log(prettyjson.render(savjeeCoin.chain[1]))

    assert.equal(false, Blockchain.validateChain(savjeeCoin.chain), 
      'illegal descendent')
    savjeeCoin.chain[1].prev = prev // revert changes
  })

  it('should not validate its chain when containing falsified hash', function() {
    let hash = savjeeCoin.chain[1].hash
    let amount = savjeeCoin.chain[1].data.amount

    console.log('from\n', prettyjson.render(savjeeCoin.chain[1]), '\n')

    savjeeCoin.chain[1].hash = 'invalid'

    assert.equal(false, Blockchain.validateChain(savjeeCoin.chain), 
      'misreported hash')

    savjeeCoin.chain[1].hash = hash // revert changes
    assert(Blockchain.validateChain(savjeeCoin.chain))

    savjeeCoin.chain[1].data.amount = 10000 // bogusly increasing my yield
    assert.equal(false, Blockchain.validateChain(savjeeCoin.chain), 
      'misreported hash')

    savjeeCoin.chain[1].data.amount = amount // revert changes
  })
})