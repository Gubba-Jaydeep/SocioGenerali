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
            var url='https://api.social-searcher.com/v2/search?q='+name+'&key=62eca409b57b0137e88508d5f931271c';


                $.getJSON(url,function(data){
                    var recordfb=[];
                    var recordfb1=[];
                    var recordtw=[];
                    var recordtw1=[];

                   // var yo=[1,2,3,4];
                    var recordothers=[];
                    var recordothers1=[];
                    var fb=/facebook/i;
                    var tw=/twitter/i;
                    var pb=/public/i;
                    var pp=/people/i;
                    for(var j =0;j<data.posts.length;j++) {
                        let obj = data.posts[j];
                        if (obj["url"].match(fb)) {
                            if (obj["url"].match(pb)) {
                                var a1 = [];

                                var a = obj["url"].slice(32, obj["url"].length);
                                a1 = a.split("//");
                                recordfb1.push("<a href='" + a + "'  >" + a1[0] + "</a>" + "<br><br>");
                                recordfb.push("<a href='" + obj["url"] + "'  >" + obj["url"] + "</a>" + "<br><br>");
                            }
                            else if (obj["url"].match(pp)) {
                                var b = obj["url"].slice(32, obj["url"].length);
                                recordfb1.push("<a href='" + obj["url"] + "'  >" + b + "</a>" + "<br><br>");
                                recordfb.push("<a href='" + obj["url"] + "'  >" + obj["url"] + "</a>" + "<br><br>");
                            }
                            else {
                                var c = obj["url"].slice(25, obj["url"].length);
                                recordfb1.push("<a href='" + obj["url"] + "'  >" + c + "</a>" + "<br><br>");
                                recordfb.push("<a href='" + obj["url"] + "'  >" + obj["url"] + "</a>" + "<br><br>");
                            }


                            // console.log(obj["url"]);
                            //recordfb.push("<a href='" + obj["url"] + "'  >" + obj["url"] + "</a>" + "<br><br>");
                        }
                    }
                        for(var j =0;j<data.posts.length;j++){
                        let obj=data.posts[j];
                        if(obj["url"].match(tw))
                        recordtw.push("<a href='"+obj["url"]+"'  >"+ obj["url"] + "</a>"+"<br><br>");

                    }
                      for(var j =0;j<data.posts.length;j++){
                        let obj=data.posts[j];
                        if(!(obj["url"].match(fb)||obj["url"].match(tw))){
  recordothers.push("<a href='"+obj["url"]+"'  >"+ obj["url"] + "</a>"+"<br><br>");

                        }

                        //console.log(obj["<b>Others ::</b> "+obj["url"]);
                        //771bf09f285365e0c4454a832fb55618
                        //f3f7f89be89f4d96950fee9e38aa50b1
                        //62eca409b57b0137e88508d5f931271c
                    }
                    //console.log(recordfb);
                    $('#msgfb').html(recordfb1);

                    $('#msgtw').html(recordtw);
                    $('#msgot').html(recordothers);
                    //+" : "+obj["user"]["location"]
                    console.log(recordfb);
                    document.getElementById("txtar").innerHTML=recordfb;
                    // localStorage.setItem('fbdata', JSON.stringify(recordfb));
                    // localStorage.setItem('twitterdata', JSON.stringify(recordtw));
                    // localStorage.setItem('otherdata', JSON.stringify(recordothers));
                    // window.open("C:\Users\iot4\Desktop\notify.html");



        });

        });
