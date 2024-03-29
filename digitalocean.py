# You may add here your
# server {
#	...
# }
# statements for each of your virtual hosts to this file

##
# You should look at the following URL's in order to grasp a solid understanding
# of Nginx configuration files in order to fully unleash the power of Nginx.
# http://wiki.nginx.org/Pitfalls
# http://wiki.nginx.org/QuickStart
# http://wiki.nginx.org/Configuration
#
# Generally, you will want to move this file somewhere, and start with a clean
# file but keep this around for reference. Or just disable in sites-enabled.
#
# Please see /usr/share/doc/nginx-doc/examples/ for more detailed examples.
##

server {
	listen 80 default_server;
	listen [::]:80 default_server ipv6only=on;

	root /var/www/html/wowonder/;
	index index.php index.html index.htm;

	# Make site accessible from http://localhost/
	server_name localhost;

	location / {

	  if (!-e $request_filename){
	    rewrite ^/password-reset/([^\/]+)(\/|)$ /index.php?link1=welcome&link2=password_reset&user_id=$1;
	  }
	  rewrite ^/$ /index.php?link1=home;
	  rewrite "^/forum/members/([a-zA-Z]{0,1})(/?|)$" /index.php?link1=forum-members-byname&char=$1;
	  if (!-e $request_filename){
	    rewrite ^/setting/([A-Za-z0-9_]+)/([A-Za-z0-9_-]+)$ /index.php?link1=setting&user=$1&page=$2;
	    rewrite ^/setting/([A-Za-z0-9_-]+)$ /index.php?link1=setting&page=$1;
	    rewrite ^/setting$ /index.php?link1=setting;
	  }	


	if (!-e $request_filename){
	    rewrite ^/@([^\/]+)(\/|)$ /index.php?link1=timeline&u=$1;
	  }
	  if (!-e $request_filename){
	    rewrite ^/([A-Za-z0-9_]+)/([^\/]+)(\/|)$ /index.php?link1=timeline&u=$1&type=$2;
	  }

	if (!-e $request_filename){
	    rewrite ^/([^\/]+)(\/|)$ /index.php?link1=timeline&u=$1;
	  }
		# First attempt to serve request as file, then
		# as directory, then fall back to displaying a 404.
		#try_files $uri $uri/ =404;
		# Uncomment to enable naxsi on this location
		# include /etc/nginx/naxsi.rules
	}

	error_page 404 /404.html;
	error_page 500 502 503 504 /50x.html;
	location = /50x.html {
		root /usr/share/nginx/html;
	}

	location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php7.2-fpm.sock;
	}

	# deny access to .htaccess files, if Apache's document root
	# concurs with nginx's one
	#
	#location ~ /\.ht {
	#	deny all;
	#}
	#
	#
	#
	#  
	
	location /admin {
		rewrite ^/admin-cp$ /admincp.php;
		rewrite ^/admin-cp/(.*)$ /admincp.php?page=$1;
		rewrite ^/admin/ads/edit/(\d+)(/?|)$ /index.php?link1=manage-ads&id=$1;
	}

	location = /admincp {
	  rewrite ^(.*)$ /admincp.php;
	}

	location /admincp {
	  rewrite ^/admincp/(.*)$ /admincp.php?page=$1;
	}

	location /adminPages/ {
	  return 301 /admin-panel/;
	}

	location ~ ^/adminPages/(.*) {
	    return 301 /admin-panel/$1;
	}

	location /start {
	  rewrite ^/start-up$ /index.php?link1=start-up;
	}

	location /saved {
		rewrite ^/saved-posts/(.*)$ /index.php?link1=saved-posts;
		rewrite ^/saved-posts$ /index.php?link1=saved-posts;
	}

	location /activated {
	  rewrite ^/activated/(.*)$ /index.php?link1=activate&link2=$1;
	}

	location = /search {
		rewrite ^(.*)$ /index.php?link1=search;
	}
	
	location /ads {
	  rewrite ^/ads-create$ /index.php?link1=ads-create;
	  rewrite ^/ads(/?|)$ /index.php?link1=ads;
	  rewrite ^/ads/create(/?|)$ /index.php?link1=create-ads;
	  rewrite ^/ads/edit/(\d+)(/?|)$ /index.php?link1=edit-ads&id=$1;
	  rewrite ^/ads/chart/(\d+)(/?|)$ /index.php?link1=chart-ads&id=$1;
	}
	location /send_money {
	  rewrite ^/send_money$ /index.php?link1=ads-create;
	}

	location = /most_liked {
	  rewrite ^(.*)$ /index.php?link1=most_liked;
	}

	location /suggested {
	  rewrite ^/suggested-pages(/?|)$ /index.php?link1=suggested-pages;
	  rewrite ^/suggested-groups(/?|)$ /index.php?link1=suggested-groups;
	}

	location = /poke {
	  rewrite ^(.*)$ /index.php?link1=poke;
	}

	location /search {
	  rewrite ^/search/([^\/]+)(\/|)$ /index.php?link1=search&query=$1;
	}

	location /app {
	  rewrite ^/app/([^\/]+)(\/|)$ /index.php?link1=app&app_id=$1;
	}

	location /messages {
	  rewrite ^/messages/([^\/]+)(\/|)$ /index.php?link1=messages&user=$1;
	}

	location /terms {
	  rewrite ^/terms/([^\/]+)(\/|)$ /index.php?link1=terms&type=$1;
	}

	location /video {
	  rewrite ^/video-call/([^\/]+)(\/|)$ /index.php?link1=video-call&call_id=$1;
	  rewrite ^/video-call-api/([^\/]+)(\/|)$ /index.php?link1=video-call-api&call_id=$1;
	}

	location /post {
	  rewrite ^/post/([^\/]+)(\/|)$ /index.php?link1=post&id=$1;
	}

	location /game {
	  rewrite ^/game/([^\/]+)(\/|)$ /index.php?link1=game&id=$1;
	}

	location = /upgraded {
	  rewrite ^(.*)$ /index.php?link1=upgraded;
	}

	location = /get_news_feed {
	  rewrite ^(.*)$ /index.php?link1=get_news_feed;
	}

	location = /games {
	  rewrite ^(.*)$ /index.php?link1=games;
	}

	location /new {
	  rewrite ^/new-game$ /index.php?link1=new-game;
	  rewrite ^/new-product$ /index.php?link1=new-product;
	}

	location /go {
	  rewrite ^/go-pro$ /index.php?link1=go-pro;
	}

	location = /oops {
	  rewrite ^(.*)$ /index.php?link1=oops;
	}	
	
	location /user {
	  rewrite ^/user-activation$ /index.php?link1=user-activation;
	}

	location /hashtag {
	  rewrite ^/hashtag/([^\/]+)(\/|)$ /index.php?link1=hashtag&hash=$1;
	}

	location /follow {
	  rewrite ^/follow-requests/(.*)$ /index.php?link1=follow-requests;
	}

	location = /home {
	  rewrite ^(.*)$ /index.php?link1=home;
	}

	location = /404 {
	  rewrite ^(.*)$ /index.php?link1=404;
	}

	location /welcome {
	  rewrite ^/welcome(.*)$ /index.php?link1=welcome;
	}

	location = /register {
	  rewrite ^(.*)$ /index.php?link1=register;
	}

	location /confirm {
	  rewrite ^/confirm-sms$ /index.php?link1=confirm-sms;
	  rewrite ^/confirm-sms-password(/?|)$ /index.php?link1=confirm-sms-password break;
	}

	location /forgot {
	  rewrite ^/forgot-password$ /index.php?link1=forgot-password;
	}

	location = /activate {
	  rewrite ^(.*)$ /index.php?link1=activate;
	}

	location = /pages {
	  rewrite ^(.*)$ /index.php?link1=pages;
	}

	location = /groups {
	  rewrite ^(.*)$ /index.php?link1=groups;
	}

	location /create {
	  rewrite ^/create-group$ /index.php?link1=create-group;
	  rewrite ^/create-page$ /index.php?link1=create-page;
	  rewrite ^/create-album$ /index.php?link1=create-album;
	  rewrite ^/create-album/([A-Za-z0-9_-]+)$ /index.php?link1=create-album&album=$1;
	  rewrite ^/create-blog(/?|)$ /index.php?link1=create-blog;
	  rewrite ^/create-app$ /index.php?link1=create-app;
	}

	location = /logout {
	  rewrite ^(.*)$ /index.php?link1=logout;
	}

	location /contact {
	  rewrite ^/contact-us$ /index.php?link1=contact-us;
	}

	location = /messages {
	  rewrite ^(.*)$ /index.php?link1=messages;
	}

	location = /albums {
	  rewrite ^(.*)$ /index.php?link1=albums;
	}

	location /albums {
	  rewrite ^/albums/([A-Za-z0-9_-]+)$ /index.php?link1=albums&user=$1;
	}

	location /album {
	  rewrite ^/album/([A-Za-z0-9_-]+)$ /index.php?link1=album&id=$1;
	}
	
	location /page {
	  rewrite ^/page-setting/([^\/]+)(\/|)$ /index.php?link1=page-setting&page=$1;
	  rewrite ^/page-setting/([A-Za-z0-9_]+)/([A-Za-z0-9_-]+)$ /index.php?link1=page-setting&page=$1&link3=$2;
	}

	location /group {
	  rewrite ^/group-setting/([^\/]+)(\/|)$ /index.php?link1=group-setting&group=$1;
	  rewrite ^/group-setting/([A-Za-z0-9_]+)/([A-Za-z0-9_-]+)$ /index.php?link1=group-setting&group=$1&link3=$2;
	}

	location /edit {
	  rewrite ^/edit-product/([A-Za-z0-9_]+)$ /index.php?link1=edit-product&id=$1;
	  rewrite ^/edit-blog/(\d+)(/?|)$ /index.php?link1=edit-blog&id=$1;
	}

	location = /products {
	  rewrite ^(.*)$ /index.php?link1=products;
	}

	location /products {
	  rewrite ^/products/([A-Za-z0-9_-]+)$ /index.php?link1=products&c_id=$1;
	}

	location /my {
	  rewrite ^/my-products$ /index.php?link1=my-products;
	  rewrite ^/my-blogs(/?|)$ /index.php?link1=my-blogs;
	}

	location /site {
	  rewrite ^/site-pages/(.*)$ /index.php?link1=site-pages&page_name=$1;
	}

	location = /blogs {
	  rewrite ^(.*)$ /index.php?link1=blogs;
	}

	location = /sharer {
	  rewrite ^(.*)$ /index.php?link1=sharer;
	}

	location /blog {
	  rewrite ^/blog-category/(\d+)(/?|)$ /index.php?link1=blog-category&id=$1;
	}

	location /read {
	  rewrite ^/read-blog/(.*)$ /index.php?link1=read-blog&id=$1;
	}

	location = /app_api {
	  rewrite ^(.*)$ /index.php?link1=app_api;
	}

	location /api {
	  rewrite ^/api(/?|)$ /api-v2.php;
	  rewrite ^/api/([^\/]+)(\/|)$ /api-v2.php?type=$1;
	}

	location = /authorize {
	  rewrite ^(.*)$ /index.php?link1=authorize;
	}

	
	location /forum {
	  rewrite ^/forum(/?|)$ /index.php?link1=forum;
	  rewrite ^/forum/members(/?|)$ /index.php?link1=forum-members;
	  rewrite ^/forum/search(/?|)$ /index.php?link1=forum-search;
	  rewrite ^/forum/search-result/(/?|)$ /index.php?link1=forum-search-result;
	  rewrite ^/forum/events(/?|)$ /index.php?link1=forum-events;
	  rewrite ^/forum/help(/?|)$ /index.php?link1=forum-help;
	}

	location /forums {
	  rewrite ^/forums/(\d+)(/?|)$ /index.php?link1=forums&fid=$1;
	  rewrite ^/forums/add/(\d+)(/?|)$ /index.php?link1=forumaddthred&fid=$1;
	  rewrite ^/forums/thread/(\d+)(/?|)$ /index.php?link1=showthread&tid=$1;
	  rewrite ^/forums/thread/reply/(\d+)(/?|)$ /index.php?link1=threadreply&tid=$1;
	  rewrite ^/forums/thread/quote/(\d+)(/?|)$ /index.php?link1=threadquote&tid=$1;
	  rewrite ^/forums/thread/edit/(\d+)(/?|)$ /index.php?link1=editreply&tid=$1;
	  rewrite ^/forums/user/threads(/?|)$ /index.php?link1=mythreads;
	  rewrite ^/forums/user/threads/edit/(\d+)(/?|)$ /index.php?link1=edithread&tid=$1;
	  rewrite ^/forums/user/messages(/?|)$ /index.php?link1=mymessages;
	}

	location /events {
	  rewrite ^/events(/?|)$ /index.php?link1=events;
	  rewrite ^/events/create-event(/?|)$ /index.php?link1=create-event;
	  rewrite ^/events/edit/(\d+)/(/?|)$ /index.php?link1=edit-event&eid=$1;
	  rewrite ^/events/my(/?|)$ /index.php?link1=my-events;
	  rewrite ^/events/going(/?|)$ /index.php?link1=events-going;
	  rewrite ^/events/invited(/?|)$ /index.php?link1=events-invited;
	  rewrite ^/events/interested(/?|)$ /index.php?link1=events-interested;
	  rewrite ^/events/past(/?|)$ /index.php?link1=events-past;
	  rewrite ^/events/(\d+)(/?|)$ /index.php?link1=show-event&eid=$1;
	}

	location /unusual {
	  rewrite ^/unusual-login$ /index.php?link1=unusual-login;
	}

	location /movies {
	  rewrite ^/movies(/?|)$ /index.php?link1=movies;
	  rewrite ^/movies/genre/([A-Za-z-]+)(/?|)$ /index.php?link1=movies-genre&genre=$1;
	  rewrite ^/movies/country/([A-Za-z-]+)(/?|)$ /index.php?link1=movies-country&country=$1;
	  rewrite ^/movies/watch/(\d+)(/?|)$ /index.php?link1=watch-film&film-id=$1;
	}

	location /wallet {
	  rewrite ^/wallet(/?|)$ /index.php?link1=wallet;
	}

	location /status {
	  rewrite ^/status/create(/?|)$ /index.php?link1=create-status;
	}

	location /more {
	  rewrite ^/more-status(/?|)$ /index.php?link1=more-status;
	}
	
	location /friends {
	  rewrite ^/friends-nearby(/?|)$ /index.php?link1=friends-nearby;
	}

	location /_ {
	  rewrite ^/_$ /requests.php;
	}

	location /graph {
	  rewrite ^/graph-success$ /index.php?link1=graph-success;
	}

	location = /developers {
	  rewrite ^(.*)$ /index.php?link1=developers;
	}

	location = /apps {
	  rewrite ^(.*)$ /index.php?link1=apps;
	}
	
	location = /graph {
	  rewrite ^(.*)$ /index.php?link1=graph;
	}

	location = /oauth {
	  rewrite ^(.*)$ /index.php?link1=oauth;
	}

	location /boosted {
	  rewrite ^/boosted-pages$ /index.php?link1=boosted-pages;
	  rewrite ^/boosted-posts$ /index.php?link1=boosted-posts;
	}

	location = /jobs {
	  rewrite ^(.*)$ /index.php?link1=jobs;
	}

	location = /common_things {
	  rewrite ^(.*)$ /index.php?link1=common_things;
	}
	
	location = /funding {
	  rewrite ^(.*)$ /index.php?link1=funding;
	}

	location = /my_funding {
	  rewrite ^(.*)$ /index.php?link1=my_funding;
	}

	location = /create_funding {
	  rewrite ^(.*)$ /index.php?link1=create_funding;
	}

	location /edit_fund {
	  rewrite ^/edit_fund/(.*)$ /index.php?link1=edit_fund&id=$1;
	}

	location /show_fund {
	  rewrite ^/show_fund/(.*)$ /index.php?link1=show_fund&id=$1;
	}

 }


# another virtual host using mix of IP-, name-, and port-based configuration
#
#server {
#	listen 8000;
#	listen somename:8080;
#	server_name somename alias another.alias;
#	root html;
#	index index.html index.htm;
#
#	location / {
#		try_files $uri $uri/ =404;
#	}
#}


# HTTPS server
#
#server {
#	listen 443;
#	server_name localhost;
#
#	root html;
#	index index.html index.htm;
#
#	ssl on;
#	ssl_certificate cert.pem;
#	ssl_certificate_key cert.key;
#
#	ssl_session_timeout 5m;
#
#	ssl_protocols SSLv3 TLSv1 TLSv1.1 TLSv1.2;
#	ssl_ciphers "HIGH:!aNULL:!MD5 or HIGH:!aNULL:!MD5:!3DES";
#	ssl_prefer_server_ciphers on;
#
#	location / {
#		try_files $uri $uri/ =404;
#	}
#}
