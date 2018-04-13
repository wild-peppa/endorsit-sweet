layui.define(['laytpl', 'base', 'home_http'], function(exports) {
    var $ = layui.jquery
    ,http = layui.home_http
  ,laytpl = layui.laytpl

    // **** init data **** {
    var init_input_area = function(data) {
        var tpl = $('#input-area-tpl').html()
        laytpl(tpl).render(data, function(html) {
            $('#layout-body').html(html)
        })
    }

    init_input_area({
        '': ''
    })

    // }

    // **** init buttons **** {

    $('#sweform').on('submit', function(e) {
        e.preventDefault()
        buttonChange($(this).find('button'), false)
        var input_content = $('#input-content').val().trim()
        if (input_content == '') {
            layer.msg('fill the input box please')
            buttonChange($(this).find('button'), true)
            return false
        }

        var settings = localStorage.getItem('settings')

        if (settings == null) {
            localStorage.clear()
            location.href = '/'
        }

        stgs = JSON.parse(settings)

        var team_id = stgs.team_id
        var settings_id = stgs.id

        var from_code = storage.getItem('from_code')

        var data = {
            team_id: team_id,
            settings_id: settings_id,
            input_content: input_content
        }

        if (from_code != null && from_code != '') {
            data.from_code = from_code
        }

        http.post_content(data, function(response) {
            localStorage.setItem('code', response.code)
            location.href = '/' + localStorage.getItem('symbol')+ '/steps'
        })
    })

    // }
    function buttonChange(obj, flag) {
        if(flag == false) {
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
