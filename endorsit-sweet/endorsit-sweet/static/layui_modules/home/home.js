layui.define(['laytpl', 'base'], function (exports) {
    var $ = layui.jquery
        , laytpl = layui.laytpl
    
    laytpl.config({
        open: '<%',
        close: '%>'
    })
    // **** init data **** {
    var init_input_area = function (data) {
        var tpl = $('#input-area-tpl').html()
        laytpl(tpl).render(data, function (html) {
            $('#layout-body').html(html)
        })
    }
    settings = JSON.parse(localStorage.getItem('settings'))
    if(settings != null) {
        init_input_area(settings.input_content_tip)
    }
    else {
        $.ajax({
            type: 'get',
            url: window.location.origin + '/user/settings',
            async: false,
            success: function (res) {
                if(res.data) {
                    window.localStorage.setItem('settings', JSON.stringify(res.data))
                    init_input_area(res.data.input_content_tip)
                }   
            }
        })
    }

    // }
    // **** init buttons **** {
    $('#sweform').on('submit', function (e) {
        e.preventDefault()
        buttonChange($(this).find('button'), false)
        var input_content = $('#input-content').val().trim()
        var emailReg = new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$");
        if (input_content == '') {
            layer.msg('fill the input box please')
            buttonChange($(this).find('button'), true)
            return false
        } else if (!emailReg.test(input_content)) { 
            layer.msg('fill the input box please')
            buttonChange($(this).find('button'), true)
            return false;
        }

        var settings = localStorage.getItem('settings')

        if (settings == null) {
            localStorage.clear()
            location.href = '/'
        }

        stgs = JSON.parse(settings)

        var team_id = stgs.team_id
        var settings_id = stgs.id

        
        var tempArr = window.location.pathname.split("/")
        var from_code = tempArr[tempArr.length - 1];
        var data = {
            team_id: team_id,
            settings_id: settings_id,
            input_content: input_content
        }

        if (from_code != null && from_code != '') {
            data.from_code = from_code
        }
        $.ajax({
            type: 'post',
            url: window.location.origin + '/user/code',
            data: data,
            success: function(res) {
                $('#sweform button').text('SUBMIT')
                $('#sweform button').prop('disabled', false)
                $('#sweform button').removeClass('layui-btn-disabled')
                localStorage.setItem('code', res.data)
                location.href = '/activity'
            }
        })
    })

    // }
    function buttonChange(obj, flag) {
        if (flag == false) {
            $(obj).text('Please Wait...')
            $(obj).prop('disabled', true)
            $(obj).addClass('layui-btn-disabled')
        }
        else {
            $(obj).text('SUBMIT')
            $(obj).prop('disabled', false)
            $(obj).removeClass('layui-btn-disabled')
        }
    }
    exports('home', {})
})
