# OAC²EIS

HTTP Adapter for [GAC²E](https://github.com/AugustUnderground/gace)
and [AC²E](https://github.com/matthschw/ace)
powered by [HAC²E](https://github.com/AugustUnderground/hace).

## Install

```bash
$ pip install git+https://github.com/augustunderground/oaceis.git
```

## GAC²E

```bash
$ gace-http --host <host address> --port <port> \
            --env <gace id> --pdk <ace backend> \
            --var <gace variant> --nenv <num envs>
```

Reset:

```bash
$ curl -X GET <host>:<port>/gace:<ace id>-<ace backend>-v<gace variant>/reset
```

Step from file:

```bash
$ curl -d '@examples/action.json' -H "Content-Type: application/json" \
       -X POST <host>:<port>/gace:<ace id>-<ace backend>-v<gace variant>/step
```

Action Space:

```bash
$ curl -X GET <host>:<port>/gace:<ace id>-<ace backend>-v<gace variant>/action_space
```

Observation Space:

```bash
$ curl -X GET <host>:<port>/gace:<ace id>-<ace backend>-v<gace variant>/observation_space
```

Random Action:

```bash
$ curl -X GET <host>:<port>/gace:<ace id>-<ace backend>-v<gace variant>/random_action
```

Take random step:

```bash
$ curl -X GET <host>:<port>/gace:<ace id>-<ace backend>-v<gace variant>/random_step
```

View Target:

```bash
$ curl -X GET <host>:<port>/gace:<ace id>-<ace backend>-v<gace variant>/target
```

## HAC²E

```bash
$ ace-http --host <host address> --port <port> --env <ace id> --pdk <pdk> --nenv <num envs>
```

From command:

```bash
$ curl -d '{"Wd":2e-6}' -H "Content-Type: application/json" \
       -X POST <host>:<port>/<ace id>-<ace backend>/sim
```

From file:

```bash
$ curl -d '@sizing.json' -X POST <host>:<port>/<ace id>-<ace backend>/sim
```

Get last result without simulating:

```bash
$ curl -X GET <host>:<port>/<ace id>-<ace backend>/performance
```

Get current sizing

```bash
$ curl -X GET <host>:<port>/<ace id>-<ace backend>/sizing
```

Get Performance Parameters:

```bash
$ curl -X GET <host>:<port>/<ace id>-<ace backend>/p-params
```

Get Sizing Parameters:

```bash
$ curl -X GET <host>:<port>/<ace id>-<ace backend>/s-params
```

Get Initial Sizing:

```bash
$ curl -X GET <host>:<port>/<ace id>-<ace backend>/init
```

Get Random Sizing:

```bash
$ curl -X GET <host>:<port>/<ace id>-<ace backend>/rng
```
