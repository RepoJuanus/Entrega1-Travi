#!/bin/bash
if [ $VIRTUAL_ENVIRONMENT ]
then 
    deactivate
fi
. django_venv/bin/activate