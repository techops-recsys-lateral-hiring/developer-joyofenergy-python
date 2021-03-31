# Welcome to PowerDale

PowerDale is a small town with around 100 residents. Most houses have a smart meter installed that can save and send
information about how much power a house is drawing/using.

There are three major providers of energy in town that charge different amounts for the power they supply.

- _Dr Evil's Dark Energy_
- _The Green Eco_
- _Power for Everyone_

# Introducing JOI Energy

JOI Energy is a new start-up in the energy industry. Rather than selling energy they want to differentiate themselves
from the market by recording their customers' energy usage from their smart meters and recommending the best supplier to
meet their needs.

You have been placed into their development team, whose current goal is to produce an API which their customers and
smart meters will interact with.

Unfortunately, two members of the team are on annual leave, and another one has called in sick! You are left with
another ThoughtWorker to progress with the current user stories on the story wall. This is your chance to make an impact
on the business, improve the code base and deliver value.

## Story Wall

At JOI energy the development team use a story wall or Kanban board to keep track of features or "stories" as they are
worked on.

The wall you will be working from today has 7 columns:

- Backlog
- Ready for Dev
- In Dev
- Ready for Testing
- In Testing
- Ready for sign off
- Done

Examples can be found
here [https://leankit.com/learn/kanban/kanban-board/](https://leankit.com/learn/kanban/kanban-board/)

## Users

To trial the new JOI software 5 people from the JOI accounts team have agreed to test the service and share their energy
data.

| User    | Smart Meter ID  | Power Supplier        |
| ------- | --------------- | --------------------- |
| Sarah   | `smart-meter-0` | Dr Evil's Dark Energy |
| Peter   | `smart-meter-1` | The Green Eco         |
| Charlie | `smart-meter-2` | Dr Evil's Dark Energy |
| Andrea  | `smart-meter-3` | Power for Everyone    |
| Alex    | `smart-meter-4` | The Green Eco         |

These values are used in the code and in the following examples too.

## Requirements

The project requires [Python 3.7](https://www.python.org/downloads/release/python-370/) or higher and
the [PIP](https://pip.pypa.io/en/stable/) package manager.

## Useful Python commands

### Installation

Install the project dependencies

```console
$ python3.7 -m pip install "connexion[swagger-ui]" Flask pytest
```

### Run the tests

Run all tests

```console
$ python3.7 -m pytest
```

### Run the application

Run the application which will be listening on port `5000`.

```console
$ python3.7 src/app.py
```

## API

Below is a list of API endpoints with their respective input and output. Please note that the application needs to be
running for the following endpoints to work. For more information about how to run the application, please refer
to [run the application](#run-the-application) section above.

### Store Readings

Endpoint

```text
POST /readings/store
```

Example of body

```json
{
  "smartMeterId": <smartMeterId>,
  "electricityReadings": [
    {
      "time": <timestamp>,
      "reading": <reading>
    },
    {
      "time": <timestamp>,
      "reading": <reading>
    },
    ...
  ]
}
```

Parameters

| Parameter      | Description                                           |
| -------------- | ----------------------------------------------------- |
| `smartMeterId` | One of the smart meters' id listed above              |
| `time`         | The date/time (as epoch) when the _reading_ was taken |
| `reading`      | The consumption in `kW` at the _time_ of the reading  |

Example readings

| Date (`GMT`)      | Epoch timestamp | Reading (`kW`) |
| ----------------- | --------------: | -------------: |
| `2020-11-11 8:00` |      1605081600 |         0.0503 |
| `2020-11-12 8:00` |      1605168000 |         0.0213 |

In the above example, `0.0213 kW` were being consumed at `2020-11-12 8:00`. The reading indicates the powered being used
at the time of the reading. If no power is being used at the time of reading, then the reading value will be `0`. Given
that `0` may introduce new challenges, we can assume that there is always some consumption, and we will never have a `0`
reading value.

Posting readings using CURL

```console
$ curl \
  -X POST \
  -H "Content-Type: application/json" \
  "http://localhost:5000/readings/store" \
  -d '{"smartMeterId":"smart-meter-0","electricityReadings":[{"time":1605081600,"reading":0.0503},{"time":1605168000,"reading":0.0213}]}'
```

The above command will return the submitted readings.

```json
{
  "electricityReadings": [
    {
      "reading": 0.0503,
      "time": 1605081600
    },
    {
      "reading": 0.0213,
      "time": 1605168000
    }
  ],
  "smartMeterId": "smart-meter-0"
}
```

### Get Stored Readings

Endpoint

```text
GET /readings/read/<smartMeterId>
```

Parameters

| Parameter      | Description                              |
| -------------- | ---------------------------------------- |
| `smartMeterId` | One of the smart meters' id listed above |

Retrieving readings using CURL

```console
$ curl "http://localhost:5000/readings/read/smart-meter-0"
```

Example output

```json
[
  {
    "time": "2020-11-11T08:00:00.000000Z",
    "reading": 0.0503
  },
  {
    "time": "2020-11-12T08:00:00.000000Z",
    "reading": 0.0213
  },
  ...
]
```

### View Current Price Plan and Compare Usage Cost Against all Price Plans

Endpoint

```text
GET /price-plans/compare-all/<smartMeterId>
```

Parameters

| Parameter      | Description                              |
| -------------- | ---------------------------------------- |
| `smartMeterId` | One of the smart meters' id listed above |

Retrieving readings using CURL

```console
$ curl "http://localhost:5000/price-plans/compare-all/smart-meter-0"
```

Example output

```json
{
  "pricePlanComparisons": [
    {
      "price-plan-2": 1.25382479924573e-06
    },
    {
      "price-plan-1": 2.50764959849146e-06
    },
    {
      "price-plan-0": 1.25382479924573e-05
    }
  ],
  "pricePlanId": "price-plan-0"
}
```

### View Recommended Price Plans for Usage

Endpoint

```text
GET /price-plans/recommend/<smartMeterId>[?limit=<limit>]
```

Parameters

| Parameter      | Description                                          |
| -------------- | ---------------------------------------------------- |
| `smartMeterId` | One of the smart meters' id listed above             |
| `limit`        | (Optional) limit the number of plans to be displayed |

Retrieving readings using CURL

```console
$ curl "http://localhost:5000/price-plans/recommend/smart-meter-0?limit=2"
```

Example output

```json
[
  {
    "price-plan-0": 1.25382479924573e-05
  },
  {
    "price-plan-2": 1.25382479924573e-06
  }
]
```
