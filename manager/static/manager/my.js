$(document).ready(

function () {

});

var filter_para = {};
function deleteStation(id){
    layer.confirm(
        '确定删除吗？', 
        { btn:['确定','取消'] }, 
        function (){
            $.ajax({
                url: id+"/delete",
                type: "Get",
                data: {},
                success: 
                    function(data){
                        if (data=='1'){
                            layer.alert('删除成功。')
                         parent.location.reload();
                        }
                        else{
                            layer.alert('删除失败。')
                        }
                    },
                })
        },
        
        function () {
            layer.close();
        }
      );
}
function setFilter(par,par_val){
    $(this).attr("class","selected");
    $("span").not(this).attr("class","unselected");
    var str = window.location.href;
    if (str.indexOf("\?") != -1){
        var ss = str.split("?");
        parent_link = ss[0]
        var pp = ss[1].split("&");
        $.each(pp,function (i,item) {
            pars = item.split("=");
            filter_para[pars[0]] = pars[1];

        })
    }
    else {
        parent_link = str;
    }
    filter_para[par] = par_val;
    console.log(par+">>>>>>"+par_val);
    new_link = "";
    for (var key in filter_para) {
        console.log(key+"======"+filter_para[key]);
        new_link += "&"+key+"="+filter_para[key];
    }
    layer.alert(parent_link+"?"+new_link.substr(1,new_link.length));
    window.location.href = parent_link+"?"+new_link.substr(1,new_link.length);
}



