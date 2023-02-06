const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  mode: 'development',  // Or 'production' or 'none'
  entry: {
    index: ['./Finance/src/index.js']
  },
  output: {
    path: path.resolve(__dirname, './build'),
    filename: 'index.bundle.js'
  },
  plugins: [
    new BundleTracker({filename: './webpack-stats.json'})
  ],
  stats: 'verbose', 
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          'style-loader',
          'css-loader', 
        ]
      }, 
      {
        test: /\.js|\.jsx$/, 
        exclude: ['C:/Users/Tengwei/Desktop/coding_projects/sgnlp_finance/Finance/node_modules'], 
        loader: 'babel-loader', 
        options: { presets: ['@babel/env','@babel/preset-react'] }, 
        resolve: {
          fullySpecified: false,
        }
      }
    ]
  }
};
