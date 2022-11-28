#!/bin/bash
for i in {1..3600}; do curl "http://localhost:5000/metric/temperature/$((50 + $RANDOM % 20 ))c"; sleep 1; done
for i in {1..3600}; do curl "http://localhost:5000/metric/humidity/$((50 + $RANDOM % 20 ))"; sleep 1; done
