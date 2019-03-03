 $("").hide();
  (function(){
    var myDiv = document.getElementById("myDiv"),

      show = function(){
        myDiv.style.display = "block";
        setTimeout(hide, 8000); // 5 seconds
      },

      hide = function(){
        myDiv.style.display = "none";
      };

    show();
  })();

  $(document).ready(function(){

                var name1= localStorage.getItem("name");
                console.log(name1);
               var name=name1.slice(1,name1.length-1);
                 document.getElementById("name").innerHTML=name;
            //var name=$(".name").val();
            //var fail='https://api.social-searcher.com/v2/search?q=%22Monthly%20fails%22&type=video&network=youtube,dailymotion&limit=100&key=f3f7f89be89f4d96950fee9e38aa50b1';
            var url='https://api.social-searcher.com/v2/search?q='+name+'&key=fa9330bda692b55c3507a60fe5c02c90';


                $.getJSON(url,function(data){
                    var recordfb=[];
                    var recordfb1=[];
                    var recordtw=[];
                    var recordtw1=[];
                    var recordothers=[];
                    var recordothers1=[];
                    var urlName = name1.replace(" ",".");

                    var fb=/facebook/i;
                    var tw=/twitter/i;
                    var pb=/public/i;
                    var pp=/people/i;

                    for(var j =0;j<data.posts.length;j++) {
                        let obj = data.posts[j];
                        if (obj["url"].match(fb)) {
                            if (obj["url"].match(pb)) {

                                var a = obj["url"].slice(32, obj["url"].length);
                                var a1 = obj["url"].slice(32, 32 + name.length);
                                recordfb1.push("<a href='" + obj["url"] + "'  >" + a1 + "</a>" + "<br><br>");
                                recordfb.push(obj["url"]);

                            }
                            else if (obj["url"].match(pp)) {

                                var b = obj["url"].slice(32, obj["url"].length);
                                var a1 = obj["url"].slice(32, 32 + name.length);
                                recordfb1.push("<a href='" + obj["url"] + "'  >" + a1 + "</a>" + "<br><br>");
                                recordfb.push(obj["url"]);
                            }
                            else {
                                var c = obj["url"].slice(25, obj["url"].length);
                                var a1 = obj["url"].slice(32, 32 + name.length);
                                recordfb1.push("<a href='" + obj["url"] + "'  >" + a1 + "</a>" + "<br><br>");
                                 recordfb.push(obj["url"]);
                            }
                        }
                    }


                        for(var j =0;j<data.posts.length;j++){
                        let obj=data.posts[j];
                        if(obj["url"].match(tw))
                        recordtw.push("<a href='"+obj["url"]+"'  >"+ obj["url"] + "</a>"+"<br><br>");
                         recordtw1.push(obj["url"]);
                        }

                      for(var j =0;j<data.posts.length;j++){
                        let obj=data.posts[j];
                        if(!(obj["url"].match(fb)||obj["url"].match(tw))){
                            recordothers.push("<a href='"+obj["url"]+"'  >"+ obj["url"] + "</a>"+"<br><br>");

                            recordothers1.push(obj["url"]);
                            console.log(typeof obj['url']);
                             }

                        //771bf09f285365e0c4454a832fb55618
                        //f3f7f89be89f4d96950fee9e38aa50b1
                        //62eca409b57b0137e88508d5f931271c
                          //09a6312abd7970cb42378e0de709ab3a
                          //fa9330bda692b55c3507a60fe5c02c90
                    }
                   console.log(recordfb+recordothers1+recordtw1+","+name1);

                    $('#msgfb').html(recordfb1);
                    $('#msgtw').html(recordtw);
                    $('#msgot').html(recordothers);
                    var l1=name1;
var ar=l1.split(' ');
//console.log(ar);
//ar=['uhuehdu','jdijeid'];
var l2='https://www.facebook.com/';
var l3=ar.join('.');
console.log(l2+l3.slice(1,l3.length-1));
abc=l2+l3.slice(1,l3.length-1);
//console.log(ar+l2+l3)
                    document.getElementById("txtar").innerHTML=abc+","+recordfb+recordothers1+recordtw1;
                    console.log("--------------");
                    console.log(abc+","+recordfb+recordothers1+recordtw1);


        });

        });
