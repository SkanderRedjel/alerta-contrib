Centreon Webhook Setup Guide
==============

For help and assistance, join [![Slack chat](https://img.shields.io/badge/chat-on%20slack-blue?logo=slack)](https://slack.alerta.dev)

🛠️ Installation Steps:
------------

To start using the Centreon Webhook with Alerta, follow these installation steps:

Clone the GitHub repo and run:

    $ python setup.py install

Alternatively, you can install the webhook remotely from GitHub using pip:

    $ pip install git+https://github.com/alerta/alerta-contrib.git#subdirectory=webhooks/centreon

Please keep in mind: if you've set up Alerta within a Python virtual environment, it's crucial that your plugins are also installed within that same environment. This ensures that Alerta can dynamically find and utilize them, exemple:
```
$ python3 -m venv alerta #Create Alerta Virtual Environment
$ alerta/bin/pip install /opt/webhooks/ #Install Centreon webhook through the same Virtual Environment (My webhook scripts are in /opt/webhooks)
```

🚀 Sending Centreon alerts to Alerta
-------------

To integrate Centreon alerts with Alerta, you need to configure Centreon to send alerts to the Alerta service using a custom webhook, for this you will need to create two notification commands, one for the hosts, and another for the services. 
This webhook acts as a bridge. Follow the steps below to set up this integration:

--> Host Notification Command:
1. Create an API Key in Alerta.
2. In your Centreon web interface, navigate to Configuration > Commands.
3. Click on the Add button to create a new command.
4. Enter a Command Name, such as "Alerta Host Notification".
5. Select type "Notification".
6. In the Command Line field, enter the following command content:
``` curl -X POST -H "Content-type: application/json" -H "Authorization: Key YourAPIKey" -d '{ "environment": "Production or Staging", "event": "$HOSTNAME$ is down", "group": "Centreon", "origin": "Centreon", "resource": "$HOSTNAME$", "service": "Centreon", "severity": "$HOSTSTATE$", "value": "DOWN", "text": "The host is DOWN" }' "https://YourAlertaIOFQDN/api/webhooks/centreon" ``` 

--> Service Notification Command:
1. Create an API Key in Alerta.
2. In your Centreon web interface, navigate to Configuration > Commands.
3. Click on the Add button to create a new command.
4. Enter a Command Name, such as "Alerta Host Notification".
5. Select type "Notification".
6. In the Command Line field, enter the following command content:
``` curl -X POST -H "Content-type: application/json" -H "Authorization: Key YourAPIKey" -d '{ "environment": "Production or Staging", "event": "$SERVICEDESC$ on $HOSTNAME$", "group": "Centreon", "origin": "Centreon", "resource": "$HOSTNAME$", "service": "Centreon", "severity": "$SERVICESTATE$", "text": "$SERVICEOUTPUT$", "value": "$SERVICEOUTPUT$" }' "https://YourAlertaIOFQDN/api/webhooks/centreon" ``` 
And now, you will just have to add this notification command to your Host/Service templates.

NB1: Before adding this command to Centreon, i'd recommand to manually send this POST request and see if it works perfectly fine.

🛡️ License:
-------
Copyright (c) 2023 Skander REDJEL. Available under the MIT License.
