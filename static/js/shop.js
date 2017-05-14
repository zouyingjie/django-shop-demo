function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
$("button.add_commodity").bind("click", function () {
        var commodity_id = $(this).attr("commodity_id");

        $.ajax({
            url: "/shop/add_commodity/",
            type: 'POST',
            data: {'commodity_id': commodity_id},
            success: function (arg) {
                alert("添加成功")
            }

        });
    }
);

$("button.delete_cartitem").bind('click', function () {
    var commodity_id = $(this).attr("commodity_id");
    alert("***")
    $.ajax({
        url: "/shop/del_commodity/",
        type: 'POST',
        data: {'commodity_id': commodity_id},
        success: function (arg) {
            alert("删除成功")
        }
    });
})

$('button#login').bind('click', function(){
     var commodity_id = $(this).attr("commodity_id");
    alert("***")
    data = {'user_email': $('#login_eamil').val(), 'user_pwd': $('#login_pwd').val()}
    $.ajax({
        url: "/shop/del_commodity/",
        type: 'POST',
        data: data,
        success: function (arg) {
            alert("登录成功")
        },
        error:function(arg){
            alert('密码不正确')
        },
    });
})