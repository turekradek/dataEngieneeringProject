from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

import os 
import logging
from datetime import datetime
import pandas as pd 

app = Flask(__name__)
metrics = PrometheusMetrics(app)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")


@app.route('/')
def index():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Hello, World! <br> {current_time}"

@app.route('/filescsv')
def filescsv():
    filespath = '../../files_csv'
    fileslist = os.listdir(filespath)
    print( fileslist )
    logger.info(f"This is an info message: Filelist: {fileslist}")
    # with open(f'{filescsvpath}/file1.csv') as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         print(line)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Reading CSV files: <br> {current_time} <br> fileslist: {fileslist}"

@app.route('/filesjson')
def filesjson():
    filespath = '../files_json'
    fileslist = os.listdir(filespath)
    print( fileslist )
    logger.info(f"This is an info message: Filelist filesjson: {fileslist}")
    # with open(f'{filescsvpath}/file1.csv') as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         print(line)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return f"Reading Json files : <br> {current_time} <br>"

@app.route('/bronze')
def filesbronze():
    filespath = '../bronze'
    fileslist = os.listdir(filespath)
    logger.info(f"This is an info message: Filelist bronze: {fileslist}")
    
    data = []
    for idx, file in enumerate(fileslist):
        name, extension = os.path.splitext(file)
        timestamp = datetime.fromtimestamp(os.path.getmtime(os.path.join(filespath, file))).strftime("%Y-%m-%d %H:%M:%S")
        data.append([idx, name, extension, timestamp])
    
    df = pd.DataFrame(data, columns=['id', 'namefile', 'extension', 'timestamp'])
    df = df.sort_values(by=['extension', 'namefile'])
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Reading bronze files <br> {current_time} <br> {df.to_html()}"

@app.route('/silver')
def filessilver():
    filespath = '../silver'
    fileslist = os.listdir(filespath)
    logger.info(f"This is an info message: Filelist silver: {fileslist}")
    
    data = []
    for idx, file in enumerate(fileslist):
        name, extension = os.path.splitext(file)
        timestamp = datetime.fromtimestamp(os.path.getmtime(os.path.join(filespath, file))).strftime("%Y-%m-%d %H:%M:%S")
        data.append([idx, name, extension, timestamp])
    
    df = pd.DataFrame(data, columns=['id', 'namefile', 'extension', 'timestamp'])
    df = df.sort_values(by=['extension', 'namefile'])
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Reading silver files <br> {current_time} <br> {df.to_html()}"

@app.route('/gold')
def filesgold():
    filespath = '../gold'
    fileslist = os.listdir(filespath)
    logger.info(f"This is an info message: Filelist gold: {fileslist}")
    
    data = []
    for idx, file in enumerate(fileslist):
        name, extension = os.path.splitext(file)
        timestamp = datetime.fromtimestamp(os.path.getmtime(os.path.join(filespath, file))).strftime("%Y-%m-%d %H:%M:%S")
        data.append([idx, name, extension, timestamp])
    
    df = pd.DataFrame(data, columns=['id', 'namefile', 'extension', 'timestamp'])
    df = df.sort_values(by=['extension', 'namefile'])
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Reading gold files <br> {current_time} <br> {df.to_html()}"

@app.route('/scripts')
def filesscripts():
    filespath = '../scripts'
    fileslist = os.listdir(filespath)
    logger.info(f"This is an info message: Filelist scripts: {fileslist}")
    
    data = []
    for idx, file in enumerate(fileslist):
        name, extension = os.path.splitext(file)
        timestamp = datetime.fromtimestamp(os.path.getmtime(os.path.join(filespath, file))).strftime("%Y-%m-%d %H:%M:%S")
        data.append([idx, name, extension, timestamp])
    
    df = pd.DataFrame(data, columns=['id', 'namefile', 'extension', 'timestamp'])
    df = df.sort_values(by=['extension', 'namefile'])
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Reading scripts files <br> {current_time} <br> {df.to_html()}"

@app.route('/dockervolume')
def filessdockervolume():
    filespath = '../docker_volume'
    fileslist = os.listdir(filespath)
    logger.info(f"This is an info message: Filelist docker_volume: {fileslist}")
    
    data = []
    for idx, file in enumerate(fileslist):
        name, extension = os.path.splitext(file)
        timestamp = datetime.fromtimestamp(os.path.getmtime(os.path.join(filespath, file))).strftime("%Y-%m-%d %H:%M:%S")
        data.append([idx, name, extension, timestamp])
    
    df = pd.DataFrame(data, columns=['id', 'namefile', 'extension', 'timestamp'])
    df = df.sort_values(by=['extension', 'namefile'])
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Reading docker_volume files <br> {current_time} <br> {df.to_html()}"

@app.route('/routes')
def show_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append(f"{rule.endpoint}: {rule.rule}")
    return "<br>".join(routes)

def files_list( path ):
    fileslist = os.listdir(path)
    return fileslist

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
