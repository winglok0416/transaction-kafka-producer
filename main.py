import sys
import time
import uuid

from data_manipulation import convert_rows_to_records
from exception import StreamingDataNotAvailableException
from persistence import save_data_to_txt
from scrapping import ScrappingDriver
from transaction_record_producer import TransactionRecordProducer
from mock_data import mock_records

# Scrap data every ? seconds
FREQUENCY = 10.0

if __name__ == '__main__':
    print("----- Program start -----\n")
    args = sys.argv
    if "-m" in args:
        mock_flag = True
    else:
        mock_flag = False

    try:
        while True:
            if mock_flag is True:
                print("Use mock data...\n")
                records = mock_records
            else:
                print("Start scrapping data from NASDAQ...\n")
                driver = ScrappingDriver()
                rows = driver.scrap_data()
                driver.close()
                print("Converting to records...\n")
                records = convert_rows_to_records(rows)
                print("Saving to text file...")
                save_data_to_txt(records)

            print("Ready to publish event...")
            producer = TransactionRecordProducer()
            for record in records:
                producer.publish(str(uuid.uuid4()), record)

            print("Sleep for {} seconds before scrapping again".format(FREQUENCY))
            time.sleep(FREQUENCY)
    except StreamingDataNotAvailableException:
        print("Please check the data in provided URL is available or not")
