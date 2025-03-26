# ---------------------------- VIEW IS RESPOSIBLE FOR RENDER THE HTML ---------------------------- #
# ---------------------------------- VIEWS RELATED TO APP MODULE --------------------------------- #

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(
        """
            <div 
                style="
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    padding: 10vh;
                    margin: 50px;
                    height: calc(100vh - 100px - 20vh);
                    background-color: salmon;
                    border-radius: 50px;
                "
            >
                <h1 style="">Server online</h1>
                <p>The server is running on port 8000</p>
            </div>
        """
    )
