#!/usr/bin/env python3
from sys import argv

# https://qualysguard.qg2.apps.qualys.com/qwebhelp/fo_portal/setup/cvss_vector_strings.htm

# CVSS3.1 Mappings
value_matrix_3 = {
'AV': {'N': 'Network', 'A': 'Adjacent Network', 'L': 'Local', 'P': 'Physical'},
'AC': {'L': 'Low', 'H': 'High'},
'PR': {'N': 'None', 'L': 'Low', 'H': 'High'}, 
'UI': {'N': 'None', 'R': 'Required'},
'S':  {'U': 'Unchanged', 'C': 'Changed'},
'C':  {'N': 'None', 'L': 'Low', 'H': 'High'},
'I':  {'N': 'None', 'L': 'Low', 'H': 'High'},
'A':  {'N': 'None', 'L': 'Low', 'H': 'High'}}

base_score_names_3 = {
'AV': 'Attack Vector:',
'AC': 'Attack Complexity',
'PR': 'Privileges Required',
'UI': 'User Interaction',
'S':  'Scope',
'C':  'Confidentiality Impact',
'I':  'Integrity Impact',
'A':  'Availability Impact'}

# CVSS2 Mappings
value_matrix_2 = {
'AV': {'L': 'Local', 'A': 'Adjacent Network', 'N': 'Network'},
'AC': {'L': 'Low', 'M': 'Medium', 'H': 'High'},
'Au': {'N': 'None', 'S': 'Single', 'M': 'Multiple'},
'C':  {'N': 'None', 'P': 'Partial', 'C': 'Complete'},
'I':  {'N': 'None', 'P': 'Partial', 'C': 'Complete'},
'A':  {'N': 'None', 'P': 'Partial', 'C': 'Complete'}}

base_score_names_2 = {
'AV': 'Access Vector',
'AC': 'Access Complexity',
'Au': 'Authentication',
'C':  'Confidentiality Impact',
'I':  'Integrity Impact',
'A':  'Availability Impact'}

def decode_cvss3(cvss):
    for c, pointer in enumerate(cvss.split('/')):
        if c > 8:
            print('Skipping score for Temporal and Environmental')
            break
        value = pointer.split(':')
        if value[0] == "CVSS":
            continue
        print('[', base_score_names_3[value[0]], ']', end = '')
        print(' -', value_matrix_3[value[0]][value[1]])

def decode_cvss2(cvss):
    for c, pointer in enumerate(cvss.split('/')):
        if c > 6:
            print('Skipping score for Temporal and Environmental')
            break
        value = pointer.split(':')
        if value[0] == "CVSS":
            continue
        print('[', base_score_names_2[value[0]], ']', end = '')
        print(' -', value_matrix_2[value[0]][value[1]])

if __name__ == '__main__':
    try:
        if argv[2] == '-2':
            cvssVersionSelect = 2
        if argv[2] == '-3':
            cvssVersionSelect = 3
    except:
        cvssVersionSelect = 0

    if cvssVersionSelect == 3 or '3.' in argv[1].split('/')[0] or len(argv[1].split('/')) == 8:
        decode_cvss3(argv[1])
    elif cvssVersionSelect == 2 or '2' in argv[1].split('/')[0] or len(argv[1].split('/')) == 6:
        decode_cvss2(argv[1])
    else:
        print('CVSS not recognised:', argv[1])

