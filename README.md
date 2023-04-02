## Transaction Kafka Producer
This program will scrap the data from NASDAQ and publish it to the Kafka with topic - transaction to simulate the real-time streaming.

Before running this program, please make sure you have following the instruction to set up the kafka brokers and spark.

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
pip install -r requirements.txt
```

### Run the program
```
# Normal run
python main.py

# Run with mock data (No scrapping)
python main.py -m
```