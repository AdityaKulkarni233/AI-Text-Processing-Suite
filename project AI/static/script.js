let currentTool = "summarizer";

function showSummarizer() {
    currentTool = "summarizer";

    document.getElementById("toolTitle").innerText = "AI Text Summarizer";
    document.getElementById("toolLogo").src = "/static/logo.png";
    document.getElementById("actionButton").innerText = "Summarize";
    document.getElementById("inputText").value = "";
    document.getElementById("outputText").innerText = "";

    document.getElementById("summarizerLink").classList.add("active");
    document.getElementById("grammarLink").classList.remove("active");
}

function showGrammar() {
    currentTool = "grammar";

    document.getElementById("toolTitle").innerText = "AI Grammar Checker";
    document.getElementById("toolLogo").src = "/static/logo1.png";
    document.getElementById("actionButton").innerText = "Check Grammar";
    document.getElementById("inputText").value = "";
    document.getElementById("outputText").innerText = "";

    document.getElementById("grammarLink").classList.add("active");
    document.getElementById("summarizerLink").classList.remove("active");
}

async function processText() {
    const text = document.getElementById("inputText").value;

    const formData = new FormData();
    formData.append("text", text);

    let endpoint = currentTool === "summarizer" ? "/summarize" : "/proofread";

    const response = await fetch(endpoint, {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    if (currentTool === "summarizer") {
        document.getElementById("outputText").innerText = data.summary;
    } else {
        document.getElementById("outputText").innerText = data.corrected_text;
    }
}

function copyText() {
    const text = document.getElementById("outputText").innerText;
    navigator.clipboard.writeText(text);
    alert("Copied!");
}

function downloadText() {
    const text = document.getElementById("outputText").innerText;
    const blob = new Blob([text], { type: "text/plain" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = currentTool === "summarizer" ? "summary.txt" : "corrected_text.txt";
    link.click();
}