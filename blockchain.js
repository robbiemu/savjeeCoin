import Block from './block'
import { Datafactory } from './datafactory'

class Blockchain {
  constructor () {
    this.chain = [this.createGenesisBlock()]
  }

  createGenesisBlock () {
    return new Block(
      0, 
      new Date().getTime(), 
      Datafactory.genData({name: 'Genesis Block'})
    )
  }

  getLatest () {
    return this.chain[this.chain.length - 1]
  }

  add (block) {
    block.prev = this.getLatest().hash
    block.hash = block.calculateHash()
    this.chain.push(block)
  }
}

Blockchain.validateChain = function (chain) {
  for (let i = 1; i < chain.length; i++) {
    let block = chain[i]
    let prev = chain[i-1]

    if(block.hash !== block.calculateHash()) {
      return false
    }

    if(block.prev !== prev.hash) {
      return false
    }
  }
  return true
}

export default Blockchain