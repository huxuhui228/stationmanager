
from django import template
register = template.Library()
@register.simple_tag
def action_all(current_url,index):
    """
    获取当前url，video-1-1-2.html
    :param current_url:
    :param item:
    :return:
    """
    url_part_list = current_url.split('-')
    if index == 3:
        if url_part_list[index] == "0.html":
            temp = "<a href='%s' class='active'>全部</a>"
        else:
            temp = "<a href='%s'>全部</a>"

        url_part_list[index] = "0.html"
    else:
        if url_part_list[index] == "0":
            temp = "<a href='%s' class='active'>全部</a>"
        else:
            temp = "<a href='%s'>全部</a>"

        url_part_list[index] = "0"


    href = '-'.join(url_part_list)

    temp = temp % (href,)
    return mark_safe(temp)

@register.simple_tag
def action(current_url, item,index):
    # videos-0-0-1.html
    # item: id name
    # video-   2   -0-0.html
    url_part_list = current_url.split('-')
 
    if index == 3:
        if str(item['id']) == url_part_list[3].split('.')[0]:
            temp = "<a href='%s' class='active'>%s</a>"
        else:
            temp = "<a href='%s'>%s</a>"
 
        url_part_list[index] = str(item['id']) + '.html'
    else:
        if str(item['id']) == url_part_list[index]:
            temp = "<a href='%s' class='active'>%s</a>"
        else:
            temp = "<a href='%s'>%s</a>"
 
        url_part_list[index] = str(item['id'])
 
    ur_str = '-'.join(url_part_list)  #拼接整体url
    temp = temp %(ur_str, item['name']) #生成对应的a标签
    return mark_safe(temp)  #返回安全的html