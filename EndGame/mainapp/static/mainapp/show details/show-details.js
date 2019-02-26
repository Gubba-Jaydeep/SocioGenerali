  $(document).ready(function(){

                var name1= localStorage.getItem("name");
                console.log(name1);
               var name=name1.slice(1,name1.length-1);
                 document.getElementById("name").innerHTML=name;
            //var name=$(".name").val();
            //var fail='https://api.social-searcher.com/v2/search?q=%22Monthly%20fails%22&type=video&network=youtube,dailymotion&limit=100&key=f3f7f89be89f4d96950fee9e38aa50b1';
            var url='https://api.social-searcher.com/v2/search?q='+name+'&key=771bf09f285365e0c4454a832fb55618';


                $.getJSON(url,function(data){
                    var recordfb=[];
                    var recordtw=[];
                   // var yo=[1,2,3,4];
                    var recordothers=[];
                    var fb=/facebook/i;
                    var tw=/twitter/i;
                    for(var j =0;j<data.posts.length;j++){
                        let obj=data.posts[j];
                        if(obj["url"].match(fb)) {

                            console.log(obj["url"]);
                            recordfb.push("<a href='"+obj["url"]+"'  >"+ obj["url"] + "</a>" + "<br><b>Last Active::</b>" + obj["posted"] + "<br>" + "<br>");
                        }
                        else if(obj["url"].match(tw))
                        recordtw.push("<a href='"+obj["url"]+"'  >"+ obj["url"] + "</a>" + "<br><b>Last Active::</b>"+obj["posted"]+"<br>"+"<br>");
                       else
                       recordothers.push("<b>Web ::</b> "+"<a href='"+obj["url"]+"'  >"+ obj["url"] + "</a>" +"<br><b>Last Active::</b>"+obj["posted"]+"<br>"+"<br>");

                        //console.log(obj["<b>Others ::</b> "+obj["url"]);
                        //771bf09f285365e0c4454a832fb55618
                        //f3f7f89be89f4d96950fee9e38aa50b1
                    }
                    //console.log(recordfb);
                    $('#msgfb').html(recordfb);

                    $('#msgtw').html(recordtw);
                    $('#msgot').html(recordothers);
                    //+" : "+obj["user"]["location"]
                    console.log(recordfb);
                    // localStorage.setItem('fbdata', JSON.stringify(recordfb));
                    // localStorage.setItem('twitterdata', JSON.stringify(recordtw));
                    // localStorage.setItem('otherdata', JSON.stringify(recordothers));
                    // window.open("C:\Users\iot4\Desktop\notify.html");



        });

        });
