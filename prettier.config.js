'use strict'

/**
 * @type {import('prettier').Options}
 */
const config = {
  plugins: [require.resolve('prettier-plugin-toml')],
  semi: false,
  singleQuote: true,
}

module.exports = config
