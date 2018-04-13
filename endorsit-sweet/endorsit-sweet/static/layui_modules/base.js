layui.define(['jquery', 'layer'], function(exports) {
    var $ = layui.jquery,
        layer = layui.layer

    var web_config = {
        api_addr: 'https://api.sweet.ext.earth'
    }


    var utils = {
        apigen: function(path) {
            return web_config.api_addr + path
        },

        isFunc: function(arg) {
            if (arg != undefined && arg != null && arg instanceof Function) {
                return true
            }
            return false
        },

        http_handler: function(response, callback, exception) {
            if (response.status) {
                if (utils.isFunc(callback)) {
                    callback(response.data)
                } else {
                    layer.msg(response.msg)
                }
            } else {
                if (utils.isFunc(exception)) {
                    exception(response)
                } else {
                    layer.msg(response.msg)
                }
            }
        },

        time_stamp: function() {
            return Math.round(new Date().getTime()/1000)
        },

        copy: function (target) {
            // target element
            var copyDOM = document.querySelector(target) 
            var range = document.createRange() 

            // checked the target element 
            range.selectNode(copyDOM) 

            // execute the target element 
            var agent = window.navigator.userAgent.toLowerCase()
            if (agent.indexOf('mac') >= 0 || agent.indexOf('iphone') >= 0 || agent.indexOf('ipad') >= 0) {
                window.getSelection().addRange(range) 
            } else {
                copyDOM.select()
            }

            // copy 
            var successful = document.execCommand('copy') 

            try { 
                var msg = successful ? 'copied!' : 'copy failed' 
                layer.msg(msg)
            } catch(err) { 
                layer.msg('can\'t copy')
            } 

            // remove checked element 
            window.getSelection().removeAllRanges()
        },

        encodeBase64: function(str) {
            if (Base64.extendString) {
                Base64.extendString()
                code = encodeURIComponent(str).toBase64()
                return code
            }
            return null
        },

        decodeBase64: function(str) {
            if (Base64.extendString) {
                Base64.extendString()
                text = decodeURIComponent(str.fromBase64())
                return text
            }
            return null
        }
    }

    exports('base', $.extend({}, web_config, utils))
})
