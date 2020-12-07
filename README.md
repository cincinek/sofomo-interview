# Interview
## `api/token/`
POST method to retrvie JWT token. Requires `username` and `password`.
To retrieve token use this combination:
`username`: future_employee
`password`: Str0ngP@ssw0rd
## `api/token/refresh/`
POST method for token refresh.
## `api/location/`
POST method.
Takes either `url` or `ip address` and returns JSON response in given form

```json
"location": {
	"id": int,
	"url": str, //null if not provided
	"ip": str,
	"ip_type": str,
	"continent_code": str,
	"continent_name": str,
	"country_code": str,
	"country_name": str,
	"region_code": str,
	"region_name": str,
	"city": str,
	"zip": str,
	"latitude": decimal,
	"longitude": decimal,
	"geoname_id": int,
	"capital": str,
	"country_flag": str,
	"calling_code": str,
	"is_eu": boolean
}
```
### Sample usage
* `api/location/?url=wp.pl`
* `api/location/?ip=217.74.65.23`

## Requirements
Requirements are in `requirements.txt` file.