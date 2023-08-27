from alerta.models.alert import Alert
from alerta.webhooks import WebhookBase
import json

class CentreonWebhook(WebhookBase):

    def incoming(self, query_string, payload):

        # Default parameters
        environment = 'Production'
        severity ='ok'
        group ='Centreon'
        text = ''
        value = ''
        tags = []
        attributes = {}
        origin = ''
        team = ''
        solveit = ''

        # A minimal version of Centreon alert, that can be customized
        return Alert(
            resource=payload['resource'],
            event=payload['event'],
            environment=payload.get('environment', environment),
            severity=payload.get('severity', severity),
            service=['Centreon'],
            group=payload.get('group', group),
            value=payload.get('value', value),
            text=payload.get('text', text),
            tags=payload.get('tags', tags),
            team=payload.get('team', team),
            solveit=payload.get('solveit', solveit),
            attributes=payload.get('attributes', attributes),
            origin=payload.get('hostname', origin),
            raw_data=json.dumps(payload, indent=4)
        )