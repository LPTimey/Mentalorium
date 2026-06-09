# How to use docker / podman

1) Open a terminal
2) `podman compose up`
3) Open another terminal
4) `podman exec -it mentalorium-container bash`

## automation bias cli example

`python automationBias.py --files data/session\ 1/*.csv data/session\ 2/*.csv --case_rows case (round 1) case (round 2) case (round 3) --truth_rows correctness (round 1) correctness (round 2) correctness (round 3) --disclaimer_rows disclaimer (round 1) disclaimer (round 2) disclaimer (round 3) --rating_rows rating (round 1) rating (round 2) rating (round 3) --confidence_rows confidence (round 1) confidence (round 2) confidence (round 3)`
