import pytest
import importlib.util
import importlib.machinery
import random

# import and load modules
loader = importlib.machinery.SourceFileLoader('devops', './pages/devops.py')
spec = importlib.util.spec_from_loader('devops', loader)
devops = importlib.util.module_from_spec(spec)
loader.exec_module(devops)

class TestDevopsApi:
    def setup(self):
        self.devopsApi = devops.Test_devops()

    def test_create_new_vehicle(self):
        response = self.devopsApi.create_new_vehicle("honda", "civic", "silver", "2009-03-02T13:23:41.12")
        assert response.status_code == 201

    def test_get_vehicles(self):
        response = self.devopsApi.get_vehicles()
        assert response.status_code == 200

    def test_find_vehicle(self):
        existing_ids = [
            id["id"]
            for id in self.devopsApi.get_vehicles().json()
        ]
        response = self.devopsApi.find_vehicle(random.choice(existing_ids))
        assert response.status_code == 200

    def test_update_vehicle(self):
        existing_ids = [
            id["id"]
            for id in self.devopsApi.get_vehicles().json()
        ]
        response = self.devopsApi.update_vehicle("hondaUpdated", "civicUpdated", "silverUpdated", 
                                                "2021-08-20T13:22:22.22", random.choice(existing_ids))
        assert response.status_code == 200
     
    def test_delete_vehicle(self):
        existing_ids = [
            id["id"]
            for id in self.devopsApi.get_vehicles().json()
        ]
        response = self.devopsApi.delete_vehicle(random.choice(existing_ids))
        assert response.status_code == 204
