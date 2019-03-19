# Traffic-Sign-Recognition-Library
A collection of utilities to promote growth in open source traffic sign recognition. For now this collection is limited to just dataset generation, but in the future expect more utilities to help anyone get started with traffic sign recognition and detection.

Prereqs:
 - Google API credentials. Add these to creds.py as `dev_key`
 - A geocoders account. Add the username as `geocoders_name`
 
# Dataset Generation
This tool allows for generating datasets of traffic signs, and can be used with any classifier.

To run: `python3 run.py --city=${city} --state=${state}`

Troubleshooting: `pip install` any dependencies you don't have until it runs or contact me
