#!/bin/bash


cd ~

python3 ~/E_project/modules/bluetooth_interface.py

~/E_project/modules/displays/display_main

source ~/E_project/myvenv/bin/activate

python3 ~/E_project/project2/manage.py runserver 0.0.0.0:4500 



exit 0
