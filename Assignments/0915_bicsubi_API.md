## bicsubi_core_api.md

## github id 가져오기
# GET /whoami
URL: /whoami
Method: GET
Response : {"name" : "chae-youn"}

## query string echo
# GET /echo?string="string"
URL: /echo?string=hihihi
Method: GET  
Response: {"value" : "hihihi"}

## CREATE
URL: /weapon
Method: POST
Request: 
{
    "name": "knife",
    "stock": 10
}
Response: 
{
    "name": "knife",
    "stock": 10
}

## READ
URL: /weapon
Method: GET
Response: 
[
    {
        "name": "hammer",
        "stock": 3
    },
    {
        "name": "ax",
        "stock": 1
    },
    {
        "name": "knife",
        "stock": 10
    }
]

## UPDATE
URL: /weapon/<string:name>
Method: PUT
Request: /weapon/hammer,
{ 
    "name" : "gun",
    "stock": 4
}
Response: 
[
    {
        "name": "gun",
        "stock": 4
    },
    {
        "name": "ax",
        "stock": 1
    },
    {
        "name": "knife",
        "stock": 10
    }
]

## DELETE
URL: /weapon/<string:name>
Method: DELETE
Request: /weapon/gun
Response: 
[
    {
        "name": "ax",
        "stock": 1
    },
    {
        "name": "knife",
        "stock": 10
    }
]
