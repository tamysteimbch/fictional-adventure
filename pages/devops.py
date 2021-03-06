import requests

class DevopsAPI():
    def __init__(self, client=requests):
        super().__init__()
        self.base_api_url = "http://localhost:8080/vehicles"
        self.http_client = client

        self.get_all_vehicles = f"{self.base_api_url}/list/all"
        self.get_vehicle_by_id = f"{self.base_api_url}/list"
        

    def create_new_vehicle(self, manufacturer, model, color, manufacturedAt):
        data = {"manufacturer": manufacturer,
                "model": model,
                "color": color,
                "manufacturedAt": manufacturedAt}
        return self.http_client.request("POST", self.base_api_url, json=data)
    
    def find_vehicle(self, vehicle_id):
        return self.http_client.request("GET", f"{self.get_vehicle_by_id}/{vehicle_id}")

    def get_vehicles(self):
        return self.http_client.request("GET", f"{self.get_all_vehicles}")

    def update_vehicle(self, manufacturer, model, color, manufacturedAt, vehicle_id):
        data = {"manufacturer": manufacturer,
                "model": model,
                "color": color,
                "manufacturedAt": manufacturedAt}
        return self.http_client.request("PUT", f"{self.base_api_url}/{vehicle_id}", json=data)

    def delete_vehicle(self, vehicle_id):
        return self.http_client.request("DELETE", f"{self.base_api_url}/{vehicle_id}")