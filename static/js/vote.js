function sendRequest(requestUrl, post) {
    $.ajax({
        type: "GET",
        url: requestUrl,
        data: {
            "pid": post.pid
        },
        dataType: "json"
    })
};

// When a user clicks the upvote button.
$(document).on("click", "#upvote", function() {
    //let information = $(this).parent().children(":first").children()[1].innerText;
    //let pid = information.split("\n")[0];

    sendRequest("/upvote", post);
});