import sha256 from 'crypto-js/sha256'

export default class Block {
  /*
   * index (optional) - where the block sits on the chain
   * timestamp - when
   * data - data associated with the block (such as details of tx, sender, reciever)
   * prev - the previous hash
   */
  constructor (index, timestamp, data, prev='') {
    this.index = index
    this.timestamp = timestamp
    this.data = data
    this.prev = prev
    this.hash = this.calculateHash()
  }

  // generate a hash with the properties of a block
  calculateHash () {
    return sha256(
      this.index + 
      this.prev + 
      this.timestamp + 
      JSON.stringify(this.data)
    ).toString()
  }
}
