function getCookie(name) {
    var x = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return x ? x[1] : undefined;
}

$(document).ready(function () {
    // alert('good');
    $('#login').click(function () {
        var user = $('#userName').val();
        var pwd = $('#userPsw').val();
        var pd = { "username": user, "password": pwd, "_xsrf": getCookie("_xsrf")};
        $.ajax({
            type: "post",
            url: "/",
            data: pd,
            cache: false,
            success: function (data) {
                window.location.href = "/user?user=" + data;
            },
            error: function () {
                alert("error!");
            },
        });
    });
});