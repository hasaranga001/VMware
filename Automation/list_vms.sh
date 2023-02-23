#!/bin/zsh

# Remember to run "get_API_token.sh" and copy paste the Key in token.txt file. 

token=`cat token.txt`

curl -k -X GET -H 'Accept: application/json' -H "vmware-api-session-id: $token" https://hx-tron.vi-test.ebi.ac.uk/api/vcenter/vm | python3 -m json.tool
