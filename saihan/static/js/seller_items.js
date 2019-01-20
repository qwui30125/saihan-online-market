for(var i=0;i<tr.length;i++){
    tr[i].onclick = function(e){
    e = e|| window.event;
    var el = e.srcElement;
    var cls = el.className;
    var input = this.getElementsByTagName('input')[1];
    var val = parseInt(input.value);
    var reduce = this.getElementsByTagName('span')[1];
    switch (cls){
     case 'add':
     input.value = val + 1;
     reduce.innerHTML = '-';
      getsubTotal(this);
     break;
     case 'reduce':
     if(val > 1){
      input.value = val - 1;
      getsubTotal(this);
     }else{
      reduce.innerHTML = '';
     }
    }
    getTotal();
    }
    tr[i].getElementsByTagName('input')[1].onkeyup = function(){
    var val = parseInt(this.value);
    var tr = this.parentNode.parentNode;//this指的是当前的input，其父节点的父节点就是当前的tr
    var reduce = tr.getElementsByTagName('span')[1];
    if(isNaN(val) || val < 1){
     val = 1;
    }
    this.value = val;//保证输入框中都是大于1的纯数字
    if(val <= 1){
     reduce.innerHTML = '';
    }
    else{
     reduce.innerHTML = '-';
    }
    getsubTotal(tr);
    getTotal();
    }
   }