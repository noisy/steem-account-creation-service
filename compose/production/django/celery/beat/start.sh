#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


celery -A steem_account_creation_service.taskapp beat -l INFO
