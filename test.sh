#!/bin/bash
# test Flask endpoints

source ~/anaconda3/etc/profile.d/conda.sh
conda activate mlh

#source "/home/centos/anaconda3/envs/mlh/bin/activate"
endpoints=$(python -c "from app import app; a=[rule.endpoint for rule in app.url_map.iter_rules()]; print(*a)")

echo $endpoints

for rule in $endpoints
    do
	echo $rule
	curl -LI https://mahzadkhoshlessan.duckdns.org/${rule} -o /dev/null -w '%{http_code}\n' -s
    done
