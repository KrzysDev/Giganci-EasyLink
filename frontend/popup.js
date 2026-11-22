const theButton = document.getElementById("button")

function changeColor(){
    theButton.style.color='purple'
    theButton.style.textDecoration='underline'
}

theButton.addEventListener('click', changeColor)

addingEventListener()
function addingEventListener(){
    
    function openPages(){
        chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
        let url = tabs[0].url;
        
        console.log(url);
    });
    }

    theButton.addEventListener('click', openPages);
}

