# Lab 4 – Real-Time Trip Event Analysis
## 📋 Summary
This project shows a real time event driven structure to track to observe suspecting or interesting information on taxi trips. The events are consumed through Azure Event hub, processed through an Azure Function and reported through a Logic app that identifies the insights and publishes them to be reviewed in operations.

---
## Review of Architecture

**Components Used:**
**Azure Event Hub** - It is utilized in ingesting real-time trip data in various vendors.
- Azure Function App - Processes the incoming data about trips and finds any insights, including:
  - Rides in Groups
  - Money Transactions
  Suspiciously short journeys
**Azure Logic App** -Subscribes an Event Hub, triggers the Azure Function and parses the results and performs conditional flows.

**Flowchart Screenshot:**
<img width="1365" height="649" alt="Image" src="https://github.com/user-attachments/assets/82456398-f5cb-4ecb-b249-5e764bf87d93" />
## ⚙️ Logic App Flow – Steps
**Trigger:**
   Uses Fire when there are new events on Event Hub.

2. **HTTP Action:**
   Is a POST request to the Azure Function endpoint with a JSON body that sends the event payload:
     ```json
     @{triggerBody()?['ContentData']}
     ```

3. **Parse JSON:**
   Deconstructs the response of the function to yield flags and insights.

4. **To Each Insight:**
   Iterations in flags such as `GroupRide`, `CashPayment`, etc.
   Raises an alert or logs as necessary (teams or email could also be integrated later).
   Azure Function Logic

   ---

## 🧮 Azure Function Logic
The Function takes a JSON payload and sends insights it finds. For example:

## Sample Input:

```json
{
  "vendorID": "V123",
  tripDistance: 0.9
  "passengerCount": 5,
  "paymentType": "2"
}
```

## Demo video link

