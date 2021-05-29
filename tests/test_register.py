import json
from tests.SetupTearDown import BaseSetupTearDown

class TestUserRegister(BaseSetupTearDown):
    
    def test_success_register(self):
        #mock
        payload = json.dumps({
            "email": "anurag.nandigama@yahoo.ca",
            "password": "VolleyBall"
        })
        
        response = self.app.post('/auth/register',
                                headers={"Content-Type": "application/json"},
                                data=payload 
                                )
        
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)
        