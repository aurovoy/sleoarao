
def imgselect_pac(datapac):
    for i in datapac:
        if i.img_exurl:
            i.imgtrans = i.img_exurl
        elif i.image:
            i.imgtrans = i.image.url
        else:
            i.imgtrans = 'http://ww4.sinaimg.cn/mw690/7204ff25jw1exlf5c4iu0j20m80goaa6.jpg'

    return datapac


def imgselect_obj(datapac):
    i = datapac
    if i.img_exurl:
        i.imgtrans = i.img_exurl
    elif i.image:
        i.imgtrans = i.image.url
    else:
        i.imgtrans = 'http://ww4.sinaimg.cn/mw690/7204ff25jw1exlf5c4iu0j20m80goaa6.jpg'

    return i
