import xml.etree.ElementTree as ET
from deepdiff import DeepDiff

# Example XML strings
xml_string1 = '''
<AuaAuthReq>
	<Auth rc='Y' ver='2.5'>
		<Hmac>HbG1W4JY/l8LEPweQOUXcYDL6QGvAmAhSYciq7yKm0Iab7hAT0apfdQUZeNUoxlk</Hmac>
		<Uses bio='n' otp='n' pa='n' pfa='n' pi='y' pin='n'/>
		<Data type='X'>MjAyNC0wMS0xMVQxNTo0MDozME+gQM/XCC6ZFHoT8zWkVBtEwsFWt9mOUObBJ/vGMazRjB5lPVaiNQR/mf7rV6sCL6uXRtST+99RHVmLSXRs097BzGgI2/tY5bPwxUSiUQn8oyK/tQ2VioRLxZaQIethMO4eWwfhTABy6bjsV6OZKKnEMROlqshm2jR/eZIu8og/6+bt7DirLoXoohmbIvulwW5UYjtUts5hn6xdk+FIsv9Twoz/QdhU4f4=</Data>
		<Skey ci='20250929'>b6a4dnCEthYMLjz+hS5RREwNHwcW/mqGQluuMlD6MSatKEwfENgIhgQRepY2uinxuDc3eG6WYQFBVylXDYTp/Mg/RRTq6efa0Mszdbn4f9lH4QvHlwmaBpp3ZS8egvBhoidNve85LHcvPplcohPEPjrTJu7p84WfseYAxwKYMQiCO9jLsmtUXginSYu3k8naBOy+m4qNKSSA5JZzIa33YmV+DjwxAZT5oO4n9XdbYmj541a9paO18+TvKsX61zQAaw0oT9FQNtUeqwerd2sCrAf1sKNywayUfH7Kr8IaLXaOg2hbzL1N8CP7sBoJ9GZ4FUD4i8hfLlNzCMgPFltBrw==</Skey>
		<Meta dc='FIG' dpId='FIG' mc='FIG' mi='FIG' rdsId='FIG' rdsVer='FIG' udc='ESU000000001761'/>
	</Auth>
	<TransactionInfo>
		<CA_ID>ESU000000001761</CA_ID>
		<CA_TID>11205764</CA_TID>
		<CA_TA>CSB NERUL MUMBAI MHIN</CA_TA>
		<Local_date>0111</Local_date>
		<Local_Trans_Time>154032</Local_Trans_Time>
		<Pos_entry_mode>019</Pos_entry_mode>
		<Stan>077874</Stan>
		<Transm_Date_time>0111154032</Transm_Date_time>
		<UID type='U'>587192671974</UID>
	</TransactionInfo>
</AuaAuthReq>
'''

xml_string2 = '''
<AuaAuthReq>
	<TransactionInfo>
		<CA_ID>ESU000000001761</CA_ID>
		<CA_TID>11205764</CA_TID>
		<CA_TA>CSB NERUL MUMBAI MHIN</CA_TA>
		<Local_date>0111</Local_date>
		<Local_Trans_Time>130908</Local_Trans_Time>
		<Pos_entry_mode>019</Pos_entry_mode>
		<Stan>358848</Stan>
		<Transm_Date_time>0111130908</Transm_Date_time>
		<UID type=\"U\">334954774849</UID>
	</TransactionInfo>
	<Auth rc=\"Y\" ver=\"2.5\">
		<Hmac>0CfIWQ0F4kSkgwa1h+ud9gAUrL6eRK5UY6zIL8ZDUwtdZ5RVApfK6KIaQZ5rw9tV</Hmac>
		<Uses bio=\"n\" otp=\"n\" pa=\"n\" pfa=\"n\" pi=\"y\" pin=\"n\" />
		<Data type=\"X\">MjAyNC0wMS0xMVQxMzowODo1OUUs2okYQksWkGbClC+7751x/XFERxhWxyWlChay9YRX2APaEjJtn9NInZW2wrz32jzAoXjiRRBVMBRMnzBH4nkGboWZQ3rJj6lz/lAsx/5KV3k9ox/JnU2gLFCjudxuSCFrKaGfBIqniVhhD/MtcuYm51Wx0x38PryXdokc45gVpon5EdELQcUKQZyARyG6xut58L5A7UCR4htqZxD4PDQ7BwoSlTMyahE=</Data>
		<Skey ci=\"20250929\">C69YiC0PGm62jhcXj4GJWBZ+4oZ49x2pxzIlFpvKCb2+wQISWpQ7JrBYcCnnOEO7Oc5T4LMW0gO9EYJXWbOTJMuoYqFmHwu/whJpNT3wVcTOHMN2b20H40oAxay0DrO0F6LY6EWBSjMCDdIeSSl+kHJmtIWztkH8eUAftEv0+VxumegG03k6BVgb0BgkKs2Y3zVlB807PjZnPoTWXH8Oa0nX4hDhn6SKb5oKQsw7yNDgFAdFjW1sxCFDBvUwONn0ApmyqhLmW9x0BM3ySdcxPNMmFbfqCp1xjVCOT5b7qzdPpm1rCI1reTvx+M5bEJHkS+C3FWiIj/OaKmVVV9KS+A==</Skey>
		<Meta dc=\"FIG\" dpId=\"FIG\" mc=\"FIG\" mi=\"FIG\" rdsId=\"FIG\" rdsVer=\"FIG\" udc=\"ESU000000001761\" />
	</Auth>
</AuaAuthReq>
'''

# Parse XML strings
root1 = ET.fromstring(xml_string1)
root2 = ET.fromstring(xml_string2)

# Convert Element objects to dictionaries
dict1 = dict((elem.tag, elem.text) for elem in root1.iter())
dict2 = dict((elem.tag, elem.text) for elem in root2.iter())

# Find differences using DeepDiff
differences = DeepDiff(dict1, dict2)

# Print the differences
print("Differences:")
for key, value in differences.items():
    print(f"{key}: {value}")
