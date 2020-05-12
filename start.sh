#!/bin/bash

export AIRFLOW_HOME="/home/xiatong/PycharmProjects/apacheairflow"

#### credentials ####
export SQL_ALCHEMY_CONN='postgresql+psycopg2://airflow:airflow@localhost/airflow_metadata'
export AIRFLOW_CONN_POSTGRES_CUSTOMER_SERVICE='postgresql://ubtspqkwsmfqtb:1bbe9e7b290046158259ac3aab3b7a6796e10ba15ab56f0052d6490c2f8d110b@ec2-46-137-84-140.eu-west-1.compute.amazonaws.com:5432/dftoar1ttuogqt'
export AIRFLOW_CONN_POSTGRES_DATA_SERVICE='postgresql://hpumayolqoeien:36b8132b58cf83000cc3911631786614d1734c9a758e9955a464e6127c42a1c8@ec2-54-75-246-118.eu-west-1.compute.amazonaws.com:5432/dad26s7icb6693'

