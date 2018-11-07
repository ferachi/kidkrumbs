const path = require('path');
const webpack = require('webpack');
var MiniCssExtractPlugin = require('mini-css-extract-plugin');
const VueLoaderPlugin = require('vue-loader/lib/plugin')

module.exports = {
	entry: {
		app: './src/main.js'
	},
	output: {
		filename: '[name].bundle.js',
		path: path.resolve(__dirname, 'dist'), // for bundling ; npm run build
		publicPath: '/' // path to prepend for both bundling and server operations
	},
	mode:'development',
	devtool: 'inline-source-map',
    devServer: {
        index: './play/index.html',
        contentBase: ['./dist', './play']
    },
	plugins: [
	    new MiniCssExtractPlugin({
			filename: 'style.css'
		}),
		new VueLoaderPlugin()
	],
    resolve:{
        extensions : ['*','.js','.jsx','.vue']
    },
	module:{
		rules:[
			{
        		test: /\.vue$/,
        		loader: 'vue-loader'
      		},
			{
				test: /\.styl(us)?$/,
				use: [
					MiniCssExtractPlugin.loader,
					{
						loader: 'css-loader',
						options: {
							importLoaders : 2,
							modules: true,
							localIdentName: '[path][name]__[local]__[hash:base64:6]',
                            getLocalIdent : function(context, localIdentName, localName, options){
                                var index = context.resource.indexOf("module=");
                                var moduleName = context.resource.substr(index).replace(/module=true|module\=|s/, "");
                                return moduleName.length > 1 ? moduleName + "--" + localName : localName;
                            }
						}
					},
				    'postcss-loader',
					'stylus-loader'
				]
			},
            {
                test: /\.scss$/,
                use: [
                    "style-loader", // creates style nodes from JS strings
                    "css-loader", // translates CSS into CommonJS
                    "sass-loader" // compiles Sass to CSS, using Node Sass by default
                ]
            },
			{
				test: /\.css$/,
				use: [
					'style-loader',
					'css-loader'
				]
			},
			{
				test: /\.coffee$/,
				use: [
					{
						loader: 'coffee-loader',
						options: {
							transpile: {
								presets: ['env']
							}
						}
					}
				]
			}
			,
			{
				test: /\.js$/,
				exclude: file => (
					/node_modules/.test(file) &&
					!/\.vue\.js/.test(file)
				),
				loader: "babel-loader"
			}
		]
	}

};
