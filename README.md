# OBD2 Display for a 2017 BMW M440i 

Application that reads data from an OBD2 port and displays information about the car in real-time.

## Includes

- Backend API to read from the car's OBD2 port 
- Frontend website to actively display the backend's data
- Systemd service and kiosk script for running on a Raspberry Pi at boot

## Tools Used
- [PyODBC](https://pypi.org/project/pyodbc/)
- [Vue.js](https://vuejs.org)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)

## Usage
- clone repo to Raspberry Pi
- run npm install in the frontend directory and pip install -r requirements.txt in the backend directory
- run chmod +x on kiosk.sh
- move kiosk.service to the correct directory and enable using systemctl