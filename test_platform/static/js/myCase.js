/**
 * Created by caden on 2018/11/15.
 */

//获取指定用例ID的信息
var CaseInit = function (case_id) {
    function () {
        //获取一个用例的信息
        $.post("/interface/get_case_info/", {
            "case_id": case_id,
        }, function(resp){
            if (resp === "true"){
                //

            }else {
                window.alert("用例ID不存在！")
            }
        })
        
    }
}
