import requests
import json

url = "https://dialer-api-sandbox-prod.doocti.com/api/v1/login"

payload = json.dumps({
  "user": "bhaghyasandar@xmedia.in",
  "station": "7418304703"
})
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnQiOiJBUEkgU2FuZGJveCIsInVzZXJuYW1lIjoiQWRtaW4iLCJ0ZW5hbnRfY29kZSI6ImN0aV9wcm9kX2FwaV9zYW5kYm94XzE5MDUyMDIyIiwic2NvcGUiOiJhZG1pbiIsImlzcyI6Imh0dHBzOi8vbGl2ZS1kb29jdGkuYXUuYXV0aDAuY29tLyIsInN1YiI6Ino2TDM5cnpEYWZrbm9LbnI1VlB5aDFPM0VvWlVMRlBkQGNsaWVudHMiLCJhdWQiOiJodHRwczovL3Byb2QtYXBpLmRvb2N0aS5jb20iLCJleHAiOjE3MTYxMTc2NTI4MDQsImlhdCI6MTY1Mjk1OTI1Mn0.oSaWv63aEcA8CnDv0wb0n685NXKPx2coIeGeFy-tOEw',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

# logging in api ...........user login with mail and phn num



url = "https://dialer-api-sandbox-prod.doocti.com/api/v1/call"

payload = json.dumps({
  "station": "7418304703",
  "phone_number": "6382384894",
  "agent": {
    "identity": "user",
    "value": "bhaghyasandar@xmedia.in"
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnQiOiJBUEkgU2FuZGJveCIsInVzZXJuYW1lIjoiQWRtaW4iLCJ0ZW5hbnRfY29kZSI6ImN0aV9wcm9kX2FwaV9zYW5kYm94XzE5MDUyMDIyIiwic2NvcGUiOiJhZG1pbiIsImlzcyI6Imh0dHBzOi8vbGl2ZS1kb29jdGkuYXUuYXV0aDAuY29tLyIsInN1YiI6Ino2TDM5cnpEYWZrbm9LbnI1VlB5aDFPM0VvWlVMRlBkQGNsaWVudHMiLCJhdWQiOiJodHRwczovL3Byb2QtYXBpLmRvb2N0aS5jb20iLCJleHAiOjE3MTYxMTc2NTI4MDQsImlhdCI6MTY1Mjk1OTI1Mn0.oSaWv63aEcA8CnDv0wb0n685NXKPx2coIeGeFy-tOEw'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)