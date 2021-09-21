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

    def test_update_vehicle(self):
        response = self.devopsApi.update_vehicle("hondaUpdated", "civicUpdated", "silverUpdated", "2021-03-02T13:22:22.22", "11")
        assert response.status_code == 200