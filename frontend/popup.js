const BACKEND = "http://127.0.0.1:8000";

const theButton = document.getElementById("button");

function setLoading(isLoading) {
    if (isLoading) {
        theButton.classList.add("loading");
    } else {
        theButton.classList.remove("loading");
    }
}

function setup() {
    return fetch(`${BACKEND}/api/setup`)
        .then((r) => r.json())
        .then((data) => console.log("setup:", data))
        .catch((err) => console.error("setup error:", err));
}

function getActiveTabUrl(callback) {
    if (typeof chrome !== "undefined" && chrome.tabs && chrome.tabs.query) {
        chrome.tabs.query({ active: true, lastFocusedWindow: true }, (tabs) => {
            if (tabs && tabs.length && tabs[0].url) {
                callback(tabs[0].url);
            } else {
                callback(null);
            }
        });
    } else {
        callback(window.location.href);
    }
}

function openPages() {
    if (theButton.classList.contains("loading")) return;

    getActiveTabUrl((url) => {
        if (!url) {
            console.error("No active tab URL found");
            return;
        }

        setLoading(true);

        fetch(`${BACKEND}/api/open_link?url=${encodeURIComponent(url)}`, {
            method: "POST",
        })
            .then((r) => r.json())
            .then((data) => console.log("open_link:", data))
            .catch((err) => console.error("open_link error:", err))
            .finally(() => {
                setLoading(false);
            });
    });
}

setup();

theButton.addEventListener("click", openPages);