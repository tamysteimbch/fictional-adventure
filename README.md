# fictional-adventure - how to use it & create your own automation

-------------------------------------------------

      HOW TO RUN THIS AUTOMATION IN YOUR COMPUTER:
     - clone this repository and this one = 'https://github.com/DouglasGorges/DevOps-TestsServer'
     - run the file VehiclesApplication.java from the DevOps-TestsServer (check which port it's running the tomcat, the default is 8080)
     - in your terminal, access the fictional-adventure directory:
       *in the same terminal, type this command line 'pytest tests/test_devops.py'
        this command line will run every test that is in test_devops.py, if you want to run just one specific function run this:
        'pytest tests/test_devops.py::TestDevopsApi::<the name of the test you want to run>'


--------------------------------------------------

       HOW TO CREATE AN AUTOMATION FOR API's FROM SCRATCH*
      - create a repo in github and clone it into your pc (optional);
      - in your project folder, install pytest using 'pip install -U pytest';
      - check if you downloaded the latest version using 'pytest --version' **;
      - create a separate folder to create the POST, GET.. etc requests, name it 'pages';
      - create another folder to create the actual test, name it 'tests'
      - pages folder:
        * in this folder you'll create a file containing your api urls, you can call it {nameOfYourApi}.py
        * after creating it you have to add 'import requests' into your code, to get all functions for api testing
        * create a class called Test_nameOfYourApi, in this step you'll want to add basic configurations such as:
          > def __init__(self, client=requests):
          >   super().__init__()
              self.base_api_url = "http://yourapplication.com/api/v1.0/..." ***
              self.http_client = client
              
              self.get_example = f"{self.base_api_url}"list/all
         
         * with this configuration you'll be able to start your tests, like in this example:
           > def get_all_example(self):
                 return http_client.request("GET", self.get_example) ****
         
       - Great, now you have the "background" so you can start testing, with this you can go crazy now
       - in the tests folder, create a file named test_nameOfYourApi.py
         * in this file you'll add: 
            import pytest
            from pages.nameOfYourApi import test_nameOfYourApi
         * after importing, you'll create a class called TestNameOfYourApiApi
         * in this class, you'll create a def setup
           > def setup(self):
                 self.exampleApi = nameOfYourApi.Test_nameOfYourApi *****
         * after this setup, you'll start your testing, in this example I'll only show you the happy path, but you can go crazy =D
           > def test_get_all_example(self):
                 response = self.exampleApi.get_all_example()
                 assert response.status_code == 200 ******
      
        - with that you'll be able to run your test using 'pytest tests/test_nameOfYourApi.py'
        
------------------------------------------------------------------------------------------------------------------------------------------
        
* python and pip are required to run some command lines, check the python.org to install python, 
  then in your terminal check if you already have the pip using the command line: pip --version
  if you don't have pip in your pc, go to https://pip.pypa.io/en/stable/installation, or try to run 'python3 -m pip', 'easy_install pip'
** pytest documentation about getting started and installation: https://docs.pytest.org/en/6.2.x/getting-started.html
-------------------------------------------------------------------------------------------------------------------------------------------
*** this is just an example, you'll add your application's base api url, with this base_api_url all the other requests you'll just increment the rest of the url 
**** this line gets the request import, send this a request as a get and the url that is trying to use 
***** this line creates a variable to shorten your coding, instead of using nameOfYourApi.Test_nameOfYourApi everytime, you'll only use self.exampleApi
****** this line is checking if the expected status code is being returned, if not the test will fail.
