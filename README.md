# Overview 
The Finance Language Analyzer is an analytics engine that analyzes news articles and returns sentiments about different stocks. It runs on Django on the backend and React on the frontend, and uses the SGNLP module to deliver its analyses. 

# Developer 
- Ngwan Teng Wei 

Using sgnlp module downloaded from here \
https://aisingapore.org/aiproducts/nlp-hub/?_ga=2.40195622.565862378.1675670806-1698464324.1670228435

## Documentation 

# Prerequisites 
Main Tech Stack: 
python - 3.8.x \
conda - 4.x.x \
Django - 3.2.5 \
node - 16.x.x \
npm - 8.5.0 \
react - 18.2.0 

# Environment set up 
Strongly recommend using gitbash. 

## 1. Install Conda 
We use conda to manage our python virtual environment. Download and install anaconda 
https://www.anaconda.com/products/distribution

```bash 
# verify conda version 
conda --version 

# verify conda installation PATH 
which conda
```

If it does not show up, you may need to configure your PATH variable. 

Next, add conda-forge repository. 

```bash 
conda config --add channels conda-forge
``` 

Create a virtual environment for the analyzer: 

```bash 
# create the environment with python version=3.8
conda create -n sgnlp_finance python=3.8 -y

# activate your environment 
conda activate sgnlp_finance 
```

## 2. Setting up project 

In the appropriate working folder, clone this repo: 

```bash 
git clone https://github.com/tw-ngwan/sgnlp_finance

# change directory and enter project 
cd sgnlp_finance 
``` 

## 3. Install required Python packages 

Ensure that your conda is activated before installing requirements. If you don't have pip, you can run conda install pip first. 
```bash 
pip install -r requirements.txt
``` 

If there are any failures, please manually install the module itself from conda or pip. For sgnlp, please visit the website and download from there if there are any failures. 

## 4. Install Node

Download Node.js 
https://nodejs.org/en/download/

Verify your node installation 

```bash 
# verify node version
node --version 

# verify npm version 
npm --version 

# verify npx version 
npx --version 
``` 

## 5. Install required JavaScript packages 

Run the following installs: 

```bash 
npm install babel 
npm install axios 
npm install babel-loader 
npm install css-loader 
npm install file-saver 
npm install heap 
npm install js-cookie 
npm install jshint 
npm install mathjs 
npm install react 
npm install react-dom 
npm install react-router-dom 
npm install style-loader 
npm install webpack 
npm install webpack-bundle-tracker 
npm install webpack-cli 
```

## 6. Run server 

The server is rendered from Django itself. To run it, enter the following command 
```bash 
python manage.py runserver 0.0.0.0:8000
```


# Footnotes 
If the evaluation of the model, throws an authentication error, it may be due to the use of relative filepaths. In sgnlp_finance/sgnlp_finance_app/model/evaluate.py, try replacing the relative filepaths with absolute filepaths to the module. The relative filepaths may be corrupted because SGNLP is calling a cached filepath

Whenever any of the JavaScript files are updated, run the following commands to update

```bash 
# to rebuild webpack 
npx webpack --config webpack.config.js --cache

# to collect and transfer to static dir 
python manage.py collectstatic
```

Reuploaded after first push failed to upload everything 
