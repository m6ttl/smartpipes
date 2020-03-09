/**
 * Created by yangzhongwei on 2018/3/14.
 */
window.onload = function(){
    /*(设计稿完成宽度)*/
    getRem(1920,100)
};
window.onresize = function(){
    getRem(1920,100)
};
function getRem(pwidth,prem){
    var html = document.getElementsByTagName("html")[0];
    var oWidth = document.body.clientWidth || document.documentElement.clientWidth;
    html.style.fontSize = oWidth/pwidth*prem + "px";
}