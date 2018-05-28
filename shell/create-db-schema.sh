#!/bin/bash

EXPECTED_ARGS=4
E_BADARGS=65
MYSQL=`which mysql`
 
Q1="use $4;"
Q2="CREATE TABLE IF NOT EXISTS versionTable (
  version int(11) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (version)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;"
SQL="${Q1}${Q2}"
 
if [ $# -ne $EXPECTED_ARGS ]
then
  echo "Usage: $0 dbhost dbuser dbpass dbname"
  exit $E_BADARGS
fi
 
$MYSQL -h$1 -u$2 -p$3 -e "$SQL"

echo "versionTable has been created"
