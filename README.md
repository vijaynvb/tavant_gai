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


ChatGPT [application]            ->          OpenAI GPT-5 [LLM model]
textbox [limitation]
fileupload [limitation]
                            [32k, 8k, 400k]
                Prompt[content]. -> 


bot-role=you are it support chat bot who is helping to solve the computer issues.
knowledge1 = laptop, desktop, mobile ...
input = my system is not starting
output=write the response not more than 2 sentences.

templatestring = "System Instruction: {bot-role}
context: {knowledge}
input data: {input}
outindicator: {output}"

prompt =  promptFormater.format(templatestring, bot-role, knowledge=knowledge1, input, output)


you'r a intelegent bot answer all questions in one word for the given medical field questions
how define body


user uploading a pdf -> 
    prompt: summarize the document 

RAG -> Retrevial Augment Generate

    Step 1: prepare the data first for filtering 

    Step 2: prompt -> filter the prepared data with the prompt's intention and append it before sending it to llm 


Chat with PDF: Front end [streamlit]
    1. upload a pdf 
    2. interact with the pdf 

    1. pdf -> RAG -> Vector data store 
    2. Prompts -> Retrival + Augment + generate