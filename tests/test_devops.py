import pytest
import importlib.util
import importlib.machinery

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

    def test_find_vehicle(self):
        response = self.devopsApi.find_vehicle(1)
        assert response.status_code == 200

    def test_get_vehicles(self):
        response = self.devopsApi.get_vehicles()
        assert response.status_code == 200
     
    def test_delete_vehicle(self):
        response = self.devopsApi.delete_vehicle(1)
        assert response.status_code == 204
