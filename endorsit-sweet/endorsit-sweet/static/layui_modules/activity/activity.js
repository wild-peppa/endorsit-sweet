layui.define(['base', 'laytpl'], function(exports) {
    var $ = layui.jquery
    ,layer = layui.layer
    ,laytpl = layui.laytpl
    ,base = layui.base

    laytpl.config({
        open: '<%',
        close: '%>'
    })
    storage = window.localStorage
    var code = storage.getItem('code')
    var settings = storage.getItem('settings')
    settings = JSON.parse(settings)

    if (code == '' || code == null) {
        storage.clear()
        location.href = '/'
    }

    var init_activity_area = function() {
        settings.code = '/' + code
        settings.share_link = window.location.origin + '/' + code

        $.ajax({
            url: window.location.origin + '/user/earn',
            type: 'get',
            async: false,
            data: {
                'code': storage.getItem('code')
            },
            success: function(res) {
                settings.invited_count = res.data.invited
                settings.earned = res.data.earned
            },
            error: function() {
                settings.invited_count = 0
                settings.earned = 0
            }
        })



        var agent = window.navigator.userAgent.toLowerCase()
        if (agent.indexOf('mac') >= 0 || agent.indexOf('iphone') >= 0 || agent.indexOf('ipad') >= 0) {
            settings.is_iphone = true
        } else {
            settings.is_iphone = false 
        }

        var tpl = $('#activity-area-tpl').html()

        laytpl(tpl).render(settings, function(html) {
            $('#layout-body').html(html)
        })
    }

    init_activity_area()

    // **** init buttons **** {
    
    document.getElementById('copy-invite-code').onclick = function() {
        base.copy('#copy-code')
    }

    document.getElementById('copy-invite-link').onclick = function() {
        base.copy('#copy-link')
    }

    $('.claim').click(function() {
        location.href = '/claim'
    })
    
    // } 

    exports('activity', {})
})
