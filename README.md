# PyTrans
Crated a simple windows application using python.
This application will take English language as input and it will translate the text into German, French & Italian using Microsoft cognitive services.

You can extend/modify this application to support multiple languages.

Before working please install python and all necessary packages.
Please registe in Microsoft Azure to get the API key for the language translator.


 # Append languages that you need to translat from the input language.
 # from --> is source language.
 # to --> is destination language.
    params = '&from=en&to=de&to=fr&to=it'
    
# update Ocp-Apim-Subscription-Key generated in Microsoft Azure portal.
    headers = {
        'Ocp-Apim-Subscription-Key': "",
        'Content-type': 'application/json'
    }
