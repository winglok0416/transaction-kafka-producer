## Transaction Kafka Producer
This program will scrap the data from NASDAQ and publish it to the Kafka with topic - transaction to simulate the real-time streaming.

Before running this program, please make sure you have following the instruction to set up the kafka brokers and spark.

### Environment
Operating System: MacOS 13.3 or Ubuntu 18

Dependencies:
Python 3.8.16
Package Installer for Python (pip)
Anaconda
Docker
Docker Compose
Chrome

### Create conda environment
```
conda create --name cmsc5702
```

### Activate conda environment
```
/opt/anaconda3/bin/activate && conda activate /opt/anaconda3/envs/cmsc5702
```

### Install dependencies
```
pip install pandas kafka-python selenium webdriver-manager
```

### Run the program
```
# Normal run
python main.py

# Run with mock data (No scrapping)
python main.py -m
```