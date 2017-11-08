import assert from 'assert'
import prettyjson from 'prettyjson'

import Block from '../block'
import Blockchain from '../blockchain'
import { Datafactory } from '../datafactory'

describe('basic blockchain', function () {
  it('it should create a blockchain and accept blocks', function () {
    let savjeeCoin = new Blockchain()
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
})