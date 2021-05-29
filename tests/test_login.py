import json
from tests.SetupTearDown import BaseSetupTearDown

class TestUserLogin(BaseSetupTearDown):
        
    def test_success_login(self):
        #mock
        payload = json.dumps({
            "email": "anurag.nandigama@yahoo.ca",
            "password": "VolleyBall"
        })        
        response = self.app.post('/auth/register',
                                headers={"Content-Type": "application/json"},
                                data=payload 
                                )        
        #When
        response = self.app.post('/auth/login',
                                headers={"Content-Type": "application/json"},
                                data=payload 
                                )        
        #Then
        self.assertEqual(str, type(response.json['token']))
        self.assertEqual(200, response.status_code)


    def test_login_invalid_credentials(self):
        #mock
        email = "anurag.nandigama@yahoo.ca"
        password = "VolleyBall"
        payload = {
            "email": email,
            "password": password
        }        
        response = self.app.post('/auth/register',
                                headers={"Content-Type": "application/json"},
                                data=json.dumps(payload)
                                )        
        #When
        payload['email'] = "anurag123.nandigama@yahoo.ca"
        response = self.app.post('/auth/login',
                                headers={"Content-Type": "application/json"},
                                data=json.dumps(payload)
                                )            
        #Then
        self.assertEqual('Internal Server Error', response.json['message'])
        #self.assertEqual('Invalid Credentials', response.json['error'])
        self.assertEqual(500, response.status_code)


        