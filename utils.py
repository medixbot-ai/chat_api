#!/usr/bin/env python
# -*- coding: utf-8 -*-
import openai


def configure_openai():
    openai.api_key = "API_KEY"

def determine_intention(text):
    text = text.lower()

    job_ads_keywords = ['job ads', 'job ad']
    job_position_keywords = ['job position','job positions','list of job positions', 'position available']
    top_employee_names_keywords = ['top employee names','top']
    all_employee_names_keywords = ['all employee names',"all employees"]

    if any(keyword in text for keyword in job_ads_keywords):
        return "Job Ads Writing"
    elif any(keyword in text for keyword in job_position_keywords):
        return "Listing Job Position"
    elif any(keyword in text for keyword in top_employee_names_keywords):
        return "Listing Top Employee Names"
    elif any(keyword in text for keyword in all_employee_names_keywords):
        return "Listing All Employee Names"
    else:
        return "Uncertain Intention"

def get_chat(prompt):
     
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=prompt,
        max_tokens=300  
    )
    return response

def read_file(file_path):
    with open(file_path,"r") as ff:
        return ff.read()
