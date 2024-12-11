
# import requests
# import json

# # ID of the user to get recommendation for
# userID=48818

# # Integrate the user ID in the URL
# url = 'http://127.0.0.1:5000/get_recommendation/{}'.format(userID)

# # Send the POST request to the web app
# r = requests.post(url)

# # Display the response
# print(r.text)

# print(json.loads(r.text))
import requests
import json

# Set the URL of the Azure function
azure_url = "https://httptriggp10.azurewebsites.net/api/http_trigger?"
# for example : azure_url = "https://netflix_recommendations.azurewebsites.net/api/get_recommandations/"

# Set the parameters of the request
request_params = {"user_id":48818}

# Send the request to the Azure function
r = requests.post(azure_url, params=request_params)

# Grab the recommendations as a Python dictionary
recommendations_dict = json.loads(r.content.decode())
print(recommendations_dict)

