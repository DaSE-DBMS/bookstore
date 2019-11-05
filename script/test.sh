#!/bin/sh
export PATHONPATH=`pwd`
coverage run --timid --branch --source fe,be --concurrency=thread -m pytest -v
coverage combine
coverage report
coverage html
