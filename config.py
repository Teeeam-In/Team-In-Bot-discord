import os

USER = str(os.environ.get('HOST'))
HOST = str(os.environ.get('HOST'))
DATABASE = str(os.environ.get('DATABASE'))
PASSWORD = str(os.environ.get('PASSWORD'))

ROLES_ADD = {
    '<a:python:866776924147286027>': 865971770422460417 ,# python
    '<:gamedev:866780079370665994>': 865972670780801084, #gamedev
    '<a:rubby:866776968023244800>': 866780399517302805, # rubby
    '<a:cpp:866776827762442240>': 865971579573633047, #c++
    '🌳': 865971308826198057, #3d designer
    '🛠️': 865973110264037416, #soft dev
    '<a:csharp:866777010294226964>': 865973760530841630, #csharp
    '<a:javascript:866777189889343540>': 865971804777742346, #javascript
    '<:java:866781829495652403>': 865971859249037352, #java
    '<a:sql:866777146273038387>': 865972812714868746, #sql
    '<a:blender:866784801838989392>': 865972970644439050, #blender
    '🎨': 865973455442673674, #3dmax
    '🎛️': 865972226539651114, #unity
    '⚙️': 865971897044697098, #unrealungine
    '<a:php:866777065688924170>': 866773847498555422, #php
    '🛡️': 866637025977171989, #html\css
    '🖥️': 865971128799330324, #Верстальщик
    '🕸️': 865971415353393162, #бекенд
    '🤖': 865972048832233473 #arduino
}

ROLES_REMOVE = {
    '<:python:866776924147286027>': 865971770422460417 ,# python
    '<:gamedev:866780079370665994>': 865972670780801084, #gamedev
    '<:rubby:866776968023244800>': 866780399517302805, # rubby
    '<:cpp:866776827762442240>': 865971579573633047, #c++
    '🌳': 865971308826198057, #3d designer
    '🛠️': 865973110264037416, #soft dev
    '<:csharp:866777010294226964>': 865973760530841630, #csharp
    '<:javascript:866777189889343540>': 865971804777742346, #javascript
    '<:java:866781829495652403>': 865971859249037352, #java
    '<:sql:866777146273038387>': 865972812714868746, #sql
    '<:blender:866784801838989392>': 865972970644439050, #blender
    '🎨': 865973455442673674, #3dmax
    '🎛️': 865972226539651114, #unity
    '⚙️': 865971897044697098, #unrealungine
    '<:php:866777065688924170>': 866773847498555422, #php
    '🛡️': 866637025977171989, #html\css
    '🖥️': 865971128799330324, #Верстальщик
    '🕸️': 865971415353393162, #бекенд
    '🤖': 865972048832233473 #arduino
}

r = [
    '🖥️', 
    '🕸️',
    '<a:gamedev:866780079370665994>',
    '🌳',
    '🛠️',
    '🤖',
    '<a:cpp:866776827762442240>',
    '<a:csharp:866777010294226964>',
    '<a:python:866776924147286027>',
    '<a:javascript:866777189889343540>',
    '<a:java:866781829495652403>',
    '<a:sql:866777146273038387>',
    '<a:blender:866784801838989392>',
    '🎨',
    '🎛️',
    '⚙️',
    '🛡️',
    '<a:php:866777065688924170>',
    '<a:rubby:866776968023244800>'
]

message = os.environ.get('MESSAGE')
channel = os.environ.get('CHANNEL')

voice_id = os.environ.get('VOICE_ID')
category_id = os.environ.get('CATEGORY_ID')