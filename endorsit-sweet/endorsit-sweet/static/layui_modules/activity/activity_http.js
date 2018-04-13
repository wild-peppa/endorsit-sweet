layui.define(['layer', 'jquery', 'base'], function(exports) {
    var $ = layui.jquery,
     base = layui.base,
    layer = layui.layer

    var http = {

        get_invite_info: function(code, callback=null, exception=null) {
            $.ajax({
                type: 'get',
                async: false,
                url: base.apigen('/invite/info/' + code),
                success: function(response) {
                    base.http_handler(response, callback, exception)
                }
            })
        }
    }

    exports('steps_http', http)
})
