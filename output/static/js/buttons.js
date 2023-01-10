$(".copy-btn").on("click", copyEmail);
$(".copy-btn").on("click", updateClipboardTooltip);

function copyEmail(id) {
    var range = document.createRange();
    range.selectNode(document.getElementById(id));
    window.getSelection().removeAllRanges(); // clear current selection
    window.getSelection().addRange(range); // to select text
    document.execCommand("copy");
    window.getSelection().removeAllRanges();// to deselect
}

function updateClipboardTooltip(id) {
    const element = $(id)
    const tooltip = bootstrap.Tooltip.getInstance(id);
    tooltip.setContent({".tooltip-inner": "Copied!"});
    setTimeout(() => {
        tooltip.setContent({".tooltip-inner": "Copy to clipboard."})
        tooltip.hide()
    }, 1500);
}