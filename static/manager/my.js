/*$(document).ready(
 
function () {
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
            if (key=="page") {
                continue;
            }
            if (filter_para[key] && $(this).attr("href")) {
                $(this).attr("href",$(this).attr("href")+"&"+key+"="+filter_para[key]);
            }
        }

    });
});*/

function closeit() {
    layer.closeAll();
}



function setcolor() {
	$(".backStatus").each(function () {
			if ($(this).text()=='未返回' || $(this).text()=='未完成') {
			 $(this).css("color","red");
		    }
		    if ($(this).text()=='已返回' || $(this).text()=='已完成') {
			 $(this).css("color","blue");
		    }
		    if ($(this).text()=='部分返回') {
			 $(this).css("color","yellow");
		    }
		    if ($(this).text()=='无需返回') {
			 $(this).css("color","green");
		    }
	});
}
function selectUnreturned(){
    $.ajax({
        type:'GET',
        url:'/deleveryIndex/unreturned',
        success:function (result) {
            $('#dataTable').html(result);
            setcolor();
        }
    });
}

function changepage(obj, first){
            if(!first){
		      if (obj) {
                    search_word = document.getElementById('search_word').value;
                    if (search_word != '') {
                    	getList('/'+$("li.layui-this").attr("lay-id")+'/'+'?page='+obj.curr+'&search_word='+search_word);
                    }
                    else {
                    	getList('/'+$("li.layui-this").attr("lay-id")+'/'+'?page='+obj.curr);
                    }
                }
                else {
                	getList('/'+$("li.layui-this").attr("lay-id")+'/');
                }
            }}
function getList(url){
    $.ajax({
        type:"get",
        url: url,
        success:function(result){
            $('.layui-show').html(result);
        }
    });

}

function refreshPage() {
    search_word = document.getElementById('search_word').value;
    curr_page = $("#"+$("li.layui-this").attr("lay-id")+"Paginator>"+".layui-laypage-curr em:last").text();
    if (search_word != '') {
    	getList('/'+$("li.layui-this").attr("lay-id")+'/'+'?page='+curr_page+'&search_word='+search_word);
    }
    else {
    	getList('/'+$("li.layui-this").attr("lay-id")+'/'+'?page='+curr_page);
    }
}

function getall(){
    $.ajax({
        type:"get",
        url: $("li.layui-this").attr("lay-id"),
        success:function(result){
            $('.layui-show').html(result);
        }
    });

}

function newtab(tabid){
  layui.use('element', function(){
  var $ = layui.jquery
  ,element = layui.element;
    if ( $(".layui-tab-title li[lay-id='"+tabid+"']").length > 0 ) {
        element.tabChange('tabs',tabid); 
    }
    else {
        
        $.ajax({
          type:'GET',
          url:"/"+tabid,
          success:function (result) {
                element.tabAdd('tabs', {
                    title: tabid
                    ,content: result
                    ,id: tabid
                  });
            
            element.tabChange('tabs',tabid);
        }
    });
}
});
  }


/*function get_para() {
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
}*/

function deleteUnit(id){

    layer.confirm(
        '确定删除吗？', 
        { btn:['确定','取消'] }, 
        function (){
            $.ajax({
                url: "/"+$("li.layui-this").attr("lay-id")+"/"+id+"/delete",
                type: "Get",
                success: 
                    function(data){
                        if (data=='1'){
                            refreshPage();
                            }
                        else{
                            layer.alert('删除失败。')
                            }
                        },
                })
            layer.closeAll('dialog');
        },
        
        function () {
            layer.close();
        }
      );
}
function setFilter(par,par_val){
    $.ajax({
        url: "/"+$("li.layui-this").attr("lay-id")+"/?"+par+"="+par_val,
        type:"GET",
        success: function (result) {
            $('.layui-show').html(result);
        }
    });
}


function edit(id) {
	$.ajax({
	   url: "/"+$("li.layui-this").attr("lay-id")+"/"+id,
	   type: "Get",
	   success:function (result) {
	       
	   	   layer.open({
	   	       type: 1,
	   	       title: "详细信息",
	   	       area: ['960px','640px'],
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
        url: '/'+$("li.layui-this").attr("lay-id")+'/'+pk,
        type: "post",
        data: $("#detail").serialize(),
        success: function (result) {
            
            if (result=='1') {
                layer.alert("修改成功。",
                    function () {
                        layer.closeAll();
                        refreshPage();
//                        top.location.reload();
                    }
                );
            }
            if (result=='2') {
                layer.msg("修改失败。");
            }
            
            
        }
    
    });
}


function newRecord() {
    $.ajax({
	   url: "/"+$("li.layui-this").attr("lay-id")+"/new",
	   type: "Get",
	   success:function (result) {
	   	   layer.open({
	   	       type: 1,
	   	       title: "new "+$("li.layui-this").attr("lay-id"),
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
    $.ajax({
        url: "/"+$('#par').val()+"/new",
        type: "post",
        data: $("#newRecord").serialize(),
        success: function (result) {
            
            if (result=='1') {
                layer.alert("添加成功。",
                    function (index) {
                        layer.closeAll();
                        refreshPage();
                    }
                );
                
            }
            if (result=='2') {
                layer.alert("添加失败，请检查。");
            }
            
        }
    
    });
}

