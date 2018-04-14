layui.define(['element', 'laytpl', 'home_http'], function (exports) {
    var element = layui.element
        , $ = layui.jquery
        , laytpl = layui.laytpl
        , base = layui.base

    laytpl.config({
        open: '<%',
        close: '%>'
    })

    ~function () {
        storage = window.localStorage
        var init_home = function(data) {
            var tpl = $('#layout-head-tpl').html()
            laytpl(tpl).render(data, function(html) {
                $('#layout-head').html(html)
            })
        }
        if(window.localStorage.getItem('settings')) {
            init_home(JSON.parse(storage.getItem('settings')));
        } else {
            $.ajax({
                type: 'get',
                url: window.location.href +'/user/settings',
                async: false,
                success: function(res) {
                   init_home(res.data);
                   storage.setItem('settings', JSON.stringify(res.data))
                }
            })
        }
       
    }()

    exports('layout', {})
})
