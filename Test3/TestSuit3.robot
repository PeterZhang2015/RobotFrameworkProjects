*** Settings ***
Metadata          @{temp}    temp
Library           Selenium2Library

*** Variables ***
${site_url}       https://google.com.au
${text_with_next_line}    automation test \n    # search information
${gmail_url}      www.gmail.com
${Browser}        Chrome

*** Test Cases ***
search in google
    log    Hello
    Open google url
    log    Open google url
    Enter search information
    log    Input search infomation

open \ Gmail
    log    Starting to open gmail site
    Open google url
    Sleep    10
    Click gmail button

*** Keywords ***
Open google url
    open browser    ${site_url}    ${Browser}

Enter search information
    Input Text    lst-ib    ${text_with_next_line}

Click gmail button
    Click Element    xpath=//*[text()="Gmail" and @href]

Open gmail url
    open browser    ${gmail_url}
