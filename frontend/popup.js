const BACKEND = "http://127.0.0.1:8000";

const theButton = document.getElementById("button");

function changeColor() {
    theButton.style.color = "purple";
    theButton.style.textDecoration = "underline";
}

function setup() {
    return fetch(`${BACKEND}/api/setup`)
        .then((r) => r.json())
        .then((data) => console.log("setup:", data))
        .catch((err) => console.error("setup error:", err));
}

function openPages() {
    chrome.tabs.query({ active: true, lastFocusedWindow: true }, (tabs) => {
        const url = tabs[0].url;
        fetch(`${BACKEND}/api/open_link?url=${encodeURIComponent(url)}`, {
            method: "POST",
        })
            .then((r) => r.json())
            .then((data) => console.log("open_link:", data))
            .catch((err) => console.error("open_link error:", err));
    });
}

setup();

theButton.addEventListener("click", changeColor);
theButton.addEventListener("click", openPages);