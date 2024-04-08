def compare_dicts(dict1, dict2, current_path=''):
    differing_pairs = []

    # Check if the keys are the same in both dictionaries
    if set(dict1.keys()) != set(dict2.keys()):
        print("Keys are different between the dictionaries.")
        return

    # Check if the values for each key match
    for key in dict1:
        current_key_path = f"{current_path}.{key}" if current_path else key

        if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            # Recursively compare nested dictionaries
            compare_dicts(dict1[key], dict2[key], current_path=current_key_path)
        elif dict1[key] != dict2[key]:
            differing_pairs.append((current_key_path, dict1[key], dict2[key]))

    if differing_pairs:
        print("Differing key-value pairs:")
        for key_path, value1, value2 in differing_pairs:
            print(f"{key_path}:oldvalue: {value1} (--) newvalue: {value2}")

# Example dictionaries
dict_a = {
  "getDigiAssetReportingDataRequest": {
    "msgHdr": {
      "cnvId": "WEB2024011115375012456814",
      "bizObjId": "WEB2024011115375012456814",
      "appId": "FOS",
      "msgId": "WEB2024011115375012456814",
      "extRefId": "WEB2024011115375012456814",
      "timestamp": "2024-01-11T15:37:50",
      "authInfo": {
        "brnchId": "9999",
        "usrId": "WEBUSER"
      }
    },
    "msgBdy": {
      "demoAuthXMLStringReqPayload": "PEF1YUF1dGhSZXE+PEF1dGggcmM9J1knIHZlcj0nMi41Jz48SG1hYz5KdmJHODJqVHBnTVNYdmkrb3NQRDBJenVROFllU1FLcTYwaWpZT241Z0treDJ0bHFJOG5JeDZmTUJOMXdMbHZmPC9IbWFjPjxVc2VzIGJpbz0nbicgb3RwPSduJyBwYT0nbicgcGZhPSduJyBwaT0neScgcGluPSduJy8+PERhdGEgdHlwZT0nWCc+TWpBeU5DMHdNUzB4TVZReE5Ub3pOem8xTUF6b3hib1M3RVN3aGJkZHFFWkZYVHRIMkZORk5tbjEzdUk5eTE3OTJzMm9nSjlaOFl0ZXB5VVB6amJGNGFUeVZPbm1zRXg2STAxeE15d1JsTkFjV2drL0t0bFZRMWVNK1FUdW52ekFnWSt0RTV2Q1FnV1JOdjk5UzQ0cnlrbmx0T3I2SWJVTTJCUGxMcTkrUGpvQit0ODBHNkNvTjdzZGJaZ3lDVnJoajgxNlc4YXhwUUp3V0hyQmxYNVZEdW56TTFJTURhNVpOZjNwaERpL1Y0SmJ5SFNCeTc0dFhDbnlnQjg9PC9EYXRhPjxTa2V5IGNpPScyMDI1MDkyOSc+S0J0MHMrSGNMZXlGNno5V2paWWRpMlN0T0QvSXFsUDN3eC80dmNqbGhjR0s5LytMbjlSZzNZNWFnQ3VZTjlrRytyb0hmTEdUc1BibXNQaG5QNlBPbVFjeDBRRGQ4UHJXVjRUZzRoOUVhcTBxRUNxb3JGdGVmWG80YnpMZFdyK25MWWN6SFJMSk1hVHk5dlBMRzJyTXZTaDhHVHNXQ3BERFhYQ3c3Z2NKQU90b2dhQklmL3BTd2s4STFoY0VpS1JqK2JBSHFZMG1kK0VuYjNaVm1aR1lheGtTNUp4OUhqL3ZYb0tYblgxNnBmVVhsdDBpQndVWTVGdThJSUU2RjFrOEVxTVdKRHpmYnE3cHBlaDBYQ1gxWWpKcm55YUtoUzFsaklDcVJtZjl3OUhNVDlJbWI2Zm5NUWdMYjhmTmlZQUpnWVdkT0Q2WkJadlh6N1dtamxRWFdRPT08L1NrZXk+PE1ldGEgZGM9J0ZJRycgZHBJZD0nRklHJyBtYz0nRklHJyBtaT0nRklHJyByZHNJZD0nRklHJyByZHNWZXI9J0ZJRycgdWRjPSdFU1UwMDAwMDAwMDE3NjEnLz48L0F1dGg+PFRyYW5zYWN0aW9uSW5mbz48Q0FfSUQ+RVNVMDAwMDAwMDAxNzYxPC9DQV9JRD48Q0FfVElEPjExMjA1NzY0PC9DQV9USUQ+PENBX1RBPkNTQiBORVJVTCBNVU1CQUkgTUhJTjwvQ0FfVEE+PExvY2FsX2RhdGU+MDExMTwvTG9jYWxfZGF0ZT48TG9jYWxfVHJhbnNfVGltZT4xNTM3NTI8L0xvY2FsX1RyYW5zX1RpbWU+PFBvc19lbnRyeV9tb2RlPjAxOTwvUG9zX2VudHJ5X21vZGU+PFN0YW4+NjY1NjkyPC9TdGFuPjxUcmFuc21fRGF0ZV90aW1lPjAxMTExNTM3NTI8L1RyYW5zbV9EYXRlX3RpbWU+PFVJRCB0eXBlPSdVJz41ODcxOTI2NzE5NzQ8L1VJRD48L1RyYW5zYWN0aW9uSW5mbz48L0F1YUF1dGhSZXE+"
    }
  }
}
dict_b = {
  "getDigiAssetReportingDataRequest": {
    "msgHdr": {
      "cnvId": "DEMO2024011114551546468758",
      "bizObjId": "DEMO2024011114551546468758",
      "appId": "MADP",
      "msgId": "DEMO2024011114551546468758",
      "extRefId": "DEMO2024011114551546468758",
      "timestamp": "2024-01-11T14:55:15.464+05:30",
      "authInfo": {
        "usrId": "IBUSER",
        "brnchId": "9999"
      }
    },
    "msgBdy": {
      "demoAuthXMLStringReqPayload": "PEF1YUF1dGhSZXE+PFRyYW5zYWN0aW9uSW5mbz48Q0FfSUQ+RVNVMDAwMDAwMDAxNzYxPC9DQV9JRD48Q0FfVElEPjExMjA1NzY0PC9DQV9USUQ+PENBX1RBPkNTQiBORVJVTCBNVU1CQUkgTUhJTjwvQ0FfVEE+PExvY2FsX2RhdGU+MDExMTwvTG9jYWxfZGF0ZT48TG9jYWxfVHJhbnNfVGltZT4xNDU1MTU8L0xvY2FsX1RyYW5zX1RpbWU+PFBvc19lbnRyeV9tb2RlPjAxOTwvUG9zX2VudHJ5X21vZGU+PFN0YW4+NTAwMTE1PC9TdGFuPjxUcmFuc21fRGF0ZV90aW1lPjAxMTExNDU1MTU8L1RyYW5zbV9EYXRlX3RpbWU+PFVJRCB0eXBlPSJVIj4zMzQ5NTQ3NzQ4NDk8L1VJRD48L1RyYW5zYWN0aW9uSW5mbz48QXV0aCByYz0iWSIgdmVyPSIyLjUiPjxIbWFjPkJUZmZCVHBiM0k3dTZGTkoySXFReU5WVDRMYzVIL2xpS2lGbjkrdFdrQU1IWVg2RE9MdjlDbVJ6ZHlMWmIvckM8L0htYWM+PFVzZXMgYmlvPSJuIiBvdHA9Im4iIHBhPSJuIiBwZmE9Im4iIHBpPSJ5IiBwaW49Im4iIC8+PERhdGEgdHlwZT0iWCI+TWpBeU5DMHdNUzB4TVZReE5EbzFOVG94TlU3SStObVMwYlJReldoeGVSaXhtd1o4TU1QVThTYVNjbUVrdW15YktRZkV3cFR5TG5rbGNGcDlyTHJyZWJJZElkSlVLZ3dGZFBpZkMxb25CQlhYMjY1R2hKb0dvWmR5Q0JkWVFHMkI2VFdscWpWL2xDNzRudGRwR2R4M0hTRHVBbmhxb3pVYTh0YmQ3LzJWTkhaWHVBTklEaTBoZk9BWmtqODd1LytBaGRGUFJ3dGtQZ0dPSzZ5YnhjdmVDK1R0UFRmcFhnY2c4WFF1T0g1ZVlpMTdLa3RDTzNMYXY0K25KcW89PC9EYXRhPjxTa2V5IGNpPSIyMDI1MDkyOSI+bGs1bHRIUnlPYmlIcFhvQnJOb0djeGxQSE43UStZT21qR3I4b3BGZEg2bCtETE8xQjkvMW9sUEMwZFpCc0IwYVJvejhoMFJNSEM4WTZsMFFxUEdaNThPeEQwUUg4dEpsUG9vOVZicjgxYUM1QXhYLy9BekpzTmZ4ckdmbXJGUStvS2o1TmUzczhvT3NTUjVkc0lHNzdjZHdVSlVuUnhkSnljU3VkdEVacXZLWk9XMFdGdy81aTdYTUhPWVZLTlNzRkxTOEFlV0NsT1RPOGUvY3FRT25iMk5RQi9RS1Uvbi9PQk1PK29FM1hRQW1jcFlEalRqUzdqblZaK3M4ZHRyN1BLRExNQVlqMUlQSWNreGoyb05mS0FiNWZPd1R6b0dtMmw4MUxLUXcreEJQL000Z2srdGtKb1hNaExxdmFSaWJKLzg4M2ZOS3haNktaWUI1NVJQYW53PT08L1NrZXk+PE1ldGEgZGM9IkZJRyIgZHBJZD0iRklHIiBtYz0iRklHIiBtaT0iRklHIiByZHNJZD0iRklHIiByZHNWZXI9IkZJRyIgdWRjPSJFU1UwMDAwMDAwMDE3NjEiIC8+PC9BdXRoPjwvQXVhQXV0aFJlcT4="
    }
  }
}

# Compare dictionaries
compare_dicts(dict_a, dict_b)
