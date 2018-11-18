/**
 * Created by caden on 2018/11/10.
 */
var ProjectInit = function (_cmbProject, _cmbModule, defaultProject, defaultMudle) {
    var cmbProject = document.getElementById(_cmbProject);
    var cmbModule = document.getElementById(_cmbModule);
    var datalist = [];

    //用例调试页面设置默认项
    function cmbSelect(cmb, str) {
        for (var i=0; i<cmb.options.length; i++){
            if (cmb.options[i].value == str){
                cmb.selectedIndex = i;
                return;
            }
        }
    }

    //创建下拉选项
    function cmbAddoption(cmb, str, obj) {
        //console.log(str)
        var option = document.createElement("option");
        cmb.options.add(option);
        option.innerHTML = str;
        option.value = str;
        option.obj = obj;
    }

    //改变项目
    function changeProject() {
        cmbModule.options.length = 0;
        if (cmbProject.selectedIndex == -1){
            return;
        }
        var item = cmbProject.options[cmbProject.selectedIndex].obj;
        for (var i = 0; i< item.modulelist.length; i++){
            cmbAddoption(cmbModule, item.modulelist[i], null);
        }
        cmbSelect(cmbModule, defaultMudle);
    }

    //调用项目列表接口
    function getProjectlist() {
        $.get("/interface/get_project_list", {}, function (resp) {
            if (resp.success === "true"){
                datalist = resp.data;
                 for (var i = 0; i < datalist.length; i++) {
                    cmbAddoption(cmbProject, datalist[i].name, datalist[i]);
                }
                cmbSelect(cmbProject, defaultProject);
                changeProject();
                cmbProject.onchange = changeProject;
            }
            cmbSelect(cmbProject, defaultProject);
        });
    }
    getProjectlist();
}