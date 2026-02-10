# AI Room Booking Chatbot

## Demo
![AI Room Booking Chatbot – Demo](demo.gif)

## Instructions

Download or clone this repository, then follow the steps below.

### 1. Set up IBM Watson Assistant
1. Create or log in to your IBM Cloud account:  
   https://cloud.ibm.com/registration  
   https://cloud.ibm.com/login
2. Provision a Watson Assistant instance:  
   https://cloud.ibm.com/catalog/services/watson-assistant  
   Name it and click **Create**.
3. Launch Watson Assistant.
4. Click **Create assistant** and give it a name (optional: add a description).
5. Choose **Add an actions or dialog skill**.
6. Open the **Upload skill** tab and upload **skill-Room-Booking.json**.

### 2. Configure IBM Cloud Function (Email Trigger)
1. Go to IBM Cloud Functions: https://cloud.ibm.com/functions/actions  
   Click **Create → Action**.
2. Name your action, leave “Enclosing Package” as default, select **Python 3.7**, then click **Create**.
3. Paste the code from **IBM_Cloud_Function.py** into the editor.
4. In your Google Account security settings (https://myaccount.google.com/security):
   - Enable **2-Step Verification**
   - Open **App Passwords**
   - Select **Mail** as the app and **Other** as the device, then generate a password.
5. Insert the generated app password into line 10 of the Cloud Function code.

### 3. Enable Web Action & Connect Webhook
1. In your IBM Cloud Function, go to **Endpoints**.
2. Enable **Web Action** and copy the URL.
3. In Watson Assistant, open **Options → Webhooks**.
4. Paste the URL and append **.json** at the end.

---

Your AI Room Booking Chatbot is now fully set up.
