;
var user_login_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        $(".login-box  .do-login").click(function(){

            var login_name = $(".login-box input[name=login_name]").val();
            var login_pwd = $(".login-box input[name=login_pwd]").val();

            if(login_name==undefined ||login_name.length<1){
                common_ops.alert("请输入正确的登录用户名");
                return;
            }

            if(login_pwd==undefined ||login_pwd.length<1){
                common_ops.alert("请输入正确的登录密码");
                return;
            }

//            使用AJAX提交
            $.ajax({
//               url:common_ops.buildUrl("/"),
                url:"http://192.168.2.21:5653/login",
               type:"POST",
               data:{'login_name':login_name,'login_pwd':login_pwd} ,
               dataType:'json',
               success:function(res){
                    var callback = null;
                    if(res.code==200){
                        callback = function(){
                            window.location.href = common_ops.buildUrl("/");
//                            window.location.href = "http://127.0.0.1:8000";

                        }
                    }
                    common_ops.alert(res.msg,callback);
               }
            });
        });
    }


};

$(document).ready(function(){
    user_login_ops.init();
})


