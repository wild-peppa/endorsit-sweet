layui.define(['layer', 'jquery', 'base'], function(exports) {
    var $ = layui.jquery,
     base = layui.base,
    layer = layui.layer

    var http = {

        get_team: function(symbol, callback=null, exception=null) {
            $.ajax({
                type: 'get',
                url: base.apigen('/team/' + symbol),
                async: false,
                success: function(response) {
                    base.http_handler(response, callback, exception)
                }
            })
        },

        post_content: function(data, callback=null, exception=null) {
            $.ajax({
                type: 'post',
                url: base.apigen('/steps/code'),
                data: data,
                success: function(response) {
                    $('#sweform button').text('SUBMIT')
                    $('#sweform button').prop('disabled', false)
                    $('#sweform button').removeClass('layui-btn-disabled')
                    base.http_handler(response, callback, exception)
                }
            })
        },

        get_code_exist: function(code, callback=null, exception=null) {
            $.ajax({
                type: 'get',
                url: base.apigen('/exist/' + code),
                async: false,
                success: function(response) {
                    base.http_handler(response, callback, exception)
                }
            })
        }

    }

    exports('home_http', http)
})

