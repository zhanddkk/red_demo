*** Settings ***
Library    ../lib/LibUc.py    

*** Test Cases ***
Test Uc Demo
    log    this is a demo for UC MIT
    LibUc.Print Args Kwargs    1  2  3  4  hash_id=${0x12345678}  index=${1}