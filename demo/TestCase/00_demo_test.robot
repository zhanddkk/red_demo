*** Settings ***
Library    Libraries.LibTestBench    

*** Test Cases ***
Demo Test The First Keyword
    [Setup]    Tb Initialize Library
    [Teardown]    Tb Clean Up Library
    Tb Set Main 1 Voltage    l1=12    l2=55    l3=74
    Tb Set Main 2 Voltage    l1=55.7    l2=32.8    l3=66.9
    Tb Set Dc Voltage    l1=99    l2=32    l3=77
    Tb Set Breaker State    name=imb    state=1
    Tb Print Log    2    
    