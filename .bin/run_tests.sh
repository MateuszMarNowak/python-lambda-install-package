#!/bin/bash

curl -X POST http://127.0.0.1:3000/describe_package --header "Content-Type: application/json" -d @jsons/jq.json

curl -X POST http://127.0.0.1:3000/describe_package --header "Content-Type: application/json" -d @jsons/dict_path.json

curl -X POST http://127.0.0.1:3000/describe_package --header "Content-Type: application/json" -d @jsons/touca-fbs.json

curl -X POST http://127.0.0.1:3000/describe_package --header "Content-Type: application/json" -d @jsons/error.json