#!/usr/bin/env python
import sys
from food_truck.crew import FoodTruckCrew
input_cmd = sys.argv[0]

input_cmd = 'São Paulo, baixo custo'

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': input_cmd
    }
    FoodTruckCrew().crew().kickoff(inputs=inputs)