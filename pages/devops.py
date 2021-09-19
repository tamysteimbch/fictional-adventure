import requests

class Test_devops():
    def __init__(self, client=requests):
        super().__init__()
        self.base_api_url = "C:/Users/Tamiris Cristiane/DevOps-TestsServer/vehicles/"
        self.http_client = client

        self.get_all_vehicles = f"{self.base_api_url}list/all"
        self.get_vehicle_by_id = f"{self.base_api_url}list"
        

    def create_new_vehicle(self, vehicle_id):
        data = {"vehicle_id": vehicle_id}
        return self.http_client.request("POST", f"{self.get_vehicle_by_id}", json=data)
        
# caso precise montar uma url, faça assim: return self.http_client.request("GET", f"{self.get_vehicle_by_id}/{self.vehicle_id}")