import _ from 'lodash'

export const Datafactory = {
  genData(defaults) {
    return _.mapValues(this.schema, 
      (v,k) => defaults.hasOwnProperty(k)? defaults[k]: undefined
    )
  },
  schema: {
    name: String,
    amount: Number
  }
}