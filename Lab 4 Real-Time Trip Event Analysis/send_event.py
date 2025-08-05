from azure.eventhub import EventHubProducerClient, EventData
import json

# Replace with your actual connection string from Azure Portal
connection_str = "Endpoint=sb://tripnamespace.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=2F87kO0CINoH86uZrK8ZGT79GVO9/iLIU+AEhJbQ/ec="
eventhub_name = "taxi-trips-hub"

producer = EventHubProducerClient.from_connection_string(conn_str=connection_str, eventhub_name=eventhub_name)

event_data_batch = producer.create_batch()

trip_event = {
    "ContentData": {
        "vendorID": "V123",
        "tripDistance": 0.9,
        "passengerCount": 5,
        "paymentType": "2"
    }
}

event_data_batch.add(EventData(json.dumps(trip_event)))

producer.send_batch(event_data_batch)
producer.close()

print("✅ Event sent successfully.")
