# Project Title

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Prerequisites](#Prerequisites)
- [Installing](#Installing)
- [Examples](#Examples)

## About <a name = "about"></a>

Simple AWS Lambda Python project that installs packages in the runtime. To be executed and developed locally using `AWS SAM`

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

## Prerequisites

```
pipenv
python 3.9
```

## Installing

```
pipenv install
pipenv shell
.bin/build.sh # sam local start-api executes in the background
.bin/run_tests/sh
```

## Examples
Success Installation
![Alt text](/scr/success.PNG?raw=true "Success Installation")

Failed Installation
![Alt text](/scr/failed.PNG?raw=true "Success Installation")
