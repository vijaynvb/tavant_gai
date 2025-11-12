# tavant_gai
Batch 1 Training


Day - 3

nova pro -> LLM -> input=text, output=predection
    function -> python method, lmbda function, api calls 
    as per bangalore weather write a poem 
        1. get weather data from api json {}
        2. parse json and write the poem 
mistral lite-> no function calling 
    as per bangalore weather write a poem 
        1. get weather data from api json {} -> writen in application scope
        2. parse json give it as a prompt to mistral lite to write the poem 
titanEmbeding model -> embending model input=text, output=vector array


python -> 
    interpreter -> 
        workingspace: -> virtual env -> dependencies + memory management + session management etc
            set of instructions

Default behaviour of a web application: 
    Server [streamlit] -> listening -> 8051
    client [browsers] -> server will server html content 

Web Solutions: 
    1. Server side session management 
        session object -> 10
    2. client side session management -> for every request this details will be sent to server to remaind the session
        browser based web application -> cookies, headers for managing sessions
        web services api -> jwt, oauth tokens