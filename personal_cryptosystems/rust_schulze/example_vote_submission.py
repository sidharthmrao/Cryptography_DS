import requests
import json

url = "http://127.0.0.1:7878/votes"

payload = json.dumps({
  "vote_string": [
    176,
    21,
    35,
    120,
    67,
    114,
    136,
    127,
    59,
    14,
    208,
    64,
    84,
    249,
    82,
    66,
    75,
    54,
    194,
    221,
    243,
    57,
    177,
    134,
    228,
    183,
    83,
    164,
    244,
    33,
    154,
    137,
    56,
    198,
    115,
    93,
    51,
    190,
    189,
    87,
    46,
    253,
    65,
    92,
    253,
    154,
    59,
    153,
    94,
    204,
    157,
    112,
    66,
    203,
    51,
    155,
    48,
    245,
    85,
    209,
    95,
    206,
    64,
    75,
    184,
    29,
    130,
    217,
    28,
    88,
    192,
    214,
    4,
    217,
    199,
    53,
    160,
    113,
    110,
    91,
    56,
    56,
    115,
    130,
    167,
    102,
    208,
    169,
    237,
    234,
    96,
    77,
    106,
    91,
    221,
    31,
    0,
    0,
    126,
    100,
    161,
    245,
    12,
    9,
    29,
    75,
    185,
    37,
    96,
    198,
    140,
    148,
    30,
    49,
    239,
    202,
    179,
    230,
    220,
    200,
    149,
    79,
    35,
    169,
    117,
    99,
    250,
    149,
    153,
    188,
    14,
    87,
    52,
    243,
    235,
    188,
    63,
    50,
    51,
    149,
    133,
    35,
    182,
    64,
    248,
    214,
    9,
    25,
    108,
    102,
    50,
    198,
    67,
    105,
    242,
    93,
    199,
    166,
    242,
    91,
    228,
    34,
    80,
    28,
    32,
    72,
    144,
    199,
    29,
    245,
    27,
    6,
    47,
    126,
    249,
    148,
    30,
    99,
    109,
    210,
    80,
    250,
    169,
    81,
    252,
    158,
    9,
    153,
    45,
    218,
    210,
    79,
    194,
    139,
    237,
    231,
    225,
    198,
    165,
    90,
    158,
    229,
    166,
    248,
    187,
    154,
    59,
    111,
    130,
    142,
    31,
    210,
    212,
    50,
    208,
    4,
    218,
    143,
    142,
    160,
    35,
    204,
    34,
    193,
    197,
    140,
    22,
    110,
    120,
    22,
    167,
    104,
    82,
    1,
    184,
    27,
    84,
    29,
    167,
    203,
    213,
    157,
    236,
    222,
    17,
    181,
    182,
    238,
    76,
    203,
    128,
    153,
    22,
    199,
    191,
    67
  ],
  "attendance_string": [
    61,
    29,
    57,
    53,
    90,
    23,
    178,
    111,
    80,
    190,
    172,
    67,
    151,
    231,
    44,
    50,
    142,
    57,
    118,
    103,
    35,
    139,
    95,
    46,
    73,
    209,
    243,
    115,
    173,
    115,
    76,
    151,
    39,
    62,
    58,
    35,
    115,
    85,
    78,
    226,
    253,
    56,
    180,
    243,
    6,
    37,
    201,
    100,
    219,
    12,
    38,
    180,
    106,
    217,
    94,
    244,
    250,
    184,
    123,
    179,
    64,
    138,
    188,
    57,
    46,
    178,
    213,
    241,
    87,
    137,
    129,
    229,
    226,
    81,
    39,
    42,
    22,
    159,
    200,
    68,
    219,
    233,
    251,
    227,
    130,
    215,
    192,
    24,
    32,
    121,
    5,
    43,
    199,
    208,
    55,
    175,
    94,
    154,
    44,
    93,
    210,
    9,
    39,
    178,
    2,
    198,
    42,
    80,
    104,
    116,
    163,
    149,
    142,
    44,
    145,
    72,
    175,
    165,
    6,
    136,
    247,
    184,
    210,
    128,
    65,
    101,
    240,
    74,
    222,
    233,
    162,
    255,
    20,
    218,
    56,
    81,
    200,
    196,
    174,
    211,
    222,
    105,
    42,
    164,
    139,
    202,
    22,
    150,
    64,
    30,
    249,
    228,
    8,
    137,
    114,
    175,
    243,
    225,
    247,
    72,
    236,
    159,
    197,
    229,
    196,
    148,
    134,
    160,
    5,
    118,
    113,
    80,
    195,
    251,
    199,
    125,
    55,
    106,
    94,
    9,
    200,
    32,
    179,
    167,
    246,
    248,
    21,
    128,
    50,
    160,
    47,
    197,
    214,
    0,
    188,
    192,
    94,
    197,
    29,
    157,
    29,
    108,
    73,
    64,
    4,
    69,
    21,
    238,
    160,
    242,
    205,
    10,
    7,
    213,
    169,
    151,
    159,
    179,
    110,
    198,
    187,
    102,
    140,
    4,
    70,
    126,
    111,
    61,
    203,
    195,
    144,
    148,
    96,
    120,
    160,
    109,
    75,
    135,
    54,
    155,
    202,
    18,
    109,
    152,
    74,
    96,
    215,
    153,
    66,
    204,
    239,
    38,
    105,
    79,
    219,
    112
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
