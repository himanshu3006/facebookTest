*** Settings ***
Documentation    facebook login
Library         OperatingSystem
Library         /lib/facebooktest.py


*** Variables ***

${Browser}        Chrome
${SiteUrl}        https://www.facebook.com
${email}          mittalhimanshu2222@gmail.com
${password}       hmmmmjhj@2y687931230

*** Test Cases ***
Test title
    Login_1
    [Tags]    Validate facebook login page has all the fields
    Open Browser to the facebook Page
    Login To facebook
    [Teardown]      Close Browser

*** Keywords ***
Open Browser to the facebook Page
    [Documentation]  Open Mentioned Browser From Variable And Pass Respective Url from Variable To UrlField
    open browser    ${SiteUrl}    ${Browser}
    Maximize Browser Window

Login to facebook
    [Documentation]  Enter  valid email and password to textField and click loginButton
    login__as__User    ${email}    ${password}