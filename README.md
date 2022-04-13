# kafka-demo

Project used for demo and training on how to use Kafka with Python. 
Project provides a kafka producer and a kafka consumer and required docker compose to run the kafka infra on your local machine.

The demo producer produces fake consumer order data to the `orders` kafka topic which can be consumed by the consumer. The data is produced by Faker library.

Demo payload for customer order

```
{
  'customer_id': 'dc03472c-ad73-49b1-b093-0b13baf23e60',  
  'customer_name': 'Andre Moran',    
  'customer_email': 'philipbrown@example.net',  
  'customer_address': '997 Jonathan Villages Suite 339\nSouth Sheila, MD 18766',  
  'order_number': 194246,  
  'date_of_delivery': '2022-04-09',  
  'price': 6.87,  
  'currency': 'AUD'  
}
```


# Pre requisite 

* Docker 
* Non M1 mac machine. (M1 macs cannot be supported as this project used Confluent kafka and schema registry. Schema registry is currently not supported for
 m1 macs. https://github.com/confluentinc/common-docker/issues/117)
* Python 3.7+


# Running the project


1. Create a virtual env and activate it.

   ```
      pyenv install 3.9.1  
      pyenv virtualenv 3.9.1 kafka-demo  
      pyenv activate kafka-demo
   ```

2. Install requirements

   ```
      pip install -r requirements.txt
   ```

3. Setup dev environment

   ```
      chmod +x dev/apply-avro-schemas.sh
      make dev-up
   ```

5. Start producer 

   ```
      from src.util.demo_order_producer import produce_orders_to_kafka  
   
      # Produces 5 randomly created order data to kafka  
      produce_orders_to_kafka(5)
   ```

6. Start consumer

   ```
      from src.util.demo_consumer import consume_messages  
      consume_messages()
   ```

    Should start seeing messages printed out in the console.



# Setting up a new topic

1. Add Avro schema to dev folder
2. Add necessary commands to apply the schema to dev/apply-avro-schemas.sh
3. run `make dev-up`
4. Add topic details to `OrderApp/Config.py` file
5. Write a function to produce message in the format required
6. Run consumer.   
   ```
      from src.util.demo_consumer import consume_messages  
      consume_messages()
   ```
   


