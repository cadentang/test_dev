/**
 * Created by caden on 2018/11/15.
 */

//获取指定用例ID的信息
var CaseInit = function (case_id) {
    function getCaseInfo() {
        //获取一个用例的信息
        $.post("/interface/get_case_info/", {
            "case_id": case_id,
        }, function(resp){
            if (resp.success === "true"){
                //获取后端返回的数据，然后将值返回给调试页面
                let result = resp.data;
                document.getElementById("response_name").value = result.name;
                document.getElementById("response_url").value = result.response_url;
                document.getElementById("response_header").value = result.response_header;
                document.getElementById("response_parameter").value = result.response_parameter;
                document.getElementById("response_assert").value = result.response_assert;

                if (result.response_method === "post"){
                    document.getElementById("post").setAttribute("checked", "")
                } else if (result.response_method === "put"){
                    document.getElementById("put").setAttribute("checked", "")
                } else if (result.response_method === "delete"){
                    document.getElementById("delete").setAttribute("checked", "")
                }
                if (result.response_type === "json"){
                    document.getElementById("json").setAttribute("checked", "")
                }
                if (result.response_status === "0"){
                    document.getElementById("0").setAttribute("checked", "")
                }
                //初始化菜单
                ProjectInit('project_name', 'module_name', result.project_name, result.module_name);
            }else {
                window.alert("用例ID不存在！")
            }
        });
        
    }

    getCaseInfo();
}
