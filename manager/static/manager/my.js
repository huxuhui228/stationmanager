
var filter_para = {};
$(document).ready(

function () {
    get_para();
    $("#district"+filter_para["district"]).attr("class","selected");    
    $("#measure_means"+filter_para["measure_means"]).attr("class","selected");
    $(".pagination a").each(function () {
//        console.log($(this).attr("href"));
        if (filter_para["district"] && $(this).attr("href")) {
            $(this).attr("href",$(this).attr("href")+"&district="+filter_para["district"]);
        }
        if (filter_para["measure_means"] && $(this).attr("href")) {
            $(this).attr("href",$(this).attr("href")+"&measure_means="+filter_para["measure_means"]);
        }
    });
});
function get_para() {
    var str = window.location.href;
    if (str.charAt(str.length-1) == '\?') {
        str = str.substr(0,str.length-1);
    }
    if (str.indexOf("\?") != -1){
        var ss = str.split("?");
        parent_link = ss[0]
        var pp = ss[1].split("&");
        $.each(pp,function (i,item) {
            pars = item.split("=");
            filter_para[pars[0]] = pars[1];
        })
    }
}

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
    var str = window.location.href;
    if (str.charAt(str.length-1) == '\?') {
        str = str.substr(0,str.length-1);
    }
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
    delete filter_para["page"];
    if (par_val=="all") {
        delete filter_para[par];
    }
    else {
        filter_para[par] = par_val;
    }
    new_link = "";
    for (var key in filter_para) {
//        console.log(key+"======"+filter_para[key]);
        new_link += "&"+key+"="+filter_para[key];
    }
    console.log("new_link:'"+new_link+"'");
    if (new_link.length>0) {
        new_link = "?"+new_link.substr(1,new_link.length);
    }
    window.location.href = parent_link+new_link;
/*    $.ajax({
        url: parent_link+"?"+new_link.substr(1,new_link.length),
        type:"GET",
        success: function (data) {
            $(".main").html(data);
        
        
        }
    })*/
}



