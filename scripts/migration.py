import sys
import os
import re
import MySQLdb

def get_db_cursor():

    try:
        cursor = db.cursor()
        return cursor
    except:
        print "unable to get the cursor object"
        sys.exit(1)

def get_sql_scripts():
    files = []
    for f in os.listdir(dir_path):
        if f.endswith(".sql"):
            files.append(f)

    return files

def execute_script(cur, script):
    fd = open(dir_path + '/' + script, 'r')
    sql_file = fd.read()
    fd.close()

    sqlCommands = sql_file.split(';')

    for command in sqlCommands:
        try:
            if command.strip() != '':
                cur.execute(command)
        except (MySQLdb.Error, MySQLdb.Warning) as ex: # pylint: disable=no-member
            print ex


def get_version_number_from_db(cur):
    sql = "select version from versionTable"
    cur.execute(sql)
    version = cur.fetchone()
    if version:
        return version[0]
    return 0

def update_version_number(cur, version):
    sql = "update versionTable set version = {0}".format(int(version))
    cur.execute(sql)

def get_version_list(scripts):
    versions = {}
    regex = r"(\d+)\.?([a-zA-Z0-9]+).sql"
    for script in scripts:
        search = script.replace(" ", "")
        m = re.search(regex, search)
        if m is not None:
            versions[int(m.group(1))] = script

    return versions


if __name__ == '__main__':

    if len(sys.argv) != 5:
        print "Usage: python {0} dbuser dbhost dbname dbpass".format(sys.argv[0])
        sys.exit(1)

    dir_path = os.path.dirname(os.path.realpath(__file__))

    db = MySQLdb.connect(host=sys.argv[2],
                         user=sys.argv[1],
                         passwd=sys.argv[4],
                         db=sys.argv[3])

    cur = get_db_cursor()
    sql_scripts = get_sql_scripts()

    if len(sql_scripts) == 0:
        print "No script found"
        sys.exit(1)

    db_version = get_version_number_from_db(cur)
    print "The last migrated version number in database: {0}".format(db_version)
    versions_list = get_version_list(sql_scripts)
    execute = sorted([k for k, v in versions_list.items() if k > db_version])

    if len(execute) == 0:
        print "No migration left to be executed"
        sys.exit()

    for e in execute:
        print "- executing script: {0}".format(versions_list[e])
        execute_script(cur, versions_list[e])
        print "- {0} has been executed successfully".format(versions_list[e])
        update_version_number(cur, e)
        print "- versionTable updated with {0}".format(e)
        print "------------------------------------------------"

    db.commit()
    cur.close()
    db.close()
    print "---------"
    print "- Done"
    print "---------"
