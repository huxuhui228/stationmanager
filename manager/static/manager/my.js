

$(document).ready(

function () {
/*    layui.use('table', function(){
	var table = layui.table;
    table.init('stationIndexTable', {
        
        limit:20,
    });
})*/
    filter_para = get_para();
    filter_para = filter_para[1];
    if (filter_para["search_word"]) {
        $("#search_word").attr("placeholder", decodeURI(filter_para["search_word"]));
    }
    $("#district"+filter_para["district"]).attr("class","selected");    
    $("#measure_means"+filter_para["measure_means"]).attr("class","selected");
    $(".pagination a").each(function () {
//        console.log($(this).attr("href"));
        for (var key in filter_para) {
            if (filter_para[key] && $(this).attr("href")) {
                $(this).attr("href",$(this).attr("href")+"&"+key+"="+filter_para[key]);
            }
        }
/*        if (filter_para["district"] && $(this).attr("href")) {
            $(this).attr("href",$(this).attr("href")+"&district="+filter_para["district"]);
        }
        if (filter_para["measure_means"] && $(this).attr("href")) {
            $(this).attr("href",$(this).attr("href")+"&measure_means="+filter_para["measure_means"]);
        }
        if (filter_para["search_word"] && $(this).attr("href")) {
            $(this).attr("href",$(this).attr("href")+"&search_word="+filter_para["search_word"]);
        }*/
    });
});
function get_para() {
    var filter_para = {};
    var parent_link = '';
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
    return [parent_link, filter_para];
}

function deleteUnit(id){
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
    filter_para = get_para();
    parent_link = filter_para[0];
    filter_para = filter_para[1];
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

function edit(id) {
	$.ajax({
	   url: id,
	   type: "Get",
	   success:function (result) {
	   	   layer.open({
	   	       type: 1,
	   	       title: "详细信息",
	   	       area: ['800px','640px'],
	   	       closeBtn: 1,
	   	       shadeClose: true,
	   	       scrollbar: false,
	   	       content: result,
	   	       });
	       }
	});
}

function saveEdit(pk) {
    $.ajax({
        url: pk,
        type: "post",
        data: $(".detail").serialize(),
        success: function (result) {
            if (result=='1') {
                layer.alert("修改成功。",
                    function () {
                        layer.closeAll();
                        top.location.reload();
                    }
                );
            }
            if (result=='2') {
                layer.msg("修改失败。");
            }
            
            
        }
    
    });
}


function newRecord(str) {
    $.ajax({
	   url: "/manager/"+str+"/new",
	   type: "Get",
	   success:function (result) {
	   	   layer.open({
	   	       type: 1,
	   	       title: "new "+str,
	   	       area: ['800px','640px'],
	   	       closeBtn: 1,
	   	       shadeClose: true,
	   	       scrollbar: false,
	   	       content: result,
	   	       });
	       }
	});
}

function saveNew() {
    layer.alert('$('#par').text()');
    $.ajax({
        url: "/manager/"+$('#par').text()+"/new",
        type: "post",
        data: $(".newRecord").serialize(),
        success: function (result) {
            if (result=='1') {
                layer.alert("添加成功。",
                    function () {
                        layer.closeAll();
                        top.location.reload();
                    }
                );
            }
            if (result=='2') {
                layer.alert("添加失败，请检查。");
            }
            
            
        }
    
    });
}