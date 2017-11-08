import Block from './block'
import { Datafactory } from './datafactory'

export default class Blockchain {
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
    block.previousHash = this.getLatest().hash
    block.hash = block.calculateHash()
    this.chain.push(block)
  }
}